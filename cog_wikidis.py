from discord.ext import commands as rta
class WikiDiscord(rta.Cog, name="Wd_to_discord"):
    def __init__(self, bot):
        super().__init__()
        self.bot = bot
        
    @rta.event
    async def on_message(message):
        """Wikidot Markdown → Discord Markdown"""
        if message.content.startswith('$ds'):
        # 文字から「$ds」を抜く
        dis_md = message.content[len('$ds'):].strip()
                
        discord1_md = dis_md.replace('//', '*').replace('**', '**').replace('//**', '***').replace('**//', '***').replace('__', '__').replace('--', '~~')

#            if re.match('##[a-z]+|', discord1_md):
#                discord2_md = discord1_md.replace('##red|', '```autohotkey\n').replace('##blue|','```ini\n[').replace('##yellow|','```md\n< ').replace('##orange|','```py\n@ ').replace('##green|','```diff\n+ ').replace('##cyan|','```py\n# ')
#                discord3_md = discord2_md.replace('##','\n```')
#            else:
#                discord3_md = discord1_md

            discord_md = discord1_md.replace('[[code]]','```\n').replace('[[/code]]','\n```')
                
        await message.channel.send(discord_md)
