from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context_processors import csrf
from django.contrib import auth

from .models import Student, Comment, Teacher
from .forms import  StudentForm, CommandForm


def students(request, page_number=1):
    all_subjects = Student.objects.all()
    current_page = Paginator(all_subjects, 10)
    return render_to_response('students.html', {'students': current_page.page(page_number),
                                                'username': auth.get_user(request).username})


def student(request, student_id=1, teacher_id=1):
    add_mark = StudentForm()
    args = {}
    args.update(csrf(request))  # Type of hackers attack
                                # Подделка данных
                                # Protected from attacks Create
                                # Token that consist unique characters
    args['teacher'] = Teacher.objects.get(id = teacher_id)
    args['student'] = Student.objects.get(id = student_id)
    args['comments'] = Comment.objects.filter(comment_subject_id=student_id)
    args['form'] = add_mark
    args['username'] = auth.get_user(request).username
    return render_to_response('student.html', args)

def addmark(request, student_id=1, teacher_mark = 0):
    try:
        if str(student_id) in request.COOKIES:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            form = StudentForm(request.POST)
            if form.is_valid():
                student = Student.objects.get(id=student_id)
                student.teacher_mark = form.teacher_mark
                form.save()
                request.session.set_expiry(60)  # session exists 60 seconds
                request.session['pause'] = True
            return redirect('/user/subjects/get/%s/' % student_id)
            response = redirect('/')
            response.set_cookie(str(student_id), 'test')
    except ObjectDoesNotExist:
        raise Http404
    return redirect('/user/subjects/get/%s/' % student_id)

def addFeedback(request, student_id=1):
    if request.POST and ("pause" not in request.session):
        form1 = CommandForm(request.POST)
        if form1.is_valid():
            comment = form1.save(commit=False)
            comment.comment_text = Student.objects.get(id=student_id)
            form1.save()
            request.session.set_expiry(60) # session exists 60 seconds
            request.session['pause'] = True
    return redirect('/user/subjects/get/%s/' % student_id)
