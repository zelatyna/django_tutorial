from django.views import generic
from .models import One_liner, User
from .serializers import OneLinerSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework import mixins, generics
#
# def index(request):
#     return HttpResponse("Hello, world. You're at the polls index.")


class IndexView(generic.ListView):
    template_name = 'one_liner/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        """Return the last five published questions."""
        return One_liner.objects.order_by('-pub_date')[:10]




# class OneLinerViewSet(viewsets.ModelViewSet):
#     """
#     API endpoint that allows users to be viewed or edited.
#     """
#     queryset = One_liner.objects.order_by('-pub_date')[:10]
#     serializer_class = OneLinerSerializer

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.order_by('-author')
    serializer_class = UserSerializer


class UpdatesList(mixins.ListModelMixin,
                  mixins.CreateModelMixin,
                  generics.GenericAPIView):
    queryset = One_liner.objects.order_by('-pub_date')
    serializer_class = OneLinerSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    # def get(self, request, format=None):
    #     one_liners = One_liner.objects.order_by('-pub_date')
    #     serializer = OneLinerSerializer(one_liners, many=True)
    #     return JsonResponse(serializer.data, safe=False)
    #
    # def post(self, request, format=None):
    #     serializer = OneLinerSerializer(data=request.data)
    #     if serializer.is_valid():
    #         serializer.save()
    #         return Response(serializer.data, status=status.HTTP_201_CREATED)
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#
# @api_view(['GET', 'POST'])
# def updates_list(request):
#     """
#     List all code snippets, or create a new snippet.
#     """
#     if request.method == 'GET':
#         one_liners = One_liner.objects.order_by('-pub_date')
#         serializer = OneLinerSerializer(one_liners, many=True)
#         return JsonResponse(serializer.data, safe=False)
#         #return Response(serializer.data)
#
#     elif request.method == 'POST':
#         serializer = OneLinerSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)