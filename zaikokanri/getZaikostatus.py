import sqlite3

# create DB connnection
dbname = 'zaikokanri'
con = sqlite3.connect(dbname)

# create cursor
cur = con.cursor()

# create zaiko table
cur.execute("DROP TABLE zaiko")
cur.execute("CREATE TABLE zaiko(name, category, change_count, yyyymmdd, price, stock_count, create_time, change_flag)")
con.commit()

# insert test data
cur.execute("""
    INSERT INTO zaiko VALUES
            ('卵', '食品', '1', '20230604', 200, 4, 202306041640, -1),
            ('牛乳', '食品', '1', '20230604', 250, 2, 202306041640, 1)
""")
con.commit()

# get all stock
stock = cur.execute("SELECT * FROM zaiko")
print (stock.fetchall())

# close DB connection
con.close()