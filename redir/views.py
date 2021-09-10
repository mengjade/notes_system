from django.shortcuts import render
from django.http import HttpResponse



def IndexView(request):

    return render(request, 'redir/index.html')



def AboutView(request):

    return render(request, 'redir/aboutus.html')



def TAView(request):

    return render(request, 'redir/teaching.html')


def BitView(request):
    with open('/home/mengjade/myweb/redir/templates/redir/Bitcoin_Pricing_HuiyiWang.pdf', 'rb') as pdf:
        response = HttpResponse(pdf.read(), content_type='application/pdf')
        response['Content-Disposition'] = 'filename=some_file.pdf'
        return response
    pdf.closed