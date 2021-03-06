#serves the predictions from whitakers using fastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess
import os

print("initializing API")
os.system("chmod +x ./words")
os.system("chmod +x ./whitakers-words-1.97/words")

app = FastAPI()
print("initialized")

@app.get("/translate/{latin_word}", response_class=HTMLResponse)
async def read_items(latin_word):
    definition = subprocess.check_output("./words " + latin_word, shell=True).decode("utf-8")
    print("ran latin-eng -> " +definition)
    return """
    <html>
        <head>
            <title>translation_plugin</title>
        </head>
        <body>
            <p style = "white-space: pre-line; white-space: pre">{definition}</p>
        </body>
    </html>
    """.format(definition = definition)

@app.get("/translate-english/{english_word}", response_class=HTMLResponse)
async def english_to_latin(english_word):
    #it is necessary to do all this changing directory magic, because if you try to run the 1.97 from an absolute path from the top-level directory, for some reason, the wrong definition returns
    os.chdir("./whitakers-words-1.97")
    print(os.getcwd())
    definition = subprocess.check_output("./words ~e " + english_word, shell=True).decode("utf-8")
    os.chdir(os.getenv("HOME"))
    print(os.getcwd())
    print("ran eng-latin -> " +definition)
    return """
    <html>
        <head>
            <title>translation_plugin</title>
        </head>
        <body>
            <p style = "white-space: pre-line; white-space: pre">{definition}</p>
        </body>
""".format(definition = definition)