from rest_framework.generics import *
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from .serializers import *
from start_page.models import Medcine, Synonyms
from .permissions import AdminOrReadonly
from rest_framework.decorators import action
from rest_framework import viewsets
from rest_framework.views import Response


class MedcineViewSet(viewsets.ModelViewSet):
    serializer_class = MedcineSerializer
    queryset = Medcine.objects.all()
    permission_classes = (AdminOrReadonly, )
    authentication_classes = TokenAuthentication


class SynonymsViewSet(viewsets.ModelViewSet):
    serializer_class = SynonymsSerializer
    queryset = Synonyms.objects.all()
    # permission_classes = (AdminOrReadonly, )
    # authentication_classes = TokenAuthentication

    @action(methods=['get'], detail=False)
    def synonyms_comm_name(self, request):
        synonyms = Synonyms.objects.all()
        return Response({'comm_names': [synonym.comm_name for synonym in synonyms]})


# class MedcineApiList(ListCreateAPIView):
#     serializer_class = MedcineSerializer
#     queryset = Medcine.objects.all()
#     permission_classes = [AdminOrReadonly]
#     authentication_classes = [TokenAuthentication]
#
#
# class MedcineApiDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Synonyms.objects.all()
#     serializer_class = MedcineSerializer
#     permission_classes = [AdminOrReadonly]
#     authentication_classes = [TokenAuthentication]


# class SynonymsApiList(ListCreateAPIView):
#     serializer_class = SynonymsSerializer
#     queryset = Synonyms.objects.all()
#     permission_classes = [AdminOrReadonly]
#     authentication_classes = [TokenAuthentication]
#
#
# class SynonymsApiDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Synonyms.objects.all()
#     serializer_class = SynonymsSerializer
#     permission_classes = [AdminOrReadonly]
#     authentication_classes = [TokenAuthentication]

# class MedicineApiView(APIView):
#     def get(self, request):
#         lst = Medcine.objects.all()
#         return Response({'medcines': MedcineSerializer(lst, many=True).data})
#
#     def post(self, request):
#         m = MedcineSerializer(data=request.data)
#         m.is_valid(raise_exception=True)
#         m.save()
#         return Response({'medcines_post': m.data})
#
#     def put(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({'error': 'not put request'})
#
#         try:
#             instance = Medcine.objects.get(pk=pk)
#         except:
#             return Response({'error': 'medcine is not exist'})
#
#         m = MedcineSerializer(
#             instance=instance,
#             data=request.data
#         )
#         m.is_valid(raise_exception=True)
#         m.save()
#         return Response({"medcines_put": m.data})
#
#     def delete(self, request, *args, **kwargs):
#         pk = kwargs.get('pk', None)
#         if not pk:
#             return Response({"error": "not del method"})
#
#         try:
#             instance = Medcine.objects.get(pk=pk)
#         except:
#             return Response({'error': 'medcine is not exist'})
#
#         instance.delete()
#         return Response({'medcines_del': f'medcine {instance.international_name} delete'})
