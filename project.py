import random

def gen_pass():
    Passchar="+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

    passlength= 50
    mainpass= ""

    for i in range(passlength):
        mainpass += random.choice(Passchar)

    return mainpass



sampah_organic = ['daun', 'makanan sisa', 'kotoran hewan', 'buah/sayur busuk', 'tulang', 'ranting']
sampah_anorganic= ['kertas','ban', 'karet', 'melamin', 'plastik','aluminium','baterai', 'kabel' ]