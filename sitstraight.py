import rumps
from subprocess import Popen, PIPE

class SitStraight(rumps.App):

	@rumps.clicked("Enable reminders")
	def onoff(self, sender):
		sender.state = not sender.state

	@rumps.clicked("Test notification")
	def sayhi(self, _):
		cmd = b"""display notification "Come on' man" with title "Dude, sit straight" """
		Popen(["osascript", '-'], stdin=PIPE, stdout=PIPE).communicate(cmd)
		
		rumps.notification("Hey! Are you sitting straight?!", "I thought so", None, True, "Yes", "Nop..")

	@rumps.clicked("About")
	def prefs(self, _):
		rumps.alert("SitStraight is an experiment by Lyser.io")

if __name__ == "__main__":
	SitStraight("SitStraight").run()
