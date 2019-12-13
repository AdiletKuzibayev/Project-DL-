from django.contrib.auth import authenticate
from django.shortcuts import render, redirect, render_to_response

from django.template.context_processors import csrf
from django.contrib import auth
from django.contrib.auth.forms import UserCreationForm


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:
        username = request.POST.get('username',
                                    '')  # Directly from POST request
        # without using form as not as in comment form
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            args['login_error'] = "User doesn't exist"
            return render_to_response('login.html', args)
    else:
        return render_to_response('login.html', args)


def logout(request):
    auth.logout(request)
    return redirect('/')

def signup(request):
    args = {}
    args.update(csrf(request))
    args['form'] = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            email = form.cleaned_data.get('email')
            user = authenticate(username=username, password=raw_password, email=email)
            login(user)
            return redirect('/')

    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
    # if request.POST:
    #     newuser_form = UserCreationForm(request.POST)
    #     if newuser_form.is_valid():
    #         newuser_form.save()
    #         newuser = auth.authenticate(username=newuser_form.cleaned_data['username'],
    #                                     password=newuser_form.cleaned_data['password2'])
    #         auth.login(request, newuser)
    #         return redirect('/')
    #     else:
    #         args['form'] = newuser_form
    # return render_to_response('signup.html', args)

