import os
import discord
from discord.ext import commands
from yeelight import Bulb

TOKEN = os.environ.get(
    "MTA5MzQyNjQ4MDYxMDAyMTQ0OA.GFw3nd.-xk8ZQY92mhyaPOWu2tFl9yocPUlaaygBCgVgE"
)
bulb_ip = os.environ.get("BULB_IP")

# "192.168.86.81"

intents = discord.Intents.default()
intents.messages = True
intents.message_content = True
bot = commands.Bot(command_prefix="$", intents=intents)

bulb = Bulb(bulb_ip)


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
