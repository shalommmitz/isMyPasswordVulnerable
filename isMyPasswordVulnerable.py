#!/usr/bin/env python
 
import os
import sys
import hashlib
import requests
 
pythonVersion = sys.version_info[0]

# Get password
if pythonVersion==2:
    password = raw_input("Enter password (WILL BE DISPLAYED) > ")
elif pythonVersion==3:
    password = input("Enter password (WILL BE DISPLAYED) > ")
    password = password.encode('utf-8')
else:
    print("Unsupported Python version")
    sys.exit()

# Create hash of password
hash = hashlib.sha1(password).hexdigest().upper()

# Create the partialHash: The partial hash is NOT enough to deduce the password
partialHash = hash[:5]
 
# Create the URL that will be sent the remote site, using ONLY the partialHash
url = "https://api.pwnedpasswords.com/range/"+ partialHash
# The only communication w/the remote site: send the partialHash
#    and get a list of hashes that match the partialHash
#    Note: the remote site does not know if your full hash is included in this list
tmpList = requests.get(url).text.split("\n")
knownHashes = [ partialHash + h.split(":")[0] for h in tmpList ]
 
# We check LOCALLY if your full hash is one of the hashes returned by the remote site
#   The site will never know.
if hash in knownHashes:
    print("Password was found in the pawned password list")
else:
    print("Password was NOT found in the pawned password list")
