import discord
import asyncio
import requests
import os
from discord.ext import commands
from discord.ext.commands import Bot
bot = commands.Bot(command_prefix = '-')


TOKEN=os.environ['BOT_TOKEN']

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

#User Suspension check 
        if u_sus == 0:
            u_sus = ":x:"
        else:
            u_sus="::white_check_mark:"
        u_admin = data["isAdmin"]
#User Admin Check
        if u_admin == 1:
            u_admin = ":white_check_mark:"

        else:
            u_admin=":x:"

            
#User verification name check            
        u_verify = data["VerifiedUser"]
        if u_verify == 1:
            u_name = data["Username"] + ' :ballot_box_with_check: '
#User Admin name check
        if u_admin ==':white_check_mark:':
            u_name = data["Username"] + '<:BPAdmin:461200993309425666>'

        if u_admin == ':white_check_mark:':
            if u_verify == 1:
                u_name = data["Username"] + '<:BPAdmin:461200993309425666>' +'<:Ver1:461208517760778272>'
#My name check
        if u_name == 'devthegamer23':
            u_name = data["Username"] + ':tools:'
            
        #############################################################################
        embed = discord.Embed(title="{}".format(u_name), description = "", color=0x00ff00)
        embed.add_field(name="ID:", value=u_ID, inline=True)
        embed.add_field(name="Forum Posts:", value=u_fp, inline=True)
        embed.add_field(name="Current Status:", value='*"'+u_status  + '*" ', inline=True)
        embed.add_field(name="Friends:", value=u_frds, inline=True)    
        embed.add_field(name="In Groups:", value=u_groups, inline=True)  
        embed.add_field(name="Networth:", value=u_net, inline=True)
        embed.add_field(name="Is the user suspended?", value=u_sus, inline=True)
        embed.add_field(name="Is the user an Admin?", value=u_admin, inline=True)
        embed.set_thumbnail(url="https://cdn.brickplanet.com/"+thumb+".png")
        embed.set_footer(text='~Made by: https://www.brickplanet.com/users/devthegamer23')
        await bot.say(embed=embed)
        
    except:
        await bot.say('An error occurred')

################################################
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


@bot.command(pass_context=True)
async def itemInfo(ctx, itemID):
    try:
        itemR = requests.get("https://www.brickplanet.com/web-api/store/get-item/"+str(itemID))
        item_Data = itemR.json()
        item_name = item_Data['Name']
        item_desc = item_Data['Description']
        item_ID = item_Data['ID']
        item_type = item_Data['ItemType']
        item_rating = item_Data['ItemRatingScore']
        item_bits = item_Data['PriceBits']
        item_crds = item_Data['PriceCredits']
        item_status = item_Data['IsOnSale']
        item_img = item_Data['Image']
        est_item_bits = 'N/A'
        est_item_crds = 'N/A'
        if item_Data['IsUnique'] == 1:
            est_item_bits = item_Data['EstimatedValueBits']
            est_item_crds = item_Data['EstimatedValueCredits']


        if item_Data['IsUnique'] == 1:
            item_status = "The item is Unique"    


        elif item_Data['IsOnSale'] ==0:
            if item_Data['IsUnique'] == 0:
                item_status = "Not on sale"


        elif item_Data['IsUnique'] == 0:
            if item_Data['IsOnSale'] == 1:
               item_status = "On sale" 
        starStr = str(item_Data['ItemRatingScore'])
        starInt = float(starStr)
        
        
    #Range from 1.1 to 1.9
        if  starInt == 1.0:
            rating_stars = '<:FullStar:461223664562470912>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>'
        if  starInt >= 1.1:
            if starInt <= 1.4: 
                rating_stars = '<:FullStar:461223664562470912>' + '<:close:461235309729021963>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>'
        if  starInt == 1.5:
            rating_stars = '<:FullStar:461223664562470912>' + '<:HalfStar:461223681243480075>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>'
        if  starInt >= 1.6:
            if starInt <= 1.9: 
                rating_stars = '<:FullStar:461223664562470912>' + '<:close:461235309729021963>' + '<:far:461235309506592799>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>'
    ####################################################### 
              #Range 2.1 to 2.9
        if  starInt == 2.0:
            rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>'
        if  starInt >= 1.1:
            if starInt <= 1.4: 
                rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:close:461235309729021963>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>'
        if  starInt == 2.5:
            rating_stars = '<:FullStar:461223664562470912>' + '<:HalfStar:461223681243480075>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>'
        if  starInt >= 2.6:
            if starInt <= 2.9: 
                rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:far:461235309506592799>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>'  
    #######################################################################################
    #Range from 3.1 to 3.9
        if  starInt == 3.0:
            rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:0_:461235343325396992>' + '<:0_:461235343325396992>'
        if  starInt >= 3.1:
            if starInt <= 3.4: 
                rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:close:461235309729021963>' + '<:0_:461235343325396992>'
        if  starInt == 3.5:
            rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:HalfStar:461223681243480075>' + '<:0_:461235343325396992>'
        if  starInt >= 3.6:
            if starInt <= 3.9: 
                rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:far:461235309506592799>' + '<:0_:461235343325396992>'
    ####################################################### 
              #Range 2.1 to 2.9
        if  starInt == 4.0:
            rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:0_:461235343325396992>'
        if  starInt >= 4.1:
            if starInt <= 4.4: 
                rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:close:461235309729021963>'
        if  starInt == 4.5:
            rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:HalfStar:461223681243480075>'
        if  starInt >= 4.6:
            if starInt <= 4.9: 
                rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:far:461235309506592799>'
        if starInt >= 5.0:
            rating_stars = '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>' + '<:FullStar:461223664562470912>'

        ##############################EMBEDS###################
        iEm = discord.Embed(title="{}".format(item_name), description = "{}".format(item_desc), color=0x00ff00)
        iEm.add_field(name="Item Type:", value=item_type, inline=False)
        iEm.add_field(name="Item ID:", value=item_ID, inline=False)
        iEm.add_field(name="Item Price In bits (On release):", value=item_bits, inline=False)
        iEm.add_field(name="Item Price In Credits (On release):", value=item_crds, inline=False)
        iEm.add_field(name="Item Status:", value=item_status, inline=False)
        iEm.add_field(name="Item Estimated Value(In bits) :", value=est_item_bits, inline=False)
        iEm.add_field(name="Item Estimated Value(In credits) :", value=est_item_bits, inline=False)
        iEm.add_field(name="Item Rating ({}):".format(starInt), value=rating_stars, inline=False)
        iEm.set_thumbnail(url="https://cdn.brickplanet.com/"+item_img)
        await bot.say( embed=iEm)

    except:
        await bot.say("An error occurred")
#########################################
bot.run(TOKEN)
