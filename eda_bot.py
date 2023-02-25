import telebot
import requests

API_link = "https://api.telegram.org/bot2117684429:AAGpIZ6VJXnRJOZ3Vnu2yogRqeikYgiNt1Q"

updates = requests.get(API_link + "/getUpdates").json()

#print (updates)

bot = telebot.TeleBot('6198295155:AAF6hW4_lJpCrC9FqbJhrhJQnbcOWBrDMic')

keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('-1 энергетик', '-1 кусок пиццы','остаток')

#keyboard2 = telebot.types.ReplyKeyboardMarkup()
#keyboard2.row('smth like poetry','smth like films')
users = []
count_p = {}
count_e = {}
count_t = {}
@bot.message_handler(commands=['start'])
def start_message(message):
    global user_id
    user_id = message.from_user.username
    users.append(user_id)
    count_p[user_id] = 2
    count_e[user_id] = 1
    count_t[user_id] = 1
    bot.send_message(message.chat.id, 'Привет! \n Как тебя зовут?', reply_markup=keyboard1) 


@bot.message_handler(content_types=['text'])
def default_test(message):
    if message.text.lower() == 'остаток':
        keyboard00 = telebot.types.InlineKeyboardMarkup()
        bot.send_message(message.chat.id,"Осталось "+str(count_p[user_id])+" кусочка пиццы! \n")
        bot.send_message(message.chat.id,"Осталось "+str(count_e[user_id])+" энергетиков!")
        bot.send_message(message.chat.id, "Берешь ещё?)", reply_markup=keyboard00)
    elif message.text.lower() == '-1 энергетик':
        if (count_e[user_id] > 0):
            bot.send_message(message.chat.id, "Заряжайся с Powercell!")
            count_e[user_id] = count_e[user_id]-1
        elif (count_e[user_id] <= 0):
            bot.send_message(message.chat.id, "Ничего не осталось!(")
    elif message.text.lower() == '-1 кусок пиццы':
        if (count_e[user_id] > 0):
            bot.send_message(message.chat.id, 'От Ростелекома с любовью!')
            count_p[user_id] = count_p[user_id]-1
        elif (count_p[user_id] <= 0):
            bot.send_message(message.chat.id, "Ничего не осталось!(")
       # bot.send_message(338756016,"Маша is waitin!")
    
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
       keyboard00.add(telebot.types.InlineKeyboardButton(text="smth like films", url="https://www.netflix.com/watch/80212201?trackId=15035895") )
        keyboard00.add(telebot.types.InlineKeyboardButton(text="smth like poetry", url="https://www.culture.ru/poems/39864/kolizei") )
       """
bot.polling()