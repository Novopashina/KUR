from django.shortcuts import render, redirect
from .forms import ImageForm
from .forms import FeedbackForm
# from PIL import Image
# from .models import Image
# from .models import Feedback



def image_upload_view(request):
    if request.method == 'POST':
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            img_obj = form.instance 
            return render(request, 'home.html', {'form': form, 'img_obj': img_obj})
    else:
        form = ImageForm()
    return render(request, 'home.html', {'form': form})


def feedback_view(request):
    message_sent = False
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            form.save()
            message_sent = True 
    else:
        form = FeedbackForm()
    return render(request, 'feedback.html', {'form': form, 'message_sent': message_sent})


# def contacts_view(request):
#     return render(request, 'contacts.html')

# def home(request):
#     if request.method == 'POST' and request.FILES.get('image'):
#         image = request.FILES['image']
        
#         # Example: Save the image to the media folder
#         makeup_image = Image(image=image)
#         makeup_image.save()

#         # Example: Display the uploaded image
#         image_path = makeup_image.image.url
#         return render(request, 'makeup_app/home.html', {'image_path': image_path})

#     return render(request, 'makeup_app/home.html')
