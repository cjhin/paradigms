###############################################
# Ryan Shea & Charles Jhin
# CSE 30332 Programming Paradigms
# Final Project

import cherrypy 
import os.path
from scripts import page_include

###############################################
# Main Page
class homepage:
    def index(self):
		test_string = "Chas"
		HTML = page_include.get_script()+''' 
			<h1>Herro '''+test_string+''' prease!</h1>

			<div style="border:2px solid;">
				<script>HttpRequest("ls") /*puts the contents of "ls" into the main */</script>
			</div>
			<div style="border:2px solid;">
				<script>HttpRequest("ps")</script>
			</div>
			<div style="border:2px solid;">
				<script>HttpRequest("itunes")</script>
			</div>
			<div style="border:2px solid;">
				<script>HttpRequest("tts")</script>
			</div>
		'''
		return HTML
    index.exposed = True

###############################################
# Initialize all "modules" 
# TODO change this so that the modules are added dynamically based on some saved preferences or something
#
#   Ex:
#   root.'url' = 'package_name'.'module_class_name'()

from modules import ls, ps, itunes, tts

root = homepage()
root.ls = ls.module_ls()
root.ps = ps.module_ps()
root.itunes = itunes.module_itunes()
root.tts = tts.module_tts()

###############################################
# Let's get this party started
if __name__ == '__main__':
	cherrypy.quickstart(root, config = os.path.join(os.path.dirname(__file__), 'conf.conf'))
