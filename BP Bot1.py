import discord
import asyncio
import requests
import os
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix = '-')

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command(pass_context=True)
async def whois(ctx, user):
    r = requests.get("https://www.brickplanet.com/web-api/users/get-user/"+user)
    data = r.json()
    u_name = data["Username"]
    u_ID = data["ID"]
    u_fp = data["ForumPosts"]
    thumb = data["AvatarImage"]
    u_status = data["Status"]
    u_about = data["About"]
    u_frds = data["NumFriends"]
    u_groups = data["NumGroups"]
    u_net = data["NetWorth"]
    #############################################################################
    embed = discord.Embed(title="{}'s Information".format(user), description = "This is all I can find!", color=0x00ff00)
    embed.add_field(name="Username:", value=u_name, inline=True)
    embed.add_field(name="ID:", value=u_ID, inline=True)
    embed.add_field(name="Forum Posts:", value=u_fp, inline=True)
    embed.add_field(name="Current Status:", value=u_status, inline=True)
    embed.add_field(name="About:", value=u_about, inline=True)
    embed.add_field(name="Friends:", value=u_frds, inline=True)    
    embed.add_field(name="In Groups:", value=u_groups, inline=True)  
    embed.add_field(name="Networth:", value=u_net, inline=True) 
    embed.set_thumbnail(url="https://cdn.brickplanet.com/"+thumb+".png")
    await bot.say(embed=embed)

    

bot.run(os.getenv('TOKEN'))
