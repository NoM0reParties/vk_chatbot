ID_GROUP_TOKEN = 'db994b5bcb24eecc8abb4622b5175713bb8b0fd657bdf6f2811590df472b46510287cc9e830c1340b2ed1'

INTENTS = [
    {
        "name": "Дата проведения",
        "tokens": ("когда", "сколько", "дата", "дату"),
        "scenario": None,
        "answer": "Конференция проводится 15го апреля, регистрация начнется в 10 утра"
    },
    {
        "name": "Место проведения",
        "tokens": ("где", "место", "локация", "адрес", "метро"),
        "scenario": None,
        "answer": "Конференция пройдет в павильоне 18Г в Экспоцентре"
    },
    {
        "name": "Регистрация",
        "tokens": ("регист", "добав"),
        "scenario": "registration",
        "answer": None
    }
]

SCENARIOS = {
    "registration": {
        "first_step": "step1",
        "steps": {
            "step1": {
                "text": "Чтобы зарегистрироваться, введите ваше имя. Оно будет написано на бэйджике.",
                "failure_text": "Имя должено состоять из 3-30 букв и дефиса. Попробуйте еще раз",
                "handler": "handle_name",
                "next_step": "step2"
            },
            "step2": {
                "text": "Введите email. Мы отправим на него все данные.",
                "failure_text": "Во введеном адресе ошибка. Попробуйте еще раз",
                "handler": "handle_email",
                "next_step": "step3"
            },
            "step3": {
                "text": "Спасибо за регистрацию, {name}! Мы отправим на {email} билет, распечатайте его.",
                "image": "generate_ticket_handler",
                "failure_text": None,
                "handler": None,
                "next_step": None
            }
        }
    }
}

DEFAULT_ANSWER = 'Не знаю как на это ответить. ' \
                 'Могу сказать когда и где пройдет конференция, а также зарегистрировать вас. Просто спросите'

DB_CONFIG = dict(
    provider='postgres',
    user='postgres',
    password='JHarden13',
    host='localhost',
    database='vk_chat_bot'
)