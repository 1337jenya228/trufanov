from tkinter import *
from tkinter import ttk
from tkinter.messagebox import showerror, showwarning, showinfo

start_file = 'text.txt'
new_file = start_file[:-4]+'.txt'
alfavitEN = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
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

def encryptionCaesar(file, move_step,alfavit):
    result = ''
    text = readFile(file)
    for letter in text:
        place = alfavit.find(letter)
        new_place =  place + move_step
        if letter.isupper():
            if letter in alfavit:
                result += alfavit[new_place].upper()
            else:
                result += letter.upper()
        else:
            if letter in alfavit:
                result += alfavit[new_place]
            else:
                result += letter
    return result

def decryptionCaesar(file, move_step,alfavit):
    result = ''
    text = readFile(file)
    for letter in text:
        place = alfavit.find(letter)
        new_place = place - move_step
        if letter.isupper():
            if letter in alfavit:
                result += alfavit[new_place].upper()
            else:
                result += letter.upper()
        else:
            if letter in alfavit:
                result += alfavit[new_place]
            else:
                result += letter
    return result

encryption_step = int(input('Введите шаг шифрования: '))
decryption_step = int(input('Введите шаг дешифрования: '))

if encryption_step or decryption_step > len(alfavitEN/2):
    alfavitEN = alfavitEN + alfavitEN

result_encryptionCaesar = (encryptionCaesar(start_file, encryption_step,alfavitEN))
writeFile(result_encryptionCaesar,'encC_')
result_decryptionCaesar = (decryptionCaesar('encC_'+new_file,decryption_step,alfavitEN))
writeFile(result_decryptionCaesar,'decC_')

first_string_start_file=printFirstStringFile(start_file)
first_string_enc_file=printFirstStringFile('encC_'+new_file)
first_string_dec_file=printFirstStringFile('decC_'+new_file)


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