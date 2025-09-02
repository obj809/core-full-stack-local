// react-frontend/src/pages/StaticPage.tsx

import React, { useEffect, useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { fetchMessage } from '../services/todoService';

const StaticPage: React.FC = () => {
  const navigate = useNavigate();
  const [message, setMessage] = useState('Welcome');

  useEffect(() => {
    const getMessage = async () => {
      try {
        const fetchedMessage = await fetchMessage();
        setMessage(fetchedMessage);
      } catch (error) {
        console.error('Failed to fetch message', error);
      }
    };

    getMessage();
  }, []);

  const redirectToForm = () => {
    navigate('/form');
  };

  return (
    <div>
      <h1>{message}</h1>
      <button onClick={redirectToForm}>Go to Form</button>
    </div>
  );
};

export default StaticPage;
