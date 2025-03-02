import os
import requests
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import os


# # Load API key from .env file
# load_dotenv()
# API_KEY = os.getenv('API_KEY')

# # URL endpoint API, dengan Application ID yang sudah diganti
# url = "https://dashscope-intl.aliyuncs.com/api/v1/apps/4f0f74ce308a435c86613251d38fcf21/completion"

# # Data yang akan dikirimkan dalam request, sesuaikan dengan input yang dibutuhkan API
# data = {
#     "input_text": "Upload an image here or pass an input",  # Ganti ini sesuai input kamu
#     "model": "qwen-max"
# }

# headers = {
#     "Authorization": f"Bearer {API_KEY}",
#     "Content-Type": "application/json"
# }

# # Mengirim POST request
# response = requests.post(url, json=data, headers=headers)

# # Mengecek apakah request berhasil
# if response.status_code == 200:
#     print("Response:", response.json())
# else:
#     print("Failed to get response:", response.status_code, response.text)




# client = OpenAI(
#     api_key=os.getenv("API_KEY"),
#     base_url="https://dashscope-intl.aliyuncs.com/api/v1/apps/4f0f74ce308a435c86613251d38fcf21/completion",
# )

# completion = client.chat.completions.create(
#     model="qwen-max-2025-01-25",
#     messages=[
#       {'role': 'system', 'content': 'You are a helpful assistant.'},
#       {'role': 'user', 'content': 'Which number is larger, 9.11 or 9.8?'}
#     ]
# )

# print(completion.choices[0].message)

# import os
# from http.client import HTTPMessage

# os.system('pip install dashscope')

# import gradio as gr
# from http import HTTPStatus
# import dashscope
# from dashscope import Generation
# from dashscope.api_entities.dashscope_response import Role
# from typing import List, Optional, Tuple, Dict
# from urllib.error import HTTPError

# default_system = 'You are Qwen, created by Alibaba Cloud. You are a helpful assistant.'

# YOUR_API_TOKEN = os.getenv('API_KEY')
# dashscope.api_key = https://dashscope-intl.aliyuncs.com/api/v1/apps/4f0f74ce308a435c86613251d38fcf21/completion

# lagi keder

base_url for SDK: https://dashscope-intl.aliyuncs.com/compatible-mode/v1

HTTP endpoint: POST https://dashscope-intl.aliyuncs.com/compatible-mode/v1/chat/completions
import os
from openai import OpenAI

client = OpenAI(
    # If the environment variable is not configured, replace the following line with: api_key="sk-xxx",
    api_key=os.getenv("DASHSCOPE_API_KEY"),
    base_url="https://dashscope-intl.aliyuncs.com/compatible-mode/v1",
)
completion = client.chat.completions.create(
    model="qwen-vl-plus",  # Here qwen-vl-plus is used as an example. You can change the model name as needed. Model list: https://www.alibabacloud.com/help/en/model-studio/getting-started/models
    messages=[{"role": "user","content": [
            {"type": "text","text": "What is this"},
            {"type": "image_url",
             "image_url": {"url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/dog_and_girl.jpeg"}}
            ]}]
    )
print(completion.model_dump_json())
