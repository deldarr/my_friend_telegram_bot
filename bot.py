from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes, MessageHandler,filters


# Define a function to handle the /start command
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("سلام چطوری عقب مونده؟")

# Define a function to handle text messages and echo them back
async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text('چی میگی اسکل؟ زبونت رو نمیهمم چاقال. فکر کنم سازنده عزیزم منو هنوز تکمیل نکرده....')

def main():
    application = ApplicationBuilder().token("7824445846:AAE4ef4Yrwz3Au-MunpCbk_4bfNYyTyXs2E").build()

    # Add handlers for commands and messages
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT, echo))

    # Start the bot
    application.run_polling()

if __name__ == "__main__":
    main()