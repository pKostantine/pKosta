import random

game=random.randint(1,3)
if game==1:
    game="rock"
elif game==2:
    game="paper"
else:
    game="scissors"
print(game)