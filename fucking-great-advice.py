#!/usr/bin/env python3
# -*- coding: utf-8 -*-

""" Telegram bot which give advice you for different life situations.
Fucking advices get from fucking-great-advice.ru by API (http://fucking-great-advice.ru/api)
Wrapper telegram bot is python-telegram-bot (https://github.com/python-telegram-bot)
"""

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import requests

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)

def start(bot, update):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Hi! I can make your life better...')

def help(bot, update):
    """Send a message when the command /help is issued."""
    update.message.reply_text('For random fucking advice just type /advice')

def error(bot, update, error):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, error)

def advice(bot, update, args):
    """Fucking random great advice"""
    r = requests.get('http://fucking-great-advice.ru/api/random')
    advice = r.json()
    text = advice["text"]
    update.message.reply_text(text)

def main():
    """Start the bot."""
    # Create the EventHandler and pass it your bot's token.
    updater = Updater("YOUR-TELEGRAM-TOKEN")

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # on different commands - answer in Telegram
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("advice", advice, pass_args=True))

    # log all errors
    dp.add_error_handler(error)

    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()

