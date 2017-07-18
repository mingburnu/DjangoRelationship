from rest_framework import viewsets, mixins, permissions

from Collection.Serializer import ArticleSerializer, ReporterSerializer, ArticleSerializer2, ReporterSerializer2
from Collection.models import Article, Reporter


class ArticleSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer


class ReporterSet(viewsets.ModelViewSet):
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer


class ArticleSet2(viewsets.ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleSerializer2


class ReporterSet2(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAdminUser,)
    queryset = Reporter.objects.all()
    serializer_class = ReporterSerializer2
