from django.shortcuts import render, redirect

from item.models import Category, Item

from .forms import SignupForm

def index(request):
    items= Item.objects.filter(is_sold=False)[0:6]
    categories=Category.objects.all()

    return render(request, 'core/index.html',{
        'items': items,
        'categories': categories,

    })
def chat(request):
    return render(request, "core/chat.html")

def career(request):
    return render(request, 'core/career.html')

def ecourses(request):
    return render(request, 'core/ecourses.html')

def pathwaytoempl(request):
    return render(request, 'core/pathwaytoempl.html')

def becomeaseller(request):
    return render(request, 'core/becomeaseller.html')

def internships(request):
    return render (request, 'core/internships.html')


def termsofuse(request):
    return render(request, 'core/termsofuse.html')


def socialmedia(request):
    return render(request, 'core/socialmedia.html')


def about(request):
    return render(request, 'core/about.html')


def privacypolicy(request):
    return render(request, 'core/privacypol.html')

def contact(request):
    return render(request, 'core/contact.html')

def buscollaboration(request):
    return render(request, 'core/buscollaboration.html')

def signup(request):
    if request.method=='POST':
        form=SignupForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = SignupForm()

    return render(request, 'core/signup.html',{
        'form': form,
    })
