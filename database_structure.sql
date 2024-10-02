-- database_structure
CREATE DATABASE healthcare_system;
USE healthcare_system;

CREATE TABLE patients (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    gender VARCHAR(10),
    contact VARCHAR(15),
    address VARCHAR(255)
);
