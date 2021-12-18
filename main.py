import csv
import re
from pprint import pprint


def unpack_person(l_name, f_name, s_name, *args):
    name = f'{l_name} {f_name} {s_name}'
    info_list = list(args)
    if len(info_list) > 2:
        info_list = info_list[:2]
    return name, info_list

def phone_to_example(phone):
    find_pattern = re.compile(r'(\+7|8)?\s*\(?(\d{3})\)?[\s-]*(\d{3})'
                              r'[\s-]*(\d{2})[\s-]*(\d{2})[\s(]*'
                              r'([а-я]*)[. ]*(\d+)*[\s )]*')
    ph_pattern = r'+7(\2)\3-\4-\5 \6.\7'
    changed_phone = find_pattern.sub(ph_pattern, phone).rstrip(' .')
    return changed_phone


class Worker:

    def __init__(self, person_list):
        self.worker_dict = {}
        self.email = person_list.pop(-1)
        self.phone = phone_to_example(person_list.pop(-1))
        self.name, self.info = unpack_person(*person_list)
        self.key_name = ' '.join(self.name.split()[:2])
        if len(self.name.split()) == 2:
            self.list_for_phbook = self.name.split() + [''] + self.info \
                                   + [self.phone] + [self.email]
        else:
            self.list_for_phbook = self.name.split() + self.info \
                                   + [self.phone] + [self.email]
        self.worker_dict[self.key_name] = self.list_for_phbook

    def change_value(self, dict_phbook):
        val_in_dict = dict_phbook[self.key_name]
        sorted_vals = list(map(sorted, zip(self.list_for_phbook, val_in_dict)))
        new_val = [val[1] for val in sorted_vals]
        return new_val


def rewrite_ph_book(phone_book):
    new_phone_book = [phone_book[0]]
    dict_new_phbook = {}

    for line in phone_book[1:]:
        person = Worker(line)
        if person.key_name in dict_new_phbook:
            dict_new_phbook[person.key_name] = person.change_value(dict_new_phbook)
        else:
            dict_new_phbook.update(person.worker_dict)

    for val in dict_new_phbook.values():
        new_phone_book.append(val)
    return new_phone_book


if __name__ == '__main__':

    with open('phonebook.csv') as f:
        rows = csv.reader(f, delimiter=',')
        phone_book = list(rows)
        new_phone_book = rewrite_ph_book(phone_book)

    with open('new_phonebook.csv', 'w') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(new_phone_book)