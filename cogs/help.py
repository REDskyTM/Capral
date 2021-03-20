import discord
from discord.ext import commands

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot



    @commands.command(aliases=['хелп'])
    async def help(self, ctx):
        await ctx.channel.purge( limit = 1 )

        emb = discord.Embed(color = 0xFFDF00)

        emb.set_author(name = '✨ Команды бота ✨', icon_url = 'https://cdn.discordapp.com/avatars/811954263445471273/9e4ca0208d8eee6f524edaf6a6c72640.png?size=512')
        emb.add_field( name = '_**⚒️Модерация🛡️**_', value = 'к!кик, к!бан, к!выдать-роль, к!снять-роль, к!очистить, к!словмод')
        emb.add_field( name = '_**🎆Обработка фото🎇**_', value = 'к!триггер, к!стекло, к!инверт, к!сепия, к!мусор')
        emb.add_field( name = '_**🎈Информация📖**_', value = 'к!профиль, к!инфо-роль, к!бот-инфо, к!аватар, инфо-эмодзи')
        emb.add_field( name = '_**🧰Голосовые каналы🔩**_', value = 'к!лимит-2, к!лимит-99')
        emb.add_field( name = '__**😆Веселье😂**__', value = 'к!монетка, к!фейк-бан, к!фейк-кик, к!кнб, к!фейк-мьют, к!сапёр, к!шар')
        emb.add_field( name = '_**🔞NSFW🔞**_', value = 'к!хентай, к!ноги, к!хентайгиф, к!трап, к!сиськи, к!футунари, к!сперма, к!нсфваватар, к!анал, к!юри, к!йифф')
        emb.add_field( name = '_**✉️Связь с создателем📩**_', value = 'к!идея, к!баг')

        await ctx.send(embed=emb)

    

def setup(client):
    client.add_cog(help(client))
