from django.conf import settings

def disqus(context):
  return {'CUR_URL': settings.CUR_URL}