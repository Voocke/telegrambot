
import telebot
from telebot import types


bot = telebot.TeleBot("6877459397:AAFHxn7WXz_TRzLJQ89n_hweoTXsdgsXTeU")


@bot.message_handler(commands=['start'])
def start(message):
  markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
  item1 = types.KeyboardButton('📚 Бриф/Заказ') 
  item2 = types.KeyboardButton('📱 Контакты') 
  item3 = types.KeyboardButton('🎨 Художникам') 
  item4 = types.KeyboardButton('❓ FAQ') 

  markup.add(item1, item2, item3, item4)
  
  bot.send_message(message.chat.id,'Привет, {0.first_name}!'.format(message.from_user), reply_markup = markup)

@bot.message_handler(content_types=['text'])
def bot_message(message):
  
    if message.text == '📚 Бриф/Заказ':     
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('Начать Бриф')
      back = types.KeyboardButton('Меню')
      markup.add(item1, back)
      bot.send_message(message.chat.id, 'Тут вы можете пройти бриф (ответить на несколлько вопросов для определения конкретного тз), и оставить заявку', reply_markup = markup)
  
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

   
    elif message.text == '❓ FAQ':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      back = types.KeyboardButton('Меню')
      markup.add(back)
      bot.send_message(message.chat.id, 'FAQ', reply_markup = markup)
      bot.send_message(message.chat.id, '❓Как узнать цену?\nЦена будет известна после прохождения брифа и определения с ТЗ.\n\n❓Сколько будет выполняться работа?\nВ среднем работа выполняется от пары дней до нескольких недель.\n\n❓Как связаться с художником?\nПосле прохождения брифа и выбора определённого художника вы получаете его кантакты', reply_markup = markup)



    elif message.text == 'Меню':
      markup = types.ReplyKeyboardMarkup(resize_keyboard = True)
      item1 = types.KeyboardButton('📚 Бриф/Заказ') 
      item2 = types.KeyboardButton('📱 Контакты') 
      item3 = types.KeyboardButton('🎨 Художникам') 
      item4 = types.KeyboardButton('❓ FAQ') 
      markup.add(item1, item2, item3, item4)
      bot.send_message(message.chat.id, 'Меню', reply_markup = markup)



if __name__ == "__main__":
  bot.polling(none_stop = True)
