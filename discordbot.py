from discord.ext import commands
import os
import traceback
prefix = '$'

bot = commands.Bot(command_prefix=prefix, help_command=JapaneseHelpCommand())
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    orig_error = getattr(error, "original", error)
    error_msg = ''.join(traceback.TracebackException.from_exception(orig_error).format())
    await ctx.send(error_msg)

@bot.command(name="ping")
async def ping(ctx):
        await ctx.send('pong')


class basic(commands.Cog, name='基本動作'):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
    
    @commands.command(name="pin")
    async def pin(self,ctx):
        await ctx.send(f"pon {ctx.author.name}")

class Greet(commands.Cog, name='あいさつ'):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot

    @commands.command(name="こんにちは")
    async def hello(self, ctx):
        """出会いのあいさつをする"""
        await ctx.send(f"どうも、{ctx.author.name}さん!")

    @commands.command(name="さようなら")
    async def goodbye(self, ctx):
        """別れの挨拶をする"""
        await ctx.send(f"じゃあね、{ctx.author.name}さん!")


class JapaneseHelpCommand(commands.DefaultHelpCommand):
    def __init__(self):
        super().__init__()
        self.commands_heading = "コマンド:"
        self.no_category = "その他"
        self.command_attrs["help"] = "コマンド一覧と簡単な説明を表示"

    def get_ending_note(self):
        return (f"各コマンドの説明: {prefix}help <コマンド名>\n"
                f"各カテゴリの説明: {prefix}help <カテゴリ名>\n")


bot = commands.Bot(command_prefix=prefix, help_command=JapaneseHelpCommand())
bot.add_cog(Greet(bot=bot))
bot.add_cog(basic(bot=bot))
bot.run(token)
