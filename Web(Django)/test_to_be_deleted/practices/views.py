from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def ping(request):
    return render(request, 'ping.html')

def pong(request):
    # print(request)
    # print(dir(request)) # request라는 객체에 무엇이 있는지 확인 가능
    # print(request.GET('temp'))
    name = request.GET.get('temp')
    context = {
        'name': name,
    }
    return render(request, 'pong.html', context)
    # One liner로도 가능하다
    # return render(request, 'pong.html', {'name': request.Get.get('ball')})