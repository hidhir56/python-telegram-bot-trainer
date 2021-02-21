#!/usr/bin/env python
# pylint: disable=W0613, C0116
# type: ignore[union-attr]
# This program is dedicated to the public domain under the CC0 license.

"""
Simple Bot to reply to Telegram messages.
First, a few handler functions are defined. Then, those functions are passed to
the Dispatcher and registered at their respective places.
Then, the bot is started and runs until we press Ctrl-C on the command line.
Usage:
Basic Echobot example, repeats messages.
Press Ctrl-C on the command line or send a signal to the process to stop the
bot.
"""

import logging
import threading

from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Enable logging
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO
)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context. Error handlers also receive the raised TelegramError object in error.
def start(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /start is issued."""
    update.message.reply_text('bye!')

player1=''
player2=''


def help_command(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /help is issued."""
    update.message.reply_text('Help!')

def send_100_times(update: Update, message):
    for i in range(100):
        update.message.reply_text(message)

def echo(update: Update, context: CallbackContext) -> None:
    """Echo the user message."""
    update.message.reply_text('Help!')

def scissors(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /scissors is issued."""
    global player1
    global player2
    
    if player1 =='':
        player1 ='scissors'
    else:
        player2= 'scissors'

    evaluate(update)

def evaluate (update):
    global player1 
    global player2 

    if player1 !=''and player2 !='':
        if player1==player2:
            update.message.reply_text('draw!')
        elif player1== 'scissors' and player2=='paper':
            update.message.reply_text('player1 win!')
        elif player1 == 'paper'and player2 =='scissors':
            update.message.reply_text('player2 win!')

        player1=''
        player2=''










def  paper(update: Update, context: CallbackContext) -> None:
    """Send a message when the command /paper is issued."""
    global player1
    global player2
    
    if player1 =='':
        player1 ='paper'
    else:
        player2= 'paper'
    evaluate(update)

    

  







def main():
    """Start the bot."""
    # Create the Updater and pass it your bot's token.
    updater = Updater("1648018686:AAFgaHrvMWktERAtYOaFMwfjX80oA2YGlW8")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # on different commands - answer in Telegram
    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("help", help_command))

    # on noncommand i.e message - echo the message on Telegram
    
    dispatcher.add_handler(CommandHandler("scissors", scissors))
    dispatcher.add_handler(CommandHandler("paper", paper))
    # Start the Bot
    updater.start_polling()

    # Run the bot until you press Ctrl-C or the process receives SIGINT,
    # SIGTERM or SIGABRT. This should be used most of the time, since
    # start_polling() is non-blocking and will stop the bot gracefully.
    updater.idle()


if __name__ == '__main__':
    main()