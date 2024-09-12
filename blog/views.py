from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms import ModelForm
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, CreateView, ListView, UpdateView, DeleteView
from pytils.translit import slugify

from blog.forms import BlogForm
from blog.models import Blog


class BlogListView(ListView, LoginRequiredMixin):
    model = Blog

    def get_queryset(self, *args, **kwargs):
        """выводит только опубликованные блоги"""
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogCreateView(CreateView, LoginRequiredMixin):
    """Создание новой статьи"""
    model = Blog
    form_class = BlogForm
    success_url = reverse_lazy('blog:blog_list')

    def form_valid(self, form):
        """Присваивание владельца при создании статьи"""

        user = self.request.user
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)
            new_blog.owner = user
            new_blog.save()

        return super().form_valid(form)


class BlogDetailView(DetailView, LoginRequiredMixin):
    """Просмотр статьи"""

    model = Blog

    def get_object(self, queryset=None):
        """Cчетчик просмотров статьи"""

        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(UpdateView):
    """Изменение статьи"""

    model = Blog
    form_class = BlogForm

    # success_url = reverse_lazy('materials:list')

    def form_valid(self, form):
        if form.is_valid():
            new_blog = form.save()
            new_blog.slug = slugify(new_blog.title)

        return super().form_valid(form)

    def get_success_url(self):
        return reverse('blog:blog_detail', args=[self.kwargs.get('pk')])


class BlogDeleteView(DeleteView, LoginRequiredMixin):
    """Удаление статьи"""

    model = Blog
    success_url = reverse_lazy('blog:blog_list')
