# vercel-django-example/vercel_app/settings.py
# https://github.com/jayhale/vercel-django-example/blob/main/vercel_app/settings.py#L43

INSTALLED_APPS = [
    # ...
    'example',
]

# vercel-django-example/vercel_app/settings.py
# https://github.com/jayhale/vercel-django-example/blob/main/vercel_app/settings.py#L28

# ...

ALLOWED_HOSTS = ['.vercel.app'] # Allow *.vercel.app

# ...

DATABASES = {} # Prevent Django from loading an adapter

# ...