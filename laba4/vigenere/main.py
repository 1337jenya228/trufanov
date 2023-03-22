from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import random as rnd

def readFile(file):
    with open(file,'r') as text:
        mystr = text.read()
    return mystr

def writeFile(file, text, value):
    with open(value+file,'w') as file:
        file.write(text)
    return text

def readFileOneLine(file):
    with open(file,'r') as text:
        mystr = text.readline()
    return mystr[0:mystr.find('.')]

alfavitEN = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
alfavitSPEC = ' \n,./;:"][}{+-*&^%#@'
#alfavit1 = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'

def form_dict():
    d = {}
    iter = 0
    for i in range(0, len(alfavitEN)):
        d[iter] = alfavitEN[i]
        iter = iter +1
    return d

def form_dict_spec():
    d = {}
    iter = 66
    for i in range(0, len(alfavitSPEC)):
        d[iter] = alfavitSPEC[i]
        iter = iter +1
    return d

def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict()
    d_spec = form_dict_spec()

    for w in range(lent):
        if word[w] in alfavitEN:
            for value in d:
                if word[w] == d[value]:
                    list_code.append(value)
        else:
            for value in d_spec:
                if word[w] == d_spec[value]:
                    list_code.append(value)



    return list_code

def comparator(value, key):
    len_key = len(key)
    dic = {}
    iter = 0
    full = 0

    for i in value:
        dic[full] = [i,key[iter]]
        full = full + 1
        iter = iter +1
        if (iter >= len_key):
            iter = 0
    return dic

def full_encode(value, key):
    dic = comparator(value, key)
    lis = []
    d = form_dict()

    for v in dic:
        if dic[v][0] > 65:
            lis.append(dic[v][0])
        else:
            go = (dic[v][0]+dic[v][1]) % len(d)
            lis.append(go)
    return lis

def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict()
    d_spec = form_dict_spec()

    for i in range(lent):
        if list_in[i] < 66:
            for value in d:
                if list_in[i] == value:
                    list_code.append(d[value])

        else:
            for value in d_spec:
                if list_in[i] == value:
                    list_code.append(d_spec[value])

    return list_code


def full_decode(value, key):
    dic = comparator(value, key)
    d = form_dict()
    lis =[]

    for v in dic:
        if dic[v][0] > 65:
            lis.append(dic[v][0])
        else:
            go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
            lis.append(go)
    return lis


def kvadratVigenera(alfavit):
    array = list(alfavitEN)
    for i in range(len(alfavit)):
        for i in array:
            if i == array[0]:
                print(end="|")
            print(i, end="|")
        array.append(array[0])
        array.remove(array[0])
        print()

alfavit_choice = int(input('Выберие алфавит замены\n1 - случайным образом\n2 - по порядку\n'))

if alfavit_choice == 1:
    alfavitEN = list(alfavitEN)
    rnd.shuffle(alfavitEN)
    new_alfavit = ''
    for letter in alfavitEN:
        new_alfavit += letter
    alfavitEN = new_alfavit
else:
    alfavitEN = alfavitEN

file_name = 'text.txt'
word = readFile(file_name)

key =input('Введите ключ:')
key_encoded = encode_val(key)
value_encoded = encode_val(word)
shifre = full_encode(value_encoded, key_encoded)
writeFile('text.txt', ''.join(decode_val(shifre)), 'encV_')
decoded = full_decode(shifre, key_encoded)
decode_word_list = decode_val(decoded)
writeFile('text.txt', ''.join(decode_word_list), 'decV_')

kvadratVigenera(alfavitEN)

first_string_start_file=readFileOneLine(file_name)
first_string_enc_file=readFileOneLine('encV_'+file_name)
first_string_dec_file=readFileOneLine('decV_'+file_name)

class windows():
    root = Tk()
    root.title('Первые строки')
    root.geometry('400x200')
    first_str_start = Label(root, text='Первая строка исходного файла')
    str_start = Label(root, text=first_string_start_file)
    first_str_encV = Label(root, text='Первая строка зашифрованого файла')
    str_enc = Label(root, text=first_string_enc_file)
    first_str_decV = Label(root, text='Первая строка расшифрованого файла')
    str_dec = Label(root, text=first_string_dec_file)
    first_str_start.pack()
    str_start.pack()
    first_str_encV.pack()
    str_enc.pack()
    first_str_decV.pack()
    str_dec.pack()
    root.mainloop()