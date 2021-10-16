from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToFrench")
def englishToFrench():
    english_text = request.args.get('textToTranslate')
    if (english_text != ''):
        translation = language_translator.translate(english_text, 
                    model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    else:
        return ''

@app.route("/frenchToEnglish")
def frenchToEnglish():
    french_text = request.args.get('textToTranslate')
    if (french_text != ''):
        translation = language_translator.translate(french_text, 
                model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    else:
        return ''

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
