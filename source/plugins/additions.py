from pyrogram import Client, filters,enums
from config import *
import asyncio
from autoname import main as name
import string_utils
import time
import csv
import json
#سورس تايجر بيمسي - @XIX_A

def get_name(msg):
    if msg.from_user.last_name:
        last_name = msg.from_user.last_name
    else:
        last_name = ""
    if msg.from_user.first_name:
        first_name = msg.from_user.first_name
    else:
        first_name = ""
    return f"[{first_name} {last_name}](tg://user?id={msg.from_user.id})"
    
@Client.on_message(filters.command("مسح جهاتي$",prefixes=f".") & filters.me )
async def my_con(c,msg):
  list_c = await c.get_contacts()
  ids = []
  for contact in list_c :
     ids.append(contact.id)
  await c.delete_contacts(ids)
  await msg.edit(f"✪ تم مسح {len(ids)} من جهاتك")
      

@Client.on_message(filters.command("جلب الاعضاء$",prefixes=f".") & filters.me )
async def get_members(c,msg):
  with open("members.txt","w") as f:
    ids = ""
    async for m in c.get_chat_members(msg.chat.id):
      ids += f"{m.user.id}\n"
    f.write(ids)
  await msg.reply_document(f"./members.txt")
  

@Client.on_message(filters.command("قلب$",prefixes=f".") & filters.me )
async def haert(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("❤💙💚💛🧡💜🖤🤍🤎❤️‍"))
    time.sleep(0.5)
    
