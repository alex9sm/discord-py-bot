import random
from initdb import SessionLocal, User, init_db
import discord

async def random_proverb():
    proverbs = ["事实胜于雄辩", "一言既出，驷马难追", "路遥知马力，日久见人心", "无规矩不成方圆", 
                "惩前毖后", "三思而后行", "冰冻三尺，非一日之寒", "人心齐，泰山移", 
                "只要功夫深，铁杵磨成针", "老骥伏枥，志在千里", "吃得苦中苦，方为人上人", "不能一口吃成胖子",
                "爱不是占有，而是欣赏", "萝卜青菜，各有所爱", "爱屋及乌", "情人眼里出西施", "有情饮水饱，无情食饭饥"]
    return random.choice(proverbs)

async def sync_user(ctx: discord.Interaction):
    db = SessionLocal()
    try:
        user = db.query(User).filter(User.discord_id == int(ctx.author.id)).first()
        if not user:
            new_user = User(name=str(ctx.author.name), discord_id=int(ctx.author.id), points=1)
            db.add(new_user)
            db.commit()
        else: 
            user.points += 1
            db.commit()
    finally:
        db.close()
        
async def get_points(points: int, ctx: discord.Interaction):
    db = SessionLocal()
    user = db.query(User).filter(
        User.id == ctx.user.id
        )
    print(f'{user.points}')