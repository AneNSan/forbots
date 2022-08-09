from main import bot, dp
from aiogram.types import Message
from config import admin_id
async def send_to_admin(dp):
  await bot.send_message(chat_id=admin_id, text="Назови своё имя, странник, я погадаю")

@dp.message_handler()
async def echo(message: Message):
  text = f"На судьбе написано, что {message.text} пидор."
  await bot.send_message(chat_id=message.from_user.id, text = text)
