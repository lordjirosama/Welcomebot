# Solurix Welcome Bot

Group me naya member join karte hi automatic welcome message bhejta hai.

## Setup Steps

### 1. Bot banao (agar pehle se nahi bana)
- Telegram me `@BotFather` ko message karo
- `/newbot` command bhejo aur naam/username set karo (e.g. SolurixBot)
- Jo **token** milega usko save kar lo

### 2. Code setup
```bash
pip install -r requirements.txt
```

### 3. Token set karo
`.env.example` file ka naam badal ke `.env` kar do, aur usme apna token daal do:
```
BOT_TOKEN=1234567890:ABCdefGhIJKlmNoPQRstuVWXyz
```

### 4. Bot ko group me add karo
- Apne Telegram group me bot ko add karo
- **Bot ko admin banana zaroori hai** — warna wo naye members detect nahi kar payega
  (Group settings → Administrators → Add Admin → apna bot select karo)

### 5. Bot chalao
```bash
python bot.py
```

Bas! Ab jaise hi koi naya member group join karega, bot automatically usko welcome message bhejega.

## Welcome message customize karna

`bot.py` file me `WELCOME_TEMPLATE` variable ko edit karo — apne hisaab se text, emojis, rules change kar sakte ho.

## Hosting (24/7 chalane ke liye)

Apna computer band karoge to bot bhi ruk jayega. 24/7 chalane ke liye ye options hai:
- **Railway.app** / **Render.com** — free tier available, easy deploy
- **VPS** (DigitalOcean, AWS EC2 etc.)
- **PythonAnywhere**

Agar chaho to main tumhe kisi ek platform pe deploy karne me bhi help kar sakta hoon.
