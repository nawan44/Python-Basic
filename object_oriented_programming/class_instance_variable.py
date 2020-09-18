class Oop :
    #class variable
    con = 0
    def __init__(self, stackTech, softSkill, scoreS):
        self.tech = stackTech
        self.softK = softSkill
        self.score = scoreS
	    Oop.con += 1
        print("Make OOP with " + stackTech)

Backend = Oop("Python", "Fast Learning", 100)
print(Oop.con)
Webd = Oop("php", "Work Hard", 80)
print(Oop.con)
Webk = Oop("ruby", "dilligent", 90)
print(Oop.con)

print(Backend.tech)
print(Webd.softK)
print(Webk.__dict__)


