import logging
import re
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext, CallbackQueryHandler

# Set your bot token here
BOT_TOKEN = '6431120896:AAHKvzTjNtxXqQ4B4tBSQdHSwY-v-FP4tkE'

# Set your wallet address here
WALLET_ADDRESS = 'bc1qmf2lquregsmy4p2q475e9w8acqqpsukp407mud'

# Words that trigger the bot's response
TRIGGER_WORDS = [
    "0.030125btc for $62.5 in btc",
    "0.0625 btc for $125 in btc",
    "0.125 btc for $250 in btc",
    "0.25 btc for $500 in btc",
    "0.5 btc for $1000 in btc",
    "0.030125btc for $62.5",
    "0.0625 btc for $125",
    "0.125 btc for $250",
    "0.25 btc for $500",
    "0.5 btc for $1000"
]

def handle_special_messages(update: Update, context: CallbackContext) -> None:
    user = update.message.from_user
    username = user.username if user.username else "user"

    response_message = (
        f"Dear @{username}, we have received your order. "
        "Proceed to checkout and pay with BTC address:\n\n"
        f"{WALLET_ADDRESS}\n\n"
        "Click the 'Continue' button below to proceed with payment."
    )

    markup = InlineKeyboardMarkup([
        [InlineKeyboardButton("Continue", callback_data="continue")]
    ])

    update.message.reply_text(response_message, reply_markup=markup)

def handle_continue_button(update: Update, context: CallbackContext) -> None:
    query = update.callback_query
    query.edit_message_text(
        text="Thank you for your payment. Your order is being processed.",
    )

    # Send a chat message with instructions when the button is clicked
    user_id = query.from_user.id
    context.bot.send_message(chat_id=user_id, text="Hello, You have ordered from Active Anonymous. "
                                                    "Please send the word 'Continue' to the group or>

def main() -> None:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging>

    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    # Register a message handler to handle special messages
    dispatcher.add_handler(MessageHandler(Filters.regex(r'|'.join(map(re.escape, TRIGGER_WORDS))), h>

    # Register a callback query handler for the "Continue" button
    dispatcher.add_handler(CallbackQueryHandler(handle_continue_button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
