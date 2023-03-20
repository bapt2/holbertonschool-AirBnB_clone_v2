-- ste up a database in MySQL server
CREATE DATABASE IF NOT EXISTS hbnb_dev_db;
USE hbnb_dev_db;
CREATE USER IF NOT EXISTS 'hbnb_dev'@'localhost' IDENTIFIED BY 'hbnb_dev_pwd';
GRANT ALL ON hbnb_dev_db.* TO hbnb_dev;
GRANT SELECT on performance_schema.* to 'hbnb_dev'@'localhost';
