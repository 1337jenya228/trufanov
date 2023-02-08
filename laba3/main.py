import json

with open('users.json', 'r') as j:
    text = j.read()
    list_of_users = json.loads(text)

#В нашем листе будут хранится словари, которые вы создаёте для каждого юзера
#теперь при регистрации нового пользователя мы делаем следующее:

with open('users.json', 'w') as j:
    text = json.dumps(list_of_users)
    j.write(text)