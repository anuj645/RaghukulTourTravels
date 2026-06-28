from django.shortcuts import render, get_object_or_404
from django.contrib.admin.views.decorators import staff_member_required
from django.shortcuts import redirect
from django.contrib import messages
from .models import TourPackage, Category
from .forms import TourPackageForm


def tour_list(request):
    """Public page — shows all active tour packages."""
    packages  = TourPackage.objects.filter(is_active=True)
    categories = Category.objects.all()

    # Filter by category
    category_slug = request.GET.get('category')
    if category_slug:
        packages = packages.filter(category__slug=category_slug)

    # Filter by price
    max_price = request.GET.get('max_price')
    if max_price:
        packages = packages.filter(price_per_person__lte=max_price)

    return render(request, 'tours/tour_list.html', {
        'packages': packages,
        'categories': categories,
    })


def tour_detail(request, slug):
    """Detail page for a single tour."""
    package = get_object_or_404(TourPackage, slug=slug, is_active=True)
    return render(request, 'tours/tour_detail.html', {'package': package})


@staff_member_required   # only admins can add/edit/delete tours
def tour_create(request):
    if request.method == 'POST':
        form = TourPackageForm(request.POST, request.FILES)
        if form.is_valid():
            tour = form.save()
            messages.success(request, f'Tour "{tour.title}" created successfully!')
            return redirect('tour_detail', slug=tour.slug)
    else:
        form = TourPackageForm()
    return render(request, 'tours/tour_form.html', {'form': form, 'action': 'Create'})


@staff_member_required
def tour_update(request, slug):
    tour = get_object_or_404(TourPackage, slug=slug)
    if request.method == 'POST':
        form = TourPackageForm(request.POST, request.FILES, instance=tour)
        if form.is_valid():
            form.save()
            messages.success(request, 'Tour updated successfully!')
            return redirect('tour_detail', slug=tour.slug)
    else:
        form = TourPackageForm(instance=tour)
    return render(request, 'tours/tour_form.html', {'form': form, 'action': 'Update'})


@staff_member_required
def tour_delete(request, slug):
    tour = get_object_or_404(TourPackage, slug=slug)
    if request.method == 'POST':
        tour.is_active = False   # soft delete — don't actually delete from DB
        tour.save()
        messages.success(request, 'Tour removed.')
        return redirect('tour_list')
    return render(request, 'tours/tour_confirm_delete.html', {'tour': tour})