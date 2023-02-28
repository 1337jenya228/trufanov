from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo
import random as rnd

start_file = 'text.txt'
new_file = start_file[:-4]+'.txt'
alfavitEN =  'abcdefghijklmnopqrstuvwxyz'
def readFile(file):
    with open(file,'r') as text:
        mylist = text.read()
    return mylist
def printFirstStringFile(file):
    with open(file,'r') as text:
        return text.readline()
def writeFile(file, value):
    with open(value+new_file,'w') as text:
        text.write(file)
    return file

def GetPos(letter):
    for i in range(len(alfavitEN)):
        if letter == alfavitEN[i]:
            return i
    return -1

def kvadratVigenera(alfavit):
    array = list(alfavit.upper())
    for i in range(len(alfavit)):
        for i in array:
            if i == array[0]:
                print(end="|")
            print(i, end="|")
        array.append(array[0])
        array.remove(array[0])
        print()
kvadratVigenera(alfavitEN)

def encryptionVigener(file,key):
    result = ''
    text = readFile(file)
    for i in range(len(text)):
        text_pos = GetPos(text[i])
        if text_pos != -1:
            key_pos = GetPos(key[i%len(key)])
            result += matrix[key_pos][text_pos]
        else:
            result += text[i]
    return result

def decryptionVigener(file,key):
    result = ''
    text = readFile(file)
    for i in range(len(text)):
        text_pos = GetPos(text[i])
        if text_pos != -1:
            key_pos = GetPos(key[i%len(key)])
            result += matrix[key_pos][text_pos]
        else:
            result += text[i]
    # result = ''
    # text = readFile(file)
    # for i in range(len(text)):
    #     text_pos = GetPos(text[i])
    #     if text_pos != -1:
    #         j = 1
    #         key_pos = GetPos(key[i%len(key)])
    #         while((matrix[j][key_pos])!=text[i]):
    #             result += alfavitEN[j]
    #             j+=1
    #     else:
    #         result += text[i]
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


len_alf = len(alfavitEN)
matrix = ['a']*len_alf
for i in range(len_alf):
    matrix[i] = ['a']*len_alf
for i in range(len_alf):
    for j in range(len_alf):
        matrix[i][j] = alfavitEN[j]

result_encryptionVigenere = (encryptionVigener(start_file, encryption_key))
writeFile(result_encryptionVigenere,'encV_')
result_decryptionVigenere = (decryptionVigener('encV_'+new_file,decryption_key))
writeFile(result_decryptionVigenere,'decV_')

# first_string_start_file=printFirstStringFile(start_file)
# first_string_enc_file=printFirstStringFile('encV_'+new_file)
# first_string_dec_file=printFirstStringFile('decV_'+new_file)
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