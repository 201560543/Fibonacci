from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
import time


# Create your views here.
def fibonacci(n):
    a,b=1,1
    if n < 2:
        return 1
    else:
        for i in range(2, n+1):
            a,b = a+b, a
        return b


class FibonacciAPIView(View):

    def get(self, request):

        number = request.GET.get('value')

        if not number:
            return render(request, 'index.html')

        else:
            start_time = time.time()
            input = int(number)
            output = fibonacci(input)
            end_time = time.time() - start_time
            return render(request, 'index.html', {
                'numeric': input,
                'output': output,
                'latency': str(end_time)
            })
