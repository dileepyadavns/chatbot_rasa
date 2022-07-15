# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import requests

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

# class ActionCoronaCases(Action):
#     try:
#         def name(self) -> Text:
#          return "actions_corona_state_stat"

#         def run(self, dispatcher: CollectingDispatcher,

#              tracker: Tracker,
#              domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#          response=requests.get("https://data.covid19india.org/data.json").json()
#          entities=tracker.latest_message['entities']
#          print("Last message Now",entities)
#          state=None
#          for e in entities:
#              if e["entity"]=="state":
#                 state=e["value"]
#          message="please enter valid state in india "
#          for data in response["statewise"]:
#              str1=state.title()
#              str2=data['state']
#              c=0
#              j=0
#              for i in str1:    
#                  if str2.find(i)>= 0 and j == str1.find(i): 
#                      c += 1
#                  j += 1

#              if c>int(len(str2)/2):
#                  print(data)
#                  message="Active: "+ data["active"]+"  Conformed: "+ data["confirmed"]+"  Recovered: "+ data["deltarecovered"] +" On: " + data["lastupdatedtime"]
#              continue
                 
#          dispatcher.utter_message(message)
#          return []
#     except:
#         pass

  
class ActionCoronaCases(Action):
    try:
        def name(self) -> Text:
         return "actions_corona_state_stat"

        def run(self, dispatcher: CollectingDispatcher,

             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         response=requests.get("https://data.covid19india.org/data.json").json()
         entities=tracker.latest_message['entities']
         print("Last message Now",entities)
         state=None
         for e in entities:
             if e["entity"]=="state":
                state=e["value"]
         message="please enter valid state in india "
         ct=0
         max1=''
         for data in response["statewise"]:
             str1=state.title()
             str2=data['state']
             c=0
             j=0
             for i in str1:    
                 if str2.find(i)>= 0 and j == str1.find(i): 
                     c += 1
                 j += 1

             if c>ct:
                 ct=c
                 max1=data
         message="Active: "+ max1["active"]+"  Conformed: "+ max1["confirmed"]+"  Recovered: "+ max1["deltarecovered"] +" On: " + max1["lastupdatedtime"]
                   
         dispatcher.utter_message(message)
         return []
    except:
        pass


