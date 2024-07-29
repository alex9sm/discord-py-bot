import discord
from discord import app_commands
from discord.ext import commands

class HelpCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="help", description="List of available commands.")
    async def help(self, ctx: discord.Interaction):
        embed = discord.Embed(title="Xing Xing Monkey commands", description="Here are the available commands:", color=discord.Color.blue())
        embed.add_field(name="/proverb", value="say a chinese proverb", inline=False)
        embed.add_field(name="/points", value="see your points", inline=False)
        embed.add_field(name="/leaderboard", value="see everyone's points", inline=False)
        embed.add_field(name="/addkey", value="add your brokerage api key", inline=False)
        embed.add_field(name="/accounts", value="view your accounts", inline=False)
        embed.add_field(name="/sell", value="sell a stock", inline=False)
        embed.add_field(name="/buy", value="purchase a stock", inline=False)
        embed.add_field(name="/news", value="news about the stock", inline=False)
        await ctx.response.send_message(embed=embed, ephemeral=True)

async def setup(bot):
    await bot.add_cog(HelpCommand(bot))