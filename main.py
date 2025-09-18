import os  
import logging  
from pyrogram import Client  
  
rip_vs = Client(  
"rip_vs",  
api_id= 25155424,  
api_hash="b8a83a9a584feba532dbf7c9ca3fe227",  
bot_token="7957702283:AAEAi6jGJsY_YmJM9A0fR9dhyDqDclv2Dn4",  
plugins=dict(root='Plugins')  
)  
  
logging.basicConfig(level=logging.INFO)  
rip_vs.run()  
  