# Then, create a SQLITE database or use an existing database
# and create a table in the database called "Ages":

"""
CREATE TABLE Ages ( 
  name VARCHAR(128), 
  age INTEGER
) 

"""

# Then make sure the table is empty by deleting any rows
# that you previously inserted, and insert these rows and
# only these rows with the following commands:

"""
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Hajra', 18);
INSERT INTO Ages (name, age) VALUES ('Sydney', 37);
INSERT INTO Ages (name, age) VALUES ('Matia', 34);
INSERT INTO Ages (name, age) VALUES ('Ewing', 36);

"""

# Once the inserts are done, run the following SQL command:

""" SELECT hex(name || age) AS X FROM Ages ORDER BY X """

# Find the first row in the resulting record set and enter the
# long string that looks like 53656C696E613333.
