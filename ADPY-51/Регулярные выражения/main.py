from pprint import pprint
import csv
import re
import os
os.system('cls||clear')

# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv",encoding='utf-8') as f:
  rows = csv.reader(f, delimiter=",")
  contacts_list = list(rows)
  
# TODO 1: выполните пункты 1-3 ДЗ
def check_contact_list(contacts_list):
    for key,_ in enumerate(contacts_list):
        if len(_) >7:
            contacts_list[key] = contacts_list[key][:7]
    return contacts_list

def format_number(contacts_list):
    phone_pattern = r'(\+7|8)(\s*)(\(*)(\d{3})(\)*)(\s*)(\-*)(\d{3})(\s*)(\-*)(\d{2})(\s*)(\-*)(\d{2})(\s*)(\(*)(доб)*(\.*)(\s*)(\d+)*(\)*)'
    phone_format = r'+7(\4)\8-\11-\14\15\17\18\19\20'
    new_contacts_list = []
    for _ in contacts_list:
        new_contacts_list.append(re.sub(phone_pattern, phone_format, ','.join(_)).split(','))
    return new_contacts_list

def format_phone(contacts_list):
    fio_pattern= r"^([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]+)(\s*)(\,?)([А-ЯЁа-яё]*)(\,?)(\,?)(\,?)"
    fio_format = r'\1\3\10\4\6\9\7\8'
    new_contacts_list = []
    for _ in contacts_list:
        new_contacts_list.append(re.sub(fio_pattern, fio_format, ','.join(_)).split(','))
    return new_contacts_list

def merging_lists(one, two):
    '''обьединяем 2 списка'''
    new_list = []
    i = 0
    c = one + two
    while i<=6:
        if len(c[i]) == 0:
            new_list.append (c[7+i])
        else:
            new_list.append (c[i])
        i+=1
    return new_list

if __name__ == "__main__":
    contacts_list = check_contact_list(contacts_list)
    output_list = format_phone(format_number(contacts_list))
    new_list=[]
    for key_i, i in enumerate(output_list):
        for key_j, j in enumerate(output_list):
            if i[0] == j[0] and i[1] == j[1] and i is not j:
                temp_contact = merging_lists(output_list[key_i],output_list[key_j])
                if temp_contact not in new_list:
                    new_list.append(temp_contact)
                    a = output_list.pop(key_i)
                    b = [a[0],a[1]]
                    for key_z, z in enumerate(output_list):
                        if a[0] == z[0] and a[1] == z[1]:
                            output_list.pop(key_z)
    output_list += new_list
    
    # TODO 2: сохраните получившиеся данные в другой файл
    # код для записи файла в формате CSV
    contacts_list = output_list
    with open("phonebook.csv", "w") as f:
      datawriter = csv.writer(f, delimiter=',')
      # Вместо contacts_list подставьте свой список
      datawriter.writerows(contacts_list)