import requests
import json
tokens_path = "all_tokens.txt"#input("Введите сюда адрес с текстовым файлом с токенами:")
tokens = open(tokens_path,'r').read().split("\n")
user = input("Введите имя логин пользователя на которого подписывать:")
try:
    #print({"Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko",'Authorization':'OAuth '+tokens[1]})
	#"Client-Id": "kimne78kx3ncx6brgo4mv6wki5h1ko"
    target_id = requests.get('https://api.twitch.tv/helix/users?login='+user,headers = {'Authorization': 'Bearer '+tokens[0],'Client-ID': 'kimne78kx3ncx6brgo4mv6wki5h1ko'})
    #print(target_id.json())
    target_id = target_id.json()['data'][0]['id']
except Exception as e:
    print("Неправильное имя пользователя или у вас нет интернета."+ str(e))
    exit()
print("ID пользователя для подписки:"+target_id)

headers = {
        'Accept': 'application/vnd.twitchtv.v5+json',
        'Client-ID': 'uo6dggojyb8d6soh92zknwmi5ej1q2',
        'Authorization':'OAuth '+tokens[1]
    }
amount = 0
while amount>=len(tokens):
    amount = int(input("Сколько крутить подписчиков:"))
    if amount>len(tokens):
        print("Недостаточное количество токенов для накрутки "+str(amount)+" подписчиков.\nИмеется только "+str(tokens(len))+"токенов.")
for token in tokens:
    headers = {"Accept": "application/json",
               "Content-Type": "application/json; charset=utf-8",
               "User-Agent": "okhttp/4.2.2",
               "Client-ID": "kd1unb4b3q4t58fwlpcbzcbnm76a8fp",
               "Authorization": "OAuth "+token,
               "X-Device-ID": "422670681a2043abbbdf8c3beddf111e"
               }
    print(headers)
    data = {"operationName":"FollowUserMutation","variables":{"targetId":target_id,"disableNotifications":False},"extensions":{"persistedQuery":{"version":1,"sha256Hash":"4578066876945d0e3dd72f8a145b63dd3f2a51dc5bcbe3d4a43bed49c81f281d"}},"query":"mutation FollowUserMutation($targetId: ID!, $disableNotifications: Boolean!) {  followUser(input: {targetID: $targetId, disableNotifications: $disableNotifications}) {    __typename    follow {      __typename      disableNotifications    }  }}"}
    print(requests.post('https://gql.twitch.tv/gql',headers = headers,data=json.dumps(data)).text)
print("Всех успешно сабнул.")
