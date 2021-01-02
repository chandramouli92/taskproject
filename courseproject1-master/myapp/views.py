from django.shortcuts import render
from .models import CourseForm
from .forms import CourseDataForm
from django.http import HttpResponse
#GET----->GETTING EMPTY  FORM
#POST---->POSTING DATA INTO DATABASE
def course_view(request):
    if request.method == "POST":
        form = CourseDataForm(request.POST)
        if form.is_valid():
            course_name=request.POST.get('course_name')
            course_provider_name=request.POST.get('course_provider_name')
            image_representing_course=request.POST.get('image_representing_course')
            iconimage_course_provider=request.POST.get('iconimage_course_provider')
            category=request.POST.get('category')
            start_date=request.POST.get('start_date')
            end_date=request.POST.get('end_date')

            data = CourseForm(
                course_name=course_name,
                course_provider_name=course_provider_name,
                image_representing_course=image_representing_course,
                iconimage_course_provider=iconimage_course_provider,
                category=category,
                start_date=start_date,
                end_date=end_date,
            )
            data.save()
            coursedata1 = CourseForm.objects.all()
            return render(request,'coursedata.html',{'coursedata1':coursedata1})

        else:
            return HttpResponse('Invalid form')

    else:
        form = CourseDataForm()
        return render(request,'coursedata.html',{'form':form})



