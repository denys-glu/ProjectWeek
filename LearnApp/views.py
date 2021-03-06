from django.shortcuts import render, redirect
from login.models import User
from .models import Reading, Student
from django.contrib import messages

def index(request):
    context = {
        "user": User.objects.get(id = request.session['user_id'])
    }
    return render(request, "parent_home.html", context)


def st_patty_page(request):
    student = Student.objects.all()
    context = {
                'student': student[0]
    }
    return render(request, "short1.html", context)

def earth_page(request):
    student = Student.objects.all()
    context = {
                'student': student[0]
    }
    return render(request, 'earth.html', context)

def history(request):
    student = Student.objects.all()
    context = {
                'student': student[0]
    }
    return render(request, 'history.html', context)

def gov_quiz(request):
    student = Student.objects.all()
    context = {
                'student': student[0]
    }
    return render(request,'gov_quiz.html', context)

def white_house(request):
    student = Student.objects.all()
    context = {
                'student': student[0]
    }
    return render(request, 'white_house_quiz.html', context)

def declaration(request):
    student = Student.objects.all()
    context = {
                'student': student[0]
    }
    return render(request, 'declaration.html', context)

def student_info(request):
    our_user = User.objects.get(id=request.session['user_id'])
    context = {
                'user': our_user
    }
    return render(request, 'student_info.html', context)

def add_student(request, user_id):
    our_user = User.objects.get(id=user_id)
    Student.objects.create(
                            name = request.POST['name'],
                            user = our_user,
                            grade = request.POST['grade']
    )
    return redirect('/platform/student_info')

def delete_student(request, student_id):
    our_student = Student.objects.get(id=student_id)
    our_student.delete()
    return redirect('/platform/student_info')


def account_info(request):
    user_id = request.session['user_id']
    if request.method == 'POST':
        user = User.objects.get(id=user_id)
        user.name= request.POST['name']
        user.email = request.POST['email']
        user.password = request.POST['password']
        user.confirm_password = request.POST['confirm_password']
        user.save()
        return redirect('/platform/account_info')
    else:
        context = {
            'our_user': User.objects.get(id=user_id)
        }
        return render(request, "accountinfo.html", context)

def generic_validator(request):
    reading = Reading.objects
    errors = getattr(reading, request.POST['validator'])(request.POST)

    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value, extra_tags=key)
        # redirect back to short1.html
        return redirect(f'/platform/{request.POST["validator"]}_page#form')
        # redirect to Good job page.
    return redirect('/platform/success')

def hands_on(request):
    student = Student.objects.all()
    context = {
                'student': student[0]
    }
    return render(request, 'hands_on.html', context)

def success(request):
    return render(request,'success.html')
