from django.shortcuts import render

# Create your views here.

#from .forms import SlipSubmitForm
from .models import SlipSubmit
from .forms import SlipSubmitForm

def contribute(request):
	title= 'Slip Submission'
	title_align_center = True
	# if request.user.is_authenticated():
	# 	title = "My title %s" %(request.user)

	#title = 'My title'

	# add a form
	# print request
	# if request.method == 'POST':
	# 	print request.POST
	form = SlipSubmitForm(request.POST or None)

	context = {
	    "form":form,
	    "title":title,
	    "title_align_center":title_align_center,
	}

	if form.is_valid():
		# form.save()
		instance = form.save(commit=False)
		# full_name = form.cleaned_data.get("full_name")
		# if not full_name:
		# 	full_name = "New full name"
		# instance.full_name = full_name		# if not instance.full_name:
		# 	instance.full_name = 'Jason'
		instance.save()
		# print instance.email
		# print instance.timestamp
		# context = {
		# 'title': 'Thank you',
		# # 'form': form
		# }
		context = {
		'SubmittedTitle': 'Thank you',
		"title_align_center":title_align_center,
		# 'SubmittedMessage': 'Dear ' + form_full_name + ',' + '\n\nYour message has been submitted.\nWe will get back to you as soon as possible.\n\nBest wishes,\nThe SEAR team'
		# 'form': form
		'SubmittedMessage': 'Thank you for your contribution! Every slip counts, do keep them coming. \n\n When the next batch of submissions has been processed, we will notify you and openly acknowledge your submission.\n\nBest wishes,\nThe SEAR team'
		}

	# if request.user.is_authenticated() and request.user.is_staff:
	# 	# print (SignUp.objects.all())
	# 	# for nr, instance in enumerate(SignUp.objects.all()):
	# 	# 	print nr, instance.full_name
	# 	queryset = SlipSubmit.objects.all()
	# 	context = {
	# 		"queryset":queryset
	# 	}



	return render(request,"contribute.html",context)


