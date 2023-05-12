from deep_translator import GoogleTranslator
translated = GoogleTranslator(source='uz', target='en').translate("muushuk bolalari") 

print(translated)

# from translate import Translator
# translator= Translator(to_lang="en", from_lang="uz")
# translation = translator.translate("mushuk bolalari")

# print(translation)



# # import requests
# # import json

# # r = requests.post(
# #     "https://api.deepai.org/chat_response", 

# #     headers = {
# #         "accept": "*/*",
# #         "accept-language": "en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7,uz;q=0.6",
# #         "api-key": "tryit-80100237501-807088b18d163bb96a39a4769025b3f6",
# #         "content-type": "multipart/form-data; boundary=----WebKitFormBoundaryTTwBWJyRc4akBKTZ",
# #         "sec-ch-ua": "\"Google Chrome\";v=\"113\", \"Chromium\";v=\"113\", \"Not-A.Brand\";v=\"24\"",
# #         "sec-ch-ua-mobile": "?0",
# #         "sec-ch-ua-platform": "\"Windows\"",
# #         "sec-fetch-dest": "empty",
# #         "sec-fetch-mode": "cors",
# #         "sec-fetch-site": "same-site",
# #     },
# #     data=json.dumps({
# #         "chat_style":"translate",
# #         "chatHistory":[
# #             {"role":"user","content":"salom"},
# #             {"role":"assistant","content":"Hello.\nCopy"},
# #             {"role":"user","content":"mushik bolalari"},
# #             {"role":"assistant","content":"\"Children of mice\" in Uzbek.\nCopy"},
# #             {"role":"user","content":"mening ismim Jeki"},
# #             {"role":"assistant","content":"\"My name is Jack\" in English.\nCopy"},
# #             {"role":"user","content":"sening isming nima"},
# #             {"role":"assistant","content":"\"What is your name?\" in Uzbek.\nCopy"},
# #             {"role":"user","content":"mening ismim \"muhiddinjon\""},
# #             {"role":"assistant","content":"\"My name is Muhiddinjon\" in proper English.\nCopy"},
# #             {"role":"user","content":"My name is Muhiddinjon"},
# #             {"role":"assistant","content":"Corrected: \"I am called Muhiddinjon.\"\nCopy\nSummarize"},
# #             {"role":"user","content":"mening ismim \"muhiddinjon\""}
# #             ]
# #     })
# # )


# # print(r)
# # print(r.content)
# # # import os
# # # import openai
# # # import requests
# # # import json



# # # r = requests.post(
# # #     'https://chatgpt-api.shn.hk/v1/',
# # #     headers={
# # #         'Content-Type':'application/json'
# # #     },
# # #     data=json.dumps({
# # #         "model": "gpt-3.5-turbo",
# # #         "messages": [{"role": "user", "content": "Hello, how are you?"}]
# # #     })
# # #     )
# # # print(r.content)
# # # print(r.status_code)


# # # # openai.api_key = os.getenv("OPENAI_API_KEY")

# # # # completion = openai.ChatCompletion.create(
# # # #   model="gpt-3.5-turbo",
# # # #   messages=[
# # # #     {"role": "user", "content": "Hello!"}
# # # #   ]
# # # # )

# # # # print(completion.choices[0].message)
