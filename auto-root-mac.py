#imports
#MACOS Version
import os
import time
import webbrowser
from colorama import Fore, Back, Style
from colorama import init
from colorama import init
#imports
#reset color
init(autoreset=True)
#reset color

#Core Def Steps
def agreement():
    os.system("clear")
    print(Style.BRIGHT+Back.BLACK+Fore.MAGENTA+"TERMS OF SERVICE:")
    print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"By Using AUTO ROOT v Magisk:")
    print(Style.BRIGHT+Back.BLACK+Fore.YELLOW+"I agree that if my device is damaged/bricked in any way, the devolper, Zevo, can not be held responsible.")
    print(Style.BRIGHT+Back.BLACK+Fore.RED+"Rooting/Installing TWRP can brick your phone if you do not use the correct version of TWRP for your Device!")
    print(Style.BRIGHT+Back.BLACK+Fore.CYAN+"PLEASE do research to find out if your Device is supported by TWRP!")

def menu():
    os.system("clear")
    print (39 * "-" , "Option" , 39 * "-")
    print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"1.First Time Installaltion (Reccomended)")
    print(Style.BRIGHT+Back.BLACK+Fore.BLUE+"2.Install TWRP on Device")
    print(Style.BRIGHT+Back.BLACK+Fore.MAGENTA+"3.Install MAGISK on device")
    print (40 * "-" , "Menu" , 40 * "-")


def fstart():
    os.system("clear")
    print (35 * "-" , "Instruction" , 35 * "-")
    print(Style.BRIGHT+Back.BLACK+Fore.YELLOW+"Please Do The Following")
    print(Style.BRIGHT+Back.BLACK+Fore.RED+"1.Make sure Bootloader is unlocked")
    print(Style.BRIGHT+Back.BLACK+Fore.RED+"2.Boot into FastMode")
    print(Style.BRIGHT+Back.BLACK+Fore.RED+"3.Rename your TWRP.img and TWRP.zip to 'auto-twrp.img' & 'auto-twrp.zip'")
    print(Style.BRIGHT+Back.BLACK+Fore.RED+"4.Rename your Magisk.zip to 'imagisk.zip'")
    print(Style.BRIGHT+Back.BLACK+Fore.YELLOW+"I agree to the terms and services, and have done the followig steps! [y/n]")
    print (40 * "-" , "Menu" , 40 * "-")




def flashTWRP():
        os.system("clear")
        print (40 * "-" , "Flashing TWRP" , 40 * "-")
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Flashing auto-twrp.img....")
        os.system("./fastboot boot auto-twrp.img")
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Watting for TWRP.IMG to load...")
        time.sleep(4)
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Should be done- if not wait.")
        time.sleep(2)
        print(Style.BRIGHT+Back.BLACK+Fore.RED+"TO INSTALL TWRP ON YOUR DEVICE:")
        print(Style.BRIGHT+Back.BLACK+Fore.RED+"TAP ON THE ADVANCED BUTTON, AND THEN ADB SIDELOAD")
        time.sleep(3)
        print (40 * "-" , "Flashing TWRP" , 40 * "-")
        print(Style.BRIGHT+Back.BLACK+Fore.YELLOW+"I have done this step [y/n]")

def installTWRP():
        os.system("clear")
        print (40 * "-" , "Installing TWRP" , 40 * "-")
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Installing auto-twrp.zip....")
        os.system("./adb sideload auto-twrp.zip")
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Watting....")
        time.sleep(4)
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Should be done- if not wait.")
        time.sleep(1)
        print(Style.BRIGHT+Back.BLACK+Fore.RED+"WHEN DONE DO NOT REBOOT SYSTEM!!")
        print(Style.BRIGHT+Back.BLACK+Fore.RED+"HIT BACK BUTTON, HIT REBOOT, THEN HIT RECOVERY")
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Watting to for phone to boot into twrp...")
        time.sleep(5)
        print(Style.BRIGHT+Back.BLACK+Fore.RED+"ONCE BOOTED INTO TWRP, TAP ON THE ADVANCED BUTTON, AND THEN ADB SIDELOAD AGAIN.")
        time.sleep(5)
        print (40 * "-" , "Installing TWRP" , 40 * "-")
        print(Style.BRIGHT+Back.BLACK+Fore.YELLOW+"I have done this step [y/n]")

def installMagisk():
    os.system("clear")
    if mLoad=="y":
        print (40 * "-" , "Installing Magisk" , 40 * "-")
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Flashing Magisk...")
        os.system("./adb sideload imagisk.zip")
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Watting to for Magisk to install on device...")
        time.sleep(5)
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"ONCE DONE, HIT REBOOT BACK INTO SYSTEM...")
        print (40 * "-" , "Installing Magisk" , 40 * "-")
        time.sleep(5)
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"NEXT DOWNLOAD AND INSTALL MAGISK.APK")
        print(Style.BRIGHT+Back.BLACK+Fore.GREEN+"Download link: https://magiskmanager.com/ ")
        webbrowser.open('https://magiskmanager.com/')
        print(Style.BRIGHT+Back.BLACK+Fore.MAGENTA+"Thank you for using Auto-Root")
#Core Def Steps


#Start on Option 1
agreement()
time.sleep(10)
menu()
sCheck=input()
if sCheck=="1":
    fstart()
    iCheck=input()
    if iCheck=="y":
        flashTWRP()
        sideLoad=input()
        if sideLoad=="y":
            installTWRP()
            mLoad=input()
            if mLoad=="y":
                installMagisk()
#Start on Option 1

#Start on Option 2
elif sCheck=='2':
        installTWRP()
        mLoad=input()
        if mLoad=="y":
            installMagisk()
#Start on Option 2

#Start on Option 3
elif sCheck=='3':
    installMagisk()
#Start on Option 3

#Invaild Option/Script Error
else:
    print("Program Aborted...")
    quit()
#Invaild Option/Script Error
