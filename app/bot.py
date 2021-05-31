import os

import slack
from slackeventsapi import SlackEventAdapter


def get_slack_event_adapter(app):
    """
    Returns slack event adapter after initializing it with signing secret.
    :param app: Flask app object
    :return: SlackEventAdapter object
    """
    return SlackEventAdapter(os.environ['SIGNING_SECRET_'], '/slack/events', app)


def get_slack_web_client():
    """
    Returns slack web client object after initializing with slack token.
    :return: Slack web client object
    """
    return slack.WebClient(token=os.environ['SLACK_TOKEN_'])


def get_bot_id(client):
    """
    Returns bot id using client object.
    :param client: Slack web client object
    :return: Client id as integer
    """
    return client.api_call("auth.test")['user_id']
