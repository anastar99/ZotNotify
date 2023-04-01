import discord



def start_monitoring(code):
    """
    The embed for when the bot starts monitoring a code
    """
    embed = discord.Embed(
        title = f'Started Monitoring: {code}   Notify Button',
        description= 'Click the Notify button to be pinged when class is available',
        colour= discord.Colour.blue()
        )
    embed.set_footer(text='UCI SOC MONITOR')

    return embed

# add copy code mechanism