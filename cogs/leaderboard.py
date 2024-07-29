import os, discord, asyncio
from discord import app_commands
from discord.ext import commands
from utils.utils import sync_user, get_points
import logging
from initdb import User, SessionLocal, init_db

class AddUserCommand(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @app_commands.command(name="leaderboard", description="shows the points leaerboard")
    async def get_leaderboard(self, ctx: discord.Interaction) -> None:
        db = SessionLocal()
        user = db.query(User).filter(User.discord_id == int(ctx.user.id)).first()
        await ctx.response.send_message(f"you have {user.points} points")

async def setup(bot):
    await bot.add_cog(AddUserCommand(bot))