import React, { useState } from 'react';

interface TodoFormProps {
  onSubmit: (title: string, description: string) => void;
  initialTitle?: string;
  initialDescription?: string;
  buttonText: string;
}

const TodoForm: React.FC<TodoFormProps> = ({ onSubmit, initialTitle = '', buttonText }) => {
  const [title, setTitle] = useState(initialTitle);

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    onSubmit(title, ''); // Pass an empty string as the second argument
    setTitle('');
  };

  return (
    <form onSubmit={handleSubmit}>
      <input
        type="text"
        name="title"
        value={title}
        onChange={(e) => setTitle(e.target.value)}
        placeholder="Title"
        required
      />
      <button type="submit">{buttonText}</button>
    </form>
  );
};

export default TodoForm;
