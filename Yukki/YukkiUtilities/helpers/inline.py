from pyrogram.types import (
    CallbackQuery,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    InputMediaPhoto,
    Message,
)


def stream_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="• ᴄᴀɴᴄᴇʟ •", callback_data=f'stopvc2'),      
                InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ •", callback_data=f'close2')
            ],
        ]
    return buttons


def play_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="• ᴍᴇɴᴜ •", callback_data=f'other {videoid}|{user_id}'),      
                InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ •", callback_data=f'close2')
            ],
        ]
    return buttons 


def others_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="▷", callback_data=f'resumevc2'),
                InlineKeyboardButton(text="II", callback_data=f'pausevc2'),
                InlineKeyboardButton(text="‣‣I", callback_data=f'skipvc2'),
                InlineKeyboardButton(text="▢", callback_data=f'stopvc2')
            ],
            [
                InlineKeyboardButton(text="✚ ᴩᴇʀsᴏɴᴀʟ ᴘʟᴀʏʟɪsᴛ", callback_data=f'playlist {videoid}|{user_id}'),
                InlineKeyboardButton(text="✚ ɢʀᴏᴜᴩ ᴘʟᴀʏʟɪsᴛ", callback_data=f'group_playlist {videoid}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="💠 ɢᴇᴛ ᴀᴜᴅɪᴏ", callback_data=f'gets audio|{videoid}|{user_id}'),
                InlineKeyboardButton(text="💠 ɢᴇᴛ ᴠɪᴅᴇᴏ", callback_data=f'gets video|{videoid}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="🔙 Go Back", callback_data=f'goback {videoid}|{user_id}')
            ],
        ]
    return buttons


play_keyboard = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "▷", callback_data="resumevc"
                    ),
                    InlineKeyboardButton(
                        "II", callback_data="pausevc"
                    ),
                    InlineKeyboardButton(
                        "‣‣I", callback_data="skipvc"
                    ),
                    InlineKeyboardButton(
                        "▢", callback_data="stopvc"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "↻ ᴄʟᴏsᴇ", callback_data="close"
                    )
                ]    
            ]
        )

def audio_markup(videoid, user_id):
    buttons= [
            [
                InlineKeyboardButton(text="▷", callback_data=f'resumevc2'),
                InlineKeyboardButton(text="II", callback_data=f'pausevc2'),
                InlineKeyboardButton(text="‣‣I", callback_data=f'skipvc2'),
                InlineKeyboardButton(text="▢", callback_data=f'stopvc2')
            ],
            [
                InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ", callback_data="close2")              
            ],
        ]
    return buttons 


def search_markup(ID1, ID2, ID3, ID4, ID5, duration1, duration2, duration3, duration4, duration5, user_id, query):
    buttons= [
            [
                InlineKeyboardButton(text="1", callback_data=f'yukki2 {ID1}|{duration1}|{user_id}'),
                InlineKeyboardButton(text="2", callback_data=f'yukki2 {ID2}|{duration2}|{user_id}'),
                InlineKeyboardButton(text="3", callback_data=f'yukki2 {ID3}|{duration3}|{user_id}')
            ],
            [ 
                InlineKeyboardButton(text="4", callback_data=f'yukki2 {ID4}|{duration4}|{user_id}'),
                InlineKeyboardButton(text="5", callback_data=f'yukki2 {ID5}|{duration5}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="‣‣", callback_data=f'popat 1|{query}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ", callback_data=f"ppcl2 smex|{user_id}")
            ],
        ]
    return buttons   


def search_markup2(ID6, ID7, ID8, ID9, ID10, duration6, duration7, duration8, duration9, duration10 ,user_id, query):
    buttons= [
            [
                InlineKeyboardButton(text="6", callback_data=f'yukki2 {ID6}|{duration6}|{user_id}'),
                InlineKeyboardButton(text="7", callback_data=f'yukki2 {ID7}|{duration7}|{user_id}'),
                InlineKeyboardButton(text="8", callback_data=f'yukki2 {ID8}|{duration8}|{user_id}')
            ],
            [ 
                InlineKeyboardButton(text="9", callback_data=f'yukki2 {ID9}|{duration9}|{user_id}'),
                InlineKeyboardButton(text="10", callback_data=f'yukki2 {ID10}|{duration10}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="◁", callback_data=f'popat 2|{query}|{user_id}')
            ],
            [
                InlineKeyboardButton(text="🔹 ᴄʟᴏsᴇ 🔹", callback_data=f"ppcl2 smex|{user_id}")
            ],
        ]
    return buttons 


def personal_markup(link):
    buttons= [
            [ 
                InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ", callback_data=f'cls')
            ],
        ]
    return buttons


start_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "📚 Commands", url="https://telegra.ph/Vayu-Music-03-11-2"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "↻ ᴄʟᴏsᴇ", callback_data="close2"
                    )
                ]    
            ]
        )
 
   
confirm_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "✔️ ʏᴇs", callback_data="cbdel"
                    ),
                    InlineKeyboardButton(
                        "❌ ɴᴏ", callback_data="close2"
                    )
                ]    
            ]
        )


confirm_group_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "✔️ ʏᴇs", callback_data="cbgroupdel"
                    ),
                    InlineKeyboardButton(
                        "❌ ɴᴏ", callback_data="close2"
                    )
                ]    
            ]
        )


close_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "↻ ᴄʟᴏsᴇ", callback_data="close2"
                    )
                ]    
            ]
        )


none_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "↻ ᴄʟᴏsᴇ", callback_data="cls"
                    )
                ]    
            ]
        )


play_list_keyboard = InlineKeyboardMarkup( 
            [
                [
                    InlineKeyboardButton(
                        "ᴩᴇʀsᴏɴᴀʟ ᴘʟᴀʏʟɪsᴛ", callback_data="P_list"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "ɢʀᴏᴜᴩ ᴘʟᴀʏʟɪsᴛ", callback_data="G_list"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "↻ ᴄʟᴏsᴇ", callback_data="close2"
                    )
                ]
            ]
        )


def playlist_markup(user_name, user_id):
    buttons= [
            [
                InlineKeyboardButton(text=f"ɢʀᴏᴜᴩ ᴘʟᴀʏʟɪsᴛ", callback_data=f'play_playlist {user_id}|group')
            ],
            [
                InlineKeyboardButton(text=f"{user_name[:8]}'s Playlist", callback_data=f'play_playlist {user_id}|personal')
            ],
            [
                InlineKeyboardButton(text="↻ ᴄʟᴏsᴇ", callback_data="close2")              
            ],
        ]
    return buttons
