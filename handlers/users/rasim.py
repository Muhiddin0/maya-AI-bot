
# telegram bot
from aiogram import types
from loader import dp
from aiogram.dispatcher import FSMContext

# rasim chizish uchun statelar
from states.states import ImageStates


# request
import requests

# translator
from deep_translator import GoogleTranslator



# BUTTONS
# rasim turlari btn
from keyboards.inline.image_styles import img_styles



# rasmin chizish uchun buyruq
@dp.message_handler(commands=['rasim'], state=None)
async def rasim(message: types.Message):
    
    user_id = message.from_user.id
    await message.answer(f"🎨 Xo'sh qanday rasim chizish kerak <b>{message.from_user.first_name}</b> aka")
    await ImageStates.text.set()



# rasim uchun matini olish
@dp.message_handler(content_types=['text'], state=ImageStates.text)
async def text_for_img(message: types.Message, state:FSMContext):

    translated = GoogleTranslator(source='uz', target='en').translate(message.text) 

    await state.set_data({
        "text": translated
    })

    await message.answer(
        "🖼 Rasimni qanday usulda chizishimni xoxlaysiz",
        reply_markup=img_styles
        )




@dp.callback_query_handler(state=ImageStates.text)
async def generate_img(query:types.CallbackQuery, state:FSMContext):
    
    if query.data == "exit_img_generate":
        
        await query.message.answer("Chat botga qaytildi")
        await state.finish()

        return
    await query.message.answer("Iltimos kuting...")

    st_data = await state.get_data()
    r = requests.post(
        f"https://api.deepai.org/api/{query.data}",
        data={
            'text': st_data['text'],
        },
        headers={'api-key': 'quickstart-QUdJIGlzIGNvbWluZy4uLi4K'}
    ).json()

    # print(r)

    await query.message.answer_photo(
        photo=r['output_url'],
    )


