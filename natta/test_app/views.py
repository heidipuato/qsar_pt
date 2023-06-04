from django.shortcuts import render
from .models import *
from .forms import *
import joblib
import numpy as npy
import keras
import tensorflow as tf

# Create your views here.
def home(request):
    return render(request,"test_app/home.html")

def test(request):
    form1 = FeatureForm
    form2 = ReferenceForm

    data = {"form1":form1, "form2":form2}
    return render(request,"test_app/test.html", data)

def about(request):
    return render(request,"test_app/about.html")

def predict(request):
   
   #load ml models
   cls1=joblib.load('xg_model.pkl')
   cls2=joblib.load('cart_model.pkl')

   #get user np features
   lis=[]
   val01 = request.POST.get('val1')
   val1 = float(val01)
   val02 = request.POST.get('val2')
   val2 = float(val02)
   val03 = request.POST.get('val3')
   val3 = float(val03)
   val04 = request.POST.get('val4')
   val4 = float(val04)
   val05 = request.POST.get('val5')
   val5 = float(val05)
   val06 = request.POST.get('val6')
   val6 = float(val06)
   val07 = request.POST.get('val7')
   val7 = float(val07)
   val08 = request.POST.get('val8')
   val8 = float(val08)
   val09 = request.POST.get('val9')
   val9 = float(val09)

   #get reference np features
   np = request.POST.get('np')
   me = request.POST.get('me')
   bt = request.POST.get('bt')
   ns = request.POST.get('ns')
   dm = request.POST.get('dm')
   ta = request.POST.get('ta')
   sc = request.POST.get('sc')

   ref = Reference.objects.get(np__exact=np,me__exact=me,bt__exact=bt,ns__exact=ns,dm__exact=dm,ta__exact=ta,sc__exact=sc)
   
   f1 = ref.f1
   f2 = ref.f2
   f3 = ref.f3
   f4 = ref.f4
   f5 = ref.f5
   f6 = ref.f6
   f7 = ref.f7
   f8 = ref.f8
   f9 = ref.f9
   f10 = ref.f10

   #get perturbation values
   val1 = val1 - f1
   val2 = val2 - f2
   val3 = val3 - f3
   val4 = val4 - f4
   val5 = val5 - f5
   val6 = val6 - f6
   val7 = val7 - f7
   val8 = val8 - f8
   val9 = val9 - f9
   val10 = f10

   #normalize input
   val1 = (val1 - (-9.599)) / (10.666 - (-9.599))
   val2 = (val2 - (-103.384)) / (71.316 - (-103.384))
   val3 = (val3 - (-421.105)) / (394.078 - (-421.105))
   val4 = (val4 - (-301.826)) / (67.751 - (-301.826))
   val5 = (val5 - (-1.345)) / (1.197 - (-1.345))
   val6 = (val6 - (-114.686)) / (87.55 - (-114.686))
   val7 = (val7 - (-57605.281)) / (38894.4 - (-57605.281))
   val8 = (val8 - (-1127.534)) / (35.027 - (-1127.534))
   val9 = (val9 - (-355915832.7)) / (28233130.49 - (-355915832.7))
   val10 = (val10 - (-1)) / (1 - (-1))

   lis.append(val1)
   lis.append(val2)
   lis.append(val3)
   lis.append(val4)
   lis.append(val5)
   lis.append(val6)
   lis.append(val7)
   lis.append(val8)
   lis.append(val9)
   lis.append(val10)
   print(lis)

   data_array = npy.asarray(lis)
   arr= data_array.reshape(1,10)
   print(arr)

   #predict 
   ans1 = cls1.predict(arr)
   print(ans1)

   ans2 = cls2.predict(arr)
   print(ans2)

   final1=''
   final2=''

   if(ans1==1):
      final1='NON-TOXIC'
   elif(ans1==0):
      final1 = 'TOXIC'
   print(final1)

   if(ans2==1):
      final2='NON-TOXIC'
   elif(ans2==0):
      final2 = 'TOXIC'
   print(final2)

   return render(request, "test_app/result.html",{'xg_ans':final1,'cart_ans':final2})


