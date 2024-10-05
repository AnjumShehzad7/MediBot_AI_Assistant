from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet

class ActionBookDoctor(Action):

    def name(self) -> Text:
        return "action_book_doctor"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        doctor = tracker.get_slot('doctor')
        date = tracker.get_slot('date')
        
        # Mock booking system
        appointment_confirmed = f"Appointment with Dr. {doctor} on {date} has been confirmed."

        dispatcher.utter_message(text=appointment_confirmed)
        return []

class ActionLogSymptoms(Action):

    def name(self) -> Text:
        return "action_log_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        symptoms = tracker.get_slot('symptom')
        
        # Log symptoms (mock action)
        symptom_log = f"Your symptoms: {symptoms} have been logged."

        dispatcher.utter_message(text=symptom_log)
        return []

class ActionRemindMedication(Action):

    def name(self) -> Text:
        return "action_remind_medication"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        time = tracker.get_slot('time')
        
        reminder_message = f"Reminder: Don't forget to take your medication at {time}."
        dispatcher.utter_message(text=reminder_message)
        return []
