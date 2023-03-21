import random
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



al_EU = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
al_spec = ' \,./;:"][}{+-*&^%#@'

def form_dict():
    d = {}
    iter = 0
    for i in range(0,len(al_EU)):
        d[iter] = al_EU[i]
        iter = iter +1
    return d

def form_dict_spec():
    d = {}
    iter = 52
    for i in range(0,len(al_spec)):
        d[iter] = al_spec[i]
        iter = iter +1
    return d

def encode_val(word):
    list_code = []
    lent = len(word)
    d = form_dict()
    d_spec = form_dict_spec()

    for w in range(lent):
        if word[w] in al_EU:
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
        if dic[v][0] > 51:
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
        if list_in[i] < 52:
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
        if dic[v][0] > 51:
            lis.append(dic[v][0])
        else:
            go = (dic[v][0]-dic[v][1]+len(d)) % len(d)
            lis.append(go)
    return lis


def kvadratVigenera(alfavit):
    array = list(al_EU)
    for i in range(len(alfavit)):
        for i in array:
            if i == array[0]:
                print(end="|")
            print(i, end="|")
        array.append(array[0])
        array.remove(array[0])
        print()



file_name = 'text.txt'
word = readFile(file_name)


