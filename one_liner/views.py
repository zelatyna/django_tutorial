from django.http import HttpResponse
from django.views import generic
from .models import One_liner

#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(generic.ListView):
    template_name = 'one_liner/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return One_liner.objects.order_by('-pub_date')[:10]
