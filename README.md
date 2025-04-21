# MediBot AI Assistant 

**MediBot AI Assistant** is a healthcare chatbot built with [Rasa](https://rasa.com/). 
It helps users book doctor appointments, log symptoms, and receive medication reminders.

## Features

* Doctor Appointment Booking: Schedule appointments with doctors.
* Symptom Logging: Log and track symptoms.
* Medication Reminders: Set and get reminders for taking medications.

## Installation

1. Clone the Repo:
```
git clone https://github.com/YOUR_USERNAME/MediBot_AI_Assistant.git cd MediBot_AI_Assistant
```

2. Create and Activate Virtual Environment:
`python -m venv rasa_env`
`source_path/rasa_env/bin/activate`

3. Train the Model:
`rasa train`

4.  Run the Bot (Both commands in seperate terminal):
`rasa run`
`rasa run actions`

5. Talk to the Bot:
`rasa shell`


## Custom Actions

* `action_book_doctor`: Books a doctor appointment.
* `action_log_symptoms`: Logs user symptoms.
* `action_remind_medication`: Sends medication reminders.

## Debugging

If you encounter issues or want to trace the bot's behavior in detail, run the bot in **debug mode**:
`rasa shell --debug`

This will display detailed logs of how the bot processes user inputs, predicts actions, and manages slots. 
Use this to trace any issues with intents, responses, or custom actions.

## Project Structure

├── actions.py         **- Custom actions**

├── config.yml         **- NLU and policies config**

├── data/              **- Training data (nlu, stories, rules)**

├── domain.yml         **- Slots, intents, and responses**

└── endpoints.yml      **- Action server configuration**