@Client.on_message(filters.command("مطر$",prefixes=f".") & filters.me )
async def rain(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🌬☁️🌩🌨🌧🌦🌥⛅🌤"))
    time.sleep(0.5)

@Client.on_message(filters.command("مكعبات$",prefixes=f".") & filters.me )
async def mokbt(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🟥🟧🟨🟩🟦🟪🟫⬛⬜"))
    time.sleep(0.5)

@Client.on_message(filters.command("نجمه$",prefixes=f".") & filters.me )
async def ngom(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🦋✨🦋✨🦋✨🦋✨"))
    time.sleep(0.5)
    
@Client.on_message(filters.command("مح$",prefixes=f".") & filters.me )
async def bosh(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("💋😙😘😽💋😘😙😽💋"))
    time.sleep(0.5)

@Client.on_message(filters.command("افكر$",prefixes=f".") & filters.me )
async def afkr(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🤔🧐🤔🧐🤔🧐"))
    time.sleep(0.5)

@Client.on_message(filters.command("بموتت$",prefixes=f".") & filters.me )
async def dhkk(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("😹🤣😂😹🤣😂"))
    time.sleep(0.5)

@Client.on_message(filters.command("ساعه$",prefixes=f".") & filters.me )
async def time(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🕙🕘🕗🕖🕕🕔🕓🕒🕑🕐🕛"))
    time.sleep(0.5)

@Client.on_message(filters.command("جيم$",prefixes=f".") & filters.me )
async def gym(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍🏃‍🏋‍🤸‍"))
    time.sleep(0.5)

@Client.on_message(filters.command("الارض$",prefixes=f".") & filters.me )
async def alard(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("🌍🌎🌎🌍🌏🌍🌎"))
    time.sleep(0.5)
    
@Client.on_message(filters.command("قلوب$",prefixes=f".") & filters.me )
async def haerts(c,msg):
  for i in range(1,15):
    await msg.edit(string_utils.shuffle("❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤❤💙💚💛🧡💜🖤🤍🤎❤️‍"))
    time.sleep(0.5)

@Client.on_message(filters.command(["قمر$","اقمار$"],prefixes=f".") & filters.me )
async def moon(c,msg):
  listt = ["🌑🌒🌓🌔🌕🌖🌗🌘","🌒🌓🌔🌕🌖🌗🌘🌑","🌓🌔🌕🌖🌗🌘🌑🌒","🌔🌕🌖🌗🌘🌑🌒🌓","🌕🌖🌗🌘🌑🌒🌓🌔","🌖🌗🌘🌑🌒🌓🌔🌕","🌗🌘🌑🌒🌓🌔🌕🌖","🌘🌑🌒🌓🌔🌕🌖🌗","🌑🌒🌓🌔🌕🌖🌗🌘"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command(["غبي$","غبيي$"],prefixes=f".") & filters.me )
async def dmah(c,msg):
  listt = ["- عقلك ➡️ 🧠\n\n🧠         <(^_^ <)🗑","- عقلك ➡️ 🧠\n\n🧠       <(^_^ <)  🗑","- عقلك ➡️ 🧠\n\n🧠     <(^_^ <)    🗑","- عقلك ➡️ 🧠\n\n🧠   <(^_^ <)      🗑","- عقلك ➡️ 🧠\n\n🧠 <(^_^ <)        🗑","- عقلك ➡️ 🧠\n\n🧠<(^_^ <)         🗑","- عقلك ➡️ 🧠\n\n(> ^_^)>🧠         🗑","- عقلك ➡️ 🧠\n\n  (> ^_^)>🧠       🗑","- عقلك ➡️ 🧠\n\n           <(^_^ <)🗑"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass
        
@Client.on_message(filters.command(["تفجير$"],prefixes=f".") & filters.me )
async def boom(c,msg):
  listt = ["جاري تفجير","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n","💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n","▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n▪️▪️▪️▪️ \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💣💣💣💣 \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n💥💥💥💥 \n💥💥💥💥 \n","▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n▪️▪️▪️▪️ \n😵😵😵😵 \n","بوووووم تم تفجير الضحيه"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command(["طوبه$"],prefixes=f".") & filters.me )
async def tobah(c,msg):
  listt = ["⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜","⬜⬜⬛⬜⬜\n⬜⬜⬜⬛⬜\n⬜⬜⬜⬜🔴","⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜","⬜⬜⬛⬜⬜\n⬜⬛⬜⬜⬜\n🔴⬜⬜⬜⬜","🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜","⬜⬜⬛⬜⬜\n⬜⬜⬛⬜⬜\n⬜⬜🔴⬜⬜","🔴⬛⬛⬜⬜\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜","⬜⬜⬛⬛🔴\n⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command(["مربعات$"],prefixes=f".") & filters.me )
async def morbat(c,msg):
  listt = ["⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜","⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬛⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜","⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬛⬜⬛⬜⬜\n⬜⬜⬛⬛⬛⬜⬜\n⬜⬜⬜⬜⬜⬜⬜\n⬜⬜⬜⬜⬜⬜⬜","⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜","⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛","⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛","⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛⬜","⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜","⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛","⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜","⬛⬛⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬛⬜⬛⬜⬛\n⬛⬜⬛⬛⬛⬜⬛\n⬛⬜⬜⬜⬜⬜⬛\n⬛⬛⬛⬛⬛⬛⬛","⬜⬜⬜⬜⬜⬜⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬜⬛⬜⬛⬜\n⬜⬛⬜⬜⬜⬛⬜\n⬜⬛⬛⬛⬛⬛⬜\n⬜⬜⬜⬜⬜⬜⬜","⬛⬛⬛⬛⬛\n⬛⬜⬜⬜⬛\n⬛⬜⬛⬜⬛\n⬛⬜⬜⬜⬛\n⬛⬛⬛⬛⬛","⬜⬜⬜\n⬜⬛⬜\n⬜⬜⬜","👉🔴👈"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass        
        
@Client.on_message(filters.command(["تهكير$"],prefixes=f".") & filters.me )
async def hacker(c,msg):
  listt = ["** جـاري التـهكير ⚠️**","** جـاري الاتصـال بجهـاز الضحـية لأختـراقـة  📳**","** أختـراق جهـاز الضحـية الهـددف محـدد جـاري أختـراقـة ㊙️**","** تحـميل الاخـتراق  ㊙️ .. 0%**\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 4%**\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ ..10%**\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 20%**\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 36%**\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 52%**\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 84%**\n█████████████████████▒▒▒▒ `","** تحـميل الاخـتراق  ㊙️ .. 100%**\n████████████████████████`","** تـم اخـتراق الضحـية 🆘 بواسطه : `{سورس مرسليو}` . بـدون تنـازل**"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(2)
      except :
        pass

@Client.on_message(filters.command(["حلويات$"],prefixes=f".") & filters.me )
async def hlyat(c,msg):
  listt = ["🍧🍩🍪🎂🍰🧁🍫🍬🍭","🍦🍧🍩🎂🍰🧁🍫🍬🍭","🍦🍧🍩🍪🎂🍰🍫🍬🍭","🍦🍧🍩🍪🎂🍰🧁🍫🍭","🍦🍧🍩🍪🍰🧁🍫🍭","🍦🍧🍩🍪??🍰🧁🍫🍬","🍦🍩🍪🎂🍰🧁🍫🍬🍭","🍦🍧🍪🎂🍰🧁🍫🍬🍭","🍦🍧🍩🍪🎂🍰🍫🍬🍭"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass
 
@Client.on_message(filters.command(["مزاج$"],prefixes=f".") & filters.me )
async def mzgg(c,msg):
  listt = ["😁","😧","😡","😢","😁","😧","😡","😢"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.7)
      except :
        pass

@Client.on_message(filters.command(["قرد$"],prefixes=f".") & filters.me )
async def qrdd(c,msg):
  listt = ["🙉","🙈","🙊","🐵","🙉","🙈","🙊","🐵"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.7)
      except :
        pass

@Client.on_message(filters.command(["ايد$"],prefixes=f".") & filters.me )
async def hand(c,msg):
  listt = ["👈","👉","☝️","👆","🖕","👇","✌️","🤞","🖖","🤘","🤙","🖐️","👌"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.7)
      except :
        pass

@Client.on_message(filters.command(["العد التنازلي$"],prefixes=f".") & filters.me )
async def alwd(c,msg):
  listt = ["🔟","9️⃣","8️⃣","7️⃣","6️⃣","5️⃣","4️⃣","3️⃣","2️⃣","1️⃣","0️⃣","🆘"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.7)
      except :
        pass

@Client.on_message(filters.command(["رموز شيطانيه$","شيطان$"],prefixes=f".") & filters.me )
async def romoz(c,msg):
  listt = ["🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️🔴🔵🌕♓♎⛎◼️◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️🔴🔵🌕♓♎⛎🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️🔴🔵🌕♓♎⛎◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️\n◼️◼️◼️◼️◼️","◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️\n◼️◼️◼️◼️","◼️◼️◼️\n◼️◼️◼️\n◼️◼️◼️","◼️◼️\n◼️◼️","◼️"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass

@Client.on_message(filters.command(["اسعاف$"],prefixes=f".") & filters.me )
async def asaf(c,msg):
  listt = ["_____🚑","_____🚑","____🚑_","___🚑__","__🚑___","🚑_____","🚑_____","________"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(3)
      except :
        pass
                
@Client.on_message(filters.command(["شرطه$"],prefixes=f".") & filters.me )
async def police(c,msg):
  listt = ["🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴","🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵","🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴","🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵","🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴","🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵","🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴","🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵\n🔴🔴🔴⬜⬜⬜🔵🔵🔵","🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴\n🔵🔵🔵⬜⬜⬜🔴🔴🔴"]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.5)
      except :
        pass
      
@Client.on_message(filters.command(["دائره$"],prefixes=f".") & filters.me )
async def dara(c,msg):
  listt = ["⚫","⬤","●","∘",""]
  for x in range(1,3):
    for i in range(0,len(listt)) :
      try :
        await msg.edit(listt[i])
        time.sleep(0.9)
      except :
        pass

@Client.on_message(filters.command("نسبة الحب$", prefixes=f".") & filters.me)
async def permalink_hob(c, msg):
    roz = ['10', '20', '30','40','50','60','70','80','90','100']
    if not msg.reply_to_message:
        return
    muh = msg.from_user.first_name.replace("\u2060", "") if msg.from_user.first_name else msg.reply_to_message
    rza = random.choice(roz)
    await msg.edit( f"⌔ العضو {get_name(msg.reply_to_message)} \n⌔ نسبه الحب بينك وبينه هي {rza}"
    )
        
@Client.on_message(filters.command("اذكار الصباح$", prefixes=f".") & filters.me)
async def jio_2(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
#اذكار_الصباح
«أعُوذُ بِكَلِمَاتِ اللهِ التَّامَّاتِ مِنْ شَرِّ مَا خَلَقَ»

- ٣ مرَّات.

-----------------------‐

«اللَّهُمَّ بِكَ أمْسَيْنَا ، وَبِكَ أصْبَحْنَا ، وَبِكَ نَحْيَا ، وَبِكَ نَمُوتُ ، وَإلَيْكَ المَصِيرُ»

-----------------------‐

«اللَّهُمَّ مَا أمْسَى بِي مِنْ نِعْمَةٍ أوْ بِأحَدٍ مِنْ خَلْقِكَ فَمِنْكَ وَحْدَكَ لَا شَرِيكَ لَكَ ، فَلَكَ الحَمْدُ وَلَكَ الشُّكْرُ»

-----------------------‐

«اللَّهُمَّ إنِّي أمْسَيْتُ أُشْهِدُكَ ، وَأُشْهِدُ حَمَلَةَ عَرْشِكَ ، وَمَلَائِكَتَكَ ، وَجَمِيعَ خَلْقِكَ ، أنَّكَ أنْتَ اللهُ لَا إلَهَ إلَّا أنْتَ وَحْدَكَ لَا شَرِيكَ لَكَ ، وَأنَّ مُحَمَّدًا عَبْدُكَ وَرَسُولُكَ»

- ٤ مرَّات.

-----------------------‐

«أمْسَيْنَا وَأمْسَى المُلْكُ للهِ رَبِّ العَالَمِينَ ،
اللَّهُمَّ إنِّي أسْألُكَ خَيْرَ هَذِهِ اللَّيْلَةِ ، فَتْحَهَا ، وَنَصْرَهَا ، وَنُورَهَا ، وَبَرَكَتَهَا ، وَهُدَاهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِيهَا وَشَرِّ مَا بَعْدَهَا»

-----------------------‐

«أمْسَيْنَا عَلَى فِطْرَةِ الإسْلَامِ ، وَعَلَى كَلِمَةِ الإخْلَاصِ ، وَعَلَى دِينِ نَبِيِّنَا مُحَمَّدٍ صَلَّى اللهُ عَلَيْهِ وَسَلَّمَ ، وَعَلَى مِلَّةِ أبِينَا إبْرَاهِيمَ ، حَنِيفًا مُسْلِمًا وَمَا كَانَ مِنَ المُشْرِكِينَ»

-----------------------‐

«أمْسَيْنَا وأمْسَى المُلْكُ للهِ والحَمْدُ للهِ ، لَا إلَهَ إلَّا اللهُ وَحْدَهُ لَا شَرِيكَ لَهُ ، لَهُ المُلْكُ وَلَهُ الحَمْدُ وَهُوَ عَلَى كُلِّ شَيْءٍ قَدِيرٌ ،
رَبِّ أسْألُكَ خَيْرَ مَا فِي هَذِهِ اللَّيْلَةِ وَخَيْرَ مَا بَعْدَهَا ، وَأعُوذُ بِكَ مِنْ شَرِّ مَا فِي هَذِهِ اللَّيْلةِ وَشَرِّ مَا بَعْدَهَا ،
رَبِّ أعُوذُ بِكَ مِنَ الكَسَلِ وَسُوءِ الكِبَرِ ، رَبِّ أعُوذُ بِكَ مِنْ عَذَابٍ فِي النَّارِ وَعَذَابٍ فِي القَبْرِ» .
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command(["اوامري$","اوامر$","الاوامر"], prefixes=f".") & filters.me)
async def shark(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر سورس تايجر ⦒
• ( `.م1` )  ⦙ اوامر الخاص 
• ( `.م2` )  ⦙ اوامر الجروبات
• ( `.م3` )  ⦙ اوامر اليوتيوب
• ( `.م4` )  ⦙ اوامر الاذاعه 
• ( `.م5` )  ⦙ اوامر الرفع 
• ( `.م6` )  ⦙ اوامر اضافيه 
• ( `.م7` )  ⦙ اوامر التسليه 1
• ( `.م8` )  ⦙ اوامر التسليه 2
• ( `.م9` )  ⦙ اوامر التسليه 3
• ( `.م10` ) ⦙ اوامر الالعاب
• ( `.م11` ) ⦙ اوامر الالعاب المتطوره
• ( `.م12` ) ⦙ اوامر الميمز
• ( `.م13` ) ⦙ اوامر الميمز 2
• ( `.م14` ) ⦙ اوامر الميمز 3
• ( `.م15` ) ⦙ اوامر النسب
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م1$", prefixes=f".") & filters.me)
async def shark1(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر الخاص في سورس تايجر ⦒
✪ تفعيل ، تعطيل الترحيب 
✪ قبول ، رفض
✪ كتم ، الغاء كتم 
✪ سبام + الكلمه + الرقم (سبام تايجر22)
✪ ايدي + ايدي بالرد
✪ انتحال ● رجوع
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م2$", prefixes=f".") & filters.me)
async def shark2(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر الجروبات في سورس تايجر ⦒
✪ حظر ، الغاء حظر
✪ مسح المحظورين
✪ كتم ، الغاء كتم 
✪ مسح المكتومين
✪ ايدي + ايدي بالرد
✪ مسح رسايله (بالرد)
✪ تدمير (لتحظر جميع اعضاء المجموعه او القناه)
✪ مسح الروابط 
✪ مسح الصور 
✪ مسح + العدد
✪ اضف جهاتي
✪ فتح الكول
✪ قفل الكول
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م3$", prefixes=f".") & filters.me)
async def shark3(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر اليوتيوب في سورس تايجر ⦒
✪ غ + اسم الاغنيه
✪ ف + اسم الفيديو
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م4$", prefixes=f".") & filters.me)
async def shark4(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر الاذاعه في سورس تايجر ⦒
✪ اذاعه خاص (بالرد علي النص)
✪ اذاعه للمجموعات (بالرد علي النص)
✪ اذاعه للقنوات (بالرد علي النص)

✪ توجيه للخاص (بالرد علي الرساله)
✪ توجيه للمجموعات (بالرد علي الرساله)
✪ توجيه للقنوات (بالرد علي الرساله)
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
     
@Client.on_message(filters.command("م5$", prefixes=f".") & filters.me)
async def shark5(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر الرفع في سورس تايجر ⦒
✪ زواج ، طلاق  زوجاتي  مسح زوجاتي
✪ رفع ، تنزيل خول  الخولات  مسح الخولات 
✪ رفع ، تنزيل بنتي  بناتي  مسح بناتي
✪ رفع ، تنزيل شاذ  الشواذ  مسح الشواذ
✪ رفع ، تنزيل عرص  المعرصين  مسح المعرصين
✪ رفع ، تنزيل قرد  القرود  مسح القرود
✪ رفع ، تنزيل ابن متناكه  ولاد المتناكه  مسح ولاد المتناكه
✪ رفع ، تنزيل اخويا  اخواتي  مسح اخواتي
✪ رفع ، تنزيل بقلبي  القلوب  مسح القلوب 
✪ رفع ، تنزيل ابني  اولادي  مسح اولادي
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م6$", prefixes=f".") & filters.me)
async def shark6(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة الاوامر الاضافيه في سورس تايجر ⦒
✪ تلجراف (بالرد علي صوره لرفعها علي تليجراف)
✪ وش يقول (بالرد علي صوت)
✪ اذكار الصباح
✪ تفعيل تعطيل الساعه 
✪ تغيير اسمي + الاسم (تغيير اسمي SHARK)
✪ سورس
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
        
@Client.on_message(filters.command("م7$", prefixes=f".") & filters.me)
async def shark7(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر التسليه في سورس تايجر ⦒
✪ `.مكعبات`
✪ `.قمر`
✪ `.قلوب`
✪ `.قلب`
✪ `.بموتت`
✪ `.افكر`
✪ `.جيم`
✪ `.مطر`
✪ `.الارض`
✪ `.نجمه`
✪ `.ساعه`
✪ `.مح`
✪ `.تحميل`
✪ `.هينه`
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م8$", prefixes=f".") & filters.me)
async def shark8(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر التسليه 2 في سورس تايجر ⦒
✪ `.غبي`
✪ `.تفجير`
✪ `.طوبه`
✪ `.مربعات`
✪ `.تهكير`
✪ `.حلويات`
✪ `.مزاج`
✪ `.قرد`
✪ `.ايد`
✪ `.العد التنازلي`
✪ `.دائره`
✪ `.قياس`
✪ `.بشره`
✪ `.مربع`
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م9$", prefixes=f".") & filters.me)
async def shark9(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر التسليه 3 في سورس تايجر  ⦒
✪ `.رموز شيطانيه`
✪ `.اسعاف`
✪ `شرطه`
✪ `.زعلت`
✪ `.فليم`
✪ `.رسم`
✪ `.موسيقي`
✪ `.مصه`
✪ `.قطار`
✪ `.فايروس`
✪ `.مايكرو`
✪ `.ولد`
✪ `.افعي`
✪ `.عبقري`
✪ `.قتل`
✪ انتظرو تحديثات عظمه ل تليثون سورس تايجر🔥
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م10$", prefixes=f".") & filters.me)
async def shark10(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر الالعاب في سورس تايجر  ⦒
 ✪ `.اكس او` 
✪ `.حجره` لعبة حجره ورقه مقص
✪ `.ريفرسي`
✪ انتظرو تحديثات عظمه ل تليثون سورس تايجر🔥
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م11$", prefixes=f".") & filters.me)
async def shark11(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر الالعاب المتطوره في سورس تايجر ⦒
 ✪ `.القط المجنون` 
✪ `.ركل الكره`
✪ `.السمك الشائك`
✪ `.كرة السله`
✪ `.اطلاق النار`
✪ `.كرة القدم`
✪ `.موتسيكلات`
✪ `.تبديل النجوم`
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م12$", prefixes=f".") & filters.me)
async def shark12(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر الميمز في سورس تايجر ⦒
✪ `.هنضحك`
✪ `.مينفعش`
✪ `.عاوزين نعملك بني ادم`
✪ `.ي حوستي السوده`
✪ `.هنضحك حاضر`
✪ `.انا تعبان ي حامد`
✪ `.نعم انها المخدرات`
✪ `.قول كلام غير ده`
✪ `.ءنا عملت ءيه`
✪ `.عيب يجدعان`
✪ `.هتتحرقو في نار جهنم`
✪ `.يالي هتتحرقو`
✪ `.احترمي نفسك يوليه`
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م13$", prefixes=f".") & filters.me)
async def shark13(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر الميمز 2 في سورس تايجر ⦒
✪ `.في رمضان`
✪ `.مش عارف اقوم`
✪ `.دمك خفيف اوي`
✪ `.لا تقتل المتعه ي مسلم`
✪ `.يختاااي`
✪ `.بيكدب`
✪ `.احنا جامدين اوي`
✪ `.اي الهبل دا`
✪ `.فاشل فاشل`
✪ `.اجمد كدا متعيطش`
✪ `.يا لاهوي`
✪ `.دا اي الهم دا`
✪ `.هعوره`
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م14$", prefixes=f".") & filters.me)
async def shark14(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """

✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر الميمز 3 في سورس تايجر ⦒
✪ `.تاخد نفس عميق`
✪ `.ربنا نصرني`
✪ `.لو معايا خنجرين`
✪ `.اماااال`
✪ `.خخ امال`
✪ `.اهلا بيكم`
✪ `.اخلاقك العاليه دي`
✪ `.علي مهلك`
✪ `.خبر اي ي مرا`
✪ `.انا بيه بن بيه`
✪ `.اتكلم بادب يولد`
✪ `.انا رمضان جانا يعم`
✪ `.انت مش مظبوط ياض`
✪ `.ي حلو ي جميل`
✪ `.خلصانه`
✪ `.انا في دوامه`
✪ `.مش اسمحلك`
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])

@Client.on_message(filters.command("م15$", prefixes=f".") & filters.me)
async def shark15(c, msg):
    animation_interval = 1
    animation_ttl = range(19)
    animation_chars = [
        """
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
: ⦑   قائمة اوامر النسب في سورس تايجر ⦒
✪ `.نسبة الانوثة`
✪ `.نسبة الغباء`
✪ `.نسبة الرجولة`
✪ `.نسبة المنيكه`
✪ `.نسبة التعريص`
✪ `.نسبة الكره`
✪ `.نسبة الجمدان`
✪ `.نسبة الايمان`
✪ `.نسبة الجمال`
✪=====⧼  [𝐒𝐎𝐔𝐑𝐂𝐄 𝐓𝐈𝐆𝐄𝐑 ](https://t.me/AG_MQ) ⧽=====✪
""",
    ]
    for i in animation_ttl:
        await asyncio.sleep(animation_interval)
        await msg.edit(animation_chars[i % 19])
 
@Client.on_message(filters.command("مسح الروابط$",prefixes=f".") & filters.me & filters.group)
async def del_urls(c,msg):
  await msg.reply("✪ جاري جلب الروابط ..")
  num = 0
  async for message in c.search_messages(msg.chat.id, filter=enums.MessagesFilter.URL):
    try :
      await message.delete(revoke=True)
      num += 1
    except : 
      pass
  await msg.edit(f"✪ تم مسح {num} رساله تحتوي علي روابط")


@Client.on_message(filters.command(["سورس$","السورس$"],prefixes=f".") & filters.me )
async def source(c,msg):
  await msg.edit("⋖⊶◎⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 ✪ 𝐒𝐇𝐀𝐑𝐊⌯⊶◎⊷⋗\n✪ ¦ [↱ 𝘿ٓ𝙀ٓ𝙑ٰٰ 𝗢𝗠𝗔𝗥 ↲](t.me/T_3_A)\n✪ ¦ [𝙎𝙐𝙋𝙋𝙊𝙍𝙏 𖧊 𝐒𝐇𝐀𝐑𝐊](t.me/QW_PN)\n✪ ¦ [𝐒𝐎𝐔𝐑𝐂𝐄 𖧊 𝐒𝐇𝐀𝐑𝐊](t.me/L_H_V)\n⋖⊶◎⊷⌯𝐒𝐎𝐔𝐑𝐂𝐄 ✪ 𝐒𝐇𝐀𝐑𝐊⌯⊶◎⊷⋗")
  

@Client.on_message(filters.command("مسح الصور$",prefixes=f".") & filters.me & filters.group)
async def del_photos(c,msg):
  await msg.reply("✪ جاري جلب الصور ..")
  num = 0
  async for message in c.search_messages(msg.chat.id, filter=enums.MessagesFilter.PHOTO):
    try :
      await message.delete(revoke=True)
      num += 1
    except : 
      pass
  await msg.edit(f"✪ تم مسح {num} رساله تحتوي علي صور")
  
@Client.on_message(filters.command("تفعيل الترحيب$",prefixes=f".") & filters.me )
async def wel(c,msg):
  r.set(f"{sudo_id}welcome","on")
  await msg.edit("✪ تم تفعيل الترحيب")

@Client.on_message(filters.command("تعطيل الترحيب$",prefixes=f".") & filters.me )
async def unwel(c,msg):
  r.delete(f"{sudo_id}welcome")
  await msg.edit("✪ تم تعطيل الترحيب")
  

@Client.on_message(filters.command("تعطيل الساعه$",prefixes=f".") & filters.me )
async def clockk(c,msg):
  r.delete(f"{sudo_id}clockk")
  get = await c.get_chat("me")
  await c.update_profile(first_name=f'{get.last_name}' ,last_name="")
  await msg.edit("✪ تم تعطيل الساعه")
@Client.on_message(filters.command("تفعيل الساعه$",prefixes=f".") & filters.me )
async def unclockk(c,msg):
  get = await c.get_chat("me")
  if get.last_name:
    my_name = f"{get.first_name} {get.last_name}"
  else :
    my_name = get.first_name
  r.set(f"{sudo_id}clockk",my_name)
  await msg.edit("✪ تم تفعيل الساعه")
  await name()
  
@Client.on_message(filters.regex("^.تغيير اسمي (.*)") & filters.me )
async def chang_name(c,msg):
  my_name = msg.text
  my_name = my_name.replace(".تغيير اسمي","")
  r.set(f"{sudo_id}clockk",my_name)
  await msg.edit(f"✪ تم تغيير اسمك الي {my_name}")
  await name()
  
@Client.on_message(filters.regex("^.مسح [0-9]+$") & filters.me )
async def del_message(c,msg):
  textt = msg.text
  num = int(textt.split(" ")[1])
  list1 = []
  msg_id = msg.id
  for i in range(1,num):
    list1.append(msg_id)
    msg_id = msg_id - 1
  try :
    await c.delete_messages(msg.chat.id, list1)
  except Exception as e :
    await msg.reply(e)
    
@Client.on_message(filters.regex("^.سبام (.*?) [0-9]+$") & filters.me )
async def spam_message(c,msg):
  await msg.delete()
  textt = msg.text
  num = int(textt.split(" ")[2])
  word = textt.split(" ")[1]
  for i in range(1,num):
    await c.send_message(msg.chat.id,word)
    
@Client.on_message(filters.regex("^.بحث (.*)") & filters.me )
async def search_word(c,msg):
  textt = msg.text
  word = textt.replace(".بحث ","")
  num = 0
  async for message in c.search_messages(msg.chat.id, query=word):
    try :
      await c.send_message(msg.chat.id,".",reply_to_message_id=message.id)
      num += 1
    except : 
      pass
  await message.reply(f"✪ العدد {num}")
  
@Client.on_message(filters.command("مسح رسايله$",prefixes=f".") & filters.me & filters.reply )
async def dell_all_msg(c,msg):
  if msg.reply_to_message.from_user.id in sudo_command:
    return await msg.edit("✪ لا يمكنك استخدام الامر علي مبرمجين السورس")
  try :
    await c.delete_user_history(msg.chat.id,msg.reply_to_message.from_user.id)
    await c.send_message(msg.chat.id,"✪ تم مسح رسايله")
  except Exception as e:
    await msg.edit("✪ ليس لديك صلاحيه المسح")