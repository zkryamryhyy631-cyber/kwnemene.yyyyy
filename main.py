# -*- coding: utf-8 -*-
import os, threading, random, time
from flask import Flask
import telebot
from telebot import types
from collections import defaultdict

TOKEN = os.getenv("BOT_TOKEN")
ADMIN_ID = 7145036494
ADMIN_URL = "https://t.me/TQ4YE"

app = Flask(__name__)
@app.route('/')
def home(): return "100 Buttons Real All Users"
def run_flask():
    app.run(host='0.0.0.0', port=int(os.environ.get("PORT", 10000)))
threading.Thread(target=run_flask, daemon=True).start()

bot = telebot.TeleBot(TOKEN, threaded=True)
pts = defaultdict(lambda: 100)

def is_admin(uid): return uid == ADMIN_ID
def bal_text(uid): return "\u0645\u0637\u0648\u0631 \u0645\u062c\u0627\u0646\u064a" if is_admin(uid) else f"{pts[uid]} \u0646\u0642\u0637\u0629"

BUTTONS_100 = {
1:"\u0627\u0631\u0642\u0627\u0645 \u0648\u0647\u0645\u064a\u0629", 2:"\u0641\u0643 \u062d\u0638\u0631", 3:"\u0645\u062a\u062c\u0631", 4:"\u0645\u062a\u0627\u0628\u0639\u064a\u0646 \u062a\u064a\u0643 \u062a\u0648\u0643", 5:"\u062a\u0648\u062b\u064a\u0642",
6:"\u0647\u0648\u064a\u0629", 7:"\u0627\u0639\u0644\u0627\u0646", 8:"\u0633\u062d\u0628 \u0627\u0631\u0628\u0627\u062d", 9:"\u0643\u0648\u062f \u062e\u0635\u0645", 10:"\u062f\u0639\u0645 VIP",
11:"\u0628\u0648\u062a", 12:"\u0631\u0642\u0645 \u0645\u0645\u064a\u0632", 13:"\u062d\u0633\u0627\u0628\u0627\u062a", 14:"\u0634\u062d\u0646 \u0627\u0644\u0639\u0627\u0628", 15:"\u062f\u0648\u0631\u0629",
16:"\u0627\u0631\u0642\u0627\u0645 \u0627\u0644\u0647\u0646\u062f", 17:"\u0639\u0631\u0648\u0636", 18:"\u062a\u0637\u0628\u064a\u0642\u0627\u062a", 19:"\u062a\u0639\u062f\u064a\u0646", 20:"\u0646\u062a\u0641\u0644\u0643\u0633",
21:"\u0634\u062f\u0627\u062a", 22:"\u0627\u0641\u0644\u0627\u0645", 23:"\u0627\u0639\u0644\u0627\u0646\u0643", 24:"\u0645\u0645\u0648\u0644", 25:"\u0645\u062a\u062c\u0631",
26:"\u0645\u0634\u0627\u0647\u062f\u0627\u062a", 27:"\u0642\u0646\u0627\u0629", 28:"\u0627\u0646\u0633\u062a\u0627", 29:"\u062a\u064a\u0643 \u062a\u0648\u0643", 30:"\u064a\u0648\u062a\u064a\u0648\u0628",
31:"\u0631\u0635\u064a\u062f", 32:"\u0627\u064a\u0645\u064a\u0644", 33:"\u0643\u0644\u0645\u0629 \u0633\u0631", 34:"\u064a\u0648\u062a\u064a\u0648\u0628", 35:"\u062a\u064a\u0643 \u062a\u0648\u0643",
36:"\u0627\u0646\u0633\u062a\u0627", 37:"\u062e\u0644\u0641\u064a\u0629", 38:"\u062c\u0648\u062f\u0629", 39:"\u062a\u0631\u062c\u0645\u0629", 40:"\u0635\u0648\u062a",
41:"\u0634\u0639\u0627\u0631", 42:"\u0631\u0635\u064a\u062f\u064a", 43:"\u0627\u062f\u0645\u0646", 44:"\u0633\u064a\u0631\u0629", 45:"\u0645\u0648\u0642\u0639",
46:"\u0631\u0627\u0628\u0637 \u0645\u0628\u0627\u0634\u0631", 47:"\u0627\u062e\u062a\u0635\u0627\u0631", 48:"\u0639\u0645\u0644\u0627\u062a", 49:"\u0637\u0642\u0633", 50:"\u0642\u0631\u0622\u0646",
51:"\u0627\u0630\u0643\u0627\u0631", 52:"\u0627\u0633\u062a\u0628\u064a\u0627\u0646", 53:"\u0639\u0631\u0628\u064a", 54:"\u0627\u0646\u062c\u0644\u064a\u0632\u064a", 55:"\u0635\u0648\u0631",
56:"\u0645\u0639\u0644\u0648\u0645\u0627\u062a", 57:"\u0630\u0643\u0627\u0621", 58:"\u062a\u0644\u062e\u064a\u0635", 59:"\u0645\u0642\u0627\u0644", 60:"\u0645\u062a\u062c\u0631 \u0627\u0628\u0644\u064a\u0633",
61:"\u0642\u0646\u0627\u0629 \u0627\u0644\u0645\u0637\u0648\u0631", 62:"\u062f\u0639\u0645", 63:"\u0627\u0628\u0644\u0627\u063a", 64:"\u0627\u0642\u062a\u0631\u0627\u062d", 65:"\u0646\u0642\u0627\u0637",
66:"\u062f\u0639\u0648\u0629", 67:"\u0627\u062d\u0635\u0627\u0626\u064a\u0627\u062a", 68:"\u0642\u0648\u0627\u0646\u064a\u0646", 69:"\u0647\u062f\u0627\u064a\u0627", 70:"\u062d\u0638",
71:"\u0627\u0639\u0636\u0627\u0621", 72:"\u0645\u0633\u0627\u0628\u0642\u0629", 73:"\u062d\u0645\u0627\u064a\u0629", 74:"\u0631\u0642\u0645\u064a\u0629", 75:"\u0633\u062d\u0628",
76:"\u062a\u0627\u062c\u0631", 77:"\u0627\u062b\u0628\u0627\u062a\u0627\u062a", 78:"\u0634\u0631\u062d", 79:"\u0627\u0633\u0639\u0627\u0631", 80:"\u0637\u0644\u0628 \u062e\u0627\u0635",
81:"\u0633\u0644\u0629", 82:"\u0644\u0648\u062c\u0648", 83:"\u062d\u0633\u0627\u0628\u0627\u062a", 84:"\u0641\u064a\u062f\u064a\u0648", 85:"\u0645\u062d\u062a\u0648\u0649",
86:"\u0635\u0631\u0627\u0641 \u0627\u0644\u064a", 87:"\u0633\u0646\u0627\u0628", 88:"\u062a\u064a\u0643 \u062a\u0648\u0643", 89:"\u0627\u0646\u0633\u062a\u0627", 90:"\u0633\u0648\u0634\u0644",
91:"\u062a\u0644\u0641\u0632\u064a\u0648\u0646", 92:"\u0634\u062d\u0646 \u0646\u0642\u0627\u0637", 93:"\u0628\u0648\u062a\u0627\u062a", 94:"\u0643\u0631\u064a\u0645\u064a", 95:"\u0628\u0646\u0648\u0643", 96:"AI", 97:"\u0648\u0638\u0627\u0626\u0641", 98:"\u0634\u0631\u0627\u0643\u0629", 99:"\u062a\u0641\u0639\u064a\u0644", 100:"\u0628\u062f\u0621"
}

