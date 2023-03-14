from django.shortcuts import render,redirect
from .models import Books
from django.contrib.auth.decorators import login_required,user_passes_test

# Create your views here.

def index(request):
    content={}
    content['data']=Books.objects.all()
    return render(request, 'index.html',content)




def insert_record(request):
    if request.method=='POST':
        x= request.POST['bname']
        y= request.POST['bauthor']
        z= request.POST['bdesc']
        l= request.POST['blink']
        b1= Books.objects.create(bname=x, bauthor=y, bdesc=z, blink=l)
        b1.save()
        return redirect('index')

    else:
        return render(request, 'insert_record.html')




def edit(request,rid):
    if request.method =='POST':
        x= request.POST['bname']
        y= request.POST['bauthor']
        z= request.POST['bdesc']
        l= request.POST['blink']
        b1=Books.objects.filter(id=rid)
        b1.update(bname=x, bauthor=y,bdesc=z,blink=l)     
        return redirect('index')
    else:
        content={}
        content['data']= Books.objects.get(id=rid)
        return render(request, 'manage.html',content)


def delete(request,rid):
    d= Books.objects.get(id=rid)
    d.delete()
    return redirect('index')
    