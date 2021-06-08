import telebot
from django.conf import settings


TOKEN = settings.BOT_TOKEN
bot = telebot.TeleBot(TOKEN)


from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = 'The Zen of Python'

    def handle(self, *args, **options):
        import this


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Hello")

bot.polling()
