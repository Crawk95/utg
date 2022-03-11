from config import client
from telethon.tl.functions.account import UpdateUsernameRequest
await client(UpdateUsernameRequest('new_username'))