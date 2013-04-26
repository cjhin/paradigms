import cherrypy, subprocess, shlex

###############################################
#
# Text-To-Speech Module
class module_tts:
    def __init__(self):
        self.speak = tts_speak()
    
    def index(self): #POST didn't work for some reason?
        return '''
            <p>Text to Speech!</p>
            <form action="tts/speak" method="GET"> 
                <textarea name="text" rows="10" cols="40"></textarea><br>
                <input type="submit" value="Speak!">
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
