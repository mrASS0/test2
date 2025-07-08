import random

def gen_pass(pass_length):
    # pass_length = int(input("immetti la lunghezza della password"))
    elements = "+-/*!&$#?=@<>"
    password = ""

    for i in range(pass_length):
        password += random.choice(elements)
        #password = passord + random.choice(elements)

    #print(password)
    return password

def testa_o_croce():
    return random.choice(['Testa', 'Croce'])

def emoji_casuale():
    return random.choice("😂🌟📚😍🎉🐱⚽🎵🌟🔥😎😂🍎😀🍕🚀🤔🐶🍀👍")

