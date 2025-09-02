export interface Todo {
  id: number;
  title: string;
}

// LOCAL BACKEND PORT
const API_URL = 'http://127.0.0.1:5000/';

export const fetchTodos = async (): Promise<Todo[]> => {
  const response = await fetch(`${API_URL}todo/`);
  const data = await response.json();
  return data;
};

export const addTodo = async (title: string): Promise<void> => {
  const response = await fetch(`${API_URL}todo/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title }),
  });
  if (!response.ok) {
    throw new Error('Failed to add todo');
  }
};

export const updateTodo = async (id: number, title: string): Promise<void> => {
  const response = await fetch(`${API_URL}todo/${id}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ title }),
  });
  if (!response.ok) {
    throw new Error('Failed to update todo');
  }
};

export const deleteTodo = async (id: number): Promise<void> => {
  const response = await fetch(`${API_URL}todo/${id}`, {
    method: 'DELETE',
  });
  if (!response.ok) {
    throw new Error('Failed to delete todo');
  }
};

export const fetchMessage = async (): Promise<string> => {
  const response = await fetch(API_URL);
  const data = await response.json();
  return `Welcome to the ${data.message}`;
};
