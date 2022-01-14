from django.shortcuts import render, redirect, get_object_or_404
from .models import Review
from .forms import PostForm 

# Create your views here.
def review_list(request):
    review=Review.objects.all()
    ctx={'review':review}
    return render(request, template_name='review_list.html',context=ctx)


def review_detail(request,pk):
    review=Review.objects.get(id=pk)
    ctx={'review':review}
    return render(request,template_name='review_detail.html',context=ctx)



def review_create(request):
    if request.method=='POST':

        form=PostForm(request.POST) 
        if form.is_valid():
            review=form.save() 
            return redirect('review:review_list') ##post앱에서 list란 이름을 가진 곳으로 url이동

    else:
        form=PostForm()
        ctx={'form':form} ##폼 객체 매핑 후 렌더링

        return render(request,template_name='post_form.html', context=ctx) #템플릿 이름 항상 같게


def review_update(request, pk): 

    review=get_object_or_404(Review,id=pk)

    if request.method=='POST':
        form=PostForm(request.POST, instance=review)
        if form.is_valid:
            review=form.save()
            return redirect('review:detail',pk)


    else: 
        form=PostForm(instance=review) ##view->템플릿에 보낸다. 내용을 담았으니깐
        ctx={'form':form}

        return render(request,template_name='post_form.html',context=ctx)

        ##form 객체를 보여준다 post_form.html

def review_delete(request,pk):
    review = get_object_or_404(Review, id=pk)
    review.delete()
    return redirect('review:review_list')