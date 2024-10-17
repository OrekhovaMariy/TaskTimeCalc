import telebot
bot = telebot.TeleBot('7282226985:AAGnYOWBF0aUG31AzVssksU2-nlmgmX8SqI')


a = 0
b = 0
c = 0
d = 0
e = 0
res = 0
@bot.message_handler(content_types=['text'])
def start(message):
    if message.text == '/start':
        mess = """Привет! Я помогу подсчитать плановое время на тестирование задачи =)
Время будет считаться по формуле:
        (a + b*0.25 + c + d + e*0.33)*1.33
где:
        a - время на изучение теории,
        b - время на фиксацию проверок в задаче,
        c - время на составление ТК и чек-листов,
        d - время на подготовку тестовых данных и окружения,
        e - количество дефектов, которое, на твой взгляд, может быть найдено,
        1.33 - коэффициент, который закладывается на возникновение рисков и непредвиденных ситуаций.
Время вводится в формате целых и дробных чисел, например 1 или 1.2
        Введи время на изучение теории: """
        bot.send_message(message.from_user.id, mess)
        bot.register_next_step_handler(message, get_a) #следующий шаг – функция get_a
    else:
        bot.send_message(message.from_user.id, 'Напиши /start')

def get_a(message): #получаем время на изучение теории
    global a
    try:
        a = float(message.text)  # проверяем, что время на изучение теории введено корректно
        bot.send_message(message.from_user.id, 'Введи время на фиксацию проверок в задаче: ')
        bot.register_next_step_handler(message, get_b)
    except Exception:
        bot.send_message(message.from_user.id, 'Попробуем еще раз ввести время на изучение теории. Принимается формат целых и дробных чисел, например 1 или 1.2')
        bot.register_next_step_handler(message, get_a)

def get_b(message): #получаем время на фиксацию проверок в задаче
    global b
    try:
        b = float(message.text)
        bot.send_message(message.from_user.id, 'Введи время на ТК и чек-листы: ')
        bot.register_next_step_handler(message, get_c)
    except Exception:
        bot.send_message(message.from_user.id, 'Попробуем еще раз ввести время на фиксацию проверок в задаче. Принимается формат целых и дробных чисел, например 1 или 1.2')
        bot.register_next_step_handler(message, get_b)

def get_c(message): #получаем время на ТК и чек-листы
    global c
    try:
        c = float(message.text)
        bot.send_message(message.from_user.id, 'Введи время на подготовку тестовых данных и окружения: ')
        bot.register_next_step_handler(message, get_d)
    except Exception:
        bot.send_message(message.from_user.id, 'Попробуем еще раз ввести время на ТК и чек-листы. Принимается формат целых и дробных чисел, например 1 или 1.2')
        bot.register_next_step_handler(message, get_c)

def get_d(message): #получаем время на подготовку тестовых данных и окружения
    global d
    try:
        d = float(message.text)
        bot.send_message(message.from_user.id, 'Предположи количество дефектов: ')
        bot.register_next_step_handler(message, get_e)
    except Exception:
        bot.send_message(message.from_user.id, 'Попробуем еще раз ввести время на подготовку тестовых данных и окружения. Принимается формат целых и дробных чисел, например 1 или 1.2')
        bot.register_next_step_handler(message, get_d)

def get_e(message): #получаем количество дефектов
    global e
    try:
        e = float(message.text)
        global res
        res = (a + b*0.25 + c + d + e*0.33)*1.33
        bot.send_message(message.from_user.id, f"Плановое время на тестирование:  {res}")
    except Exception:
        bot.send_message(message.from_user.id, 'Попробуем еще раз ввести количество дефектов. Принимается формат целых и дробных чисел, например 1 или 1.2')
        bot.register_next_step_handler(message, get_e)


bot.infinity_polling(none_stop=True, interval=0)
