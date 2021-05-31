from app.main import get_slack_bolt_app

app = get_slack_bolt_app()

if __name__ == "__main__":
    app.start(port=int(3000))
