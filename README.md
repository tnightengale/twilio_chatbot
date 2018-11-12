#Twilio Chatbot w. SQLite Integration

##Information:

This project is the play with twilio programmable SMS services. It's an agile proof-of-concept chatbot that can store responses in an SQLite database for later analysis.

##Usage:

1. Copy the repo.
2. Install dependencies with pip.
3. Edit the `env_vars` with your own credentials and SQLite server.
4. Edit the `message.txt`, and `recipients.csv` with the message you would like to text to recipients.
5. Adjust the response in `response_webhook.py`.
6. Run from terminal `$ send_messages.py`.