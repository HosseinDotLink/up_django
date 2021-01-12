from django import forms

from .models import message, project

class sendMessageForm(forms.ModelForm):
    class Meta:
        model = message
        fields = ('msg_body',)


class addProjectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ('prj_title',)


class editProjectForm(forms.ModelForm):
    class Meta:
        model = project
        fields = ('prj_title',)