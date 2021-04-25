from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet, AllSlotsReset, Restarted
from random import randint
import re


class ActionGetNPA(Action):

    def name(self):
        return "action_get_getNPA"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        time = tracker.get_slot('time')

        message = f'A NPA em {time}: {randint(1, 10000)}'
        dispatcher.utter_message(message)

        return []


class ActionGetNPAForeclosed(Action):

    def name(self):
        return "action_get_getNPAForeclosed"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        time = tracker.get_slot('time')

        message = f'Total de empréstimos excluídos em {time}: {randint(1, 10000)}'
        dispatcher.utter_message(message)

        return []


class ActionGetTimeBasedLoanDisbursed(Action):

    def name(self):
        return "action_get_getTimeBasedLoanDisbursed"

    def run(self, dispatcher, tracker, domain):
        typo = tracker.get_slot('type')
        time = tracker.get_slot('time')

        message = f'Total de empréstimos desembolsado em {time}: {randint(1, 10000)}'
        dispatcher.utter_message(message)

        return []


class ActionRestarted(Action):
    def name(self):
        return 'action_restarted'

    def run(self, dispatcher, tracker, domain):
        return[Restarted()]


class ActionSlotReset(Action):
    def name(self):
        return 'action_slot_reset'

    def run(self, dispatcher, tracker, domain):
        return[AllSlotsReset()]
