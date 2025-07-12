import asyncio
import requests
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

# حذف webhook قبل از اجرای polling
def delete_webhook(token: str):
    url = f"https://api.telegram.org/bot{token}/deleteWebhook"
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print("✅ Webhook حذف شد.")
        else:
            print("⚠️ حذف Webhook ناموفق بود:", response.text)
    except Exception as e:
        print("❌ خطا در حذف Webhook:", str(e))


# دستور /start
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text)
    await update.message.reply_text("سلام چطوری عقب مونده؟")

# پاسخ به پیام‌های متنی
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    print(update.message.text)
    await update.message.reply_text('چی میگی اسکل؟ زبونت رو نمیفهمم چاقال. فکر کنم سازنده عزیزم منو هنوز تکمیل نکرده تا نوکری شما عقب مونده‌ها رو کنم....')


def main():
    TOKEN = "7824445846:AAE4ef4Yrwz3Au-MunpCbk_4bfNYyTyXs2E"
    delete_webhook(TOKEN)  # پاک کردن Webhook قبل از شروع
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, echo))

    application.run_polling()


if __name__ == "__main__":
    main()
