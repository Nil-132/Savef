import glob
from pathlib import Path
from main.utils import load_plugins
import logging
from . import bot
from . import app  # <-- Relative import is correct

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# Start the web server in a background thread
app.keep_alive()

path = "main/plugins/*.py"
files = glob.glob(path)
for name in files:
    with open(name) as a:
        patt = Path(a.name)
        plugin_name = patt.stem
        load_plugins(plugin_name.replace(".py", ""))

print("Successfully deployed!")

if __name__ == "__main__":
    bot.run_until_disconnected()
