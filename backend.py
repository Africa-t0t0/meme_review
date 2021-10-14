import re
import base64, webbrowser
from io import BytesIO
from PIL import Image
import random
import os,os.path
from flask_cors import CORS, cross_origin
from flask import Flask, request, redirect, url_for, jsonify, Response
import psycopg2, json
from psycopg2.extras import RealDictCursor
from psycopg2.extensions import AsIs
from psycopg2 import Error, sql
app = Flask(__name__)
# cors = CORS(app, resources={r"*":{"origins":"*"}})

# app.config['CORS_HEADERS'] = 'Content-Type'

HOST = os.environ.get('HOST')
PORT = os.environ.get('PORT')
DATABASE = os.environ.get('DATABASE')
USER = os.environ.get('USER')
PASSWORD = os.environ.get('PASSWORD')

# HOST = "192.168.0.10"
# PORT = "5432"
# DATABASE = "arqui"
# USER = "admin"
# PASSWORD = "admin"

isCreated = False


@app.route('/')
@cross_origin()
def hello():
    return ("hOLO")

@app.route('/create', methods = ['GET'])
@cross_origin()
def create():
    if request.method == 'GET':
        global isCreated
        if isCreated == False:
            arr = os.listdir('memes/')
            query2 = """
                    CREATE TABLE IF NOT EXISTS memes (
                            meme_id serial PRIMARY KEY,
                            meme_name varchar,
                            meme_ranking integer,
                            meme_story text,
                            meme_image text
                        );"""
            conn = psycopg2.connect(
            host= HOST,                    # cambiar por os.environ['HOST'], etc.
            port= PORT,
            database= DATABASE,
            user= USER,
            password=PASSWORD)
            cursor = conn.cursor()
            cursor.execute((query2))
            conn.commit()


            arra = ['a','b','c','d','e','f','g','h','i','j','k','h','i','o','p']
            inb = 0

            for i in range(0,len(arra)):
                buffered = BytesIO()
                image = Image.open('memes/'+arr[inb])
                image.save(buffered, format=image.format)
                image_str = base64.b64encode(buffered.getvalue())
                image_str = str(image_str,'utf-8')
                meme_ranking = random.randint(1,10)
                query="INSERT INTO memes(meme_name, meme_ranking, meme_story, meme_image) VALUES (%s,%s,%s,%s)"
                if 'a' == arr[inb][4]:
                    inb+=1
                    meme_story = "No hace falta decir nada, no puede ser eliminado."
                    meme_name = "Rick Astley"
                    meme_ranking = 10
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'b' == arr[inb][4]:
                    inb+=1
                    meme_story = "Totalmente real.."
                    meme_name = "Dark Souls Lore"
                    meme_ranking = 7
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'c' == arr[inb][4]:
                    inb+=1
                    meme_story = "jaja dijo UDP."
                    meme_name = "TCP UDP"
                    meme_ranking = 4
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'd' == arr[inb][4]:
                    inb+=1
                    meme_story = "Pinwini ciencia.."
                    meme_name = "Pinwino"
                    meme_ranking = 10
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'e' == arr[inb][4]:
                    inb+=1
                    meme_story = "Wololo."
                    meme_name = "AoE"
                    meme_ranking = 8
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'f' == arr[inb][4]:
                    inb+=1
                    meme_story = "Camaron que se duerme."
                    meme_name = "Camaron"
                    meme_ranking = 3
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'g' == arr[inb][4]:
                    inb+=1
                    meme_story = "Camaron que se duerme."
                    meme_name = "Tengo sed"
                    meme_ranking = 3
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'h' == arr[inb][4]:
                    inb+=1
                    meme_story = "El socialismo es imparable en el LoL."
                    meme_name = "Socialismo"
                    meme_ranking = 6
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'i' == arr[inb][4]:
                    inb+=1
                    meme_story = "Hay mejores de este tipo."
                    meme_name = "Ayuda"
                    meme_ranking = 2
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'j' == arr[inb][4]:
                    inb+=1
                    meme_story = "XD."
                    meme_name = "Chocolate"
                    meme_ranking = 7
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'k' == arr[inb][4]:
                    inb+=1
                    meme_story = "Mala onda."
                    meme_name = "Huaso"
                    meme_ranking = 9
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'l' == arr[inb][4]:
                    inb+=1
                    meme_story = "Lamento boliviano."
                    meme_name = "Rock"
                    meme_ranking = 1
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'm' == arr[inb][4]:
                    inb+=1
                    meme_story = "Que es loca la soa."
                    meme_name = "Gasfiter"
                    meme_ranking = 1
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'n' == arr[inb][4]:
                    inb+=1
                    meme_story = "Infaltable, progra avanzada en minecraft."
                    meme_name = "Jonathan Frez"
                    meme_ranking = 10
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'o' == arr[inb][4]:
                    inb+=1
                    meme_story = "El invocador de la imagen indica que es admin, por lo tanto todos deben demostrar respeto maximo."
                    meme_name = "Soy admin"
                    meme_ranking = 10
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
                elif 'p' == arr[inb][4]:
                    inb+=1
                    meme_story = "Totalmente real."
                    meme_name = "Portal"
                    meme_ranking = 10
                    meme_image = image_str
                    values = (meme_name, meme_ranking, meme_story, meme_image,)
                    cursor.execute(query, values)
                    conn.commit()
            isCreated = True
            return ("db y tabla creada")


@app.route('/subir', methods =['POST', 'GET'])
@cross_origin()
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

@app.route('/ver', methods =['POST','GET','PUT'])
# @cross_origin()
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
    elif request.method == 'POST':
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
    elif request.method == "PUT":
            return(url_for(("update_meme")))
   

@app.route('/delete/<id>', methods=['DELETE'])
@cross_origin()
def delete(id):
        if request.method == 'DELETE':
            conn = psycopg2.connect(
            host= HOST,                    # cambiar por os.environ['HOST'], etc.
            port= PORT,
            database= DATABASE,
            user= USER,
            password=PASSWORD)
            cursor = conn.cursor(cursor_factory=RealDictCursor)
            query= "DELETE FROM memes WHERE meme_name = %s;"
            data = id
            if data=="Rick Astley":
                    print("Rick Rolled")
                    return (webbrowser.open(("https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley")))
            values=(data,)
            cursor.execute(query,values)
            conn.commit()
            #return(redirect(("http://localhost:3000/ver")))
            return ('owo')

@app.route('/update_meme', methods=["POST","GET"])
@cross_origin()
def update_meme():
    if request.method == "POST":
        return (redirect("http://localhost:3000/update"))


@app.route("/update", methods=["PUT"])
# @cross_origin()
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


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
    response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE')
    return response

    
if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)