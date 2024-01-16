from django.contrib import messages
from django.views.generic import TemplateView
from django.shortcuts import redirect, render


class HomeView(TemplateView):
    template_name = 'index.html'


# def test_view(request):
#     if request.method == 'POST':
#         messages.success(request, 'درخواست موفقیت آمیز.')
#         return redirect('test')
#     return render(request, 'test_dash.html')
