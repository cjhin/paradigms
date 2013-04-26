import subprocess

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
        '''
    index.exposed = True
