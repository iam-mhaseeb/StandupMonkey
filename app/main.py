import os
import logging

from slack_bolt import App

LOGGER = logging.getLogger(__name__)

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)

STANDUP_STATUS = {
    'yesterday': '',
    'today': '',
    'blocker': '',
}


def check_standup_status_submission_completed():
    if STANDUP_STATUS['yesterday'] and STANDUP_STATUS['today'] and STANDUP_STATUS['blocker']:
        return True

    return False


def ask_standup_status(say):
    say(
        {
            "blocks": [
                {
                    "type": "divider"
                },
                {
                    "dispatch_action": True,
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "lastday-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "What did you do yesterday?",
                        "emoji": True
                    }
                },
                {
                    "dispatch_action": True,
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "today-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "What are you planning to do today?",
                        "emoji": True
                    }
                },
                {
                    "dispatch_action": True,
                    "type": "input",
                    "element": {
                        "type": "plain_text_input",
                        "multiline": True,
                        "action_id": "blocker-action"
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Anything blocking you?",
                        "emoji": True
                    }
                }
            ]
        }
    )


@app.command("/standup")
def repeat_text(ack, say, command):
    ack()
    ask_standup_status(say)


@app.action("lastday-action")
def action_yesterday_standup_status(body, ack, say):
    ack()
    LOGGER.info(body)
    if check_standup_status_submission_completed():
        say(f"<@{body['user']['id']}> submitted standup status.")


@app.action("today-action")
def action_today_standup_status(body, ack, say):
    ack()
    if check_standup_status_submission_completed():
        say(f"<@{body['user']['id']}> submitted standup status.")


@app.action("blocker-action")
def action_blocker_standup_status(body, ack, say):
    ack()
    if check_standup_status_submission_completed():
        say(f"<@{body['user']['id']}> submitted standup status.")
