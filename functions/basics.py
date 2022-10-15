from logger import logger

"""
Basic Bot Functions
update: handles the bot
context: 
"""


def start(update, context):
    """Send a message when the command /start is issued."""
    update.message.reply_text('Alooo! Para ver mis comandos usa /help')


def help(update, context):
    """Send a message when the command /help is issued."""
    update.message.reply_text("/spend <desc> <amount> <category> updates google sheet \n/total returns total \n/rm removes last spend\n/recipe <food> returns random recipe")
                             
                             


def echo(update, context):
    """Echo the user message."""
    update.message.reply_text(update.message.text)


def error(update, context):
    """Log Errors caused by Updates."""
    logger.warning('Update "%s" caused error "%s"', update, context.error)
