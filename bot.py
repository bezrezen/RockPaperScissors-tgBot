import config
import telebot
from telebot import types
import random

bot = telebot.TeleBot (config.token)

@bot.message_handler(commands=['start'])
def start_message(message):
  kboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
  stone = types.KeyboardButton('✊')
  scissors = types.KeyboardButton('✌️')
  paper = types.KeyboardButton('🖐')
  kboard.add(stone,scissors,paper, row_width= 3)
  bot.send_message(message.chat.id,"Привет. Сыграем?",reply_markup = kboard)

@bot.message_handler(content_types=['text'])
def game(message):
  answers = ("✊","✌️","🖐")
  ai_answer = random.choice(answers)
  if message.text == ai_answer:
    bot.send_message(message.chat.id, "Ничья")
  elif (message.text == "✊") and (ai_answer == "✌️"):
    bot.send_message(message.chat.id,'Ты победил')
  elif (message.text == '🖐') and (ai_answer == "✊"):
    bot.send_message(message.chat.id,'Ты победил')
  elif (message.text == '✌️') and (ai_answer == '🖐'):
    bot.send_message(message.chat.id,'Ты победил')
  else:
    bot.send_message(message.chat.id,'Ты проиграл')
  bot.send_message(message.chat.id, "Я выбрал: " + ai_answer)

bot.infinity_polling()
