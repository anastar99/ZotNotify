import discord
import pyperclip



def start_monitoring(course_data):
    """
    The embed for when the bot starts monitoring a code
    """
    embed = discord.Embed(
        title = f'Started Monitoring: {course_data}',
        # description= 'Click the Notify button to be pinged when class is available',
        colour= discord.Colour.blue()
        )
    embed.set_footer(text='UCI SOC MONITOR')
    # embed.add_field(name='Course Title', value=course_data['course_name'])
    embed.add_field(name='Web Reg', value='[link](https://www.reg.uci.edu/registrar/soc/webreg.html)')
    embed.set_thumbnail(url='https://cdn.create.vista.com/api/media/small/470855628/stock-vector-anteater-blue-gradient-vector-icon')


    return embed

def class_open(course_data):
    """
    Embed for when class is open
    """
    embed = discord.Embed(
        title = f'Open: {course_data["code"]}',
        # description=f'[Webreg](https://www.reg.uci.edu/registrar/soc/webreg.html)',
        colour = discord.Colour.blue()
    )
    embed.set_footer(text=f'UCI SOC MONITOR')
    embed.add_field(name='Course Title', value=course_data['dept_section'].capitalize())
    embed.add_field(name='Open Spots', value=int(course_data['required'])-int(course_data['enrolled']))
    embed.add_field(name='Web Reg', value='[link](https://www.reg.uci.edu/registrar/soc/webreg.html)')
    embed.set_thumbnail(url='https://cdn.create.vista.com/api/media/small/470855628/stock-vector-anteater-blue-gradient-vector-icon')
    return embed

def class_waitlist(course_data):
    """
    Embed for when class is watilisted
    """
    embed = discord.Embed(
        title = f'Wailist Available: {course_data["code"]}',
        # description=f'[Webreg](https://www.reg.uci.edu/registrar/soc/webreg.html)',
        colour = discord.Colour.blue()
    )
    embed.set_footer(text='UCI SOC MONITOR')
    embed.add_field(name='Course Title', value=course_data['dept_section'].capitalize())
    embed.add_field(name='Waitlist Count', value=course_data['waitlist'])
    embed.add_field(name='Web Reg', value='[link](https://www.reg.uci.edu/registrar/soc/webreg.html)')
    embed.set_thumbnail(url='https://cdn.create.vista.com/api/media/small/470855628/stock-vector-anteater-blue-gradient-vector-icon')

    return embed

# add copy code mechanism







