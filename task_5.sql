CREATE DATABASE IF NOT EXISTS alx_book_store

-- Use the database passed as an argument
USE alx_book_store;

-- Insert a single row into the customer table
INSERT INTO customer (customer_id, customer_name, email, address)
VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');