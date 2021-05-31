import os

from app.main import app

if __name__ == "__main__":
    app.start(port=int(os.environ.get("PORT", 3000)))
