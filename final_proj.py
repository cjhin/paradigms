"""
Ryan Shea & Charles Jhin
CSE 30332 Programming Paradigms
Final Project
"""

import cherrypy, subprocess, shlex
from time import sleep

class homepage:
    def index(self):
		test_string = "Chas"
		HTML = ''' 
			<h1>Herro '''+test_string+''' prease!</h1>
            
			<h2>Modules:</h2>
            <ul>
                <li><a href='/ls/'>ls</a></li>
                <li><a href='/ps/'>ps</a></li>
				<li><a href='/itunes/'>iTunes (MacOSX)</a></li>
				<li><a href='/tts/'>Text-To-Speech (MacOSX)</a></li>
            </ul>'''
		return HTML
    index.exposed = True

class module_ls:
    def index(self):
		#subprocess.call(["ls", "-1"])	
		proc = subprocess.Popen("ls", stdout=subprocess.PIPE)
		output = proc.stdout.read()
		return '''
			<p>The output of ls is</p>'''+output+'''
			<p>[<a href="../">Return</a>]</p>
		'''
    index.exposed = True

class module_ps:
    def index(self):
		proc = subprocess.Popen("ps", stdout=subprocess.PIPE)
		# the following loop is required to make the terminal output show up in the browser with appropriate line breaks and stuff
		output = ""
		while True:
			line = proc.stdout.readline()
			if line != '':
				output += line + "<br>"
			else:
				break
	
		return '''
			<p>The output of ps is</p>'''+output+'''
			<p>[<a href="../">Return</a>]</p>
		'''
    index.exposed = True

###############################################
#
# iTunes Module
class module_itunes:
	def __init__(self):
		self.play = itunes_play()
		self.pause = itunes_pause()
		self.next = itunes_next()
		self.prev = itunes_prev()
		#other confirmed possible options:  mute, unmute, change volume, change playlist, 
		#      unconfirmed options:  play specific song, show library

		#TODO currently disabled because it was annoying when my iTunes was repeatedly brought to the front while coding
		#open iTunes if it isn't already open
		#command = """open -a iTunes"""
		#args = shlex.split(command)
		#proc = subprocess.Popen(args, stdout=subprocess.PIPE)
	
	def index(self):
		command = """osascript -e 'tell application "iTunes" to player state as string'"""
		args = shlex.split(command)
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		state = proc.stdout.readline()

		command = """osascript -e 'tell application "iTunes" to name of current track as string'"""
		args = shlex.split(command)
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		name = proc.stdout.readline()

		command = """osascript -e 'tell application "iTunes" to artist of current track as string'"""
		args = shlex.split(command)
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		artist = proc.stdout.readline()

		command = """osascript -e 'tell application "iTunes" to album of current track as string'"""
		args = shlex.split(command)
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		album = proc.stdout.readline()

		#TODO if the song changes this page wont update... is there some kind of listener? worse case we can do a manual refresh

		play_pause = ""
		if state.strip() == "playing":
			play_pause = "<li><a href='/itunes/pause'>pause</a></li>"
		else:
			play_pause = "<li><a href='/itunes/play'>play</a></li>"

		return '''
			<h2>iTunes:<br>Current Song:</h2>

			<p>'''+name+'''<br>'''+artist+'''<br>'''+album+'''</p>
            
			<h2>Sub-Modules:</h2>
            <ul>'''+play_pause+'''
                <li><a href='/itunes/next'>next</a></li>
                <li><a href='/itunes/prev'>prev</a></li>
            </ul>
			<p>[<a href="../">Return</a>]</p>
		'''
	index.exposed = True

class itunes_play:
	def index(self):
		command = """osascript -e 'tell application "iTunes" to play'"""
		args = shlex.split(command)
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		sleep(0.05) # allow itunes to update before the page is refreshed
		raise cherrypy.HTTPRedirect("../")
	index.exposed = True

class itunes_pause:
	def index(self):
		command = """osascript -e 'tell application "iTunes" to pause'"""
		args = shlex.split(command)
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		sleep(0.05) # allow itunes to update before the page is refreshed
		raise cherrypy.HTTPRedirect("../")
	index.exposed = True

class itunes_next:
	def index(self):
		command = """osascript -e 'tell application "iTunes" to next track'"""
		args = shlex.split(command)
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		sleep(0.05) # allow itunes to update before the page is refreshed
		raise cherrypy.HTTPRedirect("../")
	index.exposed = True

class itunes_prev:
	def index(self):
		command = """osascript -e 'tell application "iTunes" to previous track'"""
		args = shlex.split(command)
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		sleep(0.05) # allow itunes to update before the page is refreshed
		raise cherrypy.HTTPRedirect("../")
	index.exposed = True

###############################################
#
# Text-To-Speech Module
class module_tts:
	def __init__(self):
		self.speak = tts_speak()
	
	def index(self): #POST didn't work for some reason?
		return '''
			<p>Text to Speech!</p>
			<form action="speak" method="GET"> 
				<textarea name="text" rows="10" cols="40"></textarea><br>
				<input type="submit" value="Speak!">
			<form>
			<p>[<a href="../">Return</a>]</p>
		'''
	index.exposed = True

class tts_speak:
	def index(self, text = None):
		command = """say """+str(text)
		args = shlex.split(command)
		proc = subprocess.Popen(args, stdout=subprocess.PIPE)
		raise cherrypy.HTTPRedirect("../")
	index.exposed = True
	
###############################################
# initialize all "modules"
root = homepage()
root.ls = module_ls()
root.ps = module_ps()
root.itunes = module_itunes()
root.tts = module_tts()

# configuration files, mainly for setting IPs and stuff
import os.path
tutconf = os.path.join(os.path.dirname(__file__), 'conf.conf')

if __name__ == '__main__':
	cherrypy.quickstart(root, config=tutconf)
