import os
import subprocess
import whisper
from moviepy import VideoFileClip

def extract_audio(video_path, audio_path):
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(audio_path, codec="pcm_s16le", fps=16000)

def transcribe_audio(audio_path):
    model = whisper.load_model("base")
    result = model.transcribe(audio_path, language='ru')
    return result['text']


def main(video_path):
    audio_path = "audio.wav"
    extract_audio(video_path, audio_path)
    text = transcribe_audio(audio_path)
    print("Распознанный текст:")
    print(text)

if __name__ == "__main__":
    video_file = "pbc_515447164_9lh8gtpepnyyj75_video_iiyrs6d7qd.wpm"  # Укажи свой путь к видео
    main(video_file)
