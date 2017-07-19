# DjangoRelationship

> pip install djangorestframework

> python manage.py startapp Collection

<a href="https://github.com/mingburnu/DjangoRelationship/blob/master/DjangoRelationship/settings.py">edit /DjangoRelationship/settings.py</a>

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
    
    REST_FRAMEWORK = {
        'DEFAULT_RENDERER_CLASSES': (
            'rest_framework.renderers.JSONRenderer',
        ),
    }

<a href="https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/models.py">edit /DjangoRelationship/Collection/models.py</a>

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

<a href="https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/Serializer.py">edit DjangoRelationship/Collection/Serializer.py</a>

<a href="https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/admin.py">edit /DjangoRelationship/Collection/admin.py</a>

    admin.site.register(Article)
    admin.site.register(Reporter)
    
> python manage.py makemigrations<br>
> python manage.py migrate<br>

> python manage.py createsuperuser

<a href="https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/views.py">edit DjangoRelationship/Collection/views.py</a>

    ...
    class ArticleSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
        permission_classes = (permissions.IsAdminUser,)
        queryset = Article.objects.all()
        serializer_class = ArticleSerializer
    ...
    
<a href="https://github.com/mingburnu/DjangoRelationship/blob/master/Collection/urls.py">edit DjangoRelationship/Collection/urls.py</a>

<a href="https://github.com/mingburnu/DjangoRelationship/blob/master/DjangoRelationship/urls.py">edit DjangoRelationship/urls.py</a>

<a href="http://127.0.0.1:8000/api">127.0.0.1:8000/api</a>

### REFERECE
<a href="https://docs.djangoproject.com/en/1.11/topics/db/examples/many_to_one/">Many-to-one relationships</a>
<a href="https://eureka.ykyuen.info/2015/04/07/django-rest-framework-setting-permissions/">DJANGO REST FRAMEWORK – SETTING PERMISSIONS</a><br>
<a href="http://www.django-rest-framework.org/api-guide/relations/">Serializer relations</a><br>
<a href="http://www.django-rest-framework.org/api-guide/generic-views/">Generic views</a>
