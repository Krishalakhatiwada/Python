print("hi my name is {name}".format(name="Sanu"))
message='I love {} and I miss {}'
print(message.format("youu","youuuuuuuuuuuuuuuu"))
message='i love {} and {}'
print(message.format("tavelling", "drawing"))
number=0x2e4
print("binary of",number,"is:{0:b}".format(number))
number=345
print("hex of",number,"is:{0:x}".format(number))
text='everything happens for a {:>23}'
print(text.format("reason"))
text='everything happens for a {:<12} .'
print(text.format("reason"))
#random
import random as rn
print(rn.randint(100,200))
print(rn.random())




