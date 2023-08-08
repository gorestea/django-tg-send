import asyncio
import concurrent
import sqlite3
import json
from threading import Event

import telebot
from time import sleep
from telethon import TelegramClient, sync

api_id =
api_hash = ''

async def send_to_telegram(loop, stop_event=None):
    with sqlite3.connect('db.sqlite3') as conn:
        cursor = conn.execute("SELECT * FROM carparcapp_car")
        cars = []

        for row in cursor:
            cars.append({
                "Марка": row[1],
                "Тип": row[2],
                "Кабина": row[3],
                "Формула": row[4],
                "Двигатель": row[5],
                "Мощность": row[6],
                "КПП": row[7],
                "Мосты": row[8],
                "Евро-класс": row[9],
                "Цена": row[10],
                "Фото": 'media/' + row[11]
            })

        with open('cars.json', 'w', encoding='utf-8') as outfile:
            json.dump(cars, outfile, indent=4, ensure_ascii=False)


    with open('cars.json', 'r', encoding='utf-8') as file:
        cars_list = json.load(file)

    with open('channels.json', 'r', encoding='utf-8') as file:
        channels = json.load(file)

    async with TelegramClient("", api_id, api_hash,  system_version="4.16.30-vxYOUR_TEXT", loop=loop) as client:
        index = 0
        while not stop_event.is_set() and index < len(cars_list):
            for channel in channels:
                car = cars_list[index]
                try:
                    photo_path = car.get("Фото")
                    caption = ""
                    for key, value in car.items():
                        if key != "Фото" and value is not None:
                            caption += f"{key}: {value}\n"
                    with open(photo_path, 'rb') as photo_file:
                        await client.send_file(channel, photo_file, caption=caption)
                    sleep(10)
                except PermissionError:
                    caption = ""
                    for key, value in car.items():
                        if key != "Фото" and value is not None:
                            caption += f"{key}: {value}\n"
                    await client.send_message(channel, caption)
                    sleep(5)
            index += 1
            if index >= len(cars_list):
                break


if __name__ == '__main__':
    loop = asyncio.get_event_loop()  # создаем event loop
    loop.run_until_complete(send_to_telegram())  # вызываем main() внутри event loop
    loop.close()

