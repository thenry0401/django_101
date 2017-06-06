from django.contrib.auth import get_user_model
from django.shortcuts import render, HttpResponse, redirect

from blog.forms import PostCreationForm
from blog.models import Post

User = get_user_model()


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
    return render(request, 'post/post_list.html', context)

def post_add_view(request):
    if request.method == 'GET':
        form = PostCreationForm()
        context = {
            'forms' : form
        }

        return render(request, 'post/post_add.html', context)

    elif request.method == 'POST':
        form = PostCreationForm(request.POST)

        if form.is_valid():
            author = User.objects.first()
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            Post.objects.create(
                author=author,
                title=title,
                text=text,
            )

        return redirect('post_main')
