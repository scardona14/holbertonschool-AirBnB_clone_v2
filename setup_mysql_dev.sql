-- Script that prepares a MySQL server for AirBnB Console v2
-- This script will create a database and a user for the AirBnB project

-- Create the database
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;

-- Create the user if not exists
-- The user will be created with the password 'hbnb_dev_pwd'
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';

-- Grant all privileges on the database to the user
GRANT ALL PRIVILEGES ON hbnb_dev_db.* TO 'hbnb_dev'@'localhost';
Flush privileges;

-- Grant select privileges on performance_schema to the user
GRANT SELECT ON performance_schema.* TO 'hbnb_dev'@'localhost';
Flush privileges;
