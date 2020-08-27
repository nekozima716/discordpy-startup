from discord.ext import commands
import os,asyncio,traceback,random,datetime,discord

bot = commands.Bot(command_prefix='//')
token = os.environ['DISCORD_BOT_TOKEN']

@bot.command()
async def log(ctx,a=None,b=None):
	ch = bot.get_channel(728949181183688725)
	now = datetime.datetime.now()
	if int(a) >= int(b):
		af = datetime.datetime(now.year,now.month,now.day-1,int(a)-9)
	else:
		af = datetime.datetime(now.year,now.month,now.day,int(a)-9)
	be = datetime.datetime(now.year,now.month,now.day,int(b)-9)
	embed = discord.Embed(title=a+'時から'+b+'時の間に再生された音楽一覧',description=None,color=0xff0000)
	c = 0
	async for message in ch.history(after=af,before=be):
		if 'Now' in message.content:
			if message.author.id == 235088799074484224:
				c+=1	
				embed.add_field(name=c,value=message.content[13:-6],inline=False)
	await ctx.send(embed=embed)
				
		
		
@bot.event
async def on_member_join(member):
	await member.send(f'{member.mention} こんにちは')

bot.run(token)
