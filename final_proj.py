###############################################
# Ryan Shea & Charles Jhin
# CSE 30332 Programming Paradigms
# Final Project

import cherrypy 
from modules import ls, ps, itunes, tts


###############################################
# Main Page
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

###############################################
# Initialize all "modules"
#
# root.'url' = 'package_name'.'module_class_name'()

root = homepage()
root.ls = ls.module_ls()
root.ps = ps.module_ps()
root.itunes = itunes.module_itunes()
root.tts = tts.module_tts()

# configuration files, mainly for setting IPs and stuff
import os.path
tutconf = os.path.join(os.path.dirname(__file__), 'conf.conf')

if __name__ == '__main__':
	cherrypy.quickstart(root, config=tutconf)
