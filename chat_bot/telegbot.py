
import telebot
from telebot import types
import sqlite3

bot = telebot.TeleBot("6877459397:AAFHxn7WXz_TRzLJQ89n_hweoTXsdgsXTeU")

#СТАРТ

@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
  item1 = types.KeyboardButton('🎨 Художникам')
  item2 = types.KeyboardButton('❓ FAQ')
  item3 = types.KeyboardButton('📱 Контакты')  
  item4 = types.KeyboardButton('📚 Заказ') 

  markup.add(item1, item2, item3, item4)
  
  bot.send_message(message.chat.id,'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

#МЕНЮ

@bot.message_handler(content_types=['text'])
def bot_message(message):
  
    if message.text == '📚 Заказ':     
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('Начать бриф')
      back = types.KeyboardButton('Меню')
      markup.add(item1, back)
      bot.send_message(message.chat.id, 'Тут вы можете пройти бриф (ответить на несколько вопросов для определения конкретного тз), и создать заказ', reply_markup = markup)

 
    elif message.text == '📱 Контакты':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('Контакты художников')
      item2 = types.KeyboardButton('Контакт создателя бота')
      back = types.KeyboardButton('Меню')
      markup.add(item1, item2, back)
      bot.send_message(message.chat.id, '📱 Контакты', reply_markup = markup)
  
    elif message.text == '🎨 Художникам':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('Регистрация')
      back = types.KeyboardButton('Меню')
      markup.add(item1, back)
      bot.send_message(message.chat.id, 'Если вы художник нажмите на кнопку для регистрации', reply_markup = markup)  


    if message.text == 'Регистрация':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      back = types.KeyboardButton('Меню')
      markup.add(back)
      bot.send_message(message.chat.id, 'Напишите ваше ФИО и номер телефона по примеру:\nТимофеев Иван Сергеевич\n+79602048854', reply_markup = markup)    
      bot.register_next_step_handler(message, artist_menu) 

   
    elif message.text == '❓ FAQ':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      back = types.KeyboardButton('Меню')
      markup.add(back)
      bot.send_message(message.chat.id, 'FAQ', reply_markup = markup)
      bot.send_message(message.chat.id, '❓Как узнать цену?\nЦена будет известна после прохождения брифа и определения с ТЗ.\n\n❓Сколько будет выполняться работа?\nВ среднем работа выполняется от пары дней до нескольких недель.\n\n❓Как связаться с художником?\nПосле прохождения брифа и выбора определённого художника вы получаете его кантакты', reply_markup = markup)


    elif message.text == 'Начать бриф':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      back = types.KeyboardButton('Меню')
      markup.add(back)
      bot.send_message(message.chat.id, "Расскажите, что примерно вы хотите получить.\nВы также можете отправить референс (фото) с описанием желаемого в одном сообщении", reply_markup = markup)
      bot.register_next_step_handler(message, brif_style)


    elif message.text == 'Меню':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('🎨 Художникам')
      item2 = types.KeyboardButton('❓ FAQ')
      item3 = types.KeyboardButton('📱 Контакты')  
      item4 = types.KeyboardButton('📚 Заказ')  
      markup.add(item1, item2, item3, item4)
      bot.send_message(message.chat.id, 'Меню', reply_markup = markup)




#БРИФ ВОПРОСЫ

def brif_style(message):
  if message.text == 'Меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎨 Художникам')
    item2 = types.KeyboardButton('❓ FAQ')
    item3 = types.KeyboardButton('📱 Контакты')  
    item4 = types.KeyboardButton('📚 Заказ')  
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню', reply_markup = markup)
    bot.register_next_step_handler(message, bot_message)
  else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    back = types.KeyboardButton('Меню')
    markup.add(back)
    bot.send_message(message.chat.id, "В каком стиле вы бы хотели увидеть изображение?\n\nЕсли несколько, то перечислите через запятую", reply_markup = markup)
    bot.register_next_step_handler(message, brif_scale)

def brif_scale(message):
  if message.text == 'Меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎨 Художникам')
    item2 = types.KeyboardButton('❓ FAQ')
    item3 = types.KeyboardButton('📱 Контакты')  
    item4 = types.KeyboardButton('📚 Заказ')  
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню', reply_markup = markup)
    bot.register_next_step_handler(message, bot_message)
  else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    back = types.KeyboardButton('Меню')
    markup.add(back)
    bot.send_message(message.chat.id, "Какой вам нужен размер и разрешение у изображения?", reply_markup = markup)
    bot.register_next_step_handler(message, brif_colourmodel)

def brif_colourmodel(message):
  if message.text == 'Меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎨 Художникам')
    item2 = types.KeyboardButton('❓ FAQ')
    item3 = types.KeyboardButton('📱 Контакты')  
    item4 = types.KeyboardButton('📚 Заказ')  
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню', reply_markup = markup)
    bot.register_next_step_handler(message, bot_message)
  else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('RGB')
    btn2 = types.KeyboardButton('CMYK')
    markup.row(btn1,btn2)
    btn3 = types.KeyboardButton('HSB')
    btn4 = types.KeyboardButton('LAB')
    markup.row(btn3,btn4)
    back = types.KeyboardButton('Меню')
    markup.row(back)
    bot.send_message(message.chat.id, "Какая цветовая модель? (RGB, CMYK и тд)", reply_markup = markup )
    bot.register_next_step_handler(message, brif_colour)

