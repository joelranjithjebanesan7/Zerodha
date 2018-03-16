import psycopg2
import csv


conn = psycopg2.connect(database="zerodhadb", user = "postgres", password = "7777", host = "127.0.0.1", port = "5432")
curs = conn.cursor()

with open("/home/joelrj/Desktop/Zerodha/EQ080318.CSV", "r") as csv_file:
    csvReader = csv.DictReader(csv_file)
    value_db = [(i['SC_CODE'],i['SC_NAME'],i['SC_GROUP'],i['OPEN'],i['HIGH'],i['LOW'],i['CLOSE'],i['LAST'],i['PREVCLOSE'],i['NO_TRADES'],i['NO_OF_SHRS'],i['NET_TURNOV'],i['TDCLOINDI'])for i in csvReader]   
    curs.executemany("INSERT INTO equity1 (SC_CODE,SC_NAME,SC_GROUP,OPEN,HIGH,LOW,CLOSE,LAST,PREVCLOSE,NO_TRADES,NO_OF_SHRS,NET_TURNOV,TDCLOINDI) VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",value_db)

    conn.commit()