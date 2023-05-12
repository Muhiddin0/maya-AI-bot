
# bot
from aiogram import types
from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove
from aiogram.dispatcher.filters.builtin import CommandStart
from loader import dp

# state
from aiogram.dispatcher import FSMContext

# base
import sqlite3
db = sqlite3.connect('data/users.db')
sql = db.cursor()
sql.execute("""CREATE TABLE IF NOT EXISTS users (user_id INT) """)
db.commit()

@dp.message_handler(CommandStart(), state='*')
async def bot_start(message: types.Message, state:FSMContext):

    user_id = message.from_user.id

    # foydalanuvchi bazada bor yo'q bo'lsa bazaga kiritish
    sql.execute(f"""SELECT * FROM users WHERE user_id = {user_id}""")
    if not bool(sql.fetchall()):
        sql.execute(f"""INSERT INTO users VALUES ({user_id})""")
        db.commit()
    

    # sql.execute('SELECT * FROM users')
    # print(sql.fetchall())

    # agar bor bo'lsa
    await message.answer(
        f"Assalomu alaykum, <a href='tg://user?id={user_id}'>{message.from_user.full_name}!</a>",
        )

    # end all state
    await state.finish()