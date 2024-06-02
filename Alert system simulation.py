
import telebot
import random
import time
from datetime import datetime


bot = telebot.TeleBot("")

'''
import telebot

bot = telebot.TeleBot("YOUR_BOT_TOKEN")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

'''



    
@bot.message_handler(command=['help', 'start'])
def send_welcome(message):
	bot.reply_to(message, "Howdy, how are you doing?")
    

@bot.message_handler(func=lambda message: True)
def send_welcoming(message):
    true = True
    a = 25
    b = [1,2,3]
    c = ["RACK1","RACK2","RACK3"]
    d = 0
        
    bot.send_message(message.from_user.id, "okay")

    while message.text == "a":
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        ranger = random.choice(b)
        
###############################################################################
        
        if ranger == 1:
            a+=1
            time.sleep(1)
            
            if a > 27:
                d += 1
                print(f"temperature increase = {a} | d = {d}")
                if d/60 == 1:
                    print(f"{a} | Temperature increase | {current_time} | {d}/60 = {d/60}")
                    ranger2 = random.choice(c)
                    bot.send_message(message.chat.id, f"temperature = {a} CRITICAL\nRack = {ranger2}\nTime = {current_time}")
                elif d >= 60:
                    d-=d
               # else:
                    #continue
            else:
                d += 1
                print(f"temperature increase = {a} | d = {d}")
                if d/60 == 1:
                    print(f"{a} | Temperature increase | {current_time} | {d}/60 = {d/60}")
                elif d >= 60:
                    d-=d
               # else:
                 #   continue
            
###############################################################################
                    
        elif ranger == 2:
            a-=1
            time.sleep(1)
            
            
            if a >= 27:
                d += 1
                print(f"temperature decrease = {a} | d = {d}")
                if d/60 == 1:
                    print(f"{a} | Temperature decrease | {current_time} | {d}/60 = {d/60}")
                    ranger2 = random.choice(c)
                    bot.send_message(message.chat.id, f"temperature = {a} CRITICAL\nRack = {ranger2}\nTime = {current_time}")
                elif d >= 60:
                    d-=d
                #else:
                    #continue
            else:
                d += 1
                print(f"temperature decrease = {a} | d = {d}")
                if d/60 == 1:
                    print(f"{a} | Temperature decrease | {current_time} | {d}/60 = {d/60}")
                elif d >= 60:
                    d-=d
                #else:
                   # continue
            
            
            
###############################################################################            
            
            
        elif ranger == 3:
            time.sleep(1)
            
            
            if a >= 27:
                d += 1
                print(f"temperature remained = {a} | d = {d}")
                if d/60 == 1:
                    print(f"{a} | Temperature remained | {current_time} | {d}/60 = {d/60}")
                    ranger2 = random.choice(c)
                    bot.send_message(message.chat.id, f"temperature = {a} CRITICAL\nRack = {ranger2}\nTime = {current_time}")
                elif d >= 60:
                    d-=d
                #else:
                    #continue
                
                
            else:
                d += 1
                print(f"temperature remained = {a} | d = {d}")
                if d/60 == 1:
                    print(f"{a} | Temperature remained | {current_time} | {d}/60 = {d/60}")
                elif d >= 60:
                    d-=d
                #else:
                    #continue       
            
###############################################################################
                    
                
        else:
            print("########### ", ranger)
            print("###########")
            time.sleep(1)    



    
    
bot.infinity_polling()


"""
true= True

while true:
    print("Not broken")
    true = input("to break loop enter 'n' ")
    if true == "n":
        break
    else:
        continue
"""