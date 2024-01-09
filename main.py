if __name__ == '__main__':
    # Import the api key from .env where .env is at directory root and API_KEY is the key's variable
    from dotenv import load_dotenv
    import os
    load_dotenv()  # Load the .env file
    api_key = str(os.getenv('API_KEY'))


    ## Import modules for discord bot
    import discord
    from discord.ext import commands

    # Set the bot's destination
    server_name = 'SERVER_NAME' # Put the EXACT server name as a string here, tells the bot where to connect
    channel_name = 'general' # Prevents bot from connecting to every channel in the server
    
    # Prepare bot to connect
    intents = discord.Intents.all() # Says the bot can do everything Discord dev page bot permission list
    client = commands.Bot(command_prefix="!", intents=intents) # Initialize bot

    # Make the connection
    @client.event
    async def on_ready():
        guild = discord.utils.get(client.guilds, name=server_name)
        
        if guild:
            print(f"DEBUG: Connected to server {guild.name}")
            channel = discord.utils.get(guild.channels, name=channel_name)  # Try finding channel directly
            if channel:
                await channel.send("BOT STATUS UPDATE: Bot is now online!")
                print(f"DEBUG: Sent logon message to  '{channel.name}' channel")

    # Main loop of code
    @client.event # When something is sent in the server
    async def on_message(message):

        if message.author == client.user: # If the message is from the bot
            return  # Ignore to prevent responding to itself
        
        if message.channel.name != channel_name: # If message not received in target channel
            return # Ignore

        if str(message.author) not in ['']: # Control the users allowed to interact with bot
            return # Ignore because user is not in allow list

        command = message.content # Makes the received message more readable to humans

        if command and command[0] == "!": # See if message is a command or just text (indicated by '!')
            # Block of received commands and actions
            if message.content == "!online":
                await message.channel.send("Yes, I am online!")
            elif message.content == "!time":
                import datetime
                current_time = datetime.datetime.now()
                time_neat = current_time.strftime("%I:%M:%S %p")
                await message.channel.send(f"It is {time_neat}")
            elif message.content == "!joke":
                import time
                await message.channel.send("Why did the chicken cross the road?")
                time.sleep(2)
                await message.channel.send("To get to the other side!")
            elif message.content == "!help":
                help_msg = '''
                Commands you can run:

            1️⃣ Basic commands

                ➡️ !online - view if the bot is online
                ➡️ !time - outputs the current time
                ➡️ !joke - tells a joke
                ➡️ !help - shows this menu
                
            2️⃣ Other commands

                No other commands have been specified
                '''
                await message.channel.send(help_msg)
            else: # No defined command typed, so shows help
                await message.channel.send(f"I'm sorry, but I don't know what '{message.content}' means!")
                await message.channel.send(f"Try running '!help' to see available commands.")

    # Run the bot
    client.run(api_key)