from django.db import IntegrityError
from django.views import generic
from django.http import HttpResponseRedirect
from django.urls import reverse
from .parser.parser import parse_dev_by
from .models import Employers


def parse(request):
    result = parse_dev_by('https://companies.dev.by')
    for line in result:
        company_info = Employers(
            employer=line['name'],
            email=line['email'],
            site=line['site']
        )
        try:
            company_info.save()
        except IntegrityError:
            pass
    return HttpResponseRedirect(reverse('index'))

class IndexView(generic.ListView):
    model = Employers
    template_name = 'index.html'