# chatbot_PracticeEnglish

## Table of contents
1. [Introduction](#1-introduction)
2. [Tools using](#2-tools-using)
3. [Features list](#3-features-list)
4. [How to launch ?](#4-how-to-launch-)
<!-- 5. [Preview](#5-preview) -->

---

## 1. Introduction

A small personal project built for fun to experiment with the **OpenAI API**. The idea was to create a simple voice chatbot to practice speaking English — you speak into your microphone, the bot understands you and replies out loud using GPT.

This is a mini side project, not a production application.

---

## 2. Tools using

- **Python 3.13**
- **OpenAI API** (`gpt-3.5-turbo`) — generates the chatbot's responses
- **pyttsx3** — text-to-speech (the bot speaks out loud)
- **SpeechRecognition** — captures and transcribes voice input via Google Speech Recognition
- **PyAudio** — microphone access
- **python-dotenv** — loads the API key from a `.env` file

---

## 3. Features list

- Listens to the user via microphone
- Transcribes speech to text using Google Speech Recognition
- Sends the text to the OpenAI API and gets a response
- Reads the response out loud using text-to-speech
- Say `"exit"` to stop the conversation

---

## 4. How to launch ?

**Prerequisites:** Python 3.x, an OpenAI API key

**1. Install dependencies:**

```bash
pip install pyttsx3 speechrecognition openai pyaudio python-dotenv
```

> If `pyaudio` fails on Windows:
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

**2. Create a `.env` file** at the root of the project:

```
OPENAI_API_KEY=your_api_key_here
```

**3. Run the script:**

```bash
python speakEnglish.py
```

---

<!-- ## 5. Preview

*(screenshot / demo coming soon)* -->