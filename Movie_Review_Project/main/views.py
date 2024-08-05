from django.shortcuts import render, redirect
from .forms import MovieReviewForm
from .models import Movie_Review
from django.db.models import Q 
# Create your views here.

def home(request):
    form = MovieReviewForm()
    if request.method == 'POST':
        form = MovieReviewForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show')
    context = {"form": form}
    return render(request, 'main/index.html', locals())


def show(request):
    data = Movie_Review.objects.all()
    context = {"data":data}
    return render (request, "main/show.html", locals())

def delete(request, pk):
    obj = Movie_Review.objects.get(pk=pk)
    
    obj.delete()
    return redirect("show")
   
    
def update(request, pk):
    obj = Movie_Review.objects.get(pk=pk)
    form = MovieReviewForm(instance=obj)
    if request.method == 'POST':
        form = MovieReviewForm(request.POST, instance=obj)
        if form.is_valid():
            form.save()
            return redirect("show")
    return render (request, "main/index.html", locals())

def search(request):
    name = request.GET.get('query')
    mov = Movie_Review.objects.all()
    data = mov.filter(Q(MovieTitle__icontains=name))
    context = {'data': data}
    return render (request, "main/show.html", locals())
    

def search1(request):
    return render (request, "main/search.html", locals())