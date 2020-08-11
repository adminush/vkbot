from random import random
from vk_api import VkApi, VkUpload
from datetime import datetime
from vk_api.longpoll import VkLongPoll
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
from toks import mainToken, idGroup

print("\n\nWelcome to:        ___                            ___                 \n      ___         /__/|            _____         /  /\          ___   \n     /__/\       |  |:|           /  /::\       /  /::\        /  /\  \n     \  \:\      |  |:|          /  /:/\:\     /  /:/\:\      /  /:/  \n      \  \:\   __|  |:|         /  /:/~/::\   /  /:/  \:\    /  /:/   \n  ___  \__\:\ /__/\_|:|____    /__/:/ /:/\:| /__/:/ \__\:\  /  /::\   \n /__/\ |  |:| \  \:\/:::::/    \  \:\/:/~/:/ \  \:\ /  /:/ /__/:/\:\  \n \  \:\|  |:|  \  \::/___/      \  \::/ /:/   \  \:\  /:/  \__\/  \:\ \n  \  \:\__|:|   \  \:\           \  \:\/:/     \  \:\/:/        \  \:\ \n   \  \::::/     \  \:\           \  \::/       \  \::/          \__\/\n    \__\__/       \__\/            \__\/         \__\/              \nFuc$*ng bot for conversations! \n1. Comands: '/Старт', 'Бот инфо'   2. With users: none\n\n")

vkSession = VkApi(token = mainToken)
vk = vkSession.get_api()
longpoll = VkBotLongPoll(vkSession, idGroup)

upload = VkUpload(vkSession)

start_day = int(1)
minutka = 0

for event in longpoll.listen():
	if event.type == VkBotEventType.MESSAGE_NEW and event.from_chat:
		message = event.obj['message']
		peer_id = message['peer_id']
		text = message['text']

		if text.lower() == 'бот инфо':
			random_id = round(random() * 10 ** 9)
			chat_id = int(event.chat_id)

			vkMessage = "Всем привет, я бот ! Developer, но меня можно звать просто, бот."
			print("Comand -> 'Бот инфо'")
			vk.messages.send ( random_id = random_id, chat_id = chat_id, message = vkMessage, )

		if text.lower() == '/старт':
			print("Comand -> '/Старт'")
			random_id = round(random() * 10 ** 9)
			chat_id = int(event.chat_id)

			# Бесконечный цикл для проверки реального времени
			while True:
				try:
					current_datetime = datetime.now()

					if minutka != current_datetime.minute:
						print("Real time is: ", current_datetime.hour, ":" ,current_datetime.minute, " ", start_day)
						set_day = 1

					minutka = current_datetime.minute

					if current_datetime.hour == 16 and current_datetime.minute == 26 and current_datetime.second == 0 and set_day == 1:
						start_day += 1
						print("Number day is: ", start_day)

					# Отправка сообщения утром
					if current_datetime.hour == 8 and current_datetime.minute == 0 and current_datetime.second < 2:
						vkMessage = "Доброе утро! Расписание на сегодня:\n\n 9:00 - 10:00 Русский язык\n 11:00 - 12:00 Математика"
						vk.messages.send ( random_id = random_id, chat_id = chat_id, message = vkMessage, )

					# Отправка сообщения вечером
					if current_datetime.hour == 20 and current_datetime.minute == 0 and current_datetime.second < 2:
						vkMessage = "Доброе вечер! Расписание на завтра:\n\n 9:00 - 10:00 Философия\n 11:00 - 12:00 Психология"
						vk.messages.send ( random_id = random_id, chat_id = chat_id, message = vkMessage, )

					set_day = 0
				except Exception as e:
					print("stop")
