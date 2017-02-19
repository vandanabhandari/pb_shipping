"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import requests
import os
import json


# --------------- Helpers that build all of the responses ----------------------

def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': "SessionSpeechlet - " + title,
            'content': "SessionSpeechlet - " + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }


# --------------- Functions that control the skill's behavior ------------------

def get_welcome_response():
    """ If we wanted to initialize the session to have some attributes we could
    add those here
    """

    session_attributes = {}
    card_title = "Welcome to PB Parcel Tracker"
    speech_output = "Please say first 4 digits of tracking number, followed by word plus and then remaining digits"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "Please tell me your tracking number for usps."
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))


def handle_session_end_request():
    card_title = "Session Ended"
    speech_output = "Thank you for trying the Alexa Skills Kit sample. " \
                    "Have a nice day! "
    # Setting this to true ends the session and exits the skill.
    should_end_session = True
    return build_response({}, build_speechlet_response(
        card_title, speech_output, None, should_end_session))


#----- get tracking ------

def getParcelStatus(intent, session):
    session_attributes = {}
    should_end_session = False
    tracking_number_1 = intent['slots']['One']['value']
    tracking_number_2 = intent['slots']['Two']['value']
    tracking_number_3 = intent['slots']['Three']['value']
    tracking_number_4 = intent['slots']['Four']['value']
    tracking_number_5 = intent['slots']['Five']['value']
    tracking_number_6 = intent['slots']['Six']['value']
    tracking_number_7 = intent['slots']['Seven']['value']
    tracking_number_8 = intent['slots']['Eight']['value']
    tracking_number_9 = intent['slots']['Nine']['value']
    tracking_number_10 = intent['slots']['Ten']['value']
    tracking_number_11= intent['slots']['Eleven']['value']
    tracking_number_12 = intent['slots']['Twelve']['value']
    tracking_number_13 = intent['slots']['Thirteen']['value']
    tracking_number_14 = intent['slots']['Fourteen']['value']
    tracking_number_15 = intent['slots']['Fifteen']['value']
    tracking_number_16 = intent['slots']['Sixteen']['value']
    tracking_number_17 = intent['slots']['Seventeen']['value']
    tracking_number_18 = intent['slots']['Eighteen']['value']
    tracking_number_19 = intent['slots']['Nineteen']['value']
    tracking_number_20 = intent['slots']['Twenty']['value']
    tracking_number_21 = intent['slots']['TwentyOne']['value']
    tracking_number_22 = intent['slots']['TwentyTwo']['value']
    tracking_number = "%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s%s" % (tracking_number_1, tracking_number_2,tracking_number_3, tracking_number_4,tracking_number_5, tracking_number_6,tracking_number_7, tracking_number_8,tracking_number_9, tracking_number_10,tracking_number_11, tracking_number_12,tracking_number_13, tracking_number_14,tracking_number_15, tracking_number_16,tracking_number_17, tracking_number_18,tracking_number_19, tracking_number_20,tracking_number_21, tracking_number_22)
    print("USPS Full Tracking Number ----> %s" % (tracking_number))
    bearer = "Bearer %s" % (session['access_token'])
    url = "https://api-sandbox.pitneybowes.com/shippingservices/v1/tracking/%s?packageIdentifierType=TrackingNumber&carrier=USPS" %(tracking_number)
    r=requests.get(url, headers={"Authorization" : bearer})
    tracking_response = {}
    if(r.status_code == 200):
        tracking_response = json.loads(r.content)
    if('errors' in tracking_response and tracking_response['errors'][0]['errorCode'] == 'PB-APIM-ERR-1003') : #Access Token Expired
        oauth_request(session)
    print(r.content)
    speech_output = "The status of the parcel is "+tracking_response['status']
    reprompt_text = "The status of the parcel is "+tracking_response['status']
    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))

# --------------- Events ------------------

def on_session_started(session_started_request, session):
    """ Called when the session starts """
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    """ Called when the user launches the skill without specifying what they
    want
    """

    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # Dispatch to your skill's launch
    return get_welcome_response()


def oauth_request(session):
    access_key = os.environ['key']
    access_key_value = "Basic "+access_key
    url = 'https://api-sandbox.pitneybowes.com/oauth/token'
    r = requests.post(url, headers={"Authorization": access_key_value,
                                    "Content-Type": "application/x-www-form-urlencoded"},
                           data={"grant_type": "client_credentials"})
    print(r.status_code)
    if(r.status_code == 200):
        j = json.loads(r.content)
        print(j)
        session['access_token'] = j['access_token']


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']
    if('access_token' not in session):
        oauth_request(session)
    print(session['access_token'])
    # Dispatch to your skill's intent handlers
    if intent_name == "Tracking":
        return getParcelStatus(intent, session)
    elif intent_name == "AMAZON.HelpIntent":
        return get_welcome_response()
    elif intent_name == "AMAZON.CancelIntent" or intent_name == "AMAZON.StopIntent":
        return handle_session_end_request()
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    """ Called when the user ends the session.

    Is not called when the skill returns should_end_session=true
    """
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here


# --------------- Main handler ------------------

def lambda_handler(event, context):
    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])
