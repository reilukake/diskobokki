from discord.ext import commands
import discord
import time


class SimpleCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="ping")
    async def ping(self, ctx: commands.Context):
        start_time = time.time()
        message = await ctx.send("Piiiiiiiing?")
        end_time = time.time()
        await message.edit(
            content=f"Pong! {round(self.bot.latency * 1000)}ms\nAPI: {round((end_time - start_time) * 1000)}ms")

    @commands.command(name="setstatus")
    async def setstatus(self, ctx: commands.Context, *, text: str):
        """Set the bot's status."""
        await self.bot.change_presence(activity=discord.Game(name=text))


def setup(bot: commands.Bot):
    bot.add_cog(SimpleCommands(bot))
