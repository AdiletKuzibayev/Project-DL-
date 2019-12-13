from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from django.template.context_processors import csrf
from django.contrib import auth

from .models import Student, Comment, Teacher
from .forms import CommandForm

def subjects(request, page_number=1):
    all_subjects = Student.objects.all()
    current_page = Paginator(all_subjects, 10)
    return render_to_response('subjects.html', {'students': current_page.page(page_number),
                                                'username': auth.get_user(request).username})


def subject(request, student_id=1, teacher_id=1):
    command_form = CommandForm()
    args = {}
    args.update(csrf(request))  # Type of hackers attack
                                # Подделка данных
                                # Protected from attacks Create
                                # Token that consist unique characters
    args['teacher'] = Teacher.objects.get(id = teacher_id)
    args['student'] = Student.objects.get(id = student_id)
    args['comments'] = Comment.objects.filter(comment_subject_id=student_id)
    args['form'] = command_form
    args['username'] = auth.get_user(request).username
    return render_to_response('subject.html', args)

def addmark(request, student_id=1):
    try:
        if str(student_id) in request.COOKIES:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            form = CommandForm(request.POST)
            if form.is_valid():
                student = form.save(commit=False)
                student.teacher_mark = Student.objects.get(id=student_id)
                form.save()
                request.session.set_expiry(60)  # session exists 60 seconds
                request.session['pause'] = True
<<<<<<< HEAD
<<<<<<< HEAD
            return redirect('/subjects/get/%s/' % student_id)
=======
            return redirect('/user/get/%s/' % student_id)
>>>>>>> parent of 430dda8... Downloading
=======
            return redirect('/user/subjects/get/%s/' % student_id)
>>>>>>> parent of 34c64c1... asd
            response = redirect('/')
            response.set_cookie(str(student_id), 'test')
    except ObjectDoesNotExist:
        raise Http404
<<<<<<< HEAD
<<<<<<< HEAD
    return redirect('/subjects/get/%s/' % student_id)
=======
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
>>>>>>> parent of 430dda8... Downloading
=======
    return redirect('/user/subjects/get/%s/' % student_id)
>>>>>>> parent of 34c64c1... asd

def addFeedback(request, student_id):
    if request.POST and ("pause" not in request.session):
        form = CommandForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Student.objects.get(id=student_id)
            form.save()
            request.session.set_expiry(60) # session exists 60 seconds
            request.session['pause'] = True
<<<<<<< HEAD
<<<<<<< HEAD
    return redirect('/subjects/get/%s/' % student_id)
=======
    return redirect('/user/get/%s/' % student_id)
>>>>>>> parent of 430dda8... Downloading
=======
    return redirect('/user/subjects/get/%s/' % student_id)
>>>>>>> parent of 34c64c1... asd
