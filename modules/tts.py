import cherrypy, subprocess, shlex

###############################################
#
# Text-To-Speech Module
class module_tts:
    def __init__(self):
        self.speak = tts_speak()
    
    def index(self): #POST didn't work for some reason?
        return '''
            <form action="tts/speak" method="GET"> 
                <textarea name="text" rows="5" cols="12" placeholder="Text to be spoken goes here"></textarea><br>
                <input type="submit" value="Speak!" class="btn">
            <form>
        '''
    index.exposed = True

class tts_speak:
    def index(self, text = None):
        command = """say """+str(text)
        args = shlex.split(command)
        proc = subprocess.Popen(args, stdout=subprocess.PIPE)
        raise cherrypy.HTTPRedirect("../../")
    index.exposed = True
