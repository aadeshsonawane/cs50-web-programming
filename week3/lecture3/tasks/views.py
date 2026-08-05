from django.http import HttpResponseRedirect
from django.shortcuts import render
from django import forms
from django.urls import reverse

# Create your views here.
class NewTaskForm(forms.Form):
    task = forms.CharField(label="New Task")
    priority = forms.IntegerField(label="Priority", min_value=1, max_value=10)
tasks = []
def index(request):
    if "tasks" not in request.session:
        request.session["tasks"] = []
    return render(request, 'tasks/index.html',{
        "tasks": request.session["tasks"]
    })

def add(request):
    if request.method == "POST":
        form = NewTaskForm(request.POST)
        if form.is_valid():
            task = form.cleaned_data["task"]
            priority = form.cleaned_data["priority"]
            request.session["tasks"] += [f"{task} - {priority}"]
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, 'tasks/add.html',{
                "form": form
            })
    return render(request, 'tasks/add.html',{
        "form": NewTaskForm()
    })