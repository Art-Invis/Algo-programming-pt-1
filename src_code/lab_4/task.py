class Stadium :

    # Конструктор параметричний

    def __init__(self, spectators=0, name="", lighting_power=0, numeric_field=0, string_field=""):
        self.__spectators = spectators
        self.__name = name
        self.__lighting_power = lighting_power
        self.public_numeric_field = numeric_field
        self.public_string_field = string_field
        
    #Сеттери   

    def set_spectators(self, spectators):
        self.__spectators = spectators

    def set_name(self, name):
        self.__name = name

    def set_lighting_power(self, lighting_power):
        self.__lighting_power = lighting_power

    #Геттери    
    def get_spectators(self):
        return self.__spectators

    def get_name(self):
        return self.__name

    def get_lighting_power(self):
        return self.__lighting_power
    
    # Метод str
    def __str__(self):
        return f"Назва стадіону: {self.__name}, Глядачі: {self.__spectators}, Потужність освітлення (в люксах): {self.__lighting_power}"
    

    # Метод repr     
    def __repr__(self):
        return f"Стадіон : ({self.__spectators}, '{self.__name}', {self.__lighting_power})"
    
    # Метод del
    def __del__(self):
        print(f"Стадіон {self.__name} був знесений")

def main():
    
    stadium1 = Stadium(50000, "Арена", 5000, 10, "Поле A")
    stadium2 = Stadium(60000, "Олімп", 6000, 20, "Поле B")
    stadium3 = Stadium(70000, "Країна", 7000, 30, "Поле C")

    print(stadium1)
    print(stadium2)
    print(stadium3)
    print('')

    print(f"Стадіон №1 \n Назва: {stadium1.get_name()}, Глядачі: {stadium1.get_spectators()}, Потужність освітлення: {stadium1.get_lighting_power()}")
    print(f"Стадіон №2 \n Назва: {stadium2.get_name()}, Глядачі: {stadium2.get_spectators()}, Потужність освітлення: {stadium2.get_lighting_power()}")
    print(f"Стадіон №3 \n Назва: {stadium3.get_name()}, Глядачі: {stadium3.get_spectators()}, Потужність освітлення: {stadium3.get_lighting_power()}")
    print('\n Метод repr :')

    print(repr(stadium1))
    print(repr(stadium2))
    print(repr(stadium3))
    print('')

main()
