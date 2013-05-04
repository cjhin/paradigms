import cherrypy, subprocess, shlex

###############################################
#
# Text-To-Speech Module
class module_tts:
    def __init__(self):
        self.speak = tts_speak()
    
    def index(self): #POST didn't work for some reason?
        return '''
            <h4>Text to Speech</h4>
            <form action="tts/speak" method="GET"> 
                <textarea name="text" rows="10" cols="10"></textarea><br>
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
