from django.contrib.auth.decorators import login_required
from rest_framework import routers

from Collection.views import ArticleSet, ReporterSet, ArticleSet2, ReporterSet2

router = routers.DefaultRouter()
router.register(r'articles', ArticleSet, base_name='a1')
router.register(r'reporters', ReporterSet, base_name='r1')
router.register(r'articles2', ArticleSet2, base_name='a2')
router.register(r'reporters2', ReporterSet2, base_name='r2')
urlpatterns = router.urls
