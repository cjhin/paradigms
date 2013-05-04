###############################################
# Ryan Shea & Charles Jhin
# CSE 30332 Programming Paradigms
# Final Project

import cherrypy 
import os.path
import fnmatch
from scripts import page_include


#get ip address of this machine and print it for debugging purposes
import socket
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("gmail.com",80))
print(s.getsockname()[0])
s.close()

cur_dir = os.path.dirname(os.path.abspath(__file__))
print cur_dir

###############################################
# Main Page
class homepage:
  def index(self):
    #add get_script functions and do HTML head. Also create header. 
    HTML = page_include.get_script()+'''
      <head>
        <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css" rel="stylesheet">
        <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js"></script>		 
      </head>

      <body style="background='background.bmp'">
		<!--<img src="/images/background.bmp"/>-->


        <div class="row-fluid" style="text-align:left; padding-left:20px; background-color:#188A00">
          <h1><font color="#D0D0D0">Swag</font></h1>
        </div>
    '''       
    #HTML Body
    #Loop through modules, call each using get_script 
    mod_count = 0
    for module in module_names:
        HTML += '<div class="span4" style="text-align:center; border-top-style:solid; border-radius:5px; border-color:#188A00; padding-bottom:10px">' #module
        HTML += '<div class = "row-fluid" style="text-align: center; background-color:#D0D0D0"><h2>'+module+'</h2></div>' #title
        HTML += '<script>HttpRequest("'+module+'")</script></div>'       #body
        mod_count += 1              
    HTML = HTML + '</body>'
    return HTML
  index.exposed = True

###############################################
# Import and Initialize all "modules" 
# TODO change this so that the modules are added dynamically based on some saved preferences or something
#
#   Ex:
#   root.'url' = 'package_name'.'module_class_name'()

# Import the list of desired modules
module_names = []
for filename in os.listdir('./modules'):
      if fnmatch.fnmatch(filename, '*.py') and filename not in('__init__.py'):
        filename = filename[:-3]
        module_names.append(filename)

root = homepage()

# Initialize all modules
for module in module_names:
	import_command = 'from modules import '+module
	exec import_command
	code = 'root.'+module+' = '+module+'.module_'+module+'()'
	exec code

###############################################
# Let's get this party started
if __name__ == '__main__':

	conf = {
		'global': {
			'server.socket_host': '0.0.0.0',
			'server.socket_port': 8001},
		'/': {
			'tools.staticdir.root': os.path.join(os.path.abspath(__file__))[:-13]},
		'/images': {
			'tools.staticdir.on': True,
			'tools.staticdir.dir': 'images/'}
	}

#	cherrypy.quickstart(root, config = os.path.join(os.path.dirname(__file__), 'conf.conf'))
	cherrypy.quickstart(root, '/', config = conf)
