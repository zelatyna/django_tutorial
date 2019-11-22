from django.http import HttpResponse
from django.views import generic
from .models import One_liner, User
from .serializers import OneLinerSerializer, UserSerializer
from rest_framework import viewsets
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(generic.ListView):
    template_name = 'one_liner/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return One_liner.objects.order_by('-pub_date')[:10]




class OneLinerViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = One_liner.objects.order_by('-pub_date')[:10]
    serializer_class = OneLinerSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.order_by('-author')
    serializer_class = UserSerializer