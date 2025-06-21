from django.shortcuts import render, redirect, get_object_or_404  # type: ignore
from .forms import ReviewForm
from .models import Review
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.contrib.auth import views as auth_views

from django.http import HttpResponse
from django.core.management import call_command


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

def run_migrations(request):
    try:
        call_command("migrate")
        return HttpResponse("✅ Migrations applied successfully.")
    except Exception as e:
        return HttpResponse(f"❌ Migration failed: {str(e)}")
