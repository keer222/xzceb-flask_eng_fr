""" This Module is a translator """
import json
import os
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
from dotenv import load_dotenv

load_dotenv()

apikey = os.environ['apikey']
url = os.environ['url']

authenticator = IAMAuthenticator(apikey)
language_translator = LanguageTranslatorV3(
    version='2021-10-16',
    authenticator=authenticator
)
language_translator.set_service_url(url)

def english_to_french(english_text):
    """ This Function is to translate english to French """
    if (english_text != ''):
        translation = language_translator.translate(english_text, 
                    model_id='en-fr').get_result()
        french_text = translation['translations'][0]['translation']
        return french_text
    else:
        return ''

def french_to_english(french_text):
    """ This function is to translate french to English """
    if (french_text != ''):
        translation = language_translator.translate(french_text, 
                model_id='fr-en').get_result()
        english_text = translation['translations'][0]['translation']
        return english_text
    else:
        return ''