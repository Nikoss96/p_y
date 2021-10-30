import telebot
import requests

API_link = "https://api.telegram.org/bot2019823188:AAEd5p70bdR8HNEA-xlPUj9N12h5B9gQZmo"

updates = requests.get(API_link + "/getUpdates").json()

print (updates)

bot = telebot.TeleBot('2019823188:AAEd5p70bdR8HNEA-xlPUj9N12h5B9gQZmo')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('я соскучилась', 'мне грустно','расслабиться','что-нибудь')

#keyboard2 = telebot.types.ReplyKeyboardMarkup()
#keyboard2.row('smth like poetry','smth like films')

@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.username
    bot.send_message(message.chat.id, 'Kitten! You"re welcome!', reply_markup=keyboard1) 


@bot.message_handler(content_types=['text'])
def default_test(message):
    if message.text.lower() == 'что-нибудь':
        keyboard00 = telebot.types.InlineKeyboardMarkup()
        keyboard00.add(telebot.types.InlineKeyboardButton(text="smth like films", url="https://www.netflix.com/watch/80212201?trackId=15035895") )
        keyboard00.add(telebot.types.InlineKeyboardButton(text="smth like poetry", url="https://www.culture.ru/poems/39864/kolizei") )
        bot.send_message(message.chat.id, "Воть", reply_markup=keyboard00)
    elif message.text.lower() == 'я соскучилась':
        bot.send_message(message.chat.id, "Я тоже, малышка🧡")
        bot.send_photo(message.chat.id, 'https://www.meme-arsenal.com/memes/08d27354addf66f5e1dac77739c12c24.jpg')
    elif message.text.lower() == 'мне грустно':
        bot.send_message(message.chat.id, 'Зовем проотца русского стендапа')
        bot.send_message(338756016,"Маша is waitin!")
    elif message.text.lower() == 'расслабиться':
        #global user_id
        #user_id = message.from_user.username()
        bot.send_message(message.chat.id, 'https://www.youtube.com/watch?v=NuRjxnhfDhg')
        #if (status[2] == True):
        #bot.send_message(338756016,"чекай беседу")
        #if (status[0] == True):
        #bot.send.message(393396177,"чекай беседу")
        #if (status[1] == True):
        #bot.send.message(368587151,"чекай беседу")
       # bot.send.message(,"чекай беседу")
       # bot.send.message(,"чекай беседу")
    """
    if message.text.lower() == 'взят' and q.empty() == False:
         q.pop(0)
       # bot.send.message(393396177,"принято")
         bot.send_message(message.chat.id, "за работу: @"+q.get())
       # bot.send.message(368587151,"принято")
       # bot.send.message(,"чекай принято")
       # bot.send.message(,"чекай принято")
       
    if message.text.lower() == 'актив' and message.from_user.username == 393396177:
        status[0]=True
        bot.send_message(message.chat.id, "активен")
        
    if message.text.lower() == 'актив' and message.from_user.username == 368587151:
        status[1]=True
        bot.send_message(message.chat.id, "активен")
        
    if message.text.lower() == 'актив' and message.from_user.username == 338756016:
        status[2]=True
        bot.send_message(message.chat.id, "активен")
        
   # if message.text.lower() == 'актив' and message.from_user.username == 338756016:
      #  status[3]=True
      #  bot.send_message(message.chat.id, " активен")
         
    if message.text.lower() == 'неактив' and message.from_user.username == 393396177:
        status[0]=False
        bot.send_message(message.chat.id, "не активен")
        
    if message.text.lower() == 'неактив' and message.from_user.username == 368587151:
        status[1]=False
        bot.send_message(368587151, "не активен")
        
    if message.text.lower() == 'неактив' and message.from_user.username == 338756016:
        status[2]=False
        bot.send_message(message.chat.id, "не активен")
        
   # if message.text.lower() == 'актив' and message.from_user.username == 338756016:
      #  status[3]=False
      
       # bot.send.message(393396177,"принято")
       # bot.send.message(368587151,"принято")
       # bot.send.message(,"чекай принято")
       # bot.send.message(,"чекай принято")
       
       """
bot.polling()