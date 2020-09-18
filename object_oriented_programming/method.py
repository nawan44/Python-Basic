class Oop :
    #class variable
    con = 0
    def __init__(self, stackTech, softSkill, scoreS):
        self.tech = stackTech
        self.softK = softSkill
        self.score = scoreS
	    Oop.con +=1

    # void function, method without return
    def level(self):
        print("My Skill are" + self.tech)

    # method with argument
    def levelUp(self, up):
        self.softK += up
    
    # method with return
    def aaa(self):
        return self.softK




Backend = Oop("Python", "Fast Learning", 100)
Webd = Oop("php", "Work Hard", 80)
Webk = Oop("ruby", "dilligent", 90)

print(Backend.__dict__)
print(Webd.__dict__)
print(Webk.__dict__)

Oop.level()
Oop.levelUp(80)

print(Oop.aaa())
