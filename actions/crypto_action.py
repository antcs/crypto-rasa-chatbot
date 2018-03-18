from rasa_core.actions import Action
from rasa_core.events import SlotSet
from . import crypto_connector

class CryptoAction(Action):
   def name(self):
      # type: () -> Text
      return "crypto_action"

   def run(self, dispatcher, tracker, domain):
      # type: (Dispatcher, DialogueStateTracker, Domain) -> List[Event]
     
      # gets the current value from the slot 'currency'
      currency = tracker.get_slot("currency")
      
      result = crypto_connector.call(currency)
      
      # saves the value of result into the slot 'crypto_result'
      return [SlotSet("crypto_result", result)]
