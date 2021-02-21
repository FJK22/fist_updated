from django.shortcuts import render
# from django.conf import settings
# from django.core.mail import send_mail
# Create your views here.

# from .forms import ContactForm, SignUpForm
# from .models import Explore


# from django.shortcuts import render

def explore(request):
	title= 'Explore FIST'

	context = {
		'title': title,
	}


	return render(request,"explore.html",{})






# def explore(request):
# 	title= 'Explore SLOE'
# 	# if request.user.is_authenticated():
# 	# 	title = "My title %s" %(request.user)

# 	#title = 'My title'

# 	# add a form
# 	# print request
# 	# if request.method == 'POST':
# 	# 	print request.POST
# 	form = SignUpForm(request.POST or None)

# 	context = {
# 	'title': title,
# 	'form': form
# 	}

# 	if form.is_valid():
# 		# form.save()
# 		instance = form.save(commit=False)
# 		# full_name = form.cleaned_data.get("full_name")
# 		# if not full_name:
# 		# 	full_name = "New full name"
# 		# instance.full_name = full_name		# if not instance.full_name:
# 		# 	instance.full_name = 'Jason'
# 		instance.save()
# 		# print instance.email
# 		# print instance.timestamp
# 		context = {
# 		'title': 'Thank you',
# 		# 'form': form
# 		}

# 	if request.user.is_authenticated() and request.user.is_staff:
# 		# print (SignUp.objects.all())
# 		# for nr, instance in enumerate(SignUp.objects.all()):
# 		# 	print nr, instance.full_name
# 		queryset = SignUp.objects.all()
# 		context = {
# 			"queryset":queryset
# 		}



# 	return render(request,"home.html",context)
