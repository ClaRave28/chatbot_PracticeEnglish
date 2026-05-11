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

---

# chatbot_PracticeEnglish

## Table des matières
1. [Introduction](#1-introduction)
2. [Technologies utilisées](#2-technologies-utilisées)
3. [Liste des fonctionnalités](#3-liste-des-fonctionnalités)
4. [Comment lancer le projet ?](#4-comment-lancer-le-projet-)
<!-- 5. [Aperçu](#5-aperçu) -->

---

## 1. Introduction

Petit projet personnel réalisé pour le fun, dans le but d'expérimenter avec l'**API OpenAI**. L'idée était de créer un chatbot vocal simple pour s'entraîner à parler anglais — on parle dans le micro, le bot comprend et répond à voix haute grâce à GPT.

Il s'agit d'un mini projet personnel, pas d'une application de production.

---

## 2. Technologies utilisées

- **Python 3.13**
- **OpenAI API** (`gpt-3.5-turbo`) — génère les réponses du chatbot
- **pyttsx3** — synthèse vocale (le bot parle à voix haute)
- **SpeechRecognition** — capture et transcription de la voix via Google Speech Recognition
- **PyAudio** — accès au microphone
- **python-dotenv** — chargement de la clé API depuis un fichier `.env`

---

## 3. Liste des fonctionnalités

- Écoute l'utilisateur via le microphone
- Transcrit la parole en texte via Google Speech Recognition
- Envoie le texte à l'API OpenAI et récupère une réponse
- Lit la réponse à voix haute grâce à la synthèse vocale
- Dire `"exit"` pour arrêter la conversation

---

## 4. Comment lancer le projet ?

**Prérequis :** Python 3.x, une clé API OpenAI

**1. Installer les dépendances :**

```bash
pip install pyttsx3 speechrecognition openai pyaudio python-dotenv
```

> Si `pyaudio` échoue sur Windows :
> ```bash
> pip install pipwin
> pipwin install pyaudio
> ```

**2. Créer un fichier `.env`** à la racine du projet :

```
OPENAI_API_KEY=ta_clé_api_ici
```

**3. Lancer le script :**

```bash
python SpeakEnglish.py
```

---

<!-- ## 5. Aperçu

*(screenshot / démo à venir)* -->