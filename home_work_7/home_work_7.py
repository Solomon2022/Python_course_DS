# Создайте класс User и и его наследника класс SuperUser, которые описывают пользователя и супер-пользователя.
# В классе User необходимо описать:
# ● Конструктор, который принимает в качестве параметров значения для атрибутов name, login и password;
# ● Методы для изменения и получения значений атрибутов;
# ● Метод show_info, который печатает в произвольном формате значения атрибутов name и login;
# ● Атрибут класса count для хранения количества созданных экземпляров класса User.
# Необходимые условия, которые надо учесть после создания объекта:
# ● Атрибут name доступен и для чтения, и для изменения;
# ● Атрибут login доступен только для чтения;
# ● Атрибут password доступен только для изменения.
# В классе SuperUser необходимо описать:
# ● Конструктор, который принимает в качестве параметров значения для атрибутов name, login, password и role;
# ● Метод для изменения и получения значения атрибута role;
# ● Метод show_info, который печатает в произвольном формате значения атрибутов name, login и role;
# ● Атрибут класса count для хранения количества созданных экземпляров класса SuperUser.

class User:
    count = 0

    def __init__(self, name, login, password):
        self.__name = name
        self.__login = login
        self.__password = password
        User.count += 1

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def login(self):
        return self.__login

    def set_password(self, value):
        self.__password = value

    password = property(fset=set_password)

    def show_info(self):
        print(f'name: {self.name}, login: {self.login}', end='')


a = User('Max', 'Max2000', '111r222')
a.show_info()
a.name = 'Leo'
print(a.name)
print(a.login)
a.password = 222
print()


class SuperUser(User):
    count = 0

    def __init__(self, name, login, password, role):
        super().__init__(name, login, password)
        self.__role = role
        SuperUser.count += 1

    @property
    def role(self):
        return self.__role

    @role.setter
    def role(self, value):
        self.__role = value

    def show_info(self):
        super().show_info()
        print(f', role: {self.role}')


b = SuperUser('Viktor', 'Vik200', '111', 'Admin')
b.show_info()
print(b.role)
b.role = 'User'
b.show_info()
print()

print(f'Количество обекты класса User: {User.count}')
print(f'Количество объектов класса SuperUser: {SuperUser.count}')
