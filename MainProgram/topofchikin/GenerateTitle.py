import google.generativeai as palm
# import vertexai
# from vertexai.language_models import TextGenerationModel
from google.cloud import translate_v2 as translate
import os 



class GenerateTitle:
    def __init__(self):
        self.API_KEY = ''
        pass


    def translate_text2jp(self,text):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""
        translate_client = translate.Client()
        result = translate_client.translate(text, target_language="ja")

        return result["translatedText"]

    def translate_text2en(self,text):
        os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = ""
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
    



# model_list = [_ for _ in palm.list_models()]
# for model in model_list:
#     print(model.name)



# class GenerateTitle:
#     def __init__(self):
#         pass

#     def generate_title(self, text):
#         vertexai.init(project="gdschackathon2023test", location="us-central1")
#         parameters = {
#             "candidate_count": 1,
#             "max_output_tokens": 1024,
#             "temperature": 0.2,
#             "top_p": 0.8,
#             "top_k": 40
#         }
#         model = TextGenerationModel.from_pretrained("text-bison")
#         response = model.predict(
#             """以下の文章を10文字程度のタイトルにしてください。 {}""".format(text),
#             **parameters
#         )
#         print(f"Response from Model: {response.text}")
#         return response.text

