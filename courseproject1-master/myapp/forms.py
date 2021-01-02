from django import forms
from .models import CourseForm
class CourseDataForm(forms.ModelForm):
    class Meta:
        model = CourseForm
        fields = '__all__'
'''
class CourseDataForm(forms.Form):
    course_name = forms.CharField(
        label="Enter your course name",
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Course Name'
            }
        )       
    )
    course_provider_name = forms.CharField(
        label="Enter your course provider name",
        widget=forms.ImageInput(
            attrs={
            'class':'form-control',
            'placeholder':'Course Provider name'
            }
        )       
    )
    image_representing_course = forms.ImageField(
        label="Enter your image representing course",
        widget=forms.ImageInput(
            attrs={
            'class':'form-control',
            'placeholder':'Image representing course'
            }
        )       
    )
    iconimage_course_provider = forms.ImageField(
        label="Icon image of the course Provider",
        widget=forms.ImageInput(
            attrs={
            'class':'form-control',
            'placeholder':''
            }
        )       
    )
    category = forms.CharField(
        label="Enter your category",
        widget=forms.TextInput(
            attrs={
            'class':'form-control',
            'placeholder':'Category Name'
            }
        )       
    )
    start_date = forms.DateField(
        label="Enter your start date",
        widget=forms.DateInput(
            attrs={
            'class':'form-control',
            'placeholder':'Start date'
            }
        )       
    )
    end_date = forms.DateField(
        label="Enter your end date",
        widget=forms.DateInput(
            attrs={
            'class':'form-control',
            'placeholder':'End date'
            }
        )       
    )
##
'''