import os

from flask import Flask, render_template


app = Flask(__name__)


BOT_URL = os.getenv(
    "BOT_URL",
    "https://t.me/YOUR_BOT_USERNAME"
)

SUPPORT_EMAIL = os.getenv(
    "SUPPORT_EMAIL",
    "your-email@example.com"
)

SUPPORT_TELEGRAM = os.getenv(
    "SUPPORT_TELEGRAM",
    "https://t.me/YOUR_SUPPORT_USERNAME"
)


@app.route("/")
def home():
    return render_template(
        "home.html",
        bot_url=BOT_URL
    )


@app.route("/privacy-policy")
def privacy():
    return render_template("privacy.html")


@app.route("/terms")
def terms():
    return render_template("terms.html")


@app.route("/refund-cancellation")
def refund():
    return render_template("refund.html")


@app.route("/contact-us")
def contact():
    return render_template(
        "contact.html",
        email=SUPPORT_EMAIL,
        telegram=SUPPORT_TELEGRAM
    )


@app.route("/health")
def health():
    return "OK", 200


if __name__ == "__main__":
    port = int(os.getenv("PORT", "8080"))

    app.run(
        host="0.0.0.0",
        port=port
    )
