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
                  <h4> >>> ps </h4>'''+output+'''
               '''
    index.exposed = True
