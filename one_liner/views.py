from django.views import generic
from .models import One_liner, User
from .serializers import OneLinerSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework import mixins, generics
from rest_framework.response import Response

class IndexView(generic.ListView):
    template_name = 'one_liner/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return One_liner.objects.order_by('-pub_date')[:10]

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class UpdatesList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = One_liner.objects.order_by('-pub_date')
    serializer_class = OneLinerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data_cp = request.data.copy()
        serializer = self.get_serializer(data=data_cp)
        user_id = data_cp.pop('user_id')
        if isinstance(user_id, list):
            user_id = int(user_id[0])
        elif type(user_id) == 'str':
            user_id = int(user_id)
        data_cp['user_id'] = user_id
        if not serializer.is_valid():
            print(serializer.errors)
        serializer.save()
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
