from django.core.exceptions import ObjectDoesNotExist
from django.db.models import Q
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.template.context_processors import csrf
from django.template.loader import get_template
from django.template import Context
from django.shortcuts import render_to_response
from django.contrib import auth
from django.core.paginator import Paginator
from django.views.decorators.csrf import csrf_exempt

from .forms import CommandForm
from .models import Article, Commands
# Create your views here.

def articles(request, page_number=1):
    search_query = request.GET.get("search_field", '')
    if search_query:
        all_articles = Article.objects.filter(Q(article_title__icontains=search_query) |
                                              Q(article_text__icontains=search_query))
    else:
        all_articles = Article.objects.all()
    current_page = Paginator(all_articles, 2)
    return render_to_response('articles.html', {'articles': current_page.page(page_number),
                                                'username': auth.get_user(request).username})


def article(request, article_id=1):
    command_form = CommandForm
    args = {}
    args.update(csrf(request))  # Type of hackers attack
                                # Подделка данных
                                # Protected from attacks Create
                                # Token that consist unique characters
    args['article'] = Article.objects.get(id=article_id)
    args['comments'] = Commands.objects.filter(comments_article_id=article_id)
    args['form'] = command_form
    args['username'] = auth.get_user(request).username
    return render_to_response('article.html', args)

def addlike(request, article_id, page_number=1):
    try:
        if str(article_id) in request.COOKIES:
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
        else:
            article = Article.objects.get(id=article_id)
            article.article_likes += 1
            article.save()
            response = redirect('/')
            response.set_cookie(str(article_id), 'test')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
    except ObjectDoesNotExist:
        raise Http404
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def addcomment(request, article_id):
    if request.POST and ("pause" not in request.session):
        form = CommandForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.comments_article = Article.objects.get(id=article_id)
            form.save()
            request.session.set_expiry(60) # session exists 60 seconds
            request.session['pause'] = True
    return redirect('/articles/get/%s/' % article_id)


@csrf_exempt
def search(request):
    try:
        if request.method == "POST":
            article_text = request.POST.get("search_field")
            if len(article_text) > 0:
                search_res = Article.objects.filter(article_text__contains=article_text)
            return render(request, "search.html", {"search_res": search_res, "empty_res": "There is no article"})
    except:
        return render(request, "search.html", {"empty_res": "There is no article"})
