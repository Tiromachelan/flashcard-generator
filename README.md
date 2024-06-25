# flashcard-generator
Automatically generate flashcards from text using the OpenAI API.  The goal is eventually to produce an Anki deck; as of now, only terminal output is supported.  Be aware that AI sometimes makes mistakes.


## Dependencies:
Python 3 and the following pip packages:
- openai
- python-dotenv
- PyQt6
- pypdf


## Installation:
### Windows:
Run `.\install.bat`

### Unix:
Run `chmod +x install.sh`, and then `./install.sh`


## Configuration
You will need to create an OpenAI API key and paste it in the `.env` file, which is created by the install scripts.  All settings are stored in `config.json`.


## Usage:
Run `python main.py <name of file here>`.  Currently supported filetypes are `.txt` and `.pdf`.  Make sure that they are with the OpenAI API's context length, since automatic checking is not yet supported.  As of now, PDF support does not work very well, especially if the PDF is more than 1 page.
