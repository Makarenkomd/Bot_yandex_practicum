import logging

from config import TOKEN
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

reply_keyboard = [['/hobby', '/selfie', '/gpt']
                 ,['/stiker', '/nosql', '/love']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

async def echo(update, context):
    await update.message.reply_text("я тупой, я такой не понимай)")

async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(rf"Привет {user.mention_html()}! Давай знакомиться!",  reply_markup=markup)

async def help_command(update, context):
    await update.message.reply_text("Команды всякие нужны! Но писать скучно и долго, поэтому предлагаю только /start, /help и /source)))")

async def selfie(update, context):
    await context.bot.send_photo(
        update.message.chat_id, photo=open(r'images/selfie.jpg', 'rb'))

async def gpt(update, context):
    audio = open(r'audio/gpt.ogg', 'rb')
    await context.bot.send_audio(update.message.chat_id, audio)
    audio.close()

async def my_hobby(update, context):
    await update.message.reply_text(
        'Хобби у меня много Я люблю играть во все что с *мячем*, горные походы и гитару у костра\.\n'
        "Но айтишная страть состоит в разработке *NLP* и не только инструментов для осетинского языка:  мультимедийный учебник по фонетике осетинского языка,  словари в машиночитаемом виде\.\n"
        "Когдато давно, на заре моего увлечения, а это было еще в прошлом веке и даже тысячелетии ![😅](tg://emoji?id=128949399) , командой мы делали систему распознавания осетинского языка и компилятивный синтезатор осетинской речи\.\n"
        "Создаем маленькие языковые игры\. А прямо сейчас, работаем над системой проверки орфографии\.\n"
      , parse_mode='MarkdownV2')
          
async def source(update, context):
    await update.message.reply_html("Исходный код всего этого добра <a href='https://github.com/Makarenkomd/bot_telegram_for_yandex_practics.git'> тут </a>")

def main():
    application = Application.builder().token(TOKEN).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("hobby", my_hobby))
    application.add_handler(CommandHandler("selfie", selfie))
    application.add_handler(CommandHandler("gpt", gpt))
    application.add_handler(CommandHandler("source", source))

    application.run_polling()


if __name__ == '__main__':
    main()
