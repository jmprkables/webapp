import rethinkdb as r

conn = r.connect("192.168.6.26", 28015)
try:
	r.db_drop("hackiiitd").run(conn)
	print("deleted old db")
except:
	print("inital creation")

r.db_create("hackiiitd").run(conn)

r.db("hackiiitd").table_create("fall").run(conn)
print("."),
r.db("hackiiitd").table_create("medicine").run(conn)
print("."),
r.db("hackiiitd").table_create("door").run(conn)
print("."),
r.db("hackiiitd").table_create("photo").run(conn)
print("."),
print("done")
