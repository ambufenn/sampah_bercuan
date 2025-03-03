import os
import requests
from dotenv import load_dotenv
import streamlit as st
from openai import OpenAI
import os
from http.client import HTTPMessage

# Load API key
load_dotenv()
API_KEY = os.getenv("API_KEY")

API_URL = "https://dashscope-intl.aliyuncs.com/api/v1/apps/4f0f74ce308a435c86613251d38fcf21/completion"

st.title("Sampah Bercuan - Deteksi Kategori Sampah")

# Upload image
uploaded_file = st.file_uploader("Pilih gambar...", type=["jpg", "png", "jpeg"])

if uploaded_file is not None:
    st.image(uploaded_file, caption="Gambar yang diupload", use_column_width=True)

    # HARUS upload dulu ke server yang bisa diakses publik
    img_url = "https://your-public-image-url.com/image.jpg"

    # List model yang dipakai
    models = ["qwen-vl-plus", "qwen-vl-max"]
    results = {}

    for model in models:
        data = {
            "model": model,
            "messages": [
                {"role": "user", "content": [
                    {"type": "text", "text": "Kategori sampah apakah ini?"},
                    {"type": "image_url", "image_url": {"url": img_url}}
                ]}
            ]
        }

        headers = {
            "Authorization": f"Bearer {API_KEY}",
            "Content-Type": "application/json"
        }

        response = requests.post(API_URL, json=data, headers=headers)

        if response.status_code == 200:
            results[model] = response.json()
        else:
            results[model] = f"Error {response.status_code}: {response.text}"

    # Tampilkan hasil kedua model
    for model, result in results.items():
        st.subheader(f"Hasil dari {model}:")
        st.write(result)
