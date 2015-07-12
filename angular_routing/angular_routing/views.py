from django.shortcuts import render
from django.shortcuts import HttpResponse, HttpResponseRedirect, render_to_response
import json

def home_page(request):
	status = {"validation": "Hello this is test url", "status": True}
	return HttpResponse(json.dumps(status), content_type="application/json")