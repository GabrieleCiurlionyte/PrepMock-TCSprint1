# PrepMock

PrepMock is a Streamlit app for practicing software engineering interview questions. It lets you start a mock interview, answer technical questions in a chat-style UI, and receive structured AI feedback based on a reference answer.

This app was created as part of Turing College AI Engineering course homework.

## Features

- Choose an interview difficulty level
- Start and end an interview session
- Answer questions in a chat interface
- Get AI-generated scoring and feedback
- Configure the OpenAI model and prompt type from the sidebar
- Includes a prompt guard to reject clearly manipulative or prompt-injection-style inputs

## Requirements

- Python 3.10+
- An OpenAI API key

## Setup

1. Create and activate a virtual environment.
2. Install dependencies from `requirements.txt`.
3. Add your OpenAI API key to `.env`.

Example `.env`:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run the App

From the project root, run:

```powershell
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
streamlit run app\app.py
```

Streamlit will print a local URL, usually:

```text
http://localhost:8501
```

Open that URL in your browser to use the app.

## Notes

- If PowerShell blocks script execution when activating the virtual environment, run it in a terminal that allows local script execution or activate the environment another way.
- You can also enter the OpenAI API key in the app sidebar if it is not loaded from `.env`.
