from random import random
from vk_api import VkApi, VkUpload
from datetime import datetime
from vk_api.longpoll import VkLongPoll
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

print("Welcome to:        ___                         ___                 ")
print("      ___         /__/|         _____         /  /\          ___   ")
print("     /__/\       |  |:|        /  /::\       /  /::\        /  /\  ")
print("     \  \:\      |  |:|       /  /:/\:\     /  /:/\:\      /  /:/  ")
print("      \  \:\   __|  |:|      /  /:/~/::\   /  /:/  \:\    /  /:/   ")
print("  ___  \__\:\ /__/\_|:|____ /__/:/ /:/\:| /__/:/ \__\:\  /  /::\   ")
print(" /__/\ |  |:| \  \:\/:::::/ \  \:\/:/~/:/ \  \:\ /  /:/ /__/:/\:\  ")
print(" \  \:\|  |:|  \  \::/~~~~   \  \::/ /:/   \  \:\  /:/  \__\/  \:\ ")
print("  \  \:\__|:|   \  \:\        \  \:\/:/     \  \:\/:/        \  \:\ ")
print("   \  \::::/     \  \:\        \  \::/       \  \::/          \__\/")
print("    \__\__/       \__\/         \__\/         \__\/              \n")
print("Fuc$*ng bot for conversations! \n     1. Comands: 'Старт', 'Бот инфо'   2. With users: none")

mainToken = "ups"
idGroup = "ups"

vkSession = VkApi(token=mainToken)
vk = vkSession.get_api()
longpoll = VkBotLongPoll(vkSession, idGroup)

upload = VkUpload(vkSession)

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
			vk.messages.send ( random_id=random_id, chat_id=chat_id, message=vkMessage, )

		if text.lower() == 'старт':
			random_id = round(random() * 10 ** 9)
			chat_id = int(event.chat_id)

			# Бесконечный цикл для проверки реального времени
			while True:
				try:
					current_datetime = datetime.now()

					if minutka != current_datetime.minute:
						print("Real time is: ", current_datetime.hour, ":" ,current_datetime.minute)

					minutka = current_datetime.minute

					# Отправка сообщения утром
					if current_datetime.hour == 0 and current_datetime.minute == 5 and current_datetime.second < 2:
						vkMessage = "Доброе утро! Расписание на сегодня:\n\n 9:00 - 10:00 Сасите\n 11:00 - 12:00 Идите нахуй"
						vk.messages.send ( random_id=random_id, chat_id=chat_id, message=vkMessage, )

					# Отправка сообщения вечером
					if current_datetime.hour == 20 and current_datetime.minute == 00 and current_datetime.second < 2:
						vkMessage = "Доброе утро!"
						vk.messages.send ( random_id=random_id, chat_id=chat_id, message=vkMessage, )

				except Exception as e:
					print("stop")
