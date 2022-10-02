class Contact:
    def __init__(self, name, phone, mail):
        self.name = name
        self.phone = phone
        self.mail = mail

class Contacts:
    def __init__(self):
        self.d = [[], [], [], [], [], []] # id, фамилия, имя, отчество, номер телефона, почта

    def __add__(self, contact):
        self.d[0].append(len(self.d[0]) + 1)
        fio = contact.name.split(" ")
        while len(fio) < 3:
            fio.append(None)
        self.d[1].append(fio[0])
        self.d[2].append(fio[1])
        self.d[3].append(fio[2])
        if contact.phone != '':
            self.d[4].append(contact.phone)
        else:
            self.d[4].append(None)
        if contact.mail != '':
            self.d[5].append(contact.mail)
        else:
            self.d[5].append(None)

    def getContact(self, id):
        ans = "ID - " + str(self.d[0][id]) + "\n"
        if self.d[1][id] != None:
            ans += "ФИО: " + self.d[1][id]
        if self.d[2][id] != None:
            ans += " " + self.d[2][id]
        if self.d[3][id] != None:
            ans += " " + self.d[3][id]
        if self.d[4][id] != None:
            ans += "\n" + "Номер телефона: " + self.d[4][id]
        else:
            ans += "\n" + "Номер телефона: " + "None"
        if self.d[5][id] != None:
            ans += "\n" + "Почта: " + self.d[5][id] + "\n"
        else:
            ans += "\n" + "Почта: " + "None" + "\n"
        return ans

    def phoneSearch(self, phone):
        if self.d[4].__contains__(phone):
            id = self.d[4].index(phone)
            print(self.getContact(id))
        else:
            print("Ничего не найдено")

    def mailSearch(self, mail):
        if self.d[5].__contains__(mail):
            id = self.d[5].index(mail)
            print(self.getContact(id))
        else:
            print("Ничего не найдено")

    def search(self, fio):
        ids = []
        if fio[0] != None:
            for i in range(len(self.d[1])):
                if fio[0] == self.d[1][i]:
                    ids.append(self.d[0][i] - 1)
        if fio[1] != None:
            if fio[0] != None:
                for id in ids:
                    if fio[1] != self.d[2][id]:
                        ids.remove(id)
            else:
                for i in range(len(self.d[2])):
                    if fio[1] == self.d[2][i]:
                        ids.append(self.d[0][i] - 1)

        if fio[2] != None:
            if fio[0] != None or fio[1] != None:
                for id in ids:
                    if fio[2] != self.d[2][id]:
                        ids.remove(id)
            else:
                for i in range(len(self.d[3])):
                    if fio[2] == self.d[3][i]:
                        ids.append(self.d[0][i] - 1)

        if len(ids) == 0:
            print("Ничего не найдено")
        else:
            for id in ids:
                print(self.getContact(id))

    def withoutPhOrM(self, num):
        # 1 - без номера, 2 - без почты, 3 - без номера и без почты
        if num == 1:
            for i in range(len(self.d[4])):
                if self.d[4][i] == None:
                    print(self.getContact(i))
            return
        if num == 2:
            for i in range(len(self.d[5])):
                if self.d[5][i] == None:
                    print(self.getContact(i))
            return
        if num == 3:
            for i in range(len(self.d[4])):
                if self.d[4][i] == None and self.d[5][i] == None:
                    print(self.getContact(i))
            return

    def change(self, id, contact):
        id -= 1
        fio = contact.name.split(" ")
        while len(fio) < 3:
            fio.append(None)
        self.d[1][id] = fio[0]
        self.d[2][id] = fio[1]
        self.d[3][id] = fio[2]
        if len(contact.phone) > 0:
            self.d[4][id] = contact.phone
        else:
            self.d[4][id] = None
        if len(contact.mail) > 0:
            self.d[5][id] = contact.mail
        else:
            self.d[5][id] = None

    def printAll(self): #можно убрать, это вывод всех пользователей
        for i in range(len(self.d[0])):
            print(self.getContact(i))

def printCommands():
    print("Список доступных команд: ")
    print("1 - Вывести все контакты", "2 - Поиск по номеру телефона", "3 - Поиск по почте", "4 - Поиск по ФИО",
          "5 - поиск по отсутствию номера телефона/почты", "6 - Изменение контакта", "7 - остановить программу", sep="\n")

print("Введите название файла")
fileName = input()
file = open(fileName, encoding='utf-8')
base = Contacts()
for s in file:
    arr = s.split(",")
    contact = Contact(arr[0],arr[1].replace(" ",""),arr[2].replace(" ","").replace("\n",""))
    base.__add__(contact)
print("База данных сформирована")
printCommands()
p = int(input())
while p!="smth":
    if p==1:
        base.printAll()
    elif p==2:
        print("Введите номер телефона")
        phone = input()
        base.phoneSearch(phone)
    elif p == 3:
        print("Введите почту")
        mail = input()
        base.mailSearch(mail)
    elif p == 4:
        fio = []
        print("Введите фамилию, либо ничего")
        f = input()
        if f=='':
            fio.append(None)
        else:
            fio.append(f)
        print("Введите имя, ничего")
        i = input()
        if i == '':
            fio.append(None)
        else:
            fio.append(i)
        print("Введите отчество, ничего")
        o = input()
        if o == '':
            fio.append(None)
        else:
            fio.append(o)
        base.search(fio)
    elif p == 5:
        print("Введите по чему хотите искать: ", "1 - без номера телефона", "2 - без почты", "3 - без номера телефона и без почты", sep="\n")
        num = int(input())
        base.withoutPhOrM(num)
    elif p == 6:
        print("Введите id, который хотите изменить и новые данные для него", "(запишите данные в две разные строки)", sep="\n")
        id = int(input())
        q = input().split(",")
        contact = Contact(q[0], q[1].replace(" ", ""), q[2].replace(" ", "").replace("\n", ""))
        base.change(id, contact)
    elif p == 7:
        "Вы закрыли программу"
        break
    print()
    printCommands()
    p = int(input())
