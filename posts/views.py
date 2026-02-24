from django.shortcuts import render
from django.views.generic import DetailView, ListView
import markdown as md
import bleach
from django.utils.safestring import mark_safe

from posts.models import Post, Category

ALLOWED_TAGS = bleach.sanitizer.ALLOWED_TAGS.union({"p","pre","code","h1","h2","h3","h4","h5","h6","img"})
ALLOWED_ATTRS = {"a": ["href", "title"], "img": ["src", "alt", "title"]}

# Create your views here.

class PostListView(ListView):
    model = Post
    template_name = "posts/post_list.html"
    paginate_by = 10

    def get_queryset(self):
        qs = Post.objects.filter(status="published").order_by("-published_at", "-created_at")
        slug = self.kwargs.get("category_slug")
        if slug:
            qs = qs.filter(category__slug=slug)
        return qs

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        ctx["categories"] = Category.objects.select_related("parent").all()
        ctx["active_category_slug"] = self.kwargs.get("category_slug")
        return ctx


class PostDetailView(DetailView):
    model = Post
    template_name = "posts/post_detail.html"

    def get_queryset(self):
        return Post.objects.filter(status="published")

    def get_context_data(self, **kwargs):
        ctx = super().get_context_data(**kwargs)
        html = md.markdown(self.object.content, extensions=["fenced_code", "tables"])
        clean = bleach.clean(html, tags=ALLOWED_TAGS, attributes=ALLOWED_ATTRS, strip=True)
        ctx["content_html"] = mark_safe(clean)
        return ctx

