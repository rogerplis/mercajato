from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,generics
from .models import Servico, Orcamento, ItemOrcamento, OrdemServico
from .serializers import ServicoSerializer, OrcamentoSerializer, ItemOrcamentoSerializer, OrdemServicoSerializer


class ServicoList(APIView):
    def get(self, request):
        servicos = Servico.objects.all()
        serializer = ServicoSerializer(servicos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = ServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.partial()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrcamentoList(APIView):
    def get(self, request):
        orcamentos = Orcamento.objects.all()
        serializer = OrcamentoSerializer(orcamentos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrcamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = OrcamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ItemOrcamentoList(APIView):
    def get(self, request):
        itens = ItemOrcamento.objects.all()
        serializer = ItemOrcamentoSerializer(itens, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ItemOrcamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = ItemOrcamentoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class OrdemServicoList(APIView):
    def get(self, request):
        ordens = OrdemServico.objects.all()
        serializer = OrdemServicoSerializer(ordens, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = OrdemServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request):
        serializer = OrdemServicoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

