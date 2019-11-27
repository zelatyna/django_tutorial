from django.views import generic
from .models import One_liner, CustomUser
from .serializers import OneLinerSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework import permissions


from django.contrib.auth.models import User


class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class IndexView(generic.ListView):
    template_name = 'one_liner/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return One_liner.objects.order_by('-pub_date')[:10]

# class UserViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = User.objects.all()
#     serializer_class = UserSerializer


class UpdatesList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = One_liner.objects.order_by('-pub_date')
    serializer_class = OneLinerSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

    def post(self, request, *args, **kwargs):
        # data_cp = request.data.copy()
        # serializer = self.get_serializer(data=data_cp)
        # user_id = data_cp.pop('user_id')
        # if isinstance(user_id, list):
        #     user_id = int(user_id[0])
        # elif type(user_id) == 'str':
        #     user_id = int(user_id)
        # data_cp['user_id'] = user_id
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
