from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>ðð» Hi {message.from_user.first_name}!</b>

I am â¯sÑÎ±Ñ_Ð²ÏÑâ¯ Music Player, an open-source bot that lets you play music in your Telegram groups.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "âCOMMANDS", url="https://telegra.ph/MusicBot-Robot-MusicBot-Robo-03-14"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ð¬ Group", url="https://t.me/studyboyzandgirls"
                    ),
                    InlineKeyboardButton(
                        "Creator", url="https://t.me/blspraygod"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "ðð»ââï¸ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "â Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No â", callback_data="close"
                    )
                ]
            ]
        )
    )
