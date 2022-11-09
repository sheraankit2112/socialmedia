import re
from django.shortcuts import redirect, render
from PIL import Image, ImageTk
from keras.models import load_model
from my.models import tumor

classifier = load_model("C:/Users/ankit/Desktop/brain_tumor.h5")

from keras.preprocessing import image
import matplotlib.pyplot as plt
import numpy as np



def model(request):
    i=None
    j=None
    if request.method=="POST":
        pic=request.FILES.get("pic")
        img1 = pic
        img = img1
        
        # create a batch of size 1 [N,H,W,C]
        img = np.expand_dims(img, axis=0)
        prediction = classifier.predict(img, batch_size=None,steps=1) #gives all class prob.
        print(prediction)
        if(prediction[:,:]>0.6):
             value ='Yes :%1.2f'%(prediction[0,0]*100)
             plt.text(20, 62,value,color='red',fontsize=18,bbox=dict(facecolor='white',alpha=0.8))
        else:
             value ='No :%1.2f'%((1.0-prediction[0,0])*100)
             plt.text(20, 62,value,color='red',fontsize=18,bbox=dict(facecolor='white',alpha=0.8))

        i=plt.imshow(img1)
        j=plt.show()

        return redirect("/")

    return render(request,"index.html",{"img1":i,"img2":j})

