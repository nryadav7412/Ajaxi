class script(object):
    START_TXT = """<b>Hello {},
My Name Is <a href=https://t.me/{}>{}</a>,
I Can Provide You Movies & Series ,Just Join My Group And Enjoy đ„°</b>"""
    HELP_TXT = """<b>Hey {}
Here Is The Help Of My All Commands.</b>"""
    ABOUT_TXT = """âź My Name: {}
âź Creator: <a href=https://t.me/Legends_Nvr_Die>à€Ąà„à€à„à€à€° à€žà„à€à„à€°à„à€šà„à€</a>
âź Library: Pyrogram
âź Language: Python 3
âź Database: Mongo DB
âź Bot Sever: Heroku
âź Build Status v1.0.2 [ Beta ]"""
    SOURCE_TXT = """<b>Donation</b>

âȘŒ <b>You Can Donate Any Amount You Have đł. 

<b>âââââââââá Payment Methods áâââââââââ

âź GooglePay
âź Paytm
âź PhonePe
âź Paypal

_Contact Me Know More On This_
ââââââââââââá <a href=https://t.me/Legends_Nvr_Die><b>à€Ąà„à€à„à€à€° à€žà„à€à„à€°à„à€šà„à€</b></a> áââââââââââââ"""
    MANUELFILTER_TXT = """Help: <b>Filters</b>  

- Filter is the feature were users can set automated replies for a particular keyword and á©áá©á­ will respond whenever a keyword is found the message

<b>NOTE:</b>
1. This Bot should have admin privillage.
2. only admins can add filters in a chat.
3. alert buttons have a limit of 64 characters.

<b>Commands and Usage:</b>
âŸ /filter - <code>add a filter in chat</code>
âŸ /filters - <code>list all the filters of a chat</code>
âŸ /del - <code>delete a specific filter in chat</code>
âŸ /delall - <code>delete the whole filters in a chat (chat owner only)</code>"""
    BUTTON_TXT = """Help: <b>Buttons</b>

- This Bot Supports both url and alert inline buttons.

<b>NOTE:</b>
1. Telegram will not allows you to send buttons without any content, so content is mandatory.
2. This Bot supports buttons with any telegram media type.
3. Buttons should be properly parsed as markdown format

<b>URL buttons:</b>
<code>[Button Text](buttonurl:https://t.me/source00Devil)</code>

<b>Alert buttons:</b>
<code>[Button Text](buttonalert:This is an alert message)</code>"""
    AUTOFILTER_TXT = """Help: <b>Auto Filter</b>

<b>NOTE:</b>
1. Make me the admin of your channel if it's private.
2. make sure that your channel does not contains camrips, porn and fake files.
3. Forward the last message to me with quotes.
 I'll add all the files in that channel to my db."""
    CONNECTION_TXT = """Help: <b>Connections</b>

- Used to connect bot to PM for managing filters 
- it helps to avoid spamming in groups.

<b>NOTE:</b>
1. Only admins can add a connection.
2. Send <code>/connect</code> for connecting me to ur PM

<b>Commands and Usage:</b>
âŸ /connect  - <code>connect a particular chat to your PM</code>
âŸ /disconnect  - <code>disconnect from a chat</code>
âŸ /connections - <code>list all your connections</code>"""
    EXTRAMOD_TXT = """Help: <b>Extra Modules</b>

<b>NOTE:</b>
These are the extra features of á©áá©á­

<b>Commands and Usage:</b>
âŸ /id - <code>get id of a specifed user.</code>
âŸ /info  - <code>get information about a user.</code>
âŸ /imdb  - <code>get the film information from IMDb source.</code>
âŸ /search  - <code>get the film information from various sources.</code>"""
    ADMIN_TXT = """Help: <b>Admin mods</b>

<b>NOTE:</b>
This module only works for my OwnerâĄ

<b>Commands and Usage:</b>
âŸ /logs - <code>to get the rescent errors</code>
âŸ /stats - <code>to get status of files in db.</code>
âŸ /delete - <code>to delete a specific file from db.</code>
âŸ /users - <code>to get list of my users and ids.</code>
âŸ /chats - <code>to get list of the my chats and ids </code>
âŸ /leave  - <code>to leave from a chat.</code>
âŸ /disable  -  <code>do disable a chat.</code>
âŸ /ban  - <code>to ban a user.</code>
âŸ /unban  - <code>to unban a user.</code>
âŸ /channel - <code>to get list of total connected channels</code>
âŸ /broadcast - <code>to broadcast a message to all users</code>"""
    STATUS_TXT = """âź Total Files: <code>{}</code>
âź Total Users <code>{}</code>
âź Total Chats: <code>{}</code>
âź Used Storage: <code>{}</code> đŒđđ±
âź Free Storage: <code>{}</code> đŒđđ±"""
    LOG_TEXT_G = """#NewGroup
âź Group âșâș {}(<code>{}</code>)
âź Total Members âșâș <code>{}</code>
âź Added By âșâș {}
"""
    LOG_TEXT_P = """#NewUser
âź ID âșâș <code>{}</code>
âź Name âșâș {}
"""
