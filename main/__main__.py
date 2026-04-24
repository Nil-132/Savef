import asyncio
import glob
import logging
import os
import sys
from pathlib import Path
from main.utils import load_plugins
from . import bot, userbot, Bot   # all three clients from __init__

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# -------------------------------------------------------------------
# Load plugins (remains at module level)
# -------------------------------------------------------------------
path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")


if __name__ == "__main__":
    # 1. Validate required environment variables EARLY
    required = ["API_ID", "API_HASH", "SESSION", "BOT_TOKEN"]
    missing = [v for v in required if not os.environ.get(v)]
    if missing:
        print(f"❌ Missing environment variables: {', '.join(missing)}")
        sys.exit(1)

    # 2. Start the Flask keep‑alive server
    from main.app import keep_alive
    keep_alive()
    print("Flask keep‑alive started.")

    # 3. Async runner for all clients
    async def main():
        # Start Telethon bot (needs explicit bot_token because it wasn't passed earlier)
        await bot.start(bot_token=os.environ['BOT_TOKEN'])

        # Start Pyrogram userbot (string session)
        await userbot.start()

        # Start Pyrogram bot (bot token already provided in Client initialization)
        await Bot.start()

        # Wait until all clients disconnect – keeps the event loop alive
        await asyncio.gather(
            bot.disconnected,
            userbot.disconnected,
            Bot.disconnected,
        )

    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped manually.")
