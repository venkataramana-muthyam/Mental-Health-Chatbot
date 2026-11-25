Mental Health Support Chatbot
Project Type: Academic Mini Project
Domain: Artificial Intelligence / Mental Health
Author: VenkataRamana Muthyam

1. Project Description
This project is an AI-powered mental health assistant designed to provide supportive and empathetic conversations. It integrates an open-source Large Language Model (LLM) to generate human-like responses. The system features keyword-based mood detection to adjust the chatbot’s tone based on the user's emotions, all presented through a clean and interactive Streamlit user interface for real-time chat.

2. Objective
The main goals of this project are:

To support users emotionally using Artificial Intelligence.

To detect the user's mood, such as stress, sadness, or anxiety.

To provide self-care tools like positive affirmations and guided meditation.

To create a calm and user-friendly interface.

3. Technologies Used
Python 3: The core programming language.

Streamlit: Used for building the Frontend UI.

Ollama: The local runtime environment used to run the LLM (Qwen 2.5 3B).

4. Key Features
AI-based Chat Conversation: Real-time chatting with an AI model.

Mood Detection: Detects emotions like Stress, Sadness, Anxiety, and Emergency situations.

Mental Health Area Classification: Categorizes the conversation into specific health areas (e.g., Social, Cognitive, Academic).

Self-Care Tools: Generates positive affirmations and guided meditation scripts.

Session Summary: Provides a summary of the most discussed mental health areas during the chat session.

5. Folder Structure
The project consists of a simple and clean folder structure:

app.py (The main application code)

TXT.md (The project documentation)

6. How to Run the Application
To run this project on your local machine, follow these steps:

Install Python 3.10 or higher.

Install the required libraries by running the following command in your terminal:
pip install streamlit ollama

Download the required AI model by running:
ollama pull qwen2.5:3b

Start the application by running:
streamlit run app.py

7. Disclaimer
This chatbot is intended for mental health support only. It is not a replacement for professional medical or psychological treatment.

8. Future Enhancements
In the future, this project can be improved by adding:

Voice input and output capabilities.

Multilingual support (English & Telugu).

Advanced mood analytics with visual charts.

User authentication for privacy.

Custom CSS backgrounds and animations.