from django.shortcuts import render, redirect
from .models import Artiles, Comment
from .forms import ArtilesForm, CommentForm
from django.views.generic import DetailView, UpdateView
from django.contrib.auth.decorators import user_passes_test, login_required


from django.views import View
from django.utils.decorators import method_decorator



def news_home(request):
    news = Artiles.objects.all()
    return render(request, 'news/news_home.html', {'news': news})


#class NewsDetailView(DetailView):
#    model = Artiles
#    template_name = 'news/details_view.html'
#    context_object_name = 'article'

@method_decorator(login_required, name='dispatch')
class NewsDetailView(View):
    def get(self, request, pk):
        article = Artiles.objects.get(id=pk) #статья по айди
        comments = Comment.objects.filter(article=article) #все комментарии к статье
        form = CommentForm()
        return render(request, 'news/details_view.html', {
            'article': article,
            'comments': comments,
            'form': form
        })

    def post(self, request, pk):
        article = Artiles.objects.get(id=pk)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.author = request.user
            comment.article = article
            comment.user = request.user
            comment.save()
            return redirect('news-detail', pk=pk)
        comments = Comment.objects.filter(article=article)
        return render(request, 'news/details_view.html', {
            'article': article,
            'comments': comments,
            'form': form
        })




class NewsUpdateView(UpdateView):
    model = Artiles
    template_name = 'news/create.html'
    form_class = ArtilesForm

##################



# Проверка, является ли пользователь администратором
@user_passes_test(lambda u: u.is_superuser, login_url='/login/')  # редирект на login, если не админ
def create(request):
    error = ''
    if request.method == 'POST':
        form = ArtilesForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('news_home')
        else:
            error = "Форма была неверной/некорректной."

    form = ArtilesForm()
    data = {'form': form,
            'error': error
            }
    return render(request, 'news/create.html', data)

