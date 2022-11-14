# vercel-django-example/vercel_app/urls.py
# https://github.com/jayhale/vercel-django-example/blob/main/vercel_app/urls.py#L21

urlpatterns = [
    # ...
    path('', include('example.urls')),
]