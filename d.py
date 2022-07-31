import discord
from discord.ext import commands
from config import settings

bot = commands.Bot(command_prefix = settings['prefix'])

@bot.command()
@commands.has_any_role(770589004789448714, 756749544737341451)
async def up(ctx, member: discord.Member):
    roles = []
    for i in member.roles:
        roles.append(i)
    title = str(roles[-1])
    titles = ['Private', 'Private First Class', 'Corporal', 'Junior Sergeant', 'Sergeant', 'Master Sergeant', 'Command Sergeant', 'Specialization Commander', 'Junior Constable', 'Constable', 'Senior Constable', 'Captain']
    ids = [756609253086593134, 756609242965999627, 756609250155036672, 770654293815721985, 756609249395867759, 756609249790001162, 756609245172203552, 770654271128469514, 770654292519419934, 770654290926764032, 756609256312143924, 1000373135620710400]
    for i in range(len(titles)):
        if title == titles[i]:
            role = discord.utils.get(member.guild.roles, id = ids[i + 1])
            await member.add_roles(role)
            role = discord.utils.get(member.guild.roles, id = ids[i])
            await member.remove_roles(role)
            await ctx.message.delete()
            break
@bot.command()
@commands.has_any_role(770589004789448714, 756749544737341451)
async def down(ctx, member: discord.Member):
    roles = []
    for i in member.roles:
        roles.append(i)
    title = str(roles[-1])
    titles = ['Private', 'Private First Class', 'Corporal', 'Junior Sergeant', 'Sergeant', 'Master Sergeant', 'Command Sergeant', 'Specialization Commander', 'Junior Constable', 'Constable', 'Senior Constable', 'Captain']
    titles = titles[::-1]
    ids = [756609253086593134, 756609242965999627, 756609250155036672, 770654293815721985, 756609249395867759, 756609249790001162, 756609245172203552, 770654271128469514, 770654292519419934, 770654290926764032, 756609256312143924, 1000373135620710400]
    ids = ids[::-1]
    for i in range (len(titles)):
        if title == titles[i]:
            role = discord.utils.get(member.guild.roles, id = ids[i + 1])
            await member.add_roles(role)
            role = discord.utils.get(member.guild.roles, id = ids[i])
            await member.remove_roles(role)
            await ctx.message.delete()
            break

bot.run(settings['token'])