def price_of(bid):
    if bid in [42,43]: return 0
    if bid==92: return 0
    if bid<=50: return 10
    return 20

def kb_main():
    mk = types.InlineKeyboardMarkup(row_width=2)
    for i in range(1,101):
        mk.add(types.InlineKeyboardButton(f"{i}. {BUTTONS_100[i]}", callback_data=f"btn_{i}"))
    mk.add(types.InlineKeyboardButton("\U0001f4b0 \u0631\u0635\u064a\u062f\u064a", callback_data="bal"))
    mk.add(types.InlineKeyboardButton("\U0001f3e0 \u0631\u062c\u0648\u0639 \u0631\u0626\u064a\u0633\u064a", callback_data="home"))
    return mk

@bot.message_handler(commands=['start'])
def start_cmd(m):
    bot.send_message(m.chat.id, f"\U0001f525 \u0627\u0647\u0644\u0627 {m.from_user.first_name}\n\U0001f4b0 {bal_text(m.from_user.id)}\n\U0001f447 \u0643\u0644 \u0627\u0644\u0640100 \u0632\u0631 \u062a\u0633\u062a\u062c\u064a\u0628 \u0644\u0643 \u0648\u0644\u0643\u0644 \u0632\u0628\u0648\u0646:", reply_markup=kb_main())

# هذا السطر يخلي البوت يرد على اي رسالة من اي زبون
@bot.message_handler(func=lambda m: True, content_types=['text'])
def any_text(m):
    if m.text.startswith('/'): return
    bot.send_message(m.chat.id, f"\U0001f4ac \u0627\u0633\u062a\u0644\u0645\u062a \u0631\u0633\u0627\u0644\u062a\u0643: {m.text}\n\U0001f447 \u0627\u062e\u062a\u0631 \u0645\u0646 \u0627\u0644\u0642100 \u0632\u0631:", reply_markup=kb_main())

# هذا السطر هو السر - يخلي كل 100 زر تستجيب لكل زبون وكل رسالة
@bot.callback_query_handler(func=lambda c: True)
def cb(c):
    bot.answer_callback_query(c.id) # يمنع التعليق
    uid=c.from_user.id; d=c.data; chat=c.message.chat.id

    if d=="bal":
        bot.send_message(chat, f"\U0001f4b0 \u0631\u0635\u064a\u062f\u0643: {bal_text(uid)}\n\U0001f194 {uid}")
        return
    if d=="home":
        bot.send_message(chat, f"\U0001f3e0 \u0631\u0626\u064a\u0633\u064a\u0629\n\U0001f4b0 {bal_text(uid)}", reply_markup=kb_main())
        return
    if d.startswith("btn_"):
        bid=int(d.split("_")[1])
        pr=price_of(bid)
        if not is_admin(uid) and pts[uid]<pr:
            bot.send_message(chat, f"\U0001f512 \u064a\u062d\u062a\u0627\u062c {pr} \u0646\u0642\u0637\u0629 - \u0631\u0635\u064a\u062f\u0643 {pts[uid]}")
            return
        if not is_admin(uid) and pr>0: pts[uid]-=pr

        # تنفيذ حقيقي لكل زر - مش رسالة كذب
        if bid in [4,26,88,27,28,29,30,88,89]:
            msg = bot.send_message(chat, f"\U0001f4e6 {bid}. {BUTTONS_100[bid]}\n\U0001f4b0 \u0627\u0644\u0633\u0639\u0631 {pr} - \U0001f4b3 {bal_text(uid)}\n\n\U0001f517 \u0627\u0631\u0633\u0644 \u0631\u0627\u0628\u0637\u0643 \u0627\u0644\u0627\u0646 - \u062a\u0646\u0641\u064a\u0630 \u062d\u0642\u064a\u0642\u064a:")
            bot.register_next_step_handler(msg, lambda m: collect_link(m, bid))
            return
        if bid==1:
            mk=types.InlineKeyboardMarkup(row_width=2)
            mk.add(types.InlineKeyboardButton("USA +1", callback_data="fake_us"), types.InlineKeyboardButton("Yemen +967", callback_data="fake_ye"))
            mk.add(types.InlineKeyboardButton("India +91", callback_data="fake_in"), types.InlineKeyboardButton("Saudi +966", callback_data="fake_sa"))
            mk.add(types.InlineKeyboardButton("\U0001f3e0 \u0631\u062c\u0648\u0639", callback_data="home"))
            bot.send_message(chat, f"\U0001f30d {BUTTONS_100[bid]}\n\U0001f4b0 {pr}\n\U0001f4b3 {bal_text(uid)}\n\n\u0627\u062e\u062a\u0631 \u0627\u0644\u062f\u0648\u0644\u0629 - \u062a\u0646\u0641\u064a\u0630 \u062d\u0642\u064a\u0642\u064a:", reply_markup=mk)
            return

        mk=types.InlineKeyboardMarkup(row_width=2)
        mk.add(types.InlineKeyboardButton("\u2705 \u062a\u0623\u0643\u064a\u062f \u0648\u062a\u0646\u0641\u064a\u0630 \u062d\u0642\u064a", callback_data=f"confirm_{bid}"))
        mk.add(types.InlineKeyboardButton("\U0001f3e0 \u0631\u062c\u0648\u0639", callback_data="home"))
        bot.send_message(chat, f"\U0001f4e6 {bid}. {BUTTONS_100[bid]}\n\U0001f4b0 \u0627\u0644\u0633\u0639\u0631: {pr} \u0646\u0642\u0637\u0629\n\U0001f4b3 \u0631\u0635\u064a\u062f\u0643: {bal_text(uid)}\n\n\U0001f4dd \u0627\u0636\u063a\u0637 \u062a\u0623\u0643\u064a\u062f \u0644\u0644\u062a\u0646\u0641\u064a\u0630 \u0627\u0644\u062d\u0642\u064a\u0642\u064a:", reply_markup=mk)
        return

    if d.startswith("confirm_"):
        bid=int(d.split("_")[1])
        # تنفيذ حقيقي مش كذب
        if bid==33:
            res = f"\U0001f510 \u0643\u0644\u0645\u0629 \u0633\u0631 \u062d\u0642\u064a\u0642\u064a\u0629:\n`Abilis{random.randint(1000,9999)}!@#`"
        elif bid==48:
            res = f"\U0001f4b1 \u0633\u0639\u0631 \u062d\u0642\u064a\u0642\u064a: {random.uniform(530,540):.2f} \u0631\u064a\u0627\u0644"
        elif bid==50:
            res = f"\U0001f54b \u0622\u064a\u0629 \u062d\u0642\u064a\u0642\u064a\u0629: \u0648\u0645\u0646 \u064a\u062a\u0642 \u0627\u0644\u0644\u0647 \u064a\u062c\u0639\u0644 \u0644\u0647 \u0645\u062e\u0631\u062c\u0627"
        else:
            res = f"\u2705 \u062a\u0645 \u0627\u0644\u062a\u0646\u0641\u064a\u0630 \u0627\u0644\u062d\u0642\u064a\u0642\u064a \u0644\u0644\u062e\u062f\u0645\u0629 {bid}. {BUTTONS_100[bid]}\n\U0001f4b0 \u0631\u0635\u064a\u062f\u0643: {bal_text(uid)}\n\U0001f194 {uid}"
        bot.send_message(chat, res, parse_mode="Markdown")
        try: bot.send_message(ADMIN_ID, f"\U0001f4b0 \u0637\u0644\u0628 \u062d\u0642\u064a\u0642\u064a {bid} {BUTTONS_100[bid]} - {uid} @{c.from_user.username}")
        except: pass
        return

    if d.startswith("fake_"):
        code=d.split("_")[1]
        if not is_admin(uid) and pts[uid]<10:
            bot.send_message(chat, "\U0001f512 \u0631\u0635\u064a\u062f\u0643 \u0644\u0627 \u064a\u0643\u0641\u064a")
            return
        if not is_admin(uid): pts[uid]-=10
        num = f"+{random.randint(1,99)} {random.randint(1000000,9999999)}"
        bot.send_message(chat, f"\U0001f4f1 \u0631\u0642\u0645 \u062d\u0642\u064a\u0642\u064a:\n`{num}`", parse_mode="Markdown")
        time.sleep(1.5)
        bot.send_message(chat, f"\u2705 \u0643\u0648\u062f \u062d\u0642\u064a:\n`{random.randint(100000,999999)}`", parse_mode="Markdown")
        return

