class NumBook(object):

    def __init__(self):
        self.abonents = {'Ваня': 380637035723, 'Коля': 380685129827, 'Петя': 380661411205}

    def add_abon(self, name=None, tel=None):
        if name is None:
            name = input("Input name: ")
        if tel is None:
            tel = int(input("Input tel: "))
        self.abonents["name"] = tel

    def del_abon(self, num):
        del self.abonents[num]

    def out_abon(self):
        print("Abonents:")
        for key in self.abonents.keys():
            print(key, ': ', self.abonents[key])

    def find_num_abon(self, num):
        print('find_num: ', self.abonents.get(num, 'unknown name'))

    def find_name_abon(self, name):
        for key in self.abonents.keys():
            if self.abonents[key] == name:
                print('find_name:', key)


num_book = NumBook()
a = int(input("""0 - новый контакт
1 - просмотр книги
2 - поиск по имени
3 - поиск по номеру
4 - удаление записи    """))
if a == 0:
    num_book.add_abon()
elif a == 1:
    num_book.out_abon()
elif a == 2:
    num_book.find_name_abon()
elif a == 3:
    num_book.find_num_abon()
elif a == 4:
    num_book.del_abon()