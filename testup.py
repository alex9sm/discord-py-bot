from initdb import User, SessionLocal, init_db
from discord.ext import commands
import discord

async def get_user(ctx: discord.Interaction) -> None:
    db = SessionLocal()
    user = db.query(User).filter(User.discord_id == int(ctx.author.id)).first()
    print(user.points)
    
async def create_user(name: str, discord_id: int):
    db = SessionLocal()
    new_user = User(name=name, discord_id=discord_id)
    db.add(new_user)
    db.commit()

async def update_user(id: int, new_name: str) -> None:
    db = SessionLocal()
    user = db.query(User).filter(
        User.id == id,
        ).first()
    user.name = new_name
    db.commit() 
    
async def main(ctx):
    await get_user(ctx)
    
if __name__ == "__main__":
    import asyncio
    asyncio.run(main())
    
