# DjangoRelationship

> pip install djangorestframework

> python manage.py startapp Collection

[edit /DjangoRelationship/settings.py](https://github.com/mingburnu/DjangoRelationship/blob/master/DjangoRelationship/settings.py)

    TEMPLATES = [
        {
            ...
            'DIRS': [os.path.join(BASE_DIR, 'templates')],
            ...
        },
    ]

    INSTALLED_APPS = [
        ...
        'Collection',
        'rest_framework',
    ]
    

[edit /DjangoRelationship/Collection/models.py](https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/models.py)

    from django.db import models
    
    
    class Reporter(models.Model):
        first_name = models.CharField(max_length=30)
        last_name = models.CharField(max_length=30)
        email = models.EmailField()

        def __str__(self):
            return "%s %s" % (self.first_name, self.last_name)


    class Article(models.Model):
        headline = models.CharField(max_length=100)
        pub_date = models.DateField()
        reporter = models.ForeignKey(Reporter, related_name='articles', on_delete=models.CASCADE)

        def __str__(self):
            return self.headline

[edit DjangoRelationship/Collection/Serializer.py](https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/Serializer.py)

[edit /DjangoRelationship/Collection/admin.py](https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/admin.py)

    admin.site.register(Article)
    admin.site.register(Reporter)
    
> python manage.py makemigrations<br>
> python manage.py migrate<br>

> python manage.py createsuperuser

[edit DjangoRelationship/Collection/views.py](https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/views.py)

    ...
    class ArticleSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        permission_classes = (permissions.IsAdminUser,)
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer
    ...
    
[edit DjangoRelationship/Collection/urls.py](https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/urls.py)

[edit DjangoRelationship/urls.py](https://github.com/mingburnu/DjangoRelationship/blob/master/DjangoRelationship/urls.py)

[127.0.0.1:8000/api](http://127.0.0.1:8000/api)

### REFERECE
[Many-to-one relationships](https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_one/)
[DJANGO REST FRAMEWORK – SETTING PERMISSIONS](https://eureka.ykyuen.info/2015/04/07/django-rest-framework-setting-permissions/)
[Serializer relations](http://www.django-rest-framework.org/api-guide/relations/)
[Generic views](http://www.django-rest-framework.org/api-guide/generic-views/)
