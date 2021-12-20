from app import app
from flaskext.mysql import MySQL

mysql = MySQL()
 
# MySQL configurations
app.config['MYSQL_DATABASE_USER'] = 'wijoayal'
app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
app.config['MYSQL_DATABASE_DB'] = 'router_data'

mysql.init_app(app)

#to edit query
def telnet_to_query(connection):
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    clean = connection.split("\n")
    clean_ip = clean[0].split(" ")
    ip = clean_ip[0]
    clean_o = clean[1].strip()
    clean_origin = clean_o.split(",")
    origin = clean_origin[0].strip()
    metric = clean_origin[1].strip()
    localpref = clean_origin[2].strip()
    valid = clean_origin[3].strip()
    internal = clean_origin[4].strip()
    clean_d = clean[2].strip()
    clean_date = clean_d.split(" ")
    if (len(clean_date) > 7):
        month = clean_date[3].strip()
        day = clean_date[5].strip()
        hour = clean_date[6].strip()
        year = clean_date[7].strip()
    else:
        month = clean_date[3].strip()
        day = clean_date[4].strip()
        hour = clean_date[5].strip()
        year = clean_date[6].strip()
    if ((months.index(month) + 1) < 10):
        month_str = "0" + str(months.index(month) + 1)
    else:
        month_str = str(months.index(month) + 1)
    day = int(day)
    if (day < 10):
        day_str = "0" + str(day)
    else:
        day_str = str(day)
    date = year + "-" + month_str + "-" + day_str + " " + hour

    q1 = "INSERT INTO router_details (ip, origin, metric, localpref, valid, internal, date ) SELECT * FROM (SELECT '"
    q2 = ip + "', '" + origin + "', '" + metric + "', '" + localpref + "', '" + valid + "', '" + internal + "', '" + date + "') AS tmp "
    q3 = "WHERE NOT EXISTS (SELECT ip FROM router_details WHERE ip = '"+ip+"') LIMIT 1;"
    query = q1 + q2 + q3
    return query