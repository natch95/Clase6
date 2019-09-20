#audio.py
# from gtts import gTTS
#
#
# def tts(text_file, lang, name_file):
#     with open(text_file, "r") as file:
#         text = file.read()
#     file = gTTS(text=text, lang=lang)
#     filename = name_file
#     file.save(filename)
#
#
# tts("texto.txt", "Es", "audio.mp3")

#main.py

# from flask import Flask
#
# app = Flask(__name__)
#
#
# @app.route('/')
# def hello():
#     return 'Hola'
#
#
# if __name__ == '__main__':
#     app.run()

# Ejercicio 3
#****************************
# from flask import Flask
# import funcion
# app = Flask(__name__)
# @app.route('/')
# def hello():
#     mensaje = funcion.prueba()
#     return mensaje
#
# if __name__ == '__main__':
#     app.run()

from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def hola():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()