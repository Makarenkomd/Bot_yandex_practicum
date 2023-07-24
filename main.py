import logging


from config import TOKEN
from telegram.ext import Application, MessageHandler, filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup, KeyboardButton

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.DEBUG)
logger = logging.getLogger(__name__)

reply_keyboard = [['/hobby', '/selfie', '/gpt']
                 ,['фото и сюрприз', 'sql и nosql', 'про любовь']]
markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False, resize_keyboard=True)


async def start(update, context):
    user = update.effective_user
    await update.message.reply_html(rf"Привет {user.mention_html()}! Давай знакомиться!",  reply_markup=markup)

async def help_command(update, context):
    await update.message.reply_text("Команды всякие нужны! Но писать скучно и долго, поэтому предлагаю только /start, /help и /source)))")

async def my_hobby(update, context):
    await update.message.reply_text(
        'Хобби у меня много Я люблю играть во все что с *мячем*, горные походы и гитару у костра\.\n'
        "Но айтишная страть состоит в разработке *NLP* и не только инструментов для осетинского языка:  мультимедийный учебник по фонетике осетинского языка,  словари в машиночитаемом виде\.\n"
        "Когдато давно, на заре моего увлечения, а это было еще в прошлом веке и даже тысячелетии ![😅](tg://emoji?id=128949399) , командой мы делали систему распознавания осетинского языка и компилятивный синтезатор осетинской речи\.\n"
        "Создаем маленькие языковые игры\. А прямо сейчас, работаем над системой проверки орфографии\.\n"
      , parse_mode='MarkdownV2')

async def stiker(update, context):
    await update.message.reply_text("Команды всякие нужны! Но писать скучно и долго, поэтому предлагаю только /start, /help и /source)))")

async def selfie(update, context):
    await context.bot.send_photo(
        update.message.chat_id, photo=open(r'images/selfie.jpg', 'rb'))

async def gpt(update, context):
    audio = open(r'audio/gpt.ogg', 'rb')
    await context.bot.send_audio(update.message.chat_id, audio)
    audio.close()

async def stiker(update, context):
    await context.bot.send_photo(
        update.message.chat_id, photo=open(r'images/mak0.jpg', 'rb'))
    await update.message.reply_html(
        "Это была скучная фоточка, но у меня есть куча стикеров  <a href='https://t.me/addstickers/MD_Makarenko'> со мной. </a> Пользуйтесь, люди добрые")



async def nosql(update, context):
    audio = open(r'audio/nosql.ogg', 'rb')
    await context.bot.send_audio(update.message.chat_id, audio)
    audio.close()

async def love(update, context):
    audio = open(r'audio/love.ogg', 'rb')
    await context.bot.send_audio(update.message.chat_id, audio)
    audio.close()


async def source(update, context):
    await update.message.reply_html("Исходный код всего этого добра <a href='https://github.com/Makarenkomd/Bot_yandex_practicum.git'> тут </a>")

command_dict = {'фото и сюрприз': stiker, 'sql и nosql': nosql, "про любовь": love}
async def echo(update, context):
    text = update.message.text
    if text in command_dict:
        await command_dict[text](update, context)
    else:
        await update.message.reply_text("я тупой ботик, я такой не понимай)")

def main():
    application = Application.builder().token(TOKEN).build()
    text_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, echo)
    application.add_handler(text_handler)
    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))
    application.add_handler(CommandHandler("hobby", my_hobby))
    application.add_handler(CommandHandler("selfie", selfie))
    application.add_handler(CommandHandler("gpt", gpt))
    #application.add_handler(CommandHandler("nosql", nosql))
    #application.add_handler(CommandHandler("stiker", stiker))
    #application.add_handler(CommandHandler("love", love))

    application.add_handler(CommandHandler("source", source))

    application.run_polling()


if __name__ == '__main__':
    main()
