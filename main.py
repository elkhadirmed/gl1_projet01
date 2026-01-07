import string
import random
letters=string.ascii_letters
c=""
while c!="w":
    c=random.choice(letters)
    print(c,end="",flush=True)