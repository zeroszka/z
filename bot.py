import pyowm
import telebot

owm = pyowm.OWM('73c7828ec8e37f7644c3ac95931e6fbf')
bot = telebot.TeleBot("1077360060:AAE4wtbHdXTTPvEqMDWvUPJwBVqmmKzkIiw")

@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = owm.weather_at_place( message.text )
    w = observation.get_weather()
    temperature = w.get_temperature('celsius')['temp']
    answer = 'В указаном городе:'  +  w.get_detailed_status() + '\n'
    answer += 'В городе сейчас ' + 't:' + str(temperature) + '\n\n'
    
    bot.send_message(message.chat.id, answer)
    
bot.polling( none_stop = True)
	

