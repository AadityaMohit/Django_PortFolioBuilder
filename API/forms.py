from django import forms
from django.forms import formset_factory

class PortfolioForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100)
    experience = forms.CharField(label='Experience', widget=forms.Textarea)
    image = forms.ImageField(label='Image')
    achievements = forms.CharField(label='Achievements', widget=forms.Textarea, required=False)
    contact_number = forms.CharField(label='Contact Number', max_length=15, required=False)
    contact_email = forms.EmailField(label='Contact Email', required=False)
    linkedin = forms.CharField(label='linkedin', widget=forms.Textarea, required=False)
    github = forms.CharField(label='github', widget=forms.Textarea, required=False)



class SkillForm(forms.Form):
    skill = forms.CharField(label='Skill', max_length=100)

SkillFormSet = formset_factory(SkillForm, extra=1)

class ProjectImageForm(forms.Form):
    project_image = forms.ImageField(label='Project Image')
    project_url = forms.URLField(label='Project URL', required=False)

ProjectImageFormSet = formset_factory(ProjectImageForm, extra=1)

class TemplateChoiceForm(forms.Form):
    template_choice = forms.ChoiceField(choices=[('template1', 'Template 1'), ('template2', 'Template 2'),('template3', 'Template 3')], widget=forms.RadioSelect)
