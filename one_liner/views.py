from django.views import generic
from .models import One_liner, CustomUser
from .serializers import OneLinerSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework import mixins, generics
from rest_framework.response import Response
from rest_framework import permissions
from rest_framework.exceptions import NotFound
import numpy as np

class UserList(generics.ListAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer

class UserDetail(generics.ListAPIView):

    serializer_class = UserSerializer
    def get_queryset(self):
        phone_number =  self.request.query_params.get('phone_number', None)
        if phone_number is not None:
            queryset = CustomUser.objects.all()
            queryset = queryset.filter(phone_number=phone_number)

            return queryset
        else:
            raise NotFound()

class IndexView(generic.ListView):
    template_name = 'one_liner/update_view.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self, column_count=4, max_items=20):
        """Return the last five published questions."""

        qs = One_liner.objects.order_by('-pub_date')[:max_items]

        #reorder the result items to be displayed from left to right in masonry display
        rows_count = int(max_items/column_count)
        index_matrix = np.concatenate((np.arange(len(qs)), (-1)*np.ones(max_items - len(qs)))).reshape(rows_count, column_count)
        index_matrix = np.matrix(index_matrix)
        index_list = index_matrix.transpose().reshape(1,rows_count*column_count).tolist()[0]
        index_list = [x for x in index_list if int(x) != -1]
        reordered =  [None] * len(qs)
        for id, item in enumerate(qs):
            reordered[index_list.index(id)] = item


        return reordered


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
        print("DATA" , request.data)
        serializer = self.get_serializer(data=request.data)

        if not serializer.is_valid():
            print(serializer.errors)
        serializer.save(author=self.request.user)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
