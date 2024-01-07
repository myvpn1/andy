from regis import *

@bot.on(events.NewMessage(pattern=r"(?:.regis|/regis|/start)$"))
@bot.on(events.CallbackQuery(data=b'menu'))
async def menu(event):
	inline = [
[Button.inline(" REGIST ","registrasi"),
Button.inline(" DELETE ","deleteip")],
[Button.inline(" Owner Bot ","https://t.me/YSSHstpre")]]
	sender = await event.get_sender()
	val = valid(str(sender.id))
	if val == "false":
		try:
			await event.answer("Akses Ditolak", alert=True)
		except:
			await event.reply("Akses Ditolak")
	elif val == "true":
		sh = f' curl -sS https://raw.githubusercontent.com/myvpn1/andy/main/ip | grep "###" | wc -l'
		ssh = subprocess.check_output(sh, shell=True).decode("ascii")

		msg = f"""
━━━━━━━━━━━━━━━━━━━━━━━ 
**☘️ REGISTRASI IP AUTO SCRIPT☘️**
━━━━━━━━━━━━━━━━━━━━━━━ 
Halo Tuan {sender.first_name}
**Total Pelanggan :** `{ssh.strip()}`
"""
		x = await event.edit(msg,buttons=inline)
		if not x:
			await event.reply(msg,buttons=inline)

