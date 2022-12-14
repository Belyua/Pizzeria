from .models import Size
from .forms import SizeForm
from django.shortcuts import render
from django import forms
from django.views.generic.edit import FormView
from django.http import JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from .forms import SizeForm
from .models import Size


def add_size(request):
    res = Size.objects.all
    return render(request, 'base.html', {"showsize": res})

# def person_create_view(request):
#     form = SizeForm()
#     if request.method == 'POST':
#         form = SizeForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('size_add')
#     return render(request, 'home/homepage.html', {'form': form})
#
#
# def person_update_view(request, pk):
#     size = get_object_or_404(Size, pk=pk)
#     form = SizeForm(instance=size)
#     if request.method == 'POST':
#         form = SizeForm(request.POST, instance=size)
#         if form.is_valid():
#             form.save()
#             return redirect('size_change', pk=pk)
#     return render(request, 'home/homepage.html', {'form': form})
#
#
# def load_sizes(request):
#     size_id = request.GET.get('size_id')
#     sizes = Size.objects.filter(size_id=size_id).all()
#     form = SizeForm()
#     return render(request, 'home/templates/home/sizes_dropdown.html', {'sizes': sizes})

