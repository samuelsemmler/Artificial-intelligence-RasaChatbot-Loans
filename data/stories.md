## getNPA path 1
* greet
    - utter_greet
    - utter_ask_help
* helpNPA{"type": "count", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - action_get_getNPA
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getNPA path 2
* helpNPA{"type": "count", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - action_get_getNPA
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getNPA path 3
> check_asked_help
* affirm
    - utter_anything_else
* helpNPA{"type": "count", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - action_get_getNPA
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getNPA path 4
> check_asked_help
* helpNPA{"type": "count", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - action_get_getNPA
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getNPAForeclosed path 1
* greet
    - utter_greet
    - utter_ask_help
* helpNPAForeclosed{"type": "count", "closure": "foreclosed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"closure": "foreclosed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getNPAForeclosed
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getNPAForeclosed path 2
* helpNPAForeclosed{"type": "count", "closure": "foreclosed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"closure": "foreclosed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getNPAForeclosed
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getNPAForeclosed path 3
> check_asked_help
* affirm
    - utter_anything_else
* helpNPAForeclosed{"type": "count", "closure": "foreclosed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"closure": "foreclosed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getNPAForeclosed
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getNPAForeclosed path 4
> check_asked_help
* helpNPAForeclosed{"type": "count", "closure": "foreclosed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"closure": "foreclosed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getNPAForeclosed
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getTimeBasedLoanDisbursed path 1
* greet
    - utter_greet
    - utter_ask_help
* helpTimeBasedLoanDisbursed{"type": "count", "flag": "disbursed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"flag": "disbursed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getTimeBasedLoanDisbursed
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getTimeBasedLoanDisbursed path 2
* helpTimeBasedLoanDisbursed{"type": "count", "flag": "disbursed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"flag": "disbursed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getTimeBasedLoanDisbursed
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getTimeBasedLoanDisbursed path 3
> check_asked_help
* affirm
    - utter_anything_else
* helpTimeBasedLoanDisbursed{"type": "count", "flag": "disbursed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"flag": "disbursed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getTimeBasedLoanDisbursed
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## getTimeBasedLoanDisbursed path 4
> check_asked_help
* helpTimeBasedLoanDisbursed{"type": "count", "flag": "disbursed", "time": "2019-07-24T00:00:00.000+05:30"}
    - slot{"type": "count"}
    - slot{"flag": "disbursed"}
    - slot{"time": "2019-07-24T00:00:00.000+05:30"}
    - action_get_getTimeBasedLoanDisbursed
    - action_slot_reset
    - utter_did_that_help
> check_asked_help

## checkpoint affirm path
> check_asked_help
* affirm
    - utter_anything_else
* deny
    - utter_happy
    - utter_bye

## checkpoint 1 deny path
> check_asked_help
* deny
    - utter_ask_help
    - action_restart

## checkpoint 2 deny path
> check_asked_help
* affirm
    - utter_anything_else
* affirm
    - utter_ask_help
    - action_restart

## bye path
* bye
    - utter_bye
    - action_restart
