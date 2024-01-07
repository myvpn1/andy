from regis import *

@bot.on(events.CallbackQuery(data=b'registrasi'))
async def registrasii(event):
	async def registrasii_(event):
		async with bot.conversation(chat) as user:
			await event.respond('**Username:**')
			user = user.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			user = (await user).raw_text
		async with bot.conversation(chat) as pw:
			await event.respond("**Input IP VPS:**")
			pw = pw.wait_event(events.NewMessage(incoming=True, from_users=sender.id))
			pw = (await pw).raw_text
		async with bot.conversation(chat) as exp:
			await event.respond("**Expiry Day**",buttons=[
[Button.inline(" 30 Day ","30"),
Button.inline(" 60 Day ","60")],
[Button.inline(" 90 Day ","90"),
Button.inline(" Lifetime ","360")]])
			exp = exp.wait_event(events.CallbackQuery)
			exp = (await exp).data.decode("ascii")
		cmd = f'printf "%s\n" "{user}" "{pw}" "{exp}" | bash /root/regis/shell/bot-registrasi'
		try:
			a = subprocess.check_output(cmd, shell=True).decode("utf-8")
		except:
			await event.respond("**Not Exist**")
		else:
			msg = f"""```{a}```
**» 🤖@YSSHstore**"""
			await event.respond(msg)
	chat = event.chat_id
	sender = await event.get_sender()
	a = valid(str(sender.id))
	if a == "true":
		await registrasii_(event)
	else:
		await event.answer("Akses Ditolak",alert=True)