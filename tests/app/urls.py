from rest_framework.routers import DefaultRouter

from tests.app.views import SnippetViewSet

router = DefaultRouter()
router.register(r'snippets', SnippetViewSet, base_name='api-snippet')
urlpatterns = router.urls
