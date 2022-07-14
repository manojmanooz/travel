from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import movie
from . forms import movieform
# Create your views here.
def movies(request):
    obj=movie.objects.all()
    return render(request,'movie.html',{'value':obj})
def detail(request,movie_id):
    obj1=movie.objects.get(id=movie_id)
    return render(request,'details.html',{'detail':obj1})
def add_movie(request):
    if request.method == 'POST':
        name=request.POST.get('name',)
        desc=request.POST.get('desc',)
        year=request.POST.get('year',)
        img=request.FILES['img']
        obj=movie(name=name,decs=desc,year=year,img=img)
        obj.save()
    return render(request,'add_movie.html')
def update(request,id):
    obj=movie.objects.get(id=id)
    form=movieform(request.POST or None,request.FILES,instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':obj})
def delete(request,id):
    if request.method == 'POST':
        obj=movie.objects.get(id=id)
        obj.delete()
        return redirect('/')
    return render(request,'delete.html')

