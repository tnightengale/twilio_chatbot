# Twilio Chatbot with SQLite Integration

## Information:

This project plays with twilio programmable SMS services. It's an agile proof-of-concept chatbot that can store responses in an SQLite database for later analysis.

## Usage:

1. Copy the repo.
2. Install dependencies with pip.
3. Edit the `env_vars` with your own credentials and SQLite database path.
4. Add variables to the environments with `$ source env_vars`.
5. Edit the `message.txt`, and `recipients.csv` with the message you would like to text to the recipients.
6. Adjust the response in `response_webhook.py`. This determines what your chatbot will say when someone replies to it.
7. Run from terminal `$ send_messages.py`.