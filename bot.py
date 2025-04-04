from flask import Flask, request
import requests
import json

app = Flask(__name__)

TOKEN = "7902263399:AAEthTceGeIkisc0UjtguFYgWrfiiFhcNOE"
API_URL = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

@app.route("/", methods=["POST"])
def webhook():
    update = request.get_json()

    # logga yozamiz
    with open("log.txt", "a") as f:
        f.write(json.dumps(update, indent=4) + "\n")

    try:
        message = update.get("message", {})
        chat_id = message.get("chat", {}).get("id")

        if "new_chat_members" in message:
            for member in message["new_chat_members"]:
                username = (
                    f"@{member['username']}"
                    if "username" in member else member.get("first_name", "foydalanuvchi")
                )

                text = (
                    f"👋 Salom, {username}!\n\n"
                    f"💼 **[SALES JOBS / Работа в сфере продаж](https://t.me/SalesJobsUZB)** guruhiga xush kelibsiz!\n\n"
                    f"🔹 Ish qidiryapsizmi yoki xodim izlayapsizmi? Biz sizga yordam beramiz!"
                )

                payload = {
                    "chat_id": chat_id,
                    "text": text,
                    "parse_mode": "Markdown",
                    "disable_web_page_preview": True
                }

                requests.post(API_URL, data=payload)

    except Exception as e:
        with open("error_log.txt", "a") as f:
            f.write(str(e) + "\n")

    return "OK"