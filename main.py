import os
import sys
import asyncio
import requests
import nextcord
from nextcord.ext import commands
from asyncio_throttle.throttler import Throttler
from datetime import datetime, timedelta, timezone
from collections import deque, defaultdict
import re


BOT_TOKEN = os.getenv('DISCORD_TOKEN')
if not BOT_TOKEN:
    print("エラー: トークン入ってないよぉ")
    sys.exit(1)


intents = nextcord.Intents.default()
bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Botログイン完了: {bot.user}")
    await bot.change_presence(
    activity=nextcord.Activity(
        type=nextcord.ActivityType.watching,
        name="認証"
    )
)
    print("")


if __name__ == "__main__":
    try:
        print("=== Discord Bot 起動中 ===")
        token = os.getenv("DISCORD_TOKEN")
        if not token:
            print("トークンがなーい！")
            sys.exit(1)
        bot.run(token)
    except Exception as e:
        print(f"エラー発生: {e}")
    finally:
        print(" Bot終了:")
        sys.stdout.flush()
        sys.exit(0)
