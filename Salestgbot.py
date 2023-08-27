import logging
from telegram import Update, KeyboardButton, ReplyKeyboardMarkup, InlineKeyboardButton, InlineKeyboa>
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext, Callback>

# Set your bot token here
BOT_TOKEN = '6587861204:AAHMER5eERYZnA3rT9rN4IIse-bn_f8_474'

# States for the conversation
CHOOSING_SERVICE, CHOOSING_OPTION = range(2)

# Service options and their corresponding choices
SERVICE_OPTIONS = {
    'Wallet Private Key': [
        "0.030125btc for $62.5 in btc",
        "0.0625 btc for $125 in btc",
        "0.125 btc for $250 in btc",
        "0.25 btc for $500 in btc",
        "0.5 btc for $1000 in btc"
    ],
    'Crypto Flash Apk': [
        "0.030125btc for $62.5 in btc",
        "0.0625 btc for $125 in btc",
        "0.125 btc for $250 in btc",
        "0.25 btc for $500 in btc",
        "0.5 btc for $1000 in btc"
    ],
    'Load PayPal': [
        "0.030125btc for $62.5",
        "0.0625 btc for $125",
        "0.125 btc for $250",
        "0.25 btc for $500",
        "0.5 btc for $1000"
    ],
    'Cards Credits': [
        "0.030125btc for $62.5",
        "0.0625 btc for $125",
        "0.125 btc for $250",
        "0.25 btc for $500",
        "0.5 btc for $1000"
    ]
}

def start(update: Update, context: CallbackContext) -> int:
    update.message.reply_text(
        "Welcome to AK Trades! Please choose a service:",
        reply_markup=get_service_keyboard()
    )
    return CHOOSING_SERVICE

def get_service_keyboard():
    keyboard = [
        [KeyboardButton(service_name)] for service_name in SERVICE_OPTIONS.keys()
    ]
    return ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

def handle_service_selection(update: Update, context: CallbackContext) -> int:
    selected_service = update.message.text
    context.user_data['selected_service'] = selected_service

    choices = SERVICE_OPTIONS[selected_service]
    keyboard = [
        [KeyboardButton(choice)] for choice in choices
    ]
    reply_markup = ReplyKeyboardMarkup(keyboard, one_time_keyboard=True)

    update.message.reply_text(
        f"For {selected_service}, please choose an option:",
        reply_markup=reply_markup
    )

    return CHOOSING_OPTION

def handle_option_selection(update: Update, context: CallbackContext) -> int:
    selected_service = context.user_data.get('selected_service')
    selected_option = update.message.text

    update.message.reply_text(
        f"You have selected:\n\nService: {selected_service}\nOption: {selected_option}\n\n"
        "Please proceed with the payment."
)
  return ConversationHandler.END

def main() -> None:
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging>

    updater = Updater(token=BOT_TOKEN, use_context=True)
    dispatcher = updater.dispatcher

    conversation_handler = ConversationHandler(
        entry_points=[MessageHandler(Filters.text & ~Filters.command, start)],
        states={
            CHOOSING_SERVICE: [MessageHandler(Filters.text & ~Filters.command, handle_service_select>
            CHOOSING_OPTION: [MessageHandler(Filters.text & ~Filters.command, handle_option_selectio>
        },
        fallbacks=[]
    )

    dispatcher.add_handler(conversation_handler)

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
