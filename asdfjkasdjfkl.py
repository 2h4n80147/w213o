from telethon import TelegramClient, sync, events

api_id =  819745
api_hash = 'b62e3c87a48c8ecef7d53ddc901f3c11'

client = TelegramClient('session_name', api_id, api_hash)

@client.on(events.NewMessage(chats=('goodwin_bets')))
async def normal_handler(event):
#    print(event.message)
    user_mess=event.message.to_dict()['message']

    s_user_id=event.message.to_dict()['from_id']
    user_id=int(s_user_id)
    user=d.get(user_id)

    mess_date=event.message.to_dict()['date']

    f.write(mess_date.strftime("%d-%m-%Y %H:%M")+"\n")
    f.write(user+"\n")
    f.write(user_mess+"\n\n")

    f.flush()

client.start()

f=open('messages_from_chat', 'a') 

client.run_until_disconnected()
f.close()
