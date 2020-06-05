import requests
import json
'''
Swagger API call v 0.5
'''
# задали базовый урл
base_url = 'https://petstore.swagger.io/v2'

# получаем информацию о питомце по ид
def pet(petid):
    api_url = f"{base_url}/pet/{petid}"
    r = requests.get(api_url)
    return r

# получаем информацию о пользователе по имени
def user(username):
    api_url = f"{base_url}/user/{username}"
    r = requests.get(api_url)
    return r

# для обновления информации нам надо послать ИД, имя и статус
def pet_upd(petid, name, status="available"):
    api_url = f"{base_url}/pet/{petid}"
    # словарь с параметрами
    api_data = {
        'petId':petid,
        'name':name,
        'status':status
        }
    r = requests.post(api_url, api_data)
    return r 

# для создания пользователя
def user_create(userid, username, firstName, lastName, email, password, phone, userStatus):
    api_url = f"{base_url}/user"
    # словарь с параметрами
    api_data = {
        'id':userid,
        'username':username,
        'firstName':firstName,
        'lastName':lastName,
        'email':email,
        'password':password,
        'phone':phone,
        'userStatus':userStatus
        }
    r = requests.post(api_url, json=api_data)
    return r 

# выводим и анализируем результат
def req_info(r):
    try:
        answer = r.json()
    # если случилась ошибка декодирования
    except json.decoder.JSONDecodeError:
        answer = r.content
    # узнаем статус-код
    print("Status Code:",r.status_code)
    # и печатаем что там в ответе
    print(answer)

if __name__ == '__main__':
    # с ид 1 должно быть все ок -200
    r = pet(1)
    req_info(r)
    # тут должно быть 404
    r = pet(0)
    req_info(r)
    # по документаци при неверном ид должен возвращаться статус 400
    r = pet(5.01)
    req_info(r)

    print("UPD")
    # апд. по апи
    r = pet_upd(1, "dog")
    req_info(r)


    print("USER_Get") 
    # с именем должно быть все ок -200
    r = user("YAtyt")
    req_info(r)
    # тут должно быть 404
    r = user("yatyt")
    req_info(r)
    # по документаци при неверном имени должен возвращаться статус 400
    r = user(5.01)
    req_info(r)

    print("USER_CREATE") 
     # создание
    r = user_create(90, "TSAR", "Grozniy", "Ivan","2@2.com", "222", "222", 1)
    #r = user_create("2=!", "IMPERATOR1", "TSEZAR1", "Yuliy1","3@33.com", "33323", "3233", 1)
    req_info(r)

