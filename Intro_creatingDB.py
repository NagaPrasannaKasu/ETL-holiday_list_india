# import sqlalchemy
import sqlite3

#connect to database
connection = sqlite3.connect('TestDBs4.db')
#create a cursor
cursor = connection.cursor()
#create a table
#command1 = """Create Table if not exists stores_1(store_id Integer Primary key, location Text)"""
#cursor.execute(command1)

# #create purchases table
# command2 = """Create Table if not exists purchases_1(purchase_id Integer Primary key, store_id Integer, total_cost Float, Foreign key(store_id) references stores(store_id))"""
# cursor.execute(command2)

#insert rows into the table
#cursor.execute("Insert into stores_1 Values(1,'Chicago')")
#insert many records
#many_stores = [(2, 'Texas'),(3,'Munich'),(4,'Stuttgart'),(5,'Erfurt')]
#cursor.executemany("Insert into stores_1 Values(?,?)",many_stores)

#executing results
cursor.execute("select * from stores_1")
#there are 3 types of fetch
#fetchone() -- it will fetch only first row of the table
#fetchone()[0] -- it will fetch only first column of the row from the table
#fetchmany(3) -- it will fetch last 3 items of the table
#fetchall() -- t will fetch everything 
results = cursor.fetchall()
# after fetch nothing will display, important is we have to print to the screen
#print(results)

#more readable
# for result in results:
#     print(result)

# for result in results:
#     print(result[1])

# if there are more columns
# for result in results:
#     print(result[0]+ " | " + result[1])

print("command executed succesfully")

#commit our command
connection.commit()

#close our connection
connection.close()





