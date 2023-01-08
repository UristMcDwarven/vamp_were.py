import random
class Monster:
    def __init__(self, attack, defense, attackrand):
        self.claw = attack
        self.health = defense
        self.attackrange = attackrand
health = 20
while 1 < 2:
    vampire = Monster('4', '1', random.randint(1,6))
    damage = vampire.attackrange
    health -= damage
    print(health)
    if health < 1:
        break
        print(vampire.claw)
        print(vampire.health)
        print(vampire.attackrange)

health = 20
while 1 < 2:
    werewolf = Monster('4', '1', random.randint(2,4))
    damage = werewolf.attackrange
    health -= damage
    print(health)
    if health < 1:
        break
        print(werewolf.claw)
        print(werewolf.health)
        print(werewolf.attackrange)


#Create input that gives them a random 2 option monster fight
#Run combat function using class Monster, object vampire or werewolf


battle = input('Will you fight the vampire or werewolf?')
