from django.shortcuts import render, get_object_or_404, redirect
from .models import Devtool, Idea
from .forms import IdeaForm, DevtoolForm
from django.http import JsonResponse ####AJAX

# Create your views here.

def idea_list(request):

    swideas = Idea.objects.all()
    ctx = {'swideas': swideas}

    return render(request, template_name='idea_list.html', context=ctx)

#######AJAX##########
def plus_interest(request):
    pk = request.POST.get('pk', None)
    idea = get_object_or_404(Idea, pk=pk)
    idea.idea_like += 1
    #print(idea.interest)
    idea.save()
    context = {'plus_interest': idea.idea_like}
    return JsonResponse(context)


def minus_interest(request):
    pk = request.POST.get('pk', None)
    idea = get_object_or_404(Idea, pk=pk)
    idea.idea_like -= 1
    #print(idea.interest)
    idea.save()
    context = {'minus_interest': idea.idea_like}
    return JsonResponse(context)
#######AJAX##########



def idea_detail(request,pk):
    swidea=Idea.objects.get(id=pk)
    dev=swidea.devtool ##
    ctx = {'swidea': swidea, 'dev':dev}
    return render(request, 'idea_detail.html',context=ctx)


    

def idea_new(request):
    if request.method=='POST':
        form=IdeaForm(request.POST, request.FILES) 
        if form.is_valid():
            swidea=form.save() 
            return redirect('swidea:idea_detail',pk=swidea.pk)

    else: 
        form=IdeaForm()
        ctx = {'form': form}
        return  render(request,'idea_edit.html',context=ctx)


def idea_edit(request, pk):
    swidea = get_object_or_404(Idea, pk=pk)
    if request.method == "POST":
        form = IdeaForm(request.POST, instance=swidea)
        if form.is_valid():
            swidea.save()
            return redirect('swidea:idea_detail', pk=swidea.pk)
    else:
        form = IdeaForm(instance=swidea)
    return render(request, 'idea_edit.html', {'form': form})


def idea_delete(request,pk):
    swidea = get_object_or_404(Idea, id=pk)
    swidea.delete()
    return redirect('swidea:idea_list')



def dev_list(request):

    swideas = Devtool.objects.all()
    ctx = {'swideas': swideas}

    return render(request, template_name='dev_list.html', context=ctx)



def dev_detail(request,pk):
    swidea=Devtool.objects.get(id=pk)
    ideas=Idea.objects.filter(devtool=pk)

    ctx = {'swidea': swidea, 'ideas':ideas}

    return render(request, 'dev_detail.html',context=ctx)




def dev_new(request):
    if request.method=='POST':
        form=DevtoolForm(request.POST) 
        if form.is_valid():
            swidea=form.save() 
            return redirect('swidea:dev_detail',pk=swidea.pk)

    else: 
        form=DevtoolForm()
        ctx = {'form': form}
        return  render(request,'idea_edit.html',context=ctx)




def dev_edit(request, pk):
    swidea = get_object_or_404(Devtool, pk=pk)
    if request.method == "POST":
        form = DevtoolForm(request.POST, instance=swidea)
        if form.is_valid():
            swidea.save()
            return redirect('swidea:dev_detail', pk=swidea.pk)
    else:
        form = DevtoolForm(instance=swidea)
    return render(request, 'dev_edit.html', {'form': form})




def dev_delete(request,pk):
    swidea = get_object_or_404(Devtool, id=pk)
    swidea.delete()
    return redirect('swidea:dev_list')

