from django import forms
from .models import *

class SocietyForm(forms.ModelForm):
    class Meta:
        model = Society
        fields = ['name', 'logo', 'address','state', 'city', 'www', 'email', 'phone']

class InstituteForm(forms.ModelForm):
    class Meta:
        model=Institute
        fields=['name','logo','address','state','city','pin','www','email','phone','society']

class DepartmentForm(forms.ModelForm):
    class Meta:
        model=Department
        fields=['name','email','phone','www','insitute']


#
class ProgramCategoryForm(forms.ModelForm):
    class Meta:
        model = ProgramCategoryy
        fields = ['name', 'acro_name']

class ProgramForm(forms.ModelForm):
    class Meta:
        model=Programm
        fields=['name','program_category']


class StreamForm(forms.ModelForm):
    class Meta:
        model=Streamm
        fields=['name','program_category','program']


class MainProgramForm(forms.ModelForm):
    class Meta:
        model=MainProgramm
        fields=['department','program_category','program','stream','duration']


class CommitteeForm(forms.ModelForm):
    class Meta:
        model=Committee
        fields=['name','acronym']

class DesignationForm(forms.ModelForm):
    class Meta:
        model=Designation
        fields=['name','acronym','description']

class OfficeBearersForm(forms.ModelForm):
    class Meta:
        model=OfficeBearerss
        fields=['name','photo','address','state','city','email','phone','designation','committee','societyy']