import os

from slack_bolt import App

app = App(
    token=os.environ.get("SLACK_BOT_TOKEN"),
    signing_secret=os.environ.get("SLACK_SIGNING_SECRET")
)


@app.message("hello")
def message_hello(message, say):
    say(f"Hey there <@{message['user']}>!")
