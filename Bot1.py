import discord
import asyncio
import requests
import os
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix = '-')

bot.traders = []

TOKEN=os.environ['BOT_TOKEN']

@bot.event
async def on_connect():
    bot.say("Hello Users! Welcome to the version 1.2. In this update trading options are fianlly here. type -help for more information.)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
@bot.command(pass_context=True)
async def whois(ctx, user):
    try:
        data = requests.get("https://www.brickplanet.com/web-api/users/get-user/"+user).json()
        u_name = data["Username"]
        u_ID = data["ID"]
        u_fp = data["ForumPosts"]
        thumb = data["AvatarImage"]
        u_status = data["Status"]
        u_about = data["About"]
        u_frds = data["NumFriends"]
        u_groups = data["NumGroups"]
        u_net = data["NetWorth"]         
        u_sus = data["Suspended"]
        if u_sus == 0:
            u_sus = ":x:"
        else:
            u_sus=":white_check_mark:"
        u_admin = data["isAdmin"]
        if u_admin == 1:
            u_admin = ":white_check_mark:"
        else:
            u_admin=":x:"
        #############################################################################
        embed = discord.Embed(title="{}'s Information".format(u_name), description = "This is all I can find!", color=0x00ff00)
        embed.add_field(name="Username:", value=u_name, inline=True)
        embed.add_field(name="ID:", value=u_ID, inline=True)
        embed.add_field(name="Forum Posts:", value=u_fp, inline=True)
        embed.add_field(name="Current Status:", value=u_status, inline=True)
        embed.add_field(name="About:", value=u_about, inline=True)
        embed.add_field(name="Friends:", value=u_frds, inline=True)    
        embed.add_field(name="In Groups:", value=u_groups, inline=True)  
        embed.add_field(name="Networth:", value=u_net, inline=True)
        embed.add_field(name="Is the user suspended?", value=u_sus, inline=True)
        embed.add_field(name="Is the user an Admin?", value=u_admin, inline=True)
        embed.set_thumbnail(url="https://cdn.brickplanet.com/"+thumb+".png")
        embed.set_footer(text='~Made by: https://www.brickplanet.com/users/devthegamer23')
        await bot.say(embed=embed)
    except:
        bot.say('An error occurred')
@bot.command(pass_context=True)
async def betrader(ctx, user):
    author = str(ctx.message.author)
    server = ctx.message.server.name
    u_add = ("**- BP: **__" +user+ "  __** Discord: ** "+author+ " **From server** "+server)
    bot.traders.append(u_add)
    await bot.say('***User added to the list***')
    

@bot.command(pass_context=True)
async def seektraders(ctx):
    embed = discord.Embed(title="Current users wanting to trade", description = "Not all usernames are vaild, cuz people LOVE trolling", color=0x00ff00)
    for i in range(len(bot.traders)):
        embed.add_field(name="User {}: ".format(i), value=bot.traders[i], inline=True)
    await bot.say(embed=embed)

bot.run(TOKEN)
