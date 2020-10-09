from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Course
# Create your views here.
def index(request):

    allcourse = {}
    categoryLanguages = Course.objects.values('category', 'id')
    languages = {item['category'] for item in categoryLanguages}
    for language in languages:
        lang = Course.objects.filter(category=language)
        allcourse.update({language:[item for item in lang]})
    params = {'lang':allcourse}
    return render(request,  'rm/index.html', params)
def searchMatch(query , item):
    if query in  item.course_name.lower() or query in  item.brief_desc.lower():
        return True
    else:
        return False    

def search(request):
    query = request.GET.get('search')

    allcourse = {}
    categoryLanguages = Course.objects.values('category', 'id')
    languages = {item['category'] for item in categoryLanguages}
    for language in languages:
        langtem = Course.objects.filter(category=language)
        lang = [item for item in langtem if searchMatch(query,item)]
        if len(lang)!= 0:
            allcourse.update({language:[item for item in lang]})
    params = {'lang':allcourse, 'msg':""}
    if len(allcourse) == 0 or len(query)<3:
        params = {'msg':"No Result Found!!! Please Try Again"}

    return render(request,  'rm/search.html', params)

def display(request,category):
    course = Course.objects.filter(category=category)
    params = {'courses':course}
    return render(request, 'rm/display.html', params)


def about(request):
    return render(request,'rm/about.html')



def course(request):
    return HttpResponse("course") 

def save(request,id):
    course = Course.objects.get(id=id)
    course.status = not course.status
    course.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))    
    # return redirect('/rm/')

def learn_more(request,id):
    course = Course.objects.get(id=id)

    params = {'courses':course}
    return render(request, 'rm/learn_more.html', params)

def saved(request):
    course = Course.objects.filter(status=True)
    params = {'course':course}
    return render(request, 'rm/saved.html', params)