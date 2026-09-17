class Glassware:
    def __init__(self,id):
        self.id = id
    def __del__(self):
        print("Glassware has been shattered.")
class Beaker(Glassware):
    def __init__(self,id):
        super().__init__(id)
        print("Beaker",id,"is created ",end="")
class Tray:
    def __init__(self):
        print("Tray is created.")
        self.beaker = []
    def add_beaker(self,id):
        if len(self.beaker) < 5:
            self.beaker.append(Beaker(id))
            print("and is added to the tray.")
        else:
            print("Tray is full! Beaker",id,"cannot be added.")
    def __del__(self):
        print("Tray was destroyed")
        self.beaker.clear()
        
tray = Tray()
tray.add_beaker("001")
tray.add_beaker("002")
tray.add_beaker("004")
tray.add_beaker("005")
tray.add_beaker("006")
tray.add_beaker("010")
del tray

   
   






