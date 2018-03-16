<p align="center">
  <h3 align="center">isMyPasswordVulnerable</h3>

  <p align="center">
    Securely find if your password appears in a huge password database.
  </p>
</p>
<br>
This software is inspired by [BY-jk/pwned](https://github.com/BY-jk/pwned). 

Type your password and it will be tested against [haveibeenpwned](https://haveibeenpwned.com/) huge list of vulnerable passwords.

This short script is written in Python, to encourage YOU to review it.

The password is NOT sent anywhere - see [Overview](#overview)

## Table of contents

- [Quick start](#quick-start)
- [Overview](#overview)
- [Prerequisites and Installing](#prerequisites-and-installing)
- [Author](#author)
- [License](#license)

## Quick start

In order to test your password(s):

- Clone the repo: `git clone https://github.com/shalommmitz/isMyPasswordKnown.git`
- Run the script: "python isMyPasswordKnown.py"
- At the prompt, enter a single password. 
In order to test additional passwords, re-run the program

## Overview

Here is how this script works:

- You enter your password
- A hash of the password is calculated. 
- Only a small part of the hash (the first 5 characters) is sent to the remote site
- The remote server sends back a list of full hashes, representing passwords from compromised sites.
- The full hash is locally compered to the returned hashes.
- If the full hash match one of the returned hashes, it it a good idea to replace your password, but it does not mean that your account was compromised. 

## Prerequisites and Installing

Python (either 2.x or 3.x) is needed.
You can get and install Python from the [Python Software Foundation](https://www.python.org/) 

No other installation is needed. Just get the repository.


## Author

**Shalom Mitz** - [shalommmitz](https://github.com/shalommmitz)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

