from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton

def kbc(*rows):
    buttons_in_row = []
    inline_keyboard = InlineKeyboardMarkup()
    for row in range(len(rows)):
        for button in range(len(rows[row])):
            print(rows[row])
            buttons_in_row.append(InlineKeyboardButton(rows[row][button][0], callback_data=rows[row][button][1]))
        inline_keyboard.row(*buttons_in_row)
        buttons_in_row = []
        
    return inline_keyboard