import os

from dotenv import load_dotenv
from slack_bolt import App

load_dotenv()


def get_slack_bolt_app():
    """
    Returns slack bolt app object after initializing.
    :return: Slack bolt app object
    """
    return App(
        token=os.getenv("SLACK_BOT_TOKEN"),
        signing_secret=os.getenv("SLACK_SIGNING_SECRET")
    )


# Start app
if __name__ == "__main__":
    app = get_slack_bolt_app()
    app.start(port=int(os.environ.get("PORT", 3000)))
