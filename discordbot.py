from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='$',help_command=JapaneseHelpCommand())
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

class basic(bot.Cog, name='基本動作'):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    
    @bot.command(name="ping")
    async def ping(self,ctx):
        await ctx.send(f"{ctx.author.name}\npong")

class Greet(bot.Cog, name='Greeting'):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @bot.command(name="hello")
    async def hello(self, ctx):
        """出会いのあいさつをする"""
        await ctx.send(f"どうも、{ctx.author.name}さん!")

    @bot.command(name="goodbye")
    async def goodbye(self, ctx):
        """別れの挨拶をする"""
        await ctx.send(f"じゃあね、{ctx.author.name}さん!")


class JapaneseHelpCommand(bot.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.bot_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (f"各コマンドの説明: {prefix}help <コマンド名>\n"
                f"各カテゴリの説明: {prefix}help <カテゴリ名>\n")


bot.add_cog(Greet(bot=bot))
bot.add_cog(basic(bot=bot))
bot.run(token)
