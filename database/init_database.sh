# db/init_db.sh
#!/bin/bash
set -e

# Connect to the default database and create a sample table with dummy data
psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
  CREATE TABLE sample_table (
      id SERIAL PRIMARY KEY,
      name VARCHAR(50),
      age INT,
      city VARCHAR(50)
  );

  INSERT INTO sample_table (name, age, city) VALUES
      ('Alice', 30, 'New York'),
      ('Bob', 25, 'San Francisco'),
      ('Charlie', 35, 'Chicago');
EOSQL
