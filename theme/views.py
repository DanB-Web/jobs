from django.http import HttpResponse

def themeToggle(request):
  theme = request.POST.get('theme')
  if theme == 'dark':
    request.session['theme'] = 'dark'
  else:
    request.session['theme'] = ''
  return HttpResponse(status=200)