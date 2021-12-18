import csv

def unpack_person(l_name, f_name, s_name, *args):
    name = f'{l_name} {f_name} {s_name}'
    info = args
    return name, info


def name_to_example(name_list):
    new_name_list = ' '.join(name_list[:3]).split()
    if len(new_name_list) < 3:
        new_name_list.append('' * (3 -len(new_name_list)))
    name_list[:3] = new_name_list
    return name_list

with open('phonebook.csv') as f:
    rows = csv.reader(f, delimiter=',')
    phone_book = list(rows)
    names_dict = {}

    for person in phone_book[1:]:
        emeil = person.pop(-1)
        phone = person.pop(-1)
        name, info = unpack_person(*person)
        print(name)

lastname,firstname,surname,organization,position,phone,email
Усольцев Олег Валентинович,,,ФНС,главный специалист – эксперт отдела взаимодействия с федеральными органами власти Управления налогообложения имущества и доходов физических лиц,+7 (495) 913-04-78,opendata@nalog.ru
Мартиняхин Виталий Геннадьевич,,,ФНС,,+74959130037,
Наркаев,Вячеслав Рифхатович,,ФНС,,8 495-913-0168,
Мартиняхин,Виталий,Геннадьевич,ФНС,cоветник отдела Интернет проектов Управления информационных технологий,,,
Лукина Ольга Владимировна,,,Минфин,,+7 (495) 983-36-99 доб. 2926,Olga.Lukina@minfin.ru
Паньшин Алексей Владимирович,,,Минфин,,8(495)748-49-73,1248@minfin.ru