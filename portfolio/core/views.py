from django.shortcuts import render
from django.views.generic import TemplateView
from core.models import About, Service, RecentWork, Client, Skill, ProjectCategory

# Create your views here.
class HomeTemplateView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['about'] = About.objects.first()
        context['services'] = Service.objects.all()
        context['works'] = RecentWork.objects.all()
        context['client'] = Client.objects.all()
        context['skills'] = Skill.objects.all()
        context['projectcategory'] = ProjectCategory.objects.all()


        # print(context)
        return context

