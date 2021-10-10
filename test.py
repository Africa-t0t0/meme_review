import os,os.path,base64, psycopg2
from io import BytesIO
from PIL import Image
import random

HOST = "192.168.0.10"
PORT = "5432"
DATABASE = "arqui"
USER = "admin"
PASSWORD = "admin"
arr = os.listdir('memes/')
# print(arr[0])
# image = Image.open('memes/meme0.png')
#arr.sort(key=arr[])
# print(arr[3][4])
# image.save(buffered, format=image.format)
# image_str = base64.b64encode(buffered.getvalue())
# image_str = str(image_str,'utf-8')
# f = open('test.txt','w')
# f.write(image_str) 
#print(image_str)
# print(str(base64.b64encode(file), 'utf-8'))    

conn = psycopg2.connect(
host= HOST,                    
port= PORT,
database= DATABASE,
user= USER,
password=PASSWORD)
cursor = conn.cursor()

arra = ['a','b','c','d','e','f','g','h','i','j','k','h','i','o','p']
inb = 0

for i in arra:
    buffered = BytesIO()

    image = Image.open('memes/'+arr[inb])
    print(arr[inb])
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
        meme_name = "TCP/UDP"
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




#b64_str = str(base64.b64encode(meme_image_inBytes), 'utf-8')

