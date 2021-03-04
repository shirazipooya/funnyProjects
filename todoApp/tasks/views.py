from django.shortcuts import render

from .models import Task
from .forms import TaskForm

# Create your views here.


def index(request):
    tasks = Task.objects.all()
    form = TaskForm()
    context = {'tasks': tasks, 'form': form}
    return render(request=request,
                  template_name='tasks/list.html',
                  context=context)
