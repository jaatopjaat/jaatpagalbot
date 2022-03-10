
# All rights reserved.

from pyrogram.types import (InlineQueryResultArticle,
                            InputTextMessageContent)

answer = []

answer.extend(
    [
        InlineQueryResultArticle(
            title="Pᴀᴜsᴇ Sᴛʀᴇᴀᴍ",
            description=f"ᴘᴀᴜsᴇ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ sᴛʀᴇᴀᴍ.",
            thumb_url="https://telegra.ph/file/37d4ea97e97877eb63f93.jpg",
            input_message_content=InputTextMessageContent("/pause"),
        ),
        InlineQueryResultArticle(
            title="Rᴇsᴜᴍᴇ Sᴛʀᴇᴀᴍ",
            description=f"ʀᴇsᴜᴍᴇ ᴄᴜʀʀᴇɴᴛ ᴘᴀᴜsᴇᴅ sᴛʀᴇᴀᴍ.",
            thumb_url="https://telegra.ph/file/4e65d111fdb89809fe94e.jpg",
            input_message_content=InputTextMessageContent("/resume"),
        ),
        InlineQueryResultArticle(
            title="Sᴋɪᴘ Sᴛʀᴇᴀᴍ",
            description=f"sᴋɪᴘ ᴛᴏ ɴᴇxᴛ ᴛʀᴀᴄᴋ. | ꜰᴏʀ sᴘᴇᴄɪꜰɪᴄ ᴛʀᴀᴄᴋ ɴᴜᴍʙᴇʀ: /skip [ɴᴜᴍʙᴇʀ] ",
            thumb_url="https://telegra.ph/file/78189a482f76fdc3f8185.jpg",
            input_message_content=InputTextMessageContent("/skip"),
        ),
        InlineQueryResultArticle(
            title="Eɴᴅ Sᴛʀᴇᴀᴍ",
            description="sᴛᴏᴘ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/eb33b1f0daaecb911d013.jpg",
            input_message_content=InputTextMessageContent("/stop"),
        ),
        InlineQueryResultArticle(
            title="Sʜᴜғғʟᴇ Sᴛʀᴇᴀᴍ",
            description="sʜᴜꜰꜰʟᴇ ᴛʜᴇ ǫᴜᴇᴜᴇᴅ ᴛʀᴀᴄᴋs ʟɪsᴛ.",
            thumb_url="https://telegra.ph/file/7f6aac5c6e27d41a4a269.png",
            input_message_content=InputTextMessageContent("/shuffle"),
        ),
        InlineQueryResultArticle(
            title="Lᴏᴏᴘ Sᴛʀᴇᴀᴍ",
            description="ʟᴏᴏᴘ ᴛʜᴇ ᴄᴜʀʀᴇɴᴛ ᴘʟᴀʏɪɴɢ ᴍᴜsɪᴄ. | ᴜsᴀɢᴇ: /loop [enable|disable]",
            thumb_url="https://telegra.ph/file/081c20ce2074ea3e9b952.png",
            input_message_content=InputTextMessageContent("/loop 3"),
        ),
    ]
)

"""

InlineQueryResultArticle(
            title="Mᴜᴛᴇ Sᴛʀᴇᴀᴍ",
            description=f"ᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/66516f2976cb6d87e20f9.png",
            input_message_content=InputTextMessageContent("/mute"),
        ),
        InlineQueryResultArticle(
            title="Uɴᴍᴜᴛᴇ Sᴛʀᴇᴀᴍ",
            description=f"ᴜɴᴍᴜᴛᴇ ᴛʜᴇ ᴏɴɢᴏɪɴɢ ᴘʟᴀʏᴏᴜᴛ ᴏɴ ɢʀᴏᴜᴘ ᴄᴀʟʟ.",
            thumb_url="https://telegra.ph/file/3078794f9341ffd582e18.png",
            input_message_content=InputTextMessageContent("/unmute"),
        ),
"""
