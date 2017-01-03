from django.shortcuts import render, render_to_response
from django.contrib.auth.decorators import login_required

def ping(request):
    "Health check for determining if the server is available"
    response_content = '<html><body>OK</body></html>'
    return HttpResponse(response_content, content_type='text/html')

@login_required()
def home(request):
	return render(request, 'home.html')