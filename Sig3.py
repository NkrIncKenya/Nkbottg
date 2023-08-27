import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboa>
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# Set your bot token here
BOT_TOKEN = '6686337320:AAGeVziYg5WYQ_bLRZnsChmeoNnET8UkjN4'

# Group owner's username
GROUP_OWNER_USERNAME = '@Blackat5'

def handle_continue_message(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    username = user.username if user.username else "user"

    response_message = (
        f"Thank you for trading with us and having paid for our services, {username}!\n"
        f"Message @{GROUP_OWNER_USERNAME} with your wallet address you used for payments.\n"
        "PayPal, Gmail, and Wallet address to receive."
    )

    update.message.reply_text(response_message)

def main() -> None:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging>

    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register a message handler to respond to "Continue" message
    dispatcher.add_handler(MessageHandler(Filters.regex(r'^Continue$'), handle_continue_message))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
