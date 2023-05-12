from aiogram.dispatcher.filters.state import State, StatesGroup

class ImageStates(StatesGroup):
    
    text = State()
    style = State()
