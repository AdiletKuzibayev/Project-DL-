from django.core.exceptions import ObjectDoesNotExist
from django.core.paginator import Paginator
from django.http import Http404, HttpResponseRedirect
from django.shortcuts import render, render_to_response, redirect

# Create your views here.
from .models import Questions


def questions(request):
    questions = Questions.objects.all()
    context = {
        'question':questions
    }
    if request.method == 'POST':
        return render(request,'schedule.html',context)
    else:
        return render(request,'schedule.html',context)

def show_completed(request): #show completed task only
    questions = Questions.objects.filter(completed=True)
    context = {
        'question': questions
    }
    return render(request, 'questionary.html', context)

def show_active(request):   #show active task list
    questions = Questions.objects.filter(completed=False)
    context = {
        'question': questions
    }
    return render(request, 'index.html', context)
def clear_completed(request):    #Delete the completed tasks
    Questions.objects.filter(completed=True).delete()
    questions = Questions.objects.all()
    context = {
        'question': questions
    }
    return render(request, 'questionary.html', context)

def save_state(request):
     pass
# def questions(request):
#     try:
#         if str(article_id) in request.COOKIES:
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#         else:
#             article = Article.objects.get(id=article_id)
#             article.article_likes += 1
#             article.save()
#             response = redirect('/')
#             response.set_cookie(str(article_id), 'test')
#             return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
#     except ObjectDoesNotExist:
#         raise Http404
#     return render_to_response('questionary.html', args)