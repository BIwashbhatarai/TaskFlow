from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Task
from .forms import TaskForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.core.paginator import Paginator
from django.views.decorators.cache import never_cache
from django.views.decorators.http import require_POST


@never_cache
@login_required
def task_list(request):
    tasks = Task.objects.filter(user=request.user)

    search = request.GET.get("query")
    filtering = request.GET.get("filter")
    sort = request.GET.get("sort")

    if sort == "newest":
        tasks = tasks.order_by("-created_at")
    elif sort == "oldest":
        tasks = tasks.order_by("created_at")
    elif sort == "due":
        tasks = tasks.order_by("due_date")
    elif sort == "az":
        tasks = tasks.order_by("title")
    elif sort == "za":
        tasks = tasks.order_by("-title")
    else:
        tasks = tasks.order_by("-created_at")

    # Filter
    if filtering == "completed":
        tasks = tasks.filter(is_completed=True)
    elif filtering == "pending":
        tasks = tasks.filter(is_completed=False)
    elif filtering == "high":
        tasks = tasks.filter(priority_choices="High")

    # Search
    if search:
        tasks = tasks.filter(
            Q(title__icontains=search) | Q(description__icontains=search)
        )

    # Statistics (before pagination)
    total_tasks = tasks.count()
    completed_tasks = tasks.filter(is_completed=True).count()
    pending_tasks = tasks.filter(is_completed=False).count()
    High_priority_tasks = tasks.filter(priority_choices="High").count()

    # Progress
    progress = (completed_tasks / total_tasks * 100) if total_tasks else 0

    # Pagination (LAST)
    paginator = Paginator(tasks, 5)
    page_number = request.GET.get("page")
    tasks = paginator.get_page(page_number)

    return render(
        request,
        "tasks/task_list.html",
        {
            "tasks": tasks,
            "search": search,
            "total_tasks": total_tasks,
            "completed_tasks": completed_tasks,
            "pending_tasks": pending_tasks,
            "High_priority_tasks": High_priority_tasks,
            "progress": progress,
        },
    )


@login_required
def add_task(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save()
            return redirect("task_list")
    else:
        form = TaskForm()
    return render(request, "tasks/add_task.html", {"form": form})


@require_POST
@login_required
def delete_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.delete()
    return redirect("task_list")


@require_POST
@login_required
def completed_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)
    task.is_completed = not task.is_completed
    task.save()
    return redirect("task_list")


@require_POST
@login_required
def edit_task(request, id):
    task = get_object_or_404(Task, id=id, user=request.user)

    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = TaskForm(instance=task)
    return render(request, "tasks/edit_task.html", {"form": form})


def sign_up(request):
    if request.user.is_authenticated:
        return redirect("task_list")

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("task_list")
    else:
        form = UserCreationForm()
    return render(request, "tasks/sign_up.html", {"form": form})


def sign_in(request):
    if request.user.is_authenticated:
        return redirect("task_list")

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request, user)
                messages.success(request, "Logged in successfully")
                return redirect("task_list")
            else:
                messages.error(request, "Invalid Username or Password")
    else:
        form = AuthenticationForm()
    return render(request, "tasks/sign_in.html", {"form": form})


@never_cache
@login_required
def sign_out(request):
    if request.method == "POST":
        logout(request)
        messages.success(request, "Logged out successfully")
        return redirect("sign_in")
    return render(request, "tasks/sign_out.html")
