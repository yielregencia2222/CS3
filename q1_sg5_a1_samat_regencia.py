class Hero:
    def __init__(self,hp,name):
        self.hp = hp
        self.name = name
        print(self.name,":",self.hp,"hp")
    def damage(self,take_damage):
        self.hp -= take_damage
        
        print(self.name,"took",take_damage,"damage!")
        print(self.name,"'s health:",self.hp,"hp")

arthur = Hero(100,"Arthur")
morgana = Hero(100,"Morgana")
arthur.damage(10)




