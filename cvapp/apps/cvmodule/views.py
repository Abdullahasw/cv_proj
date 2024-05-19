from django.shortcuts import render,redirect
from apps.cvmodule import views
def index(request):
# render the appropriate template for this request
#just another comment
 return render(request, 'cvmodule/index.html')

def imag(request):
    #redirect('/')#go to the main one
    return render(request, 'cvmodule/imag.html')

def book(request,bId):
    #return redirect("/")
    book={'id':12,'title':'mynewbook','auther':'abdullah'}
    book={'id':34,'title':'myoldbook','auther':'abdullah(old)'}
    targetbook=None
    if book['id']==bId:targetbook=book
    if book['id']==bId:targetbook=book
    
    if targetbook==None: return redirect("/imag")
    context={'book':targetbook}
    return render(request,'cvmodule/book.html',context)