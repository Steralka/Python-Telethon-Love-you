from pyrogram import Client, filters
from time import sleep
from text import *

app = Client("my_account")
n = 0.35 # Время задержки 
@app.on_message(filters.command("love", prefixes=".") & filters.me)
def love(_, msg):
        while True:
                msg.edit(l1)
                sleep(n)
                msg.edit(l2)
                sleep(n)
                msg.edit(l3)
                sleep(n)
                msg.edit(l4)
                sleep(n)
                msg.edit(l5)
                sleep(n)
                msg.edit(l6)
                sleep(n)
                msg.edit(l7)
                sleep(n)
                msg.edit(l8)
                sleep(n)
                msg.edit(l9)
                sleep(n)
                msg.edit(l10)
                sleep(n)
app.run()