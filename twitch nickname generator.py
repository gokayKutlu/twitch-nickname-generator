import random
import os
import urllib.request
import urllib.error
import urllib

consonant = ["r", "t", "y", "p", "s", "d", "f", "g", "h", "k", "l", "z", "c", "v", "b", "n", "m"]
vowel = ["e", "u", "o", "a", "i"]


def clean():
    os.system('cls')

def lettervowel():
    s = random.choice(vowel)
    return s


def letterconsonant():
    s = random.choice(consonant)
    return s

sequence = input("character sequence? b for consonant, a for vowel. for example: abbaba will be like ehdaji === ")

def urlcontrol(x):
    url = 'https://api.twitch.tv/kraken/channels/' + x + '?client_id=zetwdhotx0nxkjp1bo2htn7rm0xb6y'
    try:
        conn = urllib.request.urlopen(url)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        print(x)
        return 1

    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        print('URLError: {}'.format(e.reason))

def loop():
    loop = ""
    for xz in sequence:
        if (xz == "a"):
            name=lettervowel()
            loop=loop+name
        if (xz == "b"):
            name=letterconsonant()
            loop=loop+name
    return loop


def Random():
    i = 0
    while i <= 9:
        x=loop()
        if (urlcontrol(x) == 1):
            i = i + 1

Random()
print("")

while True:
    newNick = input("New nick: A, Exit: B, Change sequence: C ===  ")
    nick = str(newNick)
    if nick == "a":
        clean()
        Random()
        print("")

    elif nick == "b":
        break

    elif nick == "c":
        clean()
        sequence = input("character sequence? b for consonant, a for vowel. for example: abbaba will be like ehdaji === ")
        Random()
        print("")





















