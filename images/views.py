# -*- coding: UTF-8 -*-
import os
import shutil

from django.shortcuts import render, redirect
from django.template.defaultfilters import slugify
from django.conf import settings
from django.core.files import File

from models import Product
from forms import ImageForm
from django.shortcuts import render, get_object_or_404


def image_list(request):
    images = Product.objects.all()
    return render(request, "images/image_list.html", {'images': images})
    
def post_detail(request, pk):    
    post = get_object_or_404(Product, pk=pk)
    return render(request, 'images/items_detail.html', {'post': post})
      


def image_upload(request, image_id=None):
    instance = None
    if image_id:
        instance = Image.objects.get(pk=image_id)

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES, instance=instance)
        if form.is_valid():
            new_instance = form.save(commit=True)  # let's save the instance to get create its primary key

            if form.cleaned_data['delete_image'] and new_instance.image:
                new_instance.image.delete()

            if form.cleaned_data['image_path']:
                tmp_path = form.cleaned_data['image_path']
                abs_tmp_path = os.path.join(settings.MEDIA_ROOT, tmp_path)

                fname, fext = os.path.splitext(os.path.basename(tmp_path))
                filename = slugify(fname) + fext

                new_instance.image.save(filename, File(open(abs_tmp_path, "rb")), False)
                os.remove(abs_tmp_path)
            new_instance.save()
            return redirect("image_list")
    else:
        form = ImageForm(instance=instance)

    return render(request, "images/image_upload.html", {'instance': instance, 'form': form})
