# Discord python bot

## Pre-requisites:
1. You've created a bot on the Discord dev page.

2. You've authorized the bot to read and send messages from the Discord dev page.

3. You've obtained your bot's api key from the Discord dev page.

4. You've added your bot to your server from the Discord user facing interface.

## Config
1. Clone repo `code`

    - From the directory you want to create the project in, run `git clone https://github.com/the-beckoning/discord_bot_template.git`

2. At the projects root directory, create a `.env` file

    - Assuming you are in the project directory, run `touch .env`

3. In the **environmental file**, make a variable called `API_KEY`
4. Set it equal to your api_key from your discord developer console (use quotations) `API_KEY='1234abcd...'`
5. In **main.py**, change the following lines as needed:
    
    Line 14 - Set the name of your server.

    Line 15 - Set the name of the channel (x1) you want the bot to connect to within the server.
    
    Line 30 - Change or disable the user facing login message.

    Lines 40 and 41 - You can comment this out to allow all channels to use the bot. Or, you can add a list with plaintext of allowed channels for the bot to use (i.e. `if message.channel.name not in ['channel_1', 'memes', 'news']:`).

    Lines 43 ans 44 - Add any users you want to be able to interact with your bot here. Any users not in the list will be ignored. Comment out to disable.

    Lines 50 to 61 - Add whatever commands you want here using the provided format in `main.py`.

    Lines 64 to 75 - Change the help message to fit the commands you've written. Remember that if a command is defined but not in the help message, it can still be accessed.

    Lines 79 and 80 - Change or disable the message for invalid commands being received.

## Notes
1. This script has a bunch of specific features such as ignoring users and channels, but if you run in to trouble, try disabling these.

2. I've used `!` as my command trigger, but you can change it for your bot if you need to.

    - I choose to include this in *Notes* rather than *Config* because this could cause conflict messages and goes against common practice, so proceed with caution.