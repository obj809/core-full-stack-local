-- mysql-db/local_database.sql

CREATE DATABASE IF NOT EXISTS `core-full-stack`
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_0900_ai_ci;

USE `core-full-stack`;

CREATE TABLE IF NOT EXISTS todos (
  id INT PRIMARY KEY AUTO_INCREMENT,
  title VARCHAR(255) NOT NULL
);

INSERT INTO todos (title) VALUES
('First task'),
('Second task'),
('Third task');

SELECT * FROM todos;
