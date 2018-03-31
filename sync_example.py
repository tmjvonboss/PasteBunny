from PasteBunny.Client import SyncClient
from PasteBunny.Models import Paste
from PasteBunny.Constants import Privacy, Expiry, Format


# Create client, add username and password only to automatically generate a user key
c = SyncClient(
    dev_key="dev_key",
    username="user",
    password="pass"
)

# Create a Paste object
paste = Paste(
    code="Finally a library for Pastebin in Python 3 I like!\n3bunny5you",
    name="PasteBunnny test",
    _format=Format.NAN,
    expiry=Expiry.HOUR,
    privacy=Privacy.PUBLIC
)

# Actually create a paste on Pastebin
c.create_paste(paste)

# Print the url
print(paste.get_url())
