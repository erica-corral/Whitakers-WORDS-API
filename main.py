#serves the predictions from whitakers using fastAPI
from fastapi import FastAPI
from fastapi.responses import HTMLResponse
import subprocess
import os

print("initializing API")
os.system("chmod +x ./words")

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

