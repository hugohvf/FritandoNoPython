from classes.enemy import Enemy

enemy = Enemy(200,60)
print("HP:",enemy.get_hp())

'''
import random


class Enemy:
    hp = 200

    def __init__(self,atkl,atkh):
        self.atkl = atkl
        self.atkh = atkh


    def getAtk(self):
        print("Enemy low attack is", self.atkl)
    def getHp(self):
        print("Hp is",self.hp)

enemy1 = Enemy(40,68)
enemy1.getAtk()
enemy1.getHp()

enemy2 = Enemy(75,140)
enemy2.getAtk()
enemy2.getHp()


'''
# playerhp = 1000
# enemyatkl = 100
# enemyatkh = 250
#
# while playerhp > 0:
#     dmg = random.randrange(enemyatkl, enemyatkh)
#     playerhp -= dmg
#     if playerhp <= 30:
#         playerhp = 30
#
#     print("Enemy strikes for",dmg,"points of damage. Current HP is",playerhp)
#
#     if playerhp > 30:
#         continue
#     print("You have low health, You've been teleported to the nearest inn")
#     break
