# work around to include the javascript needed to include the modules in the main page

# effectively the script below uses AJAX to create a function called HttpRequest(url)
# that will include the contents of url in your current HTML page
def get_script():
	script= '''
	<script type="text/javascript">
		function HttpRequest(url){
			var pageRequest = false //variable to hold ajax object
			/*@cc_on
			   @if (@_jscript_version >= 5)
				  try {
				  pageRequest = new ActiveXObject("Msxml2.XMLHTTP")
				  }
				  catch (e){
					 try {
					 pageRequest = new ActiveXObject("Microsoft.XMLHTTP")
					 }
					 catch (e2){
					 pageRequest = false
					 }
				  }
			   @end
			@*/

			if (!pageRequest && typeof XMLHttpRequest != 'undefined')
			   pageRequest = new XMLHttpRequest()

			if (pageRequest){ //if pageRequest is not false
			   pageRequest.open('GET', url, false) //get page synchronously 
			   pageRequest.send(null)
			   embedpage(pageRequest)
		   }
		}

		function embedpage(request){
			//if viewing page offline or the document was successfully retrieved online (status code=2000)
			if (window.location.href.indexOf("http")==-1 || request.status==200)
			   document.write(request.responseText)
		}
	</script>
	'''
	return script
