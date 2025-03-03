import os
import requests
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import os
from http.client import HTTPMessage
from alibabacloud_dashscope import DashScope
import requests



# Load environment variables
load_dotenv()
os.environ["DASHSCOPE_API_KEY"] = os.getenv("API_KEY")

# Base URL for Alibaba DashScope API
API_BASE_URL = "https://dashscope-intl.aliyuncs.com/api/v1/apps/4f0f74ce308a435c86613251d38fcf21/completion"

# Initialize DashScope client
client = DashScope()


def categorize_image(file_path):
    """Upload image & categorize using Qwen-VL"""
    model = "qwen-vl-plus"
    url = f"{API_BASE_URL}/vision_interpretation"

    headers = {
        "Authorization": f"Bearer {os.getenv('DASHSCOPE_API_KEY')}",
        "Content-Type": "multipart/form-data"
    }

    files = {"file": open(file_path, "rb")}

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        category = response.json().get("category", "Unknown")
        return category
    else:
        return f"Error {response.status_code}: {response.json()}"


def chatbot_response(category):
    """Chatbot response using Qwen-Max"""
    model = "qwen-max"
    url = f"{API_BASE_URL}/chat/completions"

    headers = {
        "Authorization": f"Bearer {os.getenv('DASHSCOPE_API_KEY')}",
        "Content-Type": "application/json"
    }

    prompt = f"Apa manfaat dari sampah kategori {category}?"
    payload = {
        "model": model,
        "messages": [{"role": "user", "content": prompt}]
    }

    response = requests.post(url, headers=headers, json=payload)

    if response.status_code == 200:
        return response.json().get("message", "No response")
    else:
        return f"Error {response.status_code}: {response.json()}"


def main():
    file_path = "test_image.jpg"  # Ganti dengan path gambar yang diupload
    category = categorize_image(file_path)
    print(f"Kategori: {category}")

    chat_response = chatbot_response(category)
    print(f"Chatbot: {chat_response}")


if __name__ == "__main__":
    main()




















# #set up enviroment
# set_environment_variabel()

# #initialise the client
# client = alibaba (api_key= os.getenv("API_KEY")
    
# )



# def find_the_image(file_image):
#     response= client.
                   


    



# # Load API key
# load_dotenv()
# API_KEY = os.getenv("API_KEY")

# API_URL = "https://dashscope-intl.aliyuncs.com/api/v1/apps/4f0f74ce308a435c86613251d38fcf21/completion"

# st.title("Sampah Bercuan - Deteksi Kategori Sampah")

# # Upload image
# uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "png", "jpeg"])

# if uploaded_file is not None:
#     st.image(uploaded_file, caption="Gambar yang diupload", use_column_width=True)

#     # HARUS upload dulu ke server yang bisa diakses publik
#     img_url = "https://your-public-image-url.com/image.jpg"

#     # List model yang dipakai
#     models = ["qwen-vl-plus", "qwen-max"]
#     results = {}

#     for model in models:
#         data = {
#             "model": model,
#             "messages": [
#                 {"role": "user", "content": [
#                     {"type": "text", "text": "Kategori sampah apakah ini?"},
#                     {"type": "image_url", "image_url": {"url": img_url}}
#                 ]}
#             ]
#         }

#         headers = {
#             "Authorization": f"Bearer {API_KEY}",
#             "Content-Type": "application/json"
#         }

#         response = requests.post(API_URL, json=data, headers=headers)

#         if response.status_code == 200:
#             results[model] = response.json()
#         else:
#             results[model] = f"Error {response.status_code}: {response.text}"

#     # Tampilkan hasil kedua model
#     for model, result in results.items():
#         st.subheader(f"Hasil dari {model}:")
#         st.write(result)
