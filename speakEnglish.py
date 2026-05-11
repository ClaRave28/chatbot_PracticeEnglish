# -*- coding: utf-8 -*-
import pyttsx3
import speech_recognition as sr
from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def listen():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        try:
            audio = recognizer.listen(source)
            text = recognizer.recognize_google(audio)
            print(f"You: {text}")
            return text
        except sr.UnknownValueError:
            print("Could not understand audio.")
            return ""
        except sr.RequestError:
            print("Speech Recognition service is unavailable.")
            return ""

def chat_with_bot():
    print("Chatbot: Hello! Let's practice English. Say 'exit' to stop.")
    speak("Hello! Let's practice English. Say 'exit' to stop.")

    while True:
        user_input = listen()
        if user_input.lower() == "exit":
            print("Chatbot: Goodbye! Keep practicing your English!")
            speak("Goodbye! Keep practicing your English!")
            break

        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": user_input}]
        )

        bot_reply = response.choices[0].message.content
        print(f"Chatbot: {bot_reply}")
        speak(bot_reply)

if __name__ == "__main__":
    chat_with_bot()