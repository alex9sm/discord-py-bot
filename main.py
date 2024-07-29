import discord, os, aiosqlite
from discord.ext import commands
from discord import Interaction, app_commands
import dotenv
from dotenv import load_dotenv
from typing import Final
from utils.utils import random_proverb, sync_user
import logging
from initdb import init_db

logging.basicConfig(
     level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
 ) 

load_dotenv()
TOKEN: Final[str] = os.getenv('DISCORD_TOKEN')
print(TOKEN)

bot = commands.Bot(command_prefix="/", intents= discord.Intents.all())

@bot.event
async def on_ready():
    
    logging.info(f"Logged in as {bot.user.name}")
    activity = discord.CustomActivity(name="Meditating")
    status = discord.Status.online
    await bot.change_presence(status=status, activity=activity)
    await load_cogs()
    try:
        synced = await bot.tree.sync()
        logging.debug(f"Synced {len(synced)} commands")
    except Exception as e:
        logging.error(e)

async def load_cogs():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')

@bot.event                   
async def on_message(ctx: discord.Interaction):  
        await sync_user(ctx)
        
async def main():
    await init_db()
    await bot.start(TOKEN)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())