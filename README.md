
# FRIDAY - Voice Activated Virtual Assistant

- Friday is a voice-activated assistant excelling in tasks like web browsing, music playback, news fetching, and handling complex user queries using Google AI Studio Gemini.

- It swiftly navigates websites, plays music through its musicLibrary, and responds intelligently to ”Hey Friday” , enhancing digital experience seamlessly, functions akin to Alexa or Google Assistant, ensuring unmatched efficiency


### FEATURES

- Voice Recognition
- Activates upon detecting the wake word "Hey Friday"
- Uses gTTS (Google Text-to-Speech) and pygame for playback.
- Opens websites like Google, Facebook, YouTube etc. based on voice commands like "Open Google"
- Music Playback , interfaces with a musicLibrary module to play songs via web links,based on voice commands like "play 'song name' "
- Fetches and reads the latest news headlines using NewsAPI.
- Handles complex queries and generates responses using Google AI Studio Gemini
- Acts as a general virtual assistant similar to Alexa or Google Assistant


### WORKFLOW

- Initialization
- Greets the user with "Initializing Friday...."
- Wake Word Detection, listens for the wake word "Hey Friday"
- Acknowledges activation by saying "Hii 'username', ask me anything"
- Processes commands to determine actions such as opening a website, playing music, fetching news, or generating a response via OpenAI.
- Speech Output, Provides responses using speak function with gTTS
- After completion of the task, it again waits for the Wake Word, and process commands accordingly following the same procedure
