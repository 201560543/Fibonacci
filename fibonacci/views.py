from django.shortcuts import render
from django.views.generic import TemplateView
from django.views import View
import time


# Create your views here.
def fibonacci(n):
    a,b = 0,1
    if n < 0:
        print("Incorrect input")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2, n):
            a,b = b, a+b
        return b


class FibonacciAPIView(View):

    def get(self, request):

        number = request.GET.get('value')

        if number is None:
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
