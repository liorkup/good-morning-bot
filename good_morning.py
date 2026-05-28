import os
import urllib.request
import urllib.parse
import json
from datetime import datetime

TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID = os.environ["CHAT_ID"]

messages = [
    "☀️ בוקר טוב! היום הולך להיות יום מעולה 💪",
    "🌅 בוקר אור! קום, כבש את היום 🔥",
    "😎 בוקר טוב! קפה ראשון, אחר כך כיבוש העולם ☕",
    "🌞 יום חדש, הזדמנות חדשה. בוקר טוב!",
    "🚀 בוקר טוב! היום אתה עושה דברים גדולים 💫",
    "🌄 בוקר טוב! החיים יפים, לך תחייה אותם 😄",
    "⚡ בוקר טוב! אנרגיות גבוהות להיום 🙌",
]

def send_message(text):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    data = urllib.parse.urlencode({
        "chat_id": CHAT_ID,
        "text": text,
    }).encode()
    req = urllib.request.Request(url, data=data)
    with urllib.request.urlopen(req) as response:
        result = json.loads(response.read())
        return result

if __name__ == "__main__":
    day_of_year = datetime.now().timetuple().tm_yday
    message = messages[day_of_year % len(messages)]
    result = send_message(message)
    print(f"Sent: {message}")
    print(f"Result: {result['ok']}")
