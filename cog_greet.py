from discord.ext import commands as rta
class Greet(rta.Cog, name="Greet"):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @rta.command(name="こんにちは")
    async def hello(self, ctx):
        """出会いのあいさつをする"""
        await ctx.send(f"どうも、{ctx.author.name}さん!")

    @rta.command(name="さようなら")
    async def goodbye(self, ctx):
        """別れの挨拶をする"""
        await ctx.send(f"じゃあね、{ctx.author.name}さん!")

