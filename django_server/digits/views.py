from django.shortcuts import render
from PIL import Image
import os
import pandas as pd
import numpy as np
from joblib import load
from django.contrib.staticfiles.storage import staticfiles_storage

# Create your views here.

def process_pred(pred):
    """
    This function returnns the digit predicted
    by the model.
    """
    return np.argmax(pred)

def resize_center_image(old_im):
    old_im = old_im.resize((20,20))
    old_size = old_im.size

    new_size = (28, 28)
    new_im = Image.new("L", new_size) 
    new_im.paste(old_im, (4,4))

    return new_im

def process_image(image_path):
    """
    Processes the given image.
    """
    im = Image.open(image_path)
    im = resize_center_image(im)
    return pd.DataFrame(np.asarray(im).flatten().astype(float)/255).T

def show_image(image_path):
    """
    Displays processed image.
    """
    im = Image.open(image_path)
    im = resize_center_image(im)
    return im

def digits(request):
    if (request.method == 'POST'):
        image = request.FILES['image']
        model = load(staticfiles_storage.path("model/digit_classifier_t2_256256.joblib"))
        result = process_pred(model.predict(process_image(image)))
        return render(request, 'result.html', {'result': result})
    else:
        print(staticfiles_storage.path("model/digit_classifier_t2_256256.joblib"))
        return render(request, 'test.html')