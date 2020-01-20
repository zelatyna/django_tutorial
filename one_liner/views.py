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

    def reorder_left_to_right(self, qs, column_count=4):
        """
        :param qs: queryset
        column_count: number of mansonry-columns
        :return:list of items reordered so that the items will be displayed from left to right rather than from
        top ot bottom and column by column
        """
        #reorder the result items to be displayed from left to right in masonry display
        #TODO: the items are not displayed evenly through columns. There can be 2 taller items in columns 1
        # and 4 items in column 2 if that makes the items more evenly spread
        rows_count = int(len(qs)/column_count)
        if len(qs)%column_count >0: rows_count+=1
        index_matrix = np.concatenate((np.arange(len(qs)), (-1)*np.ones(rows_count*column_count - len(qs)))).reshape(rows_count, column_count)
        index_matrix = np.matrix(index_matrix)
        index_list = index_matrix.transpose().reshape(1,rows_count*column_count).tolist()[0]
        index_list = [x for x in index_list if int(x) != -1]
        reordered =  [None] * len(qs)
        for id, item in enumerate(qs):
            reordered[index_list.index(id)] = item

    def get_queryset(self, max_items=20):
        """Return the last five published questions."""

        qs = One_liner.objects.order_by('-pub_date')[:max_items]
        # qs = self.reorder_left_to_right(qs)
        return qs


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
