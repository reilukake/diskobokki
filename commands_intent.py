from discord.ext import commands
import discord


class IntentCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        # Channel ID must be fetched from the server settings
        channel = self.bot.get_channel(666614870736764928)

        if not channel:
            return

        await channel.send(f"Tervetuloa kanavalle, {member}!")


def setup(bot: commands.Bot):
    bot.add_cog(IntentCommands(bot))
