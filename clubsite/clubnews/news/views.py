from django.shortcuts import render, redirect
from .models import Article
from django.shortcuts import get_object_or_404
from django.contrib import messages
from .forms import ArticleForm
from django.views.generic import ListView

# Create your views here.
def home(request):
    articles = Article.objects.all()
    return render(request, "news/home.html", {"articles": articles})

def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    return render(request, "news/article_detail.html", {"article": article})

def add_article(request):
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Article created successfully!")
            return redirect("news_home")
    else:
        form = ArticleForm()

    return render(request, "news/add_article.html", {"form": form})

def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        form = ArticleForm(request.POST, request.FILES, instance=article)
        if form.is_valid():
            form.save()
            messages.success(request, "Article updated successfully!")
            return redirect("news_home")
    else:
        form = ArticleForm(instance=article)

    return render(request, "news/edit_article.html", {"form": form, "article": article})

def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if request.method == "POST":
        article.delete()
        messages.success(request, "Article deleted successfully!")
        return redirect("news_home")
    return render(request, "news/delete_article.html", {"article": article})

class ArticleListView(ListView):
    model = Article
    template_name = "news/home.html"
    context_object_name = "articles"
    ordering = ["-published_at"]
    paginate_by = 5 # Show 5 articles per page

    def get_queryset(self):
        queryset = super().get_queryset()
        sort = self.request.GET.get("sort")
        search_query = self.request.GET.get("q")

        if search_query:
            queryset = queryset.filter(title__icontains=search_query)

        if sort == "title":
            return queryset.order_by("title")
        return queryset.order_by("-published_at")
