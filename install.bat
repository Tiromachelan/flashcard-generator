@echo off

REM Create the .env file with OPENAI_API_KEY=
echo OPENAI_API_KEY=> .env

REM Install the required pip packages
pip install openai
pip install python-dotenv
pip install PyQt6
