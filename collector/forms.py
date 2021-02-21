from django import forms

from .models import SlipSubmit


	# email = models.EmailField(blank=True, null=True)
	# full_name = models.CharField(max_length = 120, blank=True, null=True)
	# language_involved = models.CharField(max_length = 120)
	# where = models.CharField(max_length = 120, blank=True, null=True)
	# topic = models.CharField(max_length = 120, blank=True, null=True)
	# intended_sentence = models.CharField(max_length = 120)
	# perceived_sentence = models.CharField(max_length = 120)
	# speaker_info = models.CharField(max_length = 120)
	# hearer_info = models.CharField(max_length = 120)
	# realise_how = models.CharField(max_length = 120)
	# other_info = models.CharField(max_length = 120)

class SlipSubmitForm(forms.ModelForm):
	class Meta:
		model = SlipSubmit
		fields = ['intended_sentence',
		          'perceived_sentence',
		          'language_involved',
		          'where',
		          'topic',
		          'speaker_info',
		          'hearer_info',
		          'realise_how',
		          'other_info',
		          'full_name',
		          'email'
		          ]
		# exclude = ['full_name'] use sparingly

	# def clean_email(self):
	# 	email = self.cleaned_data.get('email')
	# 	# email_base, provider = email.split("@")
	# 	# domain, extension = provider.split(".")
	# 	# if not domain == 'USC':
	# 		# raise forms.ValidationError("please use USC email")
	# 	# if not extension == "edu":
	# 	# 	raise forms.ValidationError("Please use a valid college email address")
	# 	return email

	# def clean_full_name(self):
	# 	full_name = self.cleaned_data.get('full_name')
	# 	return full_name
		
