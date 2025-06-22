from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout

from django.contrib.auth import get_user_model
from django.http import HttpResponse
import os
from django.http import HttpResponse
from django.core.management import call_command
import os



def submit_review(request):
    submitted = False
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            form.save()
            submitted = True
    else:
        form = ReviewForm()
    return render(request, 'reviews/review_form.html', {'form': form, 'submitted': submitted})


@login_required
def admin_dashboard(request):
    reviews = Review.objects.all().order_by('-submitted_at')
    return render(request, 'reviews/dashboard.html', {'reviews': reviews})

def logout_view(request):
    logout(request)
    return redirect('login')


@login_required
def delete_review(request, review_id):
    review = get_object_or_404(Review, id=review_id)
    review.delete()
    return redirect('dashboard')


def create_superuser(request):
    User = get_user_model()
    if not User.objects.filter(username=os.environ.get("DJANGO_SUPERUSER_USERNAME")).exists():
        User.objects.create_superuser(
            username=os.environ.get("DJANGO_SUPERUSER_USERNAME"),
            email=os.environ.get("DJANGO_SUPERUSER_EMAIL"),
            password=os.environ.get("DJANGO_SUPERUSER_PASSWORD"),
        )
        return HttpResponse("Superuser created.")
    else:
        return HttpResponse("Superuser already exists.")

def run_migrations(request):
    token = request.GET.get("token")
    if token == os.environ.get("MIGRATE_TOKEN"):
        call_command("migrate")
        return HttpResponse("Migrations applied.")
    else:
        return HttpResponse("Unauthorized", status=401)

