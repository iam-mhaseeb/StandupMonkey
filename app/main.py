import os

from slack_bolt import App

from app.db import upsert_today_standup_status

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


def check_standup_status_submission_completed():
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
def standup_command(ack, say, command):
    ack()
    ask_standup_status(say)


@app.action("lastday-action")
def action_yesterday_standup_status(body, ack, say):
    ack()
    user_id = body['user']['id']
    msg = body['actions'][0]['value']
    import json
    print(json.dumps(body))
    say(f"<@{body['user']['id']}> submitted standup status with message: {msg}.")
    # upsert_today_standup_status(user_id, 'yesterday', msg)
    if check_standup_status_submission_completed():
        say(f"<@{body['user']['id']}> submitted standup status.")


@app.action("today-action")
def action_today_standup_status(body, ack, say):
    ack()
    user_id = body['user']['id']
    msg = body['actions'][0]['value']
    say(f"<@{body['user']['id']}> submitted standup status with message: {msg}.")
    # upsert_today_standup_status(user_id, 'today', msg)
    if check_standup_status_submission_completed():
        say(f"<@{body['user']['id']}> submitted standup status.")


@app.action("blocker-action")
def action_blocker_standup_status(body, ack, say):
    ack()
    user_id = body['user']['id']
    msg = body['actions'][0]['value']
    say(f"<@{body['user']['id']}> submitted standup status with message: {msg}.")
    # upsert_today_standup_status(user_id, 'blocker', msg)
    if check_standup_status_submission_completed():
        say(f"<@{body['user']['id']}> submitted standup status.")
