
# Trippy: Virtual Travel Chatbot

A lightweight, rule-based Python chatbot designed to assist users in discovering their ideal travel destinations based on personal preferences like beaches, mountains, budget options, or local cuisines. 

# Features
- **Input Sanitization:** Automatically cleans whitespace and normalizes text casing to ensure smooth user interactions.
- **Regex Keyword Matching:** Utilizes exact word boundaries to prevent accidental string triggers (e.g., matching "eat" inside "weather").
- **Dynamic Fallbacks:** Uses randomized fallback responses to keep the conversation feeling natural when an input isn't recognized.
- **Robust Error Handling:** Safely intercepts terminal interrupts (`Ctrl+C`, `Ctrl+D`) to exit gracefully without throwing ugly crash traces.

##  Built With
- **Python 3.12 (Standard libraries: `random`, `re`)

## 💻 How to Run
1. Clone this repository or download the `chatbot.py` script.
2. Open your terminal or command prompt in the project folder.
3. Execute the script using:
```bash
   python chatbot.py
