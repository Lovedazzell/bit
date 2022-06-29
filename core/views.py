from django.shortcuts import render
from django.views.generic.base import TemplateView
from django_celery_results.models import TaskResult

# Create your views here.



class Profile(TemplateView):
    template_name = 'core/dashboard.html'

    def get_context_data(self,**kwargs):
        context = super().get_context_data(**kwargs)
        data = TaskResult.objects.latest('date_created')
        print(data.result)
        print('review data ',data)
        context['task_id'] = data.task_id
        return context

