from django.shortcuts import render, redirect
# from .form import ImageForm
# from .models import Image
from .models import Contact, Blog

from .form import ContactForm


# Create your views here.
def index(request):
    # if request.method == "POST":
    #     form = ImageForm(data=request.POST, files=request.FILES)
    #     if form.is_valid():
    #         # form.save()
    #         obj = form.instance
    #         image_result, text = call_algorithm(obj.image)
    #         return render(request, "index.html", {"obj": obj, "image_result": image_result, "text": text})

    print("testinggggggggggggggggggggg")
    blogs = Blog.objects.all()
    print(blogs[0])
    print(blogs[0].title)

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print("form")
            print(form.cleaned_data.get("name"))
            Contact.objects.create(
                name=form.cleaned_data.get('name'),
                email=form.cleaned_data.get('email'),
                phone=form.cleaned_data.get('phone'),
                message=form.cleaned_data.get('message'),
            )
            message = "Contact Saved Successfully"

            return render(request, "index.html", {'message': message})
        else:
            form = ContactForm()

        return render(request, "index.html", {'form': form})
    return render(request, "index.html", {'blogs': blogs})

    # else:
    #     form = ImageForm()
    # img = Image.objects.all()
    # return render(request, "index.html", {"img": img, "form": form})
