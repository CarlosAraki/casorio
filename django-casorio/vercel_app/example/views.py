from django.shortcuts import render

# Create your views here.
# vercel-django-example/example/views.py
# https://github.com/jayhale/vercel-django-example/blob/main/example/views.py#L6

from datetime import datetime
from django.http import HttpResponse

def index(request):
    now = datetime.now()

    html = f'''
    <html>
        <body>
            <h1>Casorio !</h1>
            <p>Hoje é { now } e falta {now} para o casamento.</p>
        </body>
    </html>
    '''
    return HttpResponse(html)