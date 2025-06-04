from django.shortcuts import render

# Create your views here.
def blogs(request):
    return render(request, 'blog/blogs.html')