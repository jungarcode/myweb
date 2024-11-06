from django.shortcuts import render,get_object_or_404,redirect
from django.core import paginator
from django.http.response import Http404
from .models import Post,Category
# from django.db.models import Q
from django.core.paginator import Paginator
# from .forms import ContactForm
# from django.core.mail import EmailMessage


# Create your views here.
def home(request):
    # queryset = request.GET.get('search')
    posts= Post.objects.filter(state = True)
    # if queryset:
    #     posts= Post.objects.filter(Q(titulo__icontains=queryset)| Q(descripcion__icontains=queryset)).distinct()
    #     return redirect('/about/?ok')
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    posts= paginator.get_page(page)
    return render(request,'index.html',{'posts':posts})

def detailPost(request,slug):
    try:
        post= Post.objects.get(slug=slug)
        return render(request, 'post.html',{'detail_post':post})
    except Post.DoesNotExist:
        raise Http404

def about(request):
    # queryset = request.GET.get('search')
    posts= Post.objects.filter(state= True)
    # if queryset:
    #     posts= Post.objects.filter(
    #         Q(titulo__icontains=queryset)| 
    #         Q(descripcion__icontains=queryset),
    #         estado=True,)
            # category = Category.objects.get(nombre__iexact = 'ABOUT'),).distinct()
    paginator = Paginator(posts,3)
    page = request.GET.get('page')
    posts= paginator.get_page(page)
    # contact_form = ContactForm()
    # if request.method == "POST":
    #     contact_form = ContactForm(data=request.POST)
    #     if contact_form.is_valid():
    #         name=request.POST.get('name','')
    #         email=request.POST.get('email','')
    #         contact=request.POST.get('contact','')

    #         email=EmailMessage("Messege of App Django","user Name {} with email addres {} write me :\n\n {}".format(name,email,contact),"",["datajun2806@gmail.com"],reply_to=[email])
    #         try:
    #             email.send()
    #             return redirect('/about/?ok')
    #         except:
    #             return redirect('/about/?fail')
            
                
            
    return render(request,'about.html',{'posts':posts})

def blog(request):
    # queryset = request.GET.get('search')
    posts= Post.objects.filter(state = True, categories = Category.objects.get(name = "Blog"))
    # if queryset:
    #     posts= Post.objects.filter(
    #         Q(titulo__icontains=queryset)| 
    #         Q(descripcion__icontains=queryset),
    #         estado=True,
    #         categoria= Category.objects.get(nombre__iexact = 'BLOG'),).distinct()
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    posts= paginator.get_page(page)
    return render(request,'blog.html',{'posts':posts})

def portfolio(request):
    # queryset = request.GET.get('search')
    posts= Post.objects.filter(state = True,categories = Category.objects.get(name = "Portfolio"))
    # if queryset:
    #     posts= Post.objects.filter(
    #         Q(titulo__icontains=queryset)| 
    #         Q(descripcion__icontains=queryset),
    #         estado=True,
    #         categoria= Category.objects.get(nombre__iexact = 'PORTFOLIO'),).distinct()
    paginator = Paginator(posts,6)
    page = request.GET.get('page')
    posts= paginator.get_page(page)
    return render(request,'portfolio.html',{'posts':posts})

