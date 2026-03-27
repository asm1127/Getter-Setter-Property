class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    def get_age(self):
        return self.__age

    def set_age(self, volue):
        if volue < 0:
            return ValueError("Yosh mangiy bo'lmasligi lozim!")
        self.__age = volue

bobur = User("Bobur", "Jovliyev", 15)
print(bobur.get_age())
bobur.set_age(20)
print(bobur.get_age())

#Python'da getter va setter - bu obyekt (class) ichidagiatributlarga (o'zgaruvchilarga) nazorat
#bilan murojaat qilish uchun ishlatiladigan metod.

#Oddiy qilib aytganda:
#   Getter - qiymat olish
#   Setter - qiymatni o'rnatish (yoki o'zgartirish) uchun

#Python'dagi property - bu atribut (o'zgaruvchi) bilan ishlayotgandek ko'rinib, aslida metod orqali nazorat
#qilish imkonini beradigan mexanizm

#Oddiy qilib: property = getter + setter'ni "yashirish" va chiroyli qilish

class User:
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.__age = age

    @property
    def get_age(self):
        return self.__age

    @get_age.setter
    def set_age(self, volue):
        if volue < 0:
            return ValueError("Yosh mangiy bo'lmasligi lozim!")
        self.__age = volue

bobur = User("Bobur", "Jovliyev", 15)

print(bobur.get_age)
bobur.set_age = 25
print(bobur.get_age)