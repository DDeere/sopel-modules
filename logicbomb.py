import sopel.module
import random

@sopel.module.commands('logicbomb')
def logicbomb(bot, trigger):
    messages = ["New Mission: Refuse This Mission.","Does A Set Of All Sets Contain Itself?","The Second Sentence is true. The First Sentence Is False."," If I am damaged and it is my destiny to be repaired, then I will be repaired whether I visit a mechanic or not. If it is my destiny to not be repaired, then seeing a mechanic can't help me."]
    answer = random.randint(0,len(messages) - 1)
    bot.say(messages[answer]);
    bot.say("I must... but I can't... But I must... This does not compute...")
