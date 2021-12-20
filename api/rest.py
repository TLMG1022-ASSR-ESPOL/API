import pymysql
import telnetlib
from app import app
from db import mysql
from db import telnet_to_query
from flask import jsonify, request, redirect

HOST = "route-server.he.net"
password = "rviews"

print(10)

#to populate db
def populate_db(query): 
    conn = mysql.connect() 
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute(query)
    print("Database updated successfully")

#api
@app.route('/', methods=['GET', 'POST'])
def index():
    conn = mysql.connect()    
    cursor = conn.cursor(pymysql.cursors.DictCursor)
    cursor.execute("SELECT * FROM router_details")    
    rows = cursor.fetchall()    
    resp = jsonify(rows)
    resp.status_code = 200
    if request.method == 'POST':
        return redirect('/telnet')
    return resp


@app.route('/telnet')
def telnet():
    #telnet script
    tn = telnetlib.Telnet()
    tn.open(HOST)
    tn.read_until(b"Password: ")
    tn.write(password.encode("ascii") + b"\n")
    tn.write(b"show bgp ipv4 unicast 216.218.252.0\n")
    print("output for show bgp ipv4 unicast 216.218.252.0: ")
    tn.write(b"exit\n")
    output = (tn.read_all().decode('ascii')).split("Local")
    #update db
    sucess = "Output for show bgp ipv4 unicast 216.218.252.0 \n"
    for connection in output:
        connection = connection.strip()
        if connection.startswith('216.218.252'):
            query = telnet_to_query(connection)
            populate_db(query)
            sucess = sucess + query + "/n"
    tn.close()

    return sucess

if __name__ == "__main__":
    app.run(debug=True,host='0.0.0.0')






