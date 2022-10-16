import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from heart import beat
from functions.basics import error
from functions import basics
from settings import INSTALLED_APPS, TOKEN


def main():
  """Start the bot."""
  # Create the Updater and pass it your bot's token.
  # Make sure to set use_context=True to use the new context (based callbacks
  # Post version 12 this will no longer be necessary
  bot = Updater(token=TOKEN, use_context=True)

  # Get the dispatcher to register handlers
  dp = bot.dispatcher

  # on different commands - answer in Telegram
  dp.add_handler(CommandHandler("start", basics.start))
  dp.add_handler(CommandHandler("help", basics.help))

  if 'GSHEET' in INSTALLED_APPS:
    from functions.third_apps import google_sheet_API
    sheetAPI = google_sheet_API.Gsheet_Helper()
    dp.add_handler(CommandHandler("spend", sheetAPI.spend))
    dp.add_handler(CommandHandler("total", sheetAPI.total))
    dp.add_handler(CommandHandler("rm", sheetAPI.rm_last))
  if 'RECIPE' in INSTALLED_APPS:
    from functions.third_apps import recipeapi
    recetasAPI = recipeapi.RecipeAPI()
    dp.add_handler(CommandHandler("recipe", recetasAPI.send_recipe))

  # log all errors
  dp.add_error_handler(error)

  # Start the Bot
  bot.start_polling()

  # Run the bot until you press Ctrl-C or the process receives SIGINT,
  # SIGTERM or SIGABRT. This should be used most of the time, since
  # start_polling() is non-blocking and will stop the bot gracefully.
  bot.idle()


beat()
if __name__ == '__main__':
  main()