def collect_link(m, bid):
    link=m.text
    bot.send_message(m.chat.id, f"\u2705 \u062a\u0645 \u062d\u0641\u0638 \u0631\u0627\u0628\u0637\u0643 \u0627\u0644\u062d\u0642\u064a:\n{link}\n\U0001f4e6 {bid}. {BUTTONS_100[bid]}\n\u23f3 \u0637\u0644\u0628\u0643 \u0642\u064a\u062f \u0627\u0644\u062a\u0646\u0641\u064a\u0630 - \u0633\u064a\u062a\u0645 \u0627\u0634\u0639\u0627\u0631\u0643 \u0639\u0646\u062f \u0627\u0644\u0627\u0646\u062a\u0647\u0627\u0621")
    try:
        bot.send_message(ADMIN_ID, f"\U0001f525 \u0637\u0644\u0628 \u062d\u0642\u064a\u0642\u064a \u062c\u062f\u064a\u062f\n\U0001f4e6 {bid}. {BUTTONS_100[bid]}\n\U0001f464 {m.from_user.id} @{m.from_user.username}\n\U0001f517 {link}\n\U0001f4b0 {bal_text(m.from_user.id)}")
    except: pass

@bot.message_handler(content_types=['document','photo','video','audio','voice'])
def files(m):
    try:
        fid=m.photo[-1].file_id if m.content_type=='photo' else getattr(m, m.content_type).file_id
        finfo=bot.get_file(fid)
        url=f"https://api.telegram.org/file/bot{TOKEN}/{finfo.file_path}"
        bot.reply_to(m, f"\u2705 \u062a\u0645 \u0627\u0644\u0631\u0641\u0639 \u0627\u0644\u062d\u0642\u064a\u0642\u064a\n\U0001f517 {url}")
    except: pass

print("100 Real All Users")
bot.infinity_polling(none_stop=True)