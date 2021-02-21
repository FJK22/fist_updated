from django.db import models

# Create your models here.
class SlipSubmit(models.Model):
	email = models.EmailField("Email address (Optional)",blank=True, null=True)
	full_name = models.CharField("Your Full Name (Reporter's name) (Optional)",max_length = 120, blank=True, null=True)
	language_involved = models.CharField('Language(s) Involved',max_length = 120)
	where = models.CharField('Where did it happen?',max_length = 120, blank=True, null=True)
	topic = models.CharField('Nature/Topic of conversation (e.g. about homework, shopping, talking over the phone.)',max_length = 120, blank=True, null=True)
	intended_sentence = models.CharField('Intended sentence',max_length = 120)
	perceived_sentence = models.CharField('Perceived sentence',max_length = 120)
	speaker_info = models.CharField("Speaker's information: Sex, Age, Origin, Languages known (and their fluency)",max_length = 120)
	hearer_info = models.CharField("Hearer's information: Sex, Age, Origin, Languages known (and their fluency)",max_length = 120)
	realise_how = models.CharField("How did you realise the mishearing?",max_length = 120)
	other_info = models.CharField("Other information: Anything from.: Noise level, Speakers or Hearers have any particular accents, tiredness, echoy room...",max_length = 120)

	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	
	def __unicode__(self): # python 3.3 is __str__
		return str(self.timestamp)

# class SlipSubmit(models.Model):
# 	email = models.EmailField(blank=True, null=True)
# 	full_name = models.CharField(label="Your Name (Reporter's name) (Optional)",max_length = 120, blank=True, null=True)
# 	language_involved = models.CharField(label='Language(s) Involved',max_length = 120)
# 	where = models.CharField(label='Where did it happen?',max_length = 120, blank=True, null=True)
# 	topic = models.CharField(label='Nature/Topic of conversation (e.g. About homework, shopping, talking over the phone.)',max_length = 120, blank=True, null=True)
# 	intended_sentence = models.CharField(label='Intended sentence',max_length = 120)
# 	perceived_sentence = models.CharField(label='Perceived sentence',max_length = 120)
# 	speaker_info = models.CharField(label="Speaker's information: Sex, Age, Origin, Languages known (and their fluency)",max_length = 120)
# 	hearer_info = models.CharField(label="Hearer's information: Sex, Age, Origin, Languages known (and their fluency)",max_length = 120)
# 	realise_how = models.CharField(label="How did you realise the mishearing?",max_length = 120)
# 	other_info = models.CharField(label="Other information: Anything from.: Noise level, Speakers or Hearers have any particular accents, tiredness, echoy room...",max_length = 120)

# 	timestamp = models.DateTimeField(auto_now_add = True, auto_now = False)
# 	updated = models.DateTimeField(auto_now_add = False, auto_now = True)
	
# 	def __unicode__(self): # python 3.3 is __str__
# 		return str(self.timestamp)