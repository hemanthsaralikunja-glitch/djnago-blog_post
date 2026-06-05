from django.shortcuts import get_object_or_404, render
from django.db.models import Count

from myapp.forms import ContactForm
from myapp.models import Blog, Category

# Create your views here.
def home(request):
    categories = Category.objects.all()
    feature_posts = Blog.objects.filter(is_featured=True, status=1).order_by('-created_at')[:3]
    latest_posts = Blog.objects.filter(status=1).order_by('-created_at')
    popular_categories = Category.objects.annotate(post_count=Count('blog')).order_by('-post_count')[:5]

    context = {
        'categories': categories,
        'feature_posts': feature_posts,
        'latest_posts': latest_posts,
        'popular_categories': popular_categories,
    }
    return render(request, 'home.html', context)


def about(request):
    categories = Category.objects.all()
    popular_categories = Category.objects.annotate(post_count=Count('blog')).order_by('-post_count')[:5]

    return render(request, 'about.html', {
        'categories': categories,
        'popular_categories': popular_categories,
    })


def contact(request):
    categories = Category.objects.all()
    popular_categories = Category.objects.annotate(post_count=Count('blog')).order_by('-post_count')[:5]
    form = ContactForm(request.POST or None)
    success = False

    if request.method == 'POST' and form.is_valid():
        success = True
        form = ContactForm()

    return render(request, 'contact.html', {
        'categories': categories,
        'popular_categories': popular_categories,
        'form': form,
        'success': success,
    })


def blog_detail(request, slug):
    post = get_object_or_404(Blog, slug=slug, status=1)
    categories = Category.objects.all()
    related_posts = Blog.objects.filter(category=post.category, status=1).exclude(pk=post.pk)[:3]
    popular_categories = Category.objects.annotate(post_count=Count('blog')).order_by('-post_count')[:5]

    return render(request, 'blog_detail.html', {
        'categories': categories,
        'post': post,
        'related_posts': related_posts,
        'popular_categories': popular_categories,
    })


def category_posts(request, category_id):
    category = get_object_or_404(Category, pk=category_id)
    categories = Category.objects.all()
    posts = Blog.objects.filter(category=category, status=1).order_by('-created_at')
    popular_categories = Category.objects.annotate(post_count=Count('blog')).order_by('-post_count')[:5]

    return render(request, 'category.html', {
        'categories': categories,
        'category': category,
        'posts': posts,
        'popular_categories': popular_categories,
    })