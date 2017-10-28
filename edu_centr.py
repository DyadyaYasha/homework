class Kurs(object):
    def __init__(self, kurs):
        self.kurs = kurs

    def get_kurs(self):
        return self.kurs

    def set_kurs(self, kurs):
        self.kurs = kurs

    def add_group(self, group):
        self.Group = group



class Group(object):
    def __init__(self, nomer):
        self.nomer = nomer

    def get_nomer(self):
        return self.nomer

    def set_nomer(self, nomer):
        self.nomer = nomer


    def add_stud(self, stud):
        self.Stud = stud

    def del_stud(self, stud):
        print('Студент удалён')


    def add_prepod(self, prepod):
        if self.Prepod is Note:
            self.Prepod = prepod
        else:
            print('Нельзя добавить второго учителя')

    def re_prepod(self, prepod):
        self.Prepod = prepod
        print('У группы {} новый преподаватель {}'.format(self.get_nomer, self.prepod))

    def del_prepod(self, prepod):
        self.Prepod = None
        print('Преподаватель удалён')


class Person(object):
    def __init__(self, firstname, lastname, age):
        self.firstname = firstname
        self.lastname = lastname
        self.age = age

    def print_info(self):
        print('{}: {}, {}, {}'.format(self.__class__.c_name, self.firstname, self.lastname, self.age))


class Prepod(Person):
    c_name = u'Преподаватель'
    def __init__(self, firstname, lastname, age, predmet):
        super().__init__(firstname, lastname, age)
        self.predmet = predmet

    def print_info(self):
        super().print_info()
        print('Предмет: {}'.format(self.predmet))

class Stud(Person):
    c_name = u'Студент'
    def __init__(self, firstname, lastname, age, nom_st_bilet):
        super().__init__(firstname, lastname, age)
        self.nom_st_bilet = nom_st_bilet

    def print_info(self):
        super().print_info()
        print('Номер студня: {}'.format(self.nom_st_bilet))
