import React, { useState, useEffect } from 'react';
import TodoForm from '../forms/TodoForm';
import { fetchTodos, addTodo, updateTodo, deleteTodo, Todo } from '../services/todoService';

const FormPage: React.FC = () => {
  const [todos, setTodos] = useState<Todo[]>([]);
  const [isEditing, setIsEditing] = useState<number | null>(null);

  useEffect(() => {
    loadTodos();
  }, []);

  const loadTodos = async () => {
    const data = await fetchTodos();
    setTodos(data);
  };

  const handleAddTodo = async (title: string) => {
    try {
      await addTodo(title);
      loadTodos();
    } catch (error) {
      console.error(error);
    }
  };

  const handleUpdateTodo = async (id: number, title: string) => {
    try {
      await updateTodo(id, title);
      loadTodos();
      setIsEditing(null);
    } catch (error) {
      console.error(error);
    }
  };

  const handleDeleteTodo = async (id: number) => {
    try {
      await deleteTodo(id);
      loadTodos();
    } catch (error) {
      console.error(error);
    }
  };

  return (
    <div>
      <h1>Todo Form</h1>
      <TodoForm onSubmit={handleAddTodo} buttonText="Add Todo" />
      <ul>
        {todos.map((todo) => (
          <li key={todo.id}>
            {isEditing === todo.id ? (
              <TodoForm
                onSubmit={(title) => handleUpdateTodo(todo.id, title)}
                initialTitle={todo.title}
                buttonText="Update Todo"
              />
            ) : (
              <>
                <h3>{todo.title}</h3>
                <button onClick={() => setIsEditing(todo.id)}>Edit</button>
                <button onClick={() => handleDeleteTodo(todo.id)}>Delete</button>
              </>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
};

export default FormPage;
