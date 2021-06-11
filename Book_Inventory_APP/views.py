from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from .models import Books
from .forms import BooksForm
from django.template import Context
    
def index(request):
    emp = Books.objects.all()
    return render(request,'dashboard.html',{'emp':emp})

def AddBookform(request):
    context ={} 
    form =  BooksForm(request.POST or None, request.FILES or None) 
    if form.is_valid(): 
        form.save() 
    context['form']= form 
    return render(request, 'create_book.html',context,{'form':form})

def addBook(request):
    if (request.method=="GET"):
        form  = BooksForm()
        return render(request,'create_book.html',{"form":form})
    else:
        #save code
        form = BooksForm(request.POST)
        if form.is_valid():  
            try:  
                form.save()                                    
            except:  
                pass  
        return redirect(index)

def edit(request,id):  
    if(request.method == "GET") :
        d = Books.objects.get(id=id)                
        return render(request,'edit.html',{'emp':d})
    
    elif(request.method == "POST"):
        id = request.POST.get("id")
        d = Books.objects.get(id=id) 
        form = BooksForm(request.POST, instance = d)  
        if form.is_valid():  
            form.save()  
        return redirect(index)

def delete(request,id):
    d = Books.objects.filter(id=id)
    d.delete()    
    return redirect(index)
