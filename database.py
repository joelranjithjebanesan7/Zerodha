import psycopg2
conn = psycopg2.connect(database="zerodhadb", user = "postgres", password = "7777", host = "127.0.0.1", port = "5432")
curs = conn.cursor()
 
curs = curs.execute("""CREATE TABLE equity1(SC_CODE integer,
                                               SC_NAME text,
                                               SC_GROUP text,
                                               OPEN real,
                                               HIGH real,
                                               LOW real,
                                               CLOSE real,
                                               LAST real,
                                               PREVCLOSE real,
                                               NO_TRADES integer,
                                               NO_OF_SHRS integer,
                                               NET_TURNOV real,
                                               TDCLOINDI text);""")
    
print ("Table created")