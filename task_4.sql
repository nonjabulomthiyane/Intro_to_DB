-- Use the `information_schema` database to query metadata
USE information_schema;

-- Query to get details about columns in the `Books` table
SELECT 
    TABLE_NAME,
    COLUMN_NAME,
    COLUMN_TYPE,
    IS_NULLABLE,
    COLUMN_DEFAULT,
    EXTRA
FROM 
    COLUMNS
WHERE 
    TABLE_SCHEMA = DATABASE()  -- Get the current database name
    AND TABLE_NAME = 'Books';

mysql -u your_username -p -e "SOURCE path/to/task_4.sql" alx_book_store
