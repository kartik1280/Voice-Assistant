# Voice Assistant

A Python-based voice assistant that uses speech recognition and text-to-speech technologies to interact with users through voice commands. This assistant can perform tasks like opening websites, playing music, and answering queries, providing a hands-free way to control your computer.

## Features

- Voice recognition for natural language commands
- Text-to-speech responses
- Integration with common applications and websites
- Customizable command handling

## Installation

Make sure you have Python 3.13.7 installed.
Install the required packages:
pip install speechrecognition pyttsx3 pyaudio

You may also need to install system dependencies for `pyaudio` depending on your platform.

## Usage

Run the assistant script:
python voice_assistant.py

Speak commands clearly into the microphone. The assistant will respond via voice and perform the requested tasks.

1. Install All Dependencies
Make sure you have Python installed. Then, install these required libraries if you haven't done so:
pip install speechrecognition pyttsx3 pyaudio wikipedia newsapi-python
(If using your own music library dictionary, keep music_library.py in the same folder.)

2. Obtain an API Key for News
Go to newsapi.org, sign up, and get your API key.
Open main.py and paste your API key in place of "":
python
newsapi = NewsApiClient(api_key="YOUR_API_KEY_HERE")

3. Set Up Your Microphone
Plug in a working microphone.
Make sure no other program is using the microphone.

4. Run the Script
Navigate to your project folder in the terminal and run:
python main.py

6. How to Interact with Jarvis
Wait for the program to say "Initializing jarvis..."
Speak the wake word: "jarvis"
After hearing "yes," speak your command, such as:
"play blinding lights"
"open instagram"
"tell me the headlines"
"wikipedia The Weeknd"

6. Supported Commands
"play [song]" – Plays from your music library.
"open instagram/google/youtube/spotify" – Opens the site in your browser.
"headlines" – Reads out the top 5 news headlines.
"wikipedia [topic]" – Reads a short summary from Wikipedia.

8. Errors and Troubleshooting
If Jarvis doesn’t recognize your voice, check your mic and speak clearly.
Make sure your internet connection is active for Wikipedia and news features.
If you get an API key error, ensure your key is copied correctly.

## Customization

- Add or modify commands and responses in the script to suit your needs.
- Integrate additional APIs or services for enhanced functionality.
- Adjust voice settings such as rate, volume, and voice type.

## License

This project is for learning purposes. Feel free to use and modify it with proper credit.

## Contributing

Contributions are welcome! Please fork the repository and submit pull requests with improvements or new features.

## Author
Kartik Sharma


