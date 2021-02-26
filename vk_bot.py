import vk_api, json
from vk_api.longpoll import VkLongPoll, VkEventType
import carousels

vk_session = vk_api.VkApi(token='4d99d5546e448556c66a9a010b139665de63779331f7fa04414ab7456e8358326df6adb7b738ecd8149b5')
vk = vk_session.get_api()
longpol = VkLongPoll(vk_session)


def get_but(text, color):
    return {
        "action": {
            "type": "text",
            "payload": "{\"button\": \"" + "1" + "\"}",
            "label": f"{text}"
        },
        "color": f"{color}"
    }


keyboard = {
    "one_time": False,
    "buttons": [
        [get_but('Привет', 'positive'), get_but('Посмотреть список товаров', 'positive')],
        [get_but('Назад', 'positive'), get_but('Оформить заказ', 'positive')]
    ]
}
keyboard = json.dumps(keyboard, ensure_ascii=False).encode('utf-8')
keyboard = str(keyboard.decode('utf-8'))


car = json.dumps(carousels.categories, ensure_ascii=False).encode('utf-8')
car = str(car.decode('utf-8'))

pies = json.dumps(carousels.cat_pies, ensure_ascii=False).encode('utf-8')
pies = str(pies.decode('utf-8'))

conf = json.dumps(carousels.cat_conf_products, ensure_ascii=False).encode('utf-8')
conf = str(conf.decode('utf-8'))

flour = json.dumps(carousels.cat_flour_products, ensure_ascii=False).encode('utf-8')
flour = str(flour.decode('utf-8'))


def checker(x):
    file = open('data.txt', 'r', encoding='utf8')
    if str(x) in file.read():
        return 1
    else:
        return 0
    file.close()


def data_collect(x):
    file = open('data.txt', 'a', encoding='utf8')
    file.write(f'{x}\n')
    file.close()


def sender(id, text, car):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'template': car})


def answer(id, text):
    vk_session.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0, 'keyboard': keyboard})



def main():
    for event in longpol.listen():
        if event.type == VkEventType.MESSAGE_NEW:
            if event.to_me:
                id = event.user_id
                msg = event.text.lower()

                if msg == 'привет':
                    answer(id, "И тебе привет")
                    if checker(id) == 0:
                        data_collect(id)

                if msg == 'начать':
                    answer(id, "Выберите один из вариантов")

                if msg == 'посмотреть список товаров':
                    sender(id, 'вот, глянь', car)

                if msg == 'пирожки':
                    sender(id, 'наш ассортимент пирожков', pies)

                if msg == 'назад':
                    sender(id, 'возвращение в исходный каталог', car)

                if msg == 'кондитерские изделия':
                    sender(id, 'наш ассортимент кондитерских изделий', conf)

                if msg == 'мучные изделия без начинки':
                    sender(id, 'наш ассортимент мучных изделий без начинки', flour)

                if msg == 'печенье':
                    answer(id, 'Небольшие кусочки печеного сладкого теста.')

                if msg == 'пряник':
                    answer(id, 'Мучное кондитерское изделие, выпекаемое из специального пряничного теста.')

                if msg == 'пирожок с мясом':
                    answer(id, 'Небольшое кулинарное изделие из дрожжевого или слоёного пресного теста с начинкой из мяса внутри, которое выпекается в печи или жарится во фритюре.')

                if msg == 'пирожок с яйцом и зеленью':
                    answer(id, 'Небольшое кулинарное изделие из дрожжевого или слоёного пресного теста с начинкой из яйца и зелени внутри, которое выпекается в печи или жарится во фритюре.')

                if msg == 'крендель':
                    answer(id, 'Хлебобулочное изделие из сдобного теста, напоминающее своим видом букву «В».')

                if msg == 'слойка':
                    answer(id, 'Изделие из слоенного теста')


while True:
    main()
