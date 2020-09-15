class Oop: #template
    pass

oop1 = Oop() #object / instance
oop2 = Oop()
oop3 = Oop()

oop1.name = "python"
oop1.level = "junior"

oop2.name = "php"
oop2.level = "mid"

oop3.name = "golang"
oop3.level = "senior"

print(oop1)
print(oop1.__dict__)
print(oop1.name)