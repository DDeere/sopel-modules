import sopel.module
import random
import urllib2.urlopen

data = urllib.request.urlopen('https://gist.githubusercontent.com/deathbybandaid/cf1faedb87098224943dc04453bc3f79/raw/5ef59ed209f580bf0a7885945e816445aea178e3/gistfile1.txt')
lines = open(data).read().splitlines()
myline =random.choice(lines)


@sopel.module.commands('ferengi')

def ferengi(bot, trigger):
    bot.say(myline)
