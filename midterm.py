import sqlite3
con = sqlite3.connect('habeeb_omotunde.db')
cur = con.cursor()
cur.execute("CREATE Table CARS(name text, license_plate text, make text, model text, year int)")

insert_instr_temp = "INSERT INTO CARS VALUES (?, ?, ?, ?, ?)"
car1 = ('Cabbie','ABC0001','Ford','Taurus', 2020)
car2 = ('Muscle','XYZ0023','Honda','Accord', 2018)

cur.execute(insert_instr_temp,car1)
cur.execute(insert_instr_temp,car2)


cur.execute('select * from CARS where make = "Honda"')
cur.fetchall()
