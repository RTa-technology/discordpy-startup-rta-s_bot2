from discord.ext import commands as rta
class Basic(rta.Cog, name="Basic"):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    
    @rta.command(name="pin")
    async def pin(self,ctx):
        await ctx.send(f"pon {ctx.author.name}")

