import telebot
from telebot import types
import time

TOKEN = "TOKENINGIZ"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=["start"])
def start(message):

    # Animatsiya
    msg = bot.send_message(
        message.chat.id,
        "✨ Bot ishga tushmoqda..."
    )

    time.sleep(0.5)
    bot.edit_message_text(
        "🔄 Yuklanmoqda...",
        message.chat.id,
        msg.message_id
    )

    time.sleep(0.5)
    bot.edit_message_text(
        "✅ Tayyor!",
        message.chat.id,
        msg.message_id
    )

    time.sleep(0.5)

    # Tugmalar
    keyboard = types.InlineKeyboardMarkup(row_width=2)

    kanal1 = types.InlineKeyboardButton(
        "📢 Kanal 1",
        url="https://t.me/+DaiKDOfETJBhOGVi"
    )

    kanal2 = types.InlineKeyboardButton(
        "📢 Kanal 2",
        url="https://t.me/+Ppt8oPTa1zQxNjRi"
    )

    aloqa = types.InlineKeyboardButton(
        "📞 Men bilan aloqa",
        callback_data="aloqa"
    )

    haqida = types.InlineKeyboardButton(
        "🤖 Bot haqida",
        callback_data="haqida"
    )

    keyboard.add(kanal1, kanal2)
    keyboard.add(aloqa, haqida)

    bot.edit_message_text(
        "🔥 <b>Xush kelibsiz!</b>\n\n"
        "Kerakli bo‘limni tanlang 👇",
        message.chat.id,
        msg.message_id,
        reply_markup=keyboard,
        parse_mode="HTML"
    )


@bot.callback_query_handler(func=lambda call: call.data == "aloqa")
def aloqa(call):

    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        "📞 <b>Men bilan aloqa:</b>\n"
        "+998 94 996 83 89",
        parse_mode="HTML"
    )


@bot.callback_query_handler(func=lambda call: call.data == "haqida")
def haqida(call):

    bot.answer_callback_query(call.id)

    bot.send_message(
        call.message.chat.id,
        "🤖 <b>Bot haqida:</b>\n"
        "Bot hali yangi, sinov jarayonida.",
        parse_mode="HTML"
    )


print("🤖 Bot ishga tushdi!")

bot.infinity_polling()
