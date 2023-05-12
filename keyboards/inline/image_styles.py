
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
# from aiogram.filters.callback_data import CallbackData


img_styles = InlineKeyboardMarkup(
    row_width=2,
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Oddiy', callback_data='text2img'),
        ],
        [
            InlineKeyboardButton(text='Yoqimli jonzot', callback_data='cute-creature-generator'),
            InlineKeyboardButton(text='Fantastik olam', callback_data='fantasy-world-generator'),
        ],
        [
            InlineKeyboardButton(text='Cyberpunk', callback_data='cyberpunk-generator'),
            InlineKeyboardButton(text='Oldingi vaqtlar', callback_data='old-style-generator'),
        ],
        [
            InlineKeyboardButton(text='Tarixiy', callback_data='renaissance-painting-generator'),
            InlineKeyboardButton(text='Abstract', callback_data='abstract-painting-generator'),
        ],
        [
            InlineKeyboardButton(text='Impressionism', callback_data='impressionism-painting-generator'),
            InlineKeyboardButton(text='Syurreal', callback_data='surreal-graphics-generator'),
        ],
        [
            InlineKeyboardButton(text='3D object', callback_data='3d-objects-generator'),
            InlineKeyboardButton(text='zamondosh arxitektura', callback_data='contemporary-architecture-generator'),
        ],
        [
            InlineKeyboardButton(text='Logotip', callback_data='logo-generator'),
            InlineKeyboardButton(text='Fantaziyali portret', callback_data='fantasy-portrait-generator'),
        ],
        [
            InlineKeyboardButton(text='Comics', callback_data='comics-portrait-generator'),
            InlineKeyboardButton(text='Kiberpunk portret', callback_data='cyberpunk-portrait-generator'),
        ],
        [
            InlineKeyboardButton(text='⬅️ Rasim chizishdan chiqish', callback_data='exit_img_generate'),
        ]
    ]
)