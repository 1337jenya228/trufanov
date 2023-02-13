from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo


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
    key *= len(text) // len(key) + 1

    for i, j in enumerate(text):
        gg = (ord(j) + ord(key[i]))
        result += chr(gg % 26 + 65)
    return result

def decryptionVigener(file,key):
    result = ''
    file = readFile(file)
    for i, j in enumerate(result):
        gg = (ord(j) - ord(key[i]))
        print(chr(gg % 26 + 65))
        result += chr(gg % 26 + 65)
    return result

encryption_key = input('Введите ключ шифрования: ')
decryption_key = input('Введите ключ дешифрования: ')

result_encryptionVigenere = (encryptionVigener(start_file, encryption_key))
writeFile(result_encryptionVigenere,'encV_')
result_decryptionVigenere = (decryptionVigener('encV_'+new_file,decryption_key))
writeFile(result_decryptionVigenere,'decV_')

first_string_start_file=printFirstStringFile(start_file)
first_string_enc_file=printFirstStringFile('encV_'+new_file)
first_string_dec_file=printFirstStringFile('decV_'+new_file)
class windows():

    root = Tk()
    root.title('Первые строки')
    root.geometry('400x200')
    first_str_start = Label(root, text='Первая строка исходного файла')
    str_start = Label(root, text=first_string_start_file)
    first_str_encC = Label(root, text='Первая строка зашифрованого файла')
    str_enc = Label(root, text=first_string_enc_file)
    first_str_decC = Label(root, text='Первая строка расшифрованого файла')
    str_dec = Label(root, text=first_string_dec_file)
    first_str_start.pack()
    str_start.pack()
    first_str_encC.pack()
    str_enc.pack()
    first_str_decC.pack()
    str_dec.pack()
    root.mainloop()