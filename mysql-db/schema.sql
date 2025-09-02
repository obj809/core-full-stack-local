-- mysql-db/schema.sql

-- Create the database
CREATE DATABASE IF NOT EXISTS `core-full-stack`
  DEFAULT CHARACTER SET utf8mb4
  DEFAULT COLLATE utf8mb4_0900_ai_ci;

-- Switch to the database
USE `core-full-stack`;

-- Create the todos table
CREATE TABLE IF NOT EXISTS todos (
    id INT PRIMARY KEY AUTO_INCREMENT,
    title VARCHAR(255) NOT NULL
);