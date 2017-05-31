from django.shortcuts import render, HttpResponse

from blog.models import Post


# def main_view(request):
#     return HttpResponse('음...음..으.ㅁ...')
#
#
# def main_view2(request):
#     return HttpResponse('ㅇㅇㄹㅁㄴㅇ리맞두밎ㄱ헞ㅁㄹ지라저디')


def main_view(request):
    Post.objects.all()
    posts = Post.objects.all()
    context = {
        'posts_list': posts,
    }
    return render(request, 'base/base.html', context)


