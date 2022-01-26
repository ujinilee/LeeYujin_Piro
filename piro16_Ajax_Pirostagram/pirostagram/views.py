from django.shortcuts import render, redirect, get_object_or_404
from .models import *
from .forms import *

# Create your views here.

def ajax_list(request):
    posts = Post.objects.all()
    #form=CommentForm()
    ctx = {
        'posts': posts
        #{'form':form},
    }
    return render(request, 'ajax_list.html', ctx)



#from django.http import HttpResponse
#from django.http import JsonResponse
#from django.views.decorators.csrf import csrf_exempt
#import json
#from django.core import serializers
#from django.core.serializers.json import DjangoJSONEncoder

import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def like_ajax(request):
    req=json.loads(request.body) # json 임퐅, {'id':1, 'type':'like'} 파이썬 딕셔너리 형태로 변환하여 req변수에 담아준다
    post_id=req['id']
    button_type=req['type']

    post=Post.objects.get(id=post_id) #id가 1인 포스트를 찾아서 변수에 넣어준다

    post.save()

    return JsonResponse({'id':post_id, 'type':button_type})



@csrf_exempt
def write_comment(request):
    req = json.loads(request.body)
    id = req['id']
    type = req['type']
    content = req['content']

    post = Post.objects.get(id=id)
    comment = Comment.objects.create(post=post, content=content)
    comment.save()
    return JsonResponse({'id': id, 'type': type, 'content': content, 'comment_id': comment.id})


@csrf_exempt
def del_comment(request):
    req = json.loads(request.body)
    comment_id = req['id']

    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return JsonResponse({'id': comment_id})