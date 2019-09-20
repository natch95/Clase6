from gtts import gtts


def tts(text_file, lang, name_file):
    with open(text_file, "r") as file:
        text = file.read()
    file = gtts(text=text, lang=lang)
    filename = name_file
    file.save(filename)


tts("texto.txt", "Es", "audio.mp3")
