from flask import Flask, render_template
import pymysql.cursors

# Connect to the database
connection = pymysql.connect(host='mrbartucz.com',
                             user='zt9916nr',
                             password='Can@dafishing2',
                             db='zt9916nr_students',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


app = Flask(__name__)

@app.route('/')
def index():
    try:
        with connection.cursor() as cursor:
            # Select all Students
            sql = "SELECT * from Students"
        
            # execute the SQL command
            cursor.execute(sql)
            output = "<br>"
            # get the results
            for result in cursor:
                output += str(result)
                output += "<br>"
            
            return output
        
        # If you INSERT, UPDATE or CREATE, the connection is not autocommit by default.
        # So you must commit to save your changes. 
        # connection.commit()
        

    finally:
        connection.close()
        


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=9916)