from django.shortcuts import render, get_object_or_404, redirect
from .models import Devtool, Idea
from .forms import IdeaForm

# Create your views here.

def idea_list(request):

    swideas = Idea.objects.all()
    ctx = {'swideas': swideas}

    return render(request, template_name='idea_list.html', context=ctx)


def idea_detail(request,pk):
    swidea=get_object_or_404(Idea,pk=pk)
    ctx = {'swidea': swidea}
    return render(request, 'idea_detail.html',context=ctx)

def idea_new(request):
    if request.method=='POST':
        form=IdeaForm(request.POST) 
        if form.is_valid():
            #poster=request.FILES.get('poster')
            #Idea.idea_image=poster
            swidea=form.save() 

            return redirect('swidea:idea_detail')

    else: 
        form=IdeaForm()
        ctx = {'form': form}
        return  render(request,'idea_edit.html',context=ctx)