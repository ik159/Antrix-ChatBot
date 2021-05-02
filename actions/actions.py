# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
#
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []

class ActionHelloWorld(Action):

    def name(self) -> Text:
        return "action_ask_for_asymptomatic"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        dispatcher.utter_message(text="Rest. It can make you feel better and may speed your recovery.Drink fluids. You lose more water when you're sick. Dehydration can make symptoms worse and cause other health problems.")

        return []


class ActionCheckLevel(Action):

    def name(self) -> Text:
        return "action_check_level"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == 'o2level':
                name = e['value']
                converted_num = int(name)
            if converted_num > 94:
                message = "Your oxygen level is perfect , normal range is 95-100"
            if converted_num < 94:
                message = "Your oxygen level is below the normal range is 95-100 , please contact doctor immediately"
            else :
                message = "sorry , the range has to be in 95-100"
        dispatcher.utter_message(text=message)

        return []


class ActionSearchMedicine(Action):

    def name(self) -> Text:
        return "action_display_medicines"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        entities = tracker.latest_message['entities']
        for e in entities:
            if e['entity'] == 'medicine':
                name = e['value']
            if name == "fever":
                message = "Take Paracetamol twice a day"
            if name == "cold":
                message = "Please take Ibuprofen once a day"
            if name == "cough":
                message = "3 spposn of benadryl syrup twice a day"
            if name == "running nose":
                message = "Advisable to takre Diphenhydramine"
        dispatcher.utter_message(text=message)

        return []
