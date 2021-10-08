import re
import base64
import os
from flask_cors import CORS, cross_origin
from flask import Flask, request, redirect, url_for, jsonify
import psycopg2, json
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import AsIs
from psycopg2 import Error, sql
app = Flask(__name__)
cors = CORS(app)

app.config['CORS_HEADERS'] = 'Content-Type'

# QUÉ VOY A RESEÑAR? -> MEMES.

# HOST = os.environ.get('HOST')
# PORT = os.environ.get('PORT')
# DATABASE = os.environ.get('DATABASE')
# USER = os.environ.get('USER')
# PASSWORD = os.environ.get('PASSWORD')

HOST = "192.168.0.10"
PORT = "5432"
DATABASE = "arqui"
USER = "admin"
PASSWORD = "admin"

@app.route('/')
@cross_origin()
def hello():
    return ("hOLO")

@app.route('/create')
def create():
    f = open('script.txt','r')
    query = """CREATE USER %s WITH PASSWORD %s;
            CREATE DATABASE %s;
            GRANT ALL PRIVILEGES ON DATABASE %s TO %s;
            \connect %s %s
            BEGIN;
            CREATE TABLE memes (
                    meme_id integer NOT NULL,
                    meme_name varchar,
                    meme_ranking integer,
                    meme_story text,
                    meme_image text
                );
            COMMIT;"""
    conn = psycopg2.connect(
    host= HOST,                    # cambiar por os.environ['HOST'], etc.
    port= PORT,
    database= DATABASE,
    user= USER,
    password=PASSWORD)
    cursor = conn.cursor()
    queryy = (query.format(field=sql.Identifier(USER), table=(sql.Identifier(PASSWORD)), db=(sql.Identifier(DATABASE)), db2=(sql.Identifier(DATABASE)), field2=sql.Identifier(USER), db3=(sql.Identifier(DATABASE)), field3=sql.Identifier(USER)))
    values = ((USER), PASSWORD, DATABASE, DATABASE, USER, DATABASE, USER,)
    cursor.execute(sql.SQL(queryy))
    conn.commit()
    return ("db y tabla creada")


@app.route('/subir', methods =['POST', 'GET'])
def subir():
    if request.method == 'POST':
        conn = psycopg2.connect(
        host= HOST,                    # cambiar por os.environ['HOST'], etc.
        port= PORT,
        database= DATABASE,
        user= USER,
        password=PASSWORD)
        cursor = conn.cursor()
        print("recibimos un post owo")
        meme_name = request.form['meme_name']
        meme_ranking = request.form['meme_ranking']
        meme_story = request.form['meme_story']
        meme_image = request.files['meme_image']
        meme_image_inBytes = meme_image.read()
        b64_str = str(base64.b64encode(meme_image_inBytes), 'utf-8')
        query = "INSERT INTO memes(meme_name, meme_ranking, meme_story, meme_image) VALUES (%s,%s,%s,%s);"
        values = (meme_name, meme_ranking, meme_story, b64_str,)
        cursor.execute(query, values)
        conn.commit()
        
        return(redirect(("http://localhost:3000/ver"))) 
    else:
        pass

@app.route('/ver', methods =['POST','GET'])
def ver():
    if request.method == "GET":
        conn = psycopg2.connect(
        host= HOST,                    # cambiar por os.environ['HOST'], etc.
        port= PORT,
        database= DATABASE,
        user= USER,
        password=PASSWORD)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query = "SELECT meme_id, meme_name, meme_ranking, meme_story, meme_image FROM memes;"
        cursor.execute(query)
        result = cursor.fetchall()
        return jsonify(result)
    else:
        conn = psycopg2.connect(
        host= HOST,                    # cambiar por os.environ['HOST'], etc.
        port= PORT,
        database= DATABASE,
        user= USER,
        password=PASSWORD)
        cursor = conn.cursor(cursor_factory=RealDictCursor)
        query= "DELETE FROM memes WHERE meme_name = %s;"
        data = request.form['meme_name']
        if data=="Rick Astley":
            print("Rick Rolled")
            return(redirect(("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")))
        values=(data,)
        cursor.execute(query,values)
        conn.commit()
        return(redirect(("http://localhost:3000/ver")))

@app.route('/update_meme', methods=["POST","GET"])
def update_meme():
    if request.method == "POST":
        conn = psycopg2.connect(
        host= HOST,                    # cambiar por os.environ['HOST'], etc.
        port= PORT,
        database= DATABASE,
        user= USER,
        password=PASSWORD)
        # query = "UPDATE memes SET meme_ranking = %s WHERE meme_name = 'trololo';"
        return (redirect("http://localhost:3000/update"))


@app.route("/update", methods=["GET","PUT"])
@cross_origin()
def update():
    if request.method == "PUT":
        conn = psycopg2.connect(
        host= HOST,                    # cambiar por os.environ['HOST'], etc.
        port= PORT,
        database= DATABASE,
        user= USER,
        password=PASSWORD)
        cursor = conn.cursor()
        meme_name = request.form['meme_name']
        meme_ranking = request.form['meme_ranking']
        meme_story = request.form['meme_story']
        query = "UPDATE memes SET meme_ranking = %s, meme_story = %s WHERE meme_name = %s; "
        values = (meme_ranking,meme_story,meme_name,)
        cursor.execute(query, values)
        conn.commit()
        return (redirect("http://localhost:3000/ver"))




    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)