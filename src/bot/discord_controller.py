import os
import discord
from discord.ext import commands
from yeelight import Bulb

TOKEN = os.environ.get("DISCORD_TOKEN")
print(TOKEN)
BULB_IP = os.environ.get("BULB_IP")
print(BULB_IP)
# "192.168.86.81"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

bulb = Bulb(BULB_IP)


@bot.event
async def on_ready():
    print(f"We have logged in as {bot.user}")


@bot.command()
async def on(ctx):
    bulb.turn_on()
    await ctx.send("Turning Yeelight on.")


@bot.command()
async def off(ctx):
    bulb.turn_off()
    await ctx.send("Turning Yeelight off.")


if __name__ == "__main__":
    bot.run(TOKEN)
