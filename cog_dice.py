from discord.ext import commands as rta
class Dice(rta.Cog, name="Dice"):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        
    @rta.command(name="dice")
    async def dice(ctx, dice: str):
        try:
            rolls, limit = map(int, dice.split('d'))
        except Exception:
            await ctx.send('Format has to be in NdN!')
            return
        result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
        msg = f"{ctx.author.mention}\n" + result 
        await ctx.send(msg)
        
