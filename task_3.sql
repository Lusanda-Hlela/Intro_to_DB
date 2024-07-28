CREATE DATABASE IF NOT EXISTS alx_book_store

-- Use the database passed as an argument
USE alx_book_store;

-- List all tables in the specified database
SELECT table_name 
FROM information_schema.tables 
WHERE table_schema = 'alx_book_store';

-- Show the created tables
SHOW TABLES;