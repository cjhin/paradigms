import cherrypy, subprocess, shlex
from time import sleep

###############################################
#
# iTunes Module
#

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
