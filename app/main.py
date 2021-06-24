import os

from slack_bolt import App

from app.db import upsert_today_standup_status, get_today_standup_status

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


def check_standup_status_submission_completed(today_standup_status):
    """
    Checks if standup status is complete for user.
    :param today_standup_status: Today's standup status
    :return: True if standup is complete otherwise False
    """
    if today_standup_status[2] \
            and today_standup_status[3] \
            and today_standup_status[4] \
            and today_standup_status[5]:
        return True

    return False


def post_standup_completion_message(user_id, say):
    """
    Post standup completion message to selected channel.
    :param user_id: User for which standup needs to be posted
    :return: None
    """
    today_standup_status = get_today_standup_status(user_id)
    if check_standup_status_submission_completed(today_standup_status):
        say(
            text={
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"<@{user_id}> submitted standup status for {today_standup_status[1]} 🎉."
                        }
                    },
                    {
                        "type": "divider"
                    },
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Yesterday's standup status:",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"{today_standup_status[2]}"
                        }
                    },
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Today's standup status:",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"{today_standup_status[3]}"
                        }
                    },
                    {
                        "type": "header",
                        "text": {
                            "type": "plain_text",
                            "text": "Any blocker?",
                            "emoji": True
                        }
                    },
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": f"{today_standup_status[4]}"
                        }
                    },
                    {
                        "type": "divider"
                    }
                ]
            },
            channel=today_standup_status[5]
        )


def ask_standup_status(say):
    say(
        {
            "blocks": [
                {
                    "type": "divider"
                },
                {
                    "type": "context",
                    "elements": [
                        {
                            "type": "plain_text",
                            "text": "Select the channel to post your standup",
                            "emoji": True
                        }
                    ]
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "channels_select",
                            "placeholder": {
                                "type": "plain_text",
                                "text": "Select the channel to post your standup",
                                "emoji": True
                            },
                            "initial_channel": "C12345678",
                            "action_id": "channel-selection-action"
                        }
                    ]
                },
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


@app.action("channel-selection-action")
def action_channel_selection(body, ack, say):
    ack()
    user_id = body['user']['id']
    channel = body['actions'][0]['selected_channel']
    # say(f"<@{body['user']['id']}> selected <#{channel}>")
    upsert_today_standup_status(body['user']['id'], channel=channel)
    post_standup_completion_message(user_id, say)


@app.action("lastday-action")
def action_yesterday_standup_status(body, ack, say):
    ack()
    user_id = body['user']['id']
    msg = body['actions'][0]['value']
    # say(f"<@{body['user']['id']}> submitted standup status with message: {msg}.")
    upsert_today_standup_status(user_id, column_name='yesterday', message=msg)
    post_standup_completion_message(user_id, say)


@app.action("today-action")
def action_today_standup_status(body, ack, say):
    ack()
    user_id = body['user']['id']
    msg = body['actions'][0]['value']
    # say(f"<@{body['user']['id']}> submitted standup status with message: {msg}.")
    upsert_today_standup_status(user_id, column_name='today', message=msg)
    post_standup_completion_message(user_id, say)


@app.action("blocker-action")
def action_blocker_standup_status(body, ack, say):
    ack()
    user_id = body['user']['id']
    msg = body['actions'][0]['value']
    # say(f"<@{body['user']['id']}> submitted standup status with message: {msg}.")
    upsert_today_standup_status(user_id, column_name='blocker', message=msg)
    post_standup_completion_message(user_id, say)
