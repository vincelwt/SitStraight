import rumps
from subprocess import Popen, PIPE

#rumps.debug_mode(True)

defaultTimeout = 60*10

def notif(sender):
	print 'Sending notification'
	cmd = b"""display notification "Come on' man" with title "Dude, sit straight" subtitle "" """
	Popen(["osascript", '-'], stdin=PIPE, stdout=PIPE).communicate(cmd)

@rumps.clicked("Enable reminders")
def onoff(sender):
	sender.state = not sender.state
	if not sender.state:
	 	global_namespace_timer.stop()
	else:
	 	global_namespace_timer.start()

@rumps.clicked("About")
def about(_):
	rumps.alert("SitStraight is an experiment by Lyser.io\nGive a star on https://github.com/vincelwt/sitstraight")

if __name__ == "__main__":
	global_namespace_timer = rumps.Timer(notif, defaultTimeout)

	# Manually create the button to force default state
	button = rumps.MenuItem("Enable reminders")
	onoff(button)

	rumps.App('SitStraight', menu=(button, 'About')).run()

