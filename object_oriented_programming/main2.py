class Oop :
    def __init__(self, stackTech, softSkill, scoreS):
        self.tech = stackTech
        self.softK = softSkill
        self.score = scoreS

Backend = Oop("Python", "Fast Learning", 100)
Webd = Oop("php", "Work Hard", 80)
Webk = Oop("ruby", "dilligent", 90)

print(Backend.tech)
print(Webd.softK)
print(Webk.__dict__)


