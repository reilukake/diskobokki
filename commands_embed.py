from discord.ext import commands
import discord
from datetime import datetime

class EmbedCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

# Info
    @commands.command(name="bokkikomennot")
    async def ping(self, ctx: commands.Context):
        embed = discord.Embed(title="Diskobokin komennot:", description=":D", colour=0x87CEEB, timestamp=datetime.utcnow())
        embed.set_author(name="Kakkulapio", icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/6021a415-a6c3-41d9-ba14-c0262fa0b6fa-profile_image-70x70.png")
        embed.add_field(name="Field 1", value="Not an inline field!", inline=False)
        embed.add_field(name="Field 2", value="An inline field!", inline=True)
        embed.add_field(name="Field 3", value="Look I'm inline with field 2!", inline=True)
        embed.set_footer(text="Diskobokki", icon_url="https://static-cdn.jtvnw.net/jtv_user_pictures/6021a415-a6c3-41d9-ba14-c0262fa0b6fa-profile_image-70x70.png")
        await ctx.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(EmbedCommands(bot))
