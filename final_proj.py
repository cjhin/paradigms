###############################################
# Ryan Shea & Charles Jhin
# CSE 30332 Programming Paradigms
# Final Project

import cherrypy 
import os.path
import fnmatch
from scripts import page_include

colors = ['B0F5FF','FFD5AF']

module_names = []
for filename in os.listdir('./modules'):
      if fnmatch.fnmatch(filename, '*.py') and filename not in('__init__.py','itunes.py'):
        filename = filename[:-3]
        module_names.append(filename)

###############################################
# Main Page
class homepage:
  def index(self):
    #add get_script functions and do HTML head
    HTML = page_include.get_script()+'''
      <head>
        <link href="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/css/bootstrap-combined.min.css" rel="stylesheet">
        <script src="//netdna.bootstrapcdn.com/twitter-bootstrap/2.3.1/js/bootstrap.min.js"></script>		    
        <h1 style="text-align: center"> THINK OF A KICKASS TITLE </h1>
      </head>

      <body>
    '''        
    #HTML Body
    #Loop through modules, call each using get_script 
    mod_count = 0
    for module in module_names:
        HTML = HTML + '<div class = "row-fluid" style="text-align: center; background-color:#'+colors[mod_count%len(colors)]+'">'
        HTML = HTML + '<script>HttpRequest("'+module+'")</script></div>'       
        mod_count += 1              
    HTML = HTML + '</body>'
    return HTML
  index.exposed = True

###############################################
# Initialize all "modules" 
# TODO change this so that the modules are added dynamically based on some saved preferences or something
#
#   Ex:
#   root.'url' = 'package_name'.'module_class_name'()
#from modules import ls,ps,itunes,tts

for module in module_names:
    code = 'from modules import '+module
    exec code

root = homepage()

for module in module_names:
    code = 'root.'+module+' = '+module+'.module_'+module+'()'
    exec code

###############################################
# Let's get this party started
if __name__ == '__main__':
	cherrypy.quickstart(root, config = os.path.join(os.path.dirname(__file__), 'conf.conf'))
