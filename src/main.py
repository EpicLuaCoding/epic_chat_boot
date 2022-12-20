from random import random # auswahl was gesagt wird
from model import AI # ai zum ai erstellen
from functions.load import *

KI = AI(load_file("memory.json")) # KI objekt erstellen
print("start")
while True:
    text = input()
    an = KI.chat_mode(text)
    print(an)
    



