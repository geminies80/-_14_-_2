import unittest
# подключа код, который написали
import swagger

'''
Swagger API  test v0.3
'''

# функция просто возвращает статус-код
def status(r):
    return r.status_code

# класс для апи тестов
class SwaggerAPITest(unittest.TestCase):
    def test_get_petinfo01(self):
        "Получение информации о питомце, позитивный"
        # сначала функция pet(1) выполнется в swagger и вернет объект ответа, 
        # затем функция status примет объект ответа и вернет целое число - статус-код
        self.assertEqual(status(swagger.pet(1)), 200)
    def test_get_petinfo02(self):
        "Получение информации о питомце, негативный - не найден"
        self.assertEqual(status(swagger.pet(600)), 404)
    def test_get_petinfo03(self):
        "Получение информации о питомце, негативный - Invalid ID supplied"
        self.assertEqual(status(swagger.pet("2+2")), 400)
    # Тест обновлений питомца    
    def test_get_pet_upd01(self):
        "Обновление информации о питомце, позитивный"
        # сначала функция pet_upd(1,"dog") выполнется в swagger и вернет объект ответа, 
        # затем функция status примет объект ответа и вернет целое число - статус-код
        self.assertEqual(status(swagger.pet_upd(1,"dog")), 200) 
    def test_get_pet_upd02(self):
        "Обновление информации о питомце, негативный"
        self.assertEqual(status(swagger.pet_upd(0,"cat")), 405) 
    def test_get_pet_upd03(self):
        "Обновление информации о питомце, Invalid ID"
        self.assertEqual(status(swagger.pet_upd("abc","frog")), 405)

   # Тест для пользователя - получение инфы
    def test_get_userinfo01(self):
        "Получение информации о пользователе, позитивный"
        self.assertEqual(status(swagger.user("YAtyt")), 200)
    def test_get_userinfo02(self):
        "Получение информации о пользователе, негативный - пользователь не найден"
        self.assertEqual(status(swagger.user("yatyt")), 404)
    def test_get_userinfo03(self):
        "Получение информации о пользователе, негативный - Invalid username supplied"
        self.assertEqual(status(swagger.user("!")), 400)
   
   # Тест для пользователя - создание
    def test_post_usercreate01(self):
        "Создание, позитивный"
        self.assertEqual(status(swagger.user_create(67, "IMPERATOR", "TSEZAR", "Yuliy","3@3.com", "3333", "333", 1)), 200)
    def test_post_usercreate02(self):
        "Создание, негативный"
        self.assertEqual(status(swagger.user_create("2=!", "IMPERATOR", "TSEZAR", "Yuliy","3@3.com", "3333", "333", 1)), 500)     


if __name__ == '__main__':
    unittest.main(verbosity=2)