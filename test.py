import telebot
import wikipedia
import re


bot = telebot.TeleBot('7362011089:AAGus5SbLCbJ_lji7mi8Oo-7BNy_xgIZYzg')

wikipedia.set_lang('ru')

@bot.message_handler(commands=['start', 'hi'])
def start_message(message, res=False):
  bot.send_message(message.chat.id, 'Привет, отправь мне слово и я найду тебе информацию')

def getwiki(message):
  try:
    info = wikipedia.page(message)
    text = info.content[:1000]
    info_list = text.split('.')
    info_list = info_list[:-1]
    res_text = ''

    for i in info_list:
      if not ('==' in i):
        if len((i.strip())) > 3:
          res_text = res_text + i + '.'
      else:
          break

    res_text = re.sub('\([^()]*\)', '', res_text)
    res_text = re.sub('\([^()]*\)', '', res_text)
    res_text = re.sub('\{[^\{\}]*\}', '', res_text)

    return res_text
    
  except Exception as e:
    return 'В википедии нет информации на это слово'


@bot.message_handler(content_types=['text'])
def answer(message):
  bot.send_message(message.chat.id, getwiki(message.text))


bot.polling(none_stop=True, interval=0)