def brif_colour(message):
  if message.text == 'Меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎨 Художникам')
    item2 = types.KeyboardButton('❓ FAQ')
    item3 = types.KeyboardButton('📱 Контакты')  
    item4 = types.KeyboardButton('📚 Заказ')  
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню', reply_markup = markup)
    bot.register_next_step_handler(message, bot_message)
  else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('ЧБ')
    btn2 = types.KeyboardButton('ЦВЕТ')
    markup.row(btn1,btn2)
    back = types.KeyboardButton('Меню')
    markup.add(back)
    bot.send_message(message.chat.id, "ЧБ или цветное изображение?", reply_markup = markup)
    bot.register_next_step_handler(message, brif_purpose)


def brif_purpose(message):
  if message.text == 'Меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎨 Художникам')
    item2 = types.KeyboardButton('❓ FAQ')
    item3 = types.KeyboardButton('📱 Контакты')  
    item4 = types.KeyboardButton('📚 Заказ')  
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню', reply_markup = markup)
    bot.register_next_step_handler(message, bot_message)
  else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    btn1 = types.KeyboardButton('Личное')
    btn2 = types.KeyboardButton('Коммерческое')
    markup.row(btn1,btn2)
    back = types.KeyboardButton('Меню')
    markup.add(back)
    bot.send_message(message.chat.id, "Какое назначение?\nДля личного пользования или в коммерческих целях.", reply_markup = markup)
    bot.register_next_step_handler(message, brif_deadline)


def brif_deadline(message):
  if message.text == 'Меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎨 Художникам')
    item2 = types.KeyboardButton('❓ FAQ')
    item3 = types.KeyboardButton('📱 Контакты')  
    item4 = types.KeyboardButton('📚 Заказ')  
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню', reply_markup = markup)
    bot.register_next_step_handler(message, bot_message)
  else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    back = types.KeyboardButton('Меню')
    markup.add(back)
    bot.send_message(message.chat.id, "Какой срок на выполнение?\n (в днях)", reply_markup = markup)
    bot.register_next_step_handler(message, brif_id)

def brif_id(message):
  if message.text == 'Меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎨 Художникам')
    item2 = types.KeyboardButton('❓ FAQ')
    item3 = types.KeyboardButton('📱 Контакты')  
    item4 = types.KeyboardButton('📚 Заказ')  
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню', reply_markup = markup)
    bot.register_next_step_handler(message, bot_message)
  else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    back = types.KeyboardButton('Меню')
    markup.add(back)
    bot.send_message(message.chat.id, "И последнее, Напишите ваше имя и номер телефона", reply_markup = markup)
    bot.register_next_step_handler(message, brif_end)

def brif_end(message):
  if message.text == 'Меню':
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    item1 = types.KeyboardButton('🎨 Художникам')
    item2 = types.KeyboardButton('❓ FAQ')
    item3 = types.KeyboardButton('📱 Контакты')  
    item4 = types.KeyboardButton('📚 Заказ')  
    markup.add(item1, item2, item3, item4)
    bot.send_message(message.chat.id, 'Меню', reply_markup = markup)
    bot.register_next_step_handler(message, bot_message)
  else:
    markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
    back = types.KeyboardButton('Меню')
    markup.add(back)
    bot.send_message(message.chat.id, 'Спасибо за предоставленное тз!\nВ ближайшее время с вами свяжется один из наших художников.')


# МЕНЮ ДЛЯ ХУДОЖНИКОВ
@bot.message_handler(content_types=['text'])
def artist_menu(message):
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('📑 Партфолио')
      item2 = types.KeyboardButton('❔ Поддержка') 
      markup.row(item1,item2)
      item3 = types.KeyboardButton('📚 Заказы')  
      markup.add(item3)
      bot.send_message(message.chat.id,'Добро пожаловать, {0.first_name}!'.format(message.from_user), reply_markup = markup)
      bot.register_next_step_handler(message, artist)


def artist(message):
    if message.text == 'рабочее меню':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('📑 Партфолио')
      item2 = types.KeyboardButton('❔ Поддержка') 
      markup.row(item1,item2)
      item3 = types.KeyboardButton('📚 Заказы')  
      markup.add(item3) 
      bot.send_message(message.chat.id, 'рабочее меню', reply_markup = markup)
      bot.register_next_step_handler(message, artist)

    elif message.text == '📑 Партфолио':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      back = types.KeyboardButton('рабочее меню')
      markup.add(back)
      bot.send_message(message.chat.id, 'В разработке.', reply_markup = markup)
      bot.register_next_step_handler(message, artist)

    elif message.text == '❔ Поддержка':
      keyboard = types.InlineKeyboardMarkup()
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      url_button = types.InlineKeyboardButton(text="Перейти к ассистенту", url="https://t.me/jesbyu")
      back = types.KeyboardButton('рабочее меню')
      keyboard.add(url_button)
      markup.add(back)
      bot.send_message(message.chat.id, 'Напишите ваш вопрос нашему ассистенту', reply_markup = keyboard)
      bot.register_next_step_handler(message, artist)








if __name__ == "__main__":
  bot.polling(none_stop = True)
