from PasteBunny.Client import AsyncClient
from PasteBunny.Models import Paste
from PasteBunny.Constants import Privacy, Expiry, Format
import asyncio

# Get event loop
loop = asyncio.get_event_loop()

# Initialize client
c = AsyncClient(
    dev_key="dev_key",
    username="user",
    password="pass"
)

# Login to generate user key
loop.run_until_complete(c.login())

# Create paste object
paste = Paste(
    code="Finally a library for Pastebin in Python 3 I like!\n3bunny5you",
    name="PasteBunnny test",
    _format=Format.NAN,
    expiry=Expiry.HOUR,
    privacy=Privacy.PUBLIC
)

# Actually creating a post on Pastebin
loop.run_until_complete(c.create_paste(paste))

# Close the session
loop.run_until_complete(c.close())

# Print the url
print(paste.get_url())
