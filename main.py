import discord
from discord import Member
from discord.ext import commands
from asyncio import sleep
client = commands.Bot(command_prefix="!", self_bot = True)
@client.event
async def on_ready():
    print(f"{client.user.name}#{client.user.discriminator} is ready")
#dm just one memebr
@client.command()
async def dm(ctx, member : Member, *, message):
    try:
        await ctx.message.delete()
        await member.send(message)
    except Exception as e:
        print(e)
#mass dm command
@client.command()
async def mass_dm(ctx, num : int, *,message):
        await ctx.message.delete()
        try:
            int(num)
        except:
            await ctx.send("pls enter a true number")
        members = ctx.guild.members
        for member in members:
            for i in range(num):
                try:
                    await member.send(message)
                    print(f"message sent to {member.name}#{member.discriminator}")
                    await sleep(5)
                except Exception as e:
                    print(e)
client.run("token")#put your token here 


