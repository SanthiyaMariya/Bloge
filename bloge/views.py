from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
from .models import Post,Content
import logging
from django.http import Http404
from django.core.paginator import Paginator
from .forms import ContactForm
import logging

# Configure logging
logging.basicConfig(level=logging.DEBUG)
      
# posts=[ 
#         {'id':1,'title':'post 1','content':'this is the first post'},
#         {'id':2,'title':'post 2','content':'this is the second post'},
#         {'id':3,'title':'post 3','content':'this is the third post'},
#         {'id':4,'title':'post 4','content':'this is the fourth post'}
#         
#     ]
       

def index(request):
    latest_name='Latest post'
    post =Post.objects.all()

    #pagination
    paginator= Paginator(post,4) # 4 is how many posts in the page
    page_number=request.GET.get('page')
    page_obj=paginator.get_page(page_number)


    return render(request, 'bloge/index.html',{'latest_name':latest_name,'page_obj':page_obj})  #rendering the index.html page with the context data

def detail(request, post_id):
  # post=next((item for item in post if item['id']==int(post_id)),None)
   
  # logger=logging.getLogger('texting')
  # logger.debug(f'post variables are {post}')
    try:
        post = Post.objects.get(slug=post_id)
        related_post=Post.objects.filter(category=post.category).exclude(pk=post.id)
    except Post.DoesNotExist:
        raise Http404("Post does not exist")

    return render(request, 'bloge/detail.html', {'post': post,'related_post':related_post})
  

def contact(request):
    if request.method=='POST':
       form=ContactForm(request.POST)
       name=request.POST.get('name')
       email=request.POST.get('email')
       message=request.POST.get('message')


       logger=logging.getLogger('testing')
       if form.is_valid():
          
           logger.debug(f'POST data is{ form.cleaned_data['name']}  {form.cleaned_data['email']} {form.cleaned_data['message']}' )
           success_msg="email has been sent successfully !"
           return render(request,'bloge/contact.html',{'form':form,'success_msg':success_msg})



       else:
           logger.debug('Form validation failure')
           return render(request,'bloge/contact.html',{'form':form,'name':name,'email':email,'message':message})   
    return render(request,'bloge/contact.html')


def about(request):

    about=Content.objects.first().content
    return render(request,'bloge/about.html',{'about':about})



