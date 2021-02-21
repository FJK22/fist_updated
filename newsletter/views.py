from django.shortcuts import render
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.

from .forms import ContactForm, SignUpForm
from .models import SignUp


def home(request):
	title= 'Newsletter Sign Up'
	subtitle= 'Sign up to our newsletter for updates of the FIST Project!'
	# if request.user.is_authenticated():
	# 	title = "My title %s" %(request.user)

	#title = 'My title'

	# add a form
	# print request
	# if request.method == 'POST':
	# 	print request.POST
	form = SignUpForm(request.POST or None)

	context = {
	'title': title,
	'subtitle':subtitle,
	'form': form
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
		context = {
		'title': 'Thank you',
		# 'form': form
		}

	if request.user.is_authenticated() and request.user.is_staff:
		# print (SignUp.objects.all())
		# for nr, instance in enumerate(SignUp.objects.all()):
		# 	print nr, instance.full_name
		queryset = SignUp.objects.all()
		context = {
			"queryset":queryset
		}



	return render(request,"home.html",context)

def contact(request):
	title = 'Contact Us'
	title_align_center = True

	form = ContactForm(request.POST or None)

	context = {
	    "form":form,
	    "title":title,
	    "title_align_center":title_align_center,
	}


	if form.is_valid():
		# for key,value in form.cleaned_data.iteritems():
		# 	print key,value
			# print form.cleaned_data.get(key)
		form_email = form.cleaned_data.get("email")
		form_message = form.cleaned_data.get("message")
		form_full_name = form.cleaned_data.get("full_name")

		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = [from_email]
		contact_message = "%s: %s via %s"%(
			form_full_name,form_message,form_email)

		send_mail(subject, contact_message, from_email, to_email, fail_silently = False)
		# print email,message,full_name

		context = {
		'SubmittedTitle': 'Thank you',
		"title_align_center":title_align_center,
		'SubmittedMessage': 'Dear ' + form_full_name + ',' + '\n\nYour message has been submitted.\nWe will get back to you as soon as possible.\n\nBest wishes,\nThe FIST team'
		# 'form': form
		}




	return render(request, "forms.html", context)
