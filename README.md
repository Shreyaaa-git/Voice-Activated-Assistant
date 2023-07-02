# Voice-Activated-Assistant
We designed and implemented a voice-activated assistant that can perform various tasks based on user commands.The assistant listens for a wakeup command, recognizes and extracts meaningful words from the user's voice input, and performs different actions accordingly. It utilizes speech recognition, natural language processing, and external APIs to provide a seamless user experience.

Features:
Wakeup Command: The assistant is activated when the user says "hello."
Time and Date: The assistant can retrieve the current time and date upon user request.
Weather Information: The assistant can fetch weather information for a specified city using an external weather API.
ChatGPT Integration: When a specific command is not recognized, the assistant uses the ChatGPT API to generate responses based on user queries.
Exit Command: The user can exit the assistant by saying "exit."

Requirements:
Python 3.x
Requests library (pip install requests)
SpeechRecognition library (pip install SpeechRecognition)
Pyttsx3 library (pip install pyttsx3)
OpenAI library (pip install openai)

Usage:
Install the required libraries mentioned above.
Set up the OpenAI API by obtaining an API key. Replace "YOUR_API_KEY" in the code with your actual API key.
Run the script main.py using Python.
Once the assistant is activated, you can give voice commands and wait for the assistant to respond.
Use commands like "time now" to get the current time, "date today" to get the current date, and include the word "weather" to fetch weather information for a specific city.
If a specific command is not recognized, the assistant will use ChatGPT to generate a response based on your query.
To exit the assistant, say "exit."
