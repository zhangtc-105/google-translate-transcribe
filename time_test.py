import io
import time
from google.cloud import speech_v1p1beta1 as speech
from google.cloud import translate_v2 as translate

def transcribe_audio(file_path):
    client = speech.SpeechClient()
    with io.open(file_path, "rb") as audio_file:
        content = audio_file.read()
    audio = speech.RecognitionAudio(content=content)
    config = speech.RecognitionConfig(
        encoding=speech.RecognitionConfig.AudioEncoding.LINEAR16,
        sample_rate_hertz=16000,
        language_code="en-US",
    )

    start_time = time.time()
    response = client.recognize(config=config, audio=audio)
    end_time = time.time()
    
    transcribe_time = end_time - start_time
    transcription = ""
    for result in response.results:
        transcription += result.alternatives[0].transcript
    
    return transcription, transcribe_time


def translate_text(text, target_language):
    client = translate.Client()
    start_time = time.time()
    result = client.translate(text, target_language=target_language)
    end_time = time.time()
    
    translation_time = end_time - start_time
    translation = result['translatedText']
    
    return translation, translation_time


def main():
    # Replace with the path to your audio file
    file_path = "path_to_your_audio_file.wav"
    target_language = "es"  # Translate to Spanish
    
    transcription, transcribe_time = transcribe_audio(file_path)
    print(f"Transcription: {transcription}")
    print(f"Time taken for transcription: {transcribe_time} seconds")
    
    translation, translation_time = translate_text(transcription, target_language)
    print(f"Translation: {translation}")
    print(f"Time taken for translation: {translation_time} seconds")


if __name__ == "__main__":
    main()