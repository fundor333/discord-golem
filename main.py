import logging
import logging.handlers
import os

from discord import Intents
from discord.ext import commands
from dotenv import load_dotenv

logger = logging.getLogger("discord")
logger.setLevel(logging.INFO)

handler = logging.handlers.RotatingFileHandler(
    filename="discord.log",
    encoding="utf-8",
    maxBytes=32 * 1024 * 1024,  # 32 MiB
    backupCount=5,  # Rotate through 5 files
)
dt_fmt = "%Y-%m-%d %H:%M:%S"
formatter = logging.Formatter(
    "[{asctime}] [{levelname:<8}] {name}: {message}", dt_fmt, style="{"
)
handler.setFormatter(formatter)
logger.addHandler(handler)
handler = logging.StreamHandler()
handler.setFormatter(formatter)
logger.addHandler(handler)


load_dotenv()


def get_prefix(client, message):
    prefixes = ["=", "==", "$"]

    if not message.guild:
        prefixes = ["=="]
    return commands.when_mentioned_or(*prefixes)(client, message)


class Client(commands.Bot):
    def __init__(self):
        intents = Intents.default()
        intents.message_content = True
        super().__init__(
            command_prefix=get_prefix,
            intents=intents,
            help_command=commands.DefaultHelpCommand(dm_help=True),
        )

    async def setup_hook(self):  # overwriting a handler
        logging.info(f"Logged in as {client.user}")
        cogs_folder = f"{os.path.abspath(os.path.dirname(__file__))}/cogs"
        for filename in os.listdir(cogs_folder):
            if filename.endswith(".py"):
                await client.load_extension(f"cogs.{filename[:-3]}")
        await client.tree.sync()
        logging.info("Loaded cogs")


client = Client()
client.run(os.getenv("DISCORD_TOKEN"))
