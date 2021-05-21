from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic import TemplateView, ListView, DetailView, CreateView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
from .forms import UserCreateForm, PostsForm, CommentsForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .models import Posts, Comments
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required

# Create your views here.


class HomeView(TemplateView):
    template_name = 'blogem/home.html'


def registerView(request):
    form = UserCreateForm()

    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            # messages.success(request, 'Account was created for ' + user)
            return redirect('blogem:login')
    context = {'form': form}
    return render(request, 'accounts/register.html', context)


def loginView(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect('blogem:home')
            else:
                return HttpResponse("account not active")
        else:
            messages.warning(request, 'Username OR password is incorrect')

    return render(request, 'accounts/login.html')


@login_required
def logoutView(request):
    logout(request)
    return redirect('blogem:home')


class PostsListView(ListView):
    model = Posts

    def get_queryset(self):
        return Posts.objects.all()


class PostsDetailView(DetailView):
    model = Posts


class PostsCreateView(CreateView, LoginRequiredMixin):
    login_url = '/login/'
    redirect_field_name = 'blogem/posts_detail'
    form_class = PostsForm
    model = Posts


class PostsDeleteView(DeleteView):
    model = Posts
    success_url = reverse_lazy('blogem:all_posts')


class PostsUpdateView(UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blogem/posts_detail'
    form_class = PostsForm
    model = Posts


# @login_required
# def publish_post(request, pk):
#     post = get_object_or_404(Posts, pk=pk)
#     post.publish()
#     return redirect('blogem:posts_detail', pk=pk)


@login_required
def add_comment(request, pk):
    post = get_object_or_404(Posts, pk=pk)
    if request.method == 'POST':
        form = CommentsForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('blogem:posts_detail', pk=post.pk)
    else:
        form = CommentsForm()
    return render(request, 'blogem/comment_form.html', {'form': form})


# @login_required
# def remove_comment(request, pk):

#     comment = get_object_or_404(Comments, pk=pk)
#     postpk = comment.post.pk
#     comment.delete()
#     return redirect('blogem:posts_details', pk=postpk)
