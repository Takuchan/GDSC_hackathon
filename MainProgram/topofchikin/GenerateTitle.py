import google.generativeai as palm
# import vertexai
# from vertexai.language_models import TextGenerationModel
from google.cloud import translate_v2 as translate
import os 

class GenerateTitle:
    def __init__(self):
        self.API_KEY = 'AIzaSyAYjhqxhJoHcHikFFesvYGe2-KSU1pJBPg'
        pass

    def translate_text2jp(self,text):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gdschackathon2023test-6650457dbb53.json"
        translate_client = translate.Client()
        result = translate_client.translate(text, target_language="ja")

        return result["translatedText"]

    def translate_text2en(self,text):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "gdschackathon2023test-6650457dbb53.json"
        translate_client = translate.Client()
        result = translate_client.translate(text, target_language="en")
        # print("Text: {}".format(result["input"]))
        # print("Translation: {}".format(result["translatedText"]))
        return result["translatedText"]

    def process(self,text):
        palm.configure(api_key=self.API_KEY)
        model_id = 'models/text-bison-001'
        engText = self.translate_text2en(text)
        prompt = '''Read the following sentence and make it a 10-word title.
        
        '''+ engText

        completion = palm.generate_text(
            model=model_id,
            prompt=prompt,
            temperature=0.8,
            max_output_tokens=800,
        )


        return self.translate_text2jp(completion.result)
    


