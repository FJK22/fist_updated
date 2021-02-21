from django.contrib import admin

# Register your models here.
from .forms import SlipSubmitForm
from .models import SlipSubmit


class SlipSubmitAdmin(admin.ModelAdmin):
	list_display = ["__unicode__","timestamp","updated"] # ,"timestamp","updated"
	form  = SlipSubmitForm
	# class Meta:
	# 	model = SignUp

admin.site.register(SlipSubmit, SlipSubmitAdmin)