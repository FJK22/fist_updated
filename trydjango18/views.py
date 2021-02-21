from django.shortcuts import render

def about(request):
	return render(request,"about.html",{})

def citations(request):
	return render(request,"citations.html",{})

def fistresearch(request):
	return render(request,"fist.research.html",{})

def resources(request):
	return render(request,"resources.html",{})
