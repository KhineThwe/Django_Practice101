from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from .forms import AuthorForm,BookForm
from .models import Author,Book
# Create your views here.

def home(request):
    context={}
    #return HttpResponse("Hello World!")
    return render(request,'index.html',context)
    
def author_list(request):
    # authors = Author.objects.all().order_by('id').values()
    authors = Author.objects.all().values()
    context = {"authors":authors}
    return render(request,'author_list.html',context)

def author_create(request):
    if request.method == 'POST':
        form = AuthorForm(request.POST)#takes as json type
        if form.is_valid():
            form.save()
            return redirect('list_author')
    else:
        form = AuthorForm()
    return render(request,'author_form.html',{'form':form,'action':'Create'})

def author_delete(request,id):
    Author.objects.get(id=id).delete()
    return redirect('list_author')

def author_update(request,id):
    if request.method == 'POST':
        author = Author.objects.get(id=id)
        form = AuthorForm(request.POST,instance=author)
        if form.is_valid():
            form.save()
            return redirect('list_author')   
    else:
        author = Author.objects.get(id=id)
        form = AuthorForm(instance=author)  
    return render(request,'author_form.html',{'form':form,'action':'Update'})

def book_list(request):
    #***
    books = Book.objects.select_related('author').all()
    context = {"books":books}
    return render(request,'book_list.html',context)

def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)#takes as json type
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request,'book_form.html',{'form':form,'action':'Create'})
 
def book_delete(request,id):
    Book.objects.get(id=id).delete()
    return redirect('book_list')
   
def student_list(request):
    return render(request,'student_list.html')

def course_list(request):
    return render(request,'course_list.html')