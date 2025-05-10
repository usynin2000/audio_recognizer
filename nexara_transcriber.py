import requests
from config import API_KEY
url = "https://api.nexara.ru/api/v1/audio/transcriptions"
api_key = API_KEY

headers = {
    "Authorization": f"Bearer {api_key}",
}

file_path = "test_record.mp3"

with open(file_path, "rb") as audio_file:
    files = {
        "file": (file_path, audio_file, "audio/mpeg"), # Use 'audio/mpeg' for MP3
    }
    data = {
        "response_format": "verbose_json",
    }

    response = requests.post(url, headers=headers, files=files, data=data)

    if response.status_code == 200:
        transcription = response.json()
        print(transcription)
    else:
        print(f"Error: {response.status_code}")
        print(response.text)