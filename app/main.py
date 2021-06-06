import os

from slack_bolt import App

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


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
    say(f"<@{body['user']['id']}> submitted yesterday's standup status.")


@app.action("today-action")
def action_today_standup_status(body, ack, say):
    ack()
    say(f"<@{body['user']['id']}> submitted today's standup status.")


@app.action("blocker-action")
def action_blocker_standup_status(body, ack, say):
    ack()
    say(f"<@{body['user']['id']}> submitted blocking status.")
