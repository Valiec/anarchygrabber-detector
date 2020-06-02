import platform
import os
import sys

goodstr = "module.exports = require('./core.asar');"

badstrs = ["4n4rchy", "inject", "hook", "modDir"]

def get_all_versions(dirs):
	versions = []
	for dir in dirs:
		if dir.startswith("0"):
			versions.append(dir)
	return versions
			

def check_version(path, name):
	with open(path+"/modules/discord_desktop_core/index.js") as f:
		content = f.read()
		badcount = 0	
		for badstr in badstrs:
			if badstr in content:
				badcount+=1
		if badcount>0:
			print("DANGER: Discord "+name+" is likely INFECTED with AnarchyGrabber, "+str(badcount)+" signatures found!")
		elif content == goodstr:
			print("SUCCESS: Discord "+name+" is OK, no traces of AnarchyGrabber found!")
		else:
			print("WARNING: Discord "+name+" index.js content unknown. If you do not have a modified client, this may be an AnarchyGrabber infection!")


def check_discord(path, name):
	dirs = os.listdir(path)
	versions = get_all_versions(dirs)
	for version in versions:
		print("Version is "+version)
		check_version(path+"/"+version, name)
	
		

osname = platform.system()

discordbase = ""

if osname == "Darwin":
	homedir = os.path.expanduser("~")
	discordbase = homedir+"/Library/Application Support"
	print("OS is Mac OS X")

elif osname == "Windows":
	homedir = os.path.expanduser("~")
	discordbase = homedir+"/AppData/Roaming"
	print("OS is Windows")

else:
	print("This tool does not currently support "+osname+"!")
	sys.exit(1)

print("Checking for Discord Stable...")
if os.path.exists(discordbase+"/discord"):
	print("Discord found at "+discordbase+"/discord")
	check_discord(discordbase+"/discord", "Stable")
else:
	print("Discord Stable not found.")

print("\nChecking for Discord PTB...")
if os.path.exists(discordbase+"/discordptb"):
	print("Discord found at "+discordbase+"/discordptb")
	check_discord(discordbase+"/discordptb", "PTB")
else:
	print("Discord PTB not found.")

print("\nChecking for Discord Canary...")
if os.path.exists(discordbase+"/discordcanary"):
	print("Discord found at "+discordbase+"/discordcanary")
	check_discord(discordbase+"/discordcanary", "Canary")
else:
	print("Discord Canary not found.")	

