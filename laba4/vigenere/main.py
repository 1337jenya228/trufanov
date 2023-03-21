from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import random as rnd

start_file = 'text.txt'
new_file = start_file[:-4]+'.txt'
alfavitEN =  'abcdefghijklmnopqrstuvwxyz'
alfavit_spec = ' \,./;:"][}{+-*&^%#@'
def readFile(file):
    with open(file,'r') as text:
        mylist = text.read()
    return mylist

def printFirstString(file):
    with open(file,'r') as text:
        return text.readline()

def writeFile(file, value):
    with open(value+new_file,'w') as text:
        text.write(file)
    return file

def kvadratVigenere(alfavit):
    array = list(alfavit.upper())
    for i in range(len(alfavit)):
        for i in array:
            if i == array[0]:
                print(end="|")
            print(i, end="|")
        array.append(array[0])
        array.remove(array[0])
        print()

def form_dict():
    dict = {}
    iter = 0
    for i in range(0,len(alfavitEN)):
        dict[iter] = alfavitEN[i]
        iter = iter +1
    return dict

def form_dict_spec():
    dict = {}
    iter = 52
    for i in range(0,len(alfavit_spec)):
        dict[iter] = alfavit_spec[i]
        iter = iter +1
    return dict

def encode_val(file):
    text = readFile(file)
    list_code = []
    lent = len(text)
    d = form_dict()
    d_spec = form_dict_spec()

    for w in range(lent):
        if text[w] in alfavitEN:
            for value in d:
                if text[w] == d[value]:
                    list_code.append(value)
        else:
            for value in d_spec:
                if text[w] == d_spec[value]:
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

def encryptionVigener(value, key):
    dic = comparator(value, key)
    result = []
    d = form_dict()
    for v in dic:
        if dic[v][0] > 51:
            result.append(dic[v][0])
        else:
            go = (dic[v][0]+dic[v][1]) % len(d)
            result.append(go)
    return result

def decode_val(list_in):
    list_code = []
    lent = len(list_in)
    d = form_dict()
    d_spec = form_dict_spec()
    for i in range(lent):
        if list_in[i] < 52:
            for value in d:
                if list_in[i] == value:
                    list_code.append(d[value])
        else:
            for value in d_spec:
                if list_in[i] == value:
                    list_code.append(d_spec[value])

    return list_code


def decryptionVigener(value, key):
    dic = comparator(value, key)
    d = form_dict()
    result =[]
    for v in dic:
        if dic[v][0] > 51:
            result.append(dic[v][0])
        else:
            go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
            result.append(go)
    return result

encryption_key = input('Введите ключ шифрования: ')
decryption_key = input('Введите ключ дешифрования: ')
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


kvadratVigenere(alfavitEN)



result_encryptionVigenere = encryptionVigener(start_file, encryption_key)
writeFile(result_encryptionVigenere, 'encV_')
result_decryptionVigenere = decryptionVigener('encV_' + new_file, decryption_key)
writeFile(result_decryptionVigenere, 'decV_')

# first_string_start_file=PrintFirstStringFile(start_file)
# first_string_enc_file=PrintFirstStringFile('encV_'+new_file)
# first_string_dec_file=PrintFirstStringFile('decV_'+new_file)
# class windows():

#     root = Tk()
#     root.title('Первые строки')
#     root.geometry('400x200')
#     first_str_start = Label(root, text='Первая строка исходного файла')
#     str_start = Label(root, text=first_string_start_file)
#     first_str_encC = Label(root, text='Первая строка зашифрованого файла')
#     str_enc = Label(root, text=first_string_enc_file)
#     first_str_decC = Label(root, text='Первая строка расшифрованого файла')
#     str_dec = Label(root, text=first_string_dec_file)
#     first_str_start.pack()
#     str_start.pack()
#     first_str_encC.pack()
#     str_enc.pack()
#     first_str_decC.pack()
#     str_dec.pack()
#     root.mainloop()
