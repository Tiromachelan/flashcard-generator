# flashcard-generator
Automatically generate flashcards from text using the OpenAI API.  The goal is eventually to produce an Anki deck; as of now, only terminal output is supported.


## Dependencies:
Python 3 and the following pip packages:
- openai
- python-dotenv
- PyQt6


## Installation:
### Windows:
Run `.\install.bat`

### Unix:
Run `chmod +x install.sh`, and then `./install.sh`


## Configuration
You will need to create an OpenAI API key and paste it in the `.env` file, which is created by the install scripts.  All settings are stored in `config.json`.


## Usage:
Paste your text into `user_input.txt` and run `main.py`
