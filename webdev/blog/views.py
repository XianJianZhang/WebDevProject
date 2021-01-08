from django.shortcuts import render

# Create your views here.
def homepage(request):
    return render(request, 'blog/home.html', context={'title':'Homepage'})

def about(request):
  return render(request, 'blog/about.html', context={'title':'About page'})

def design(request):
  return(render(request, 'blog/design.html', context={'title':'Design'}))