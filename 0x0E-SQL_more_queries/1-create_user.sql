--script that creates the MySQL server user user_0d_1
--user_0d_1 should have all privileges in  MySQL server
--password should be set to user_0d_1_pwd
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL ON *.* TO user_0d_1@localhost;

