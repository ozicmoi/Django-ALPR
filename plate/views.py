from django.shortcuts import render,HttpResponse,redirect,get_object_or_404
import cv2
from .forms import PlateForm
from django.contrib import messages
from .models import Plate
from django.contrib.auth.decorators import login_required
# Create your views here.

# Create your views here.
def index(request):
    content={"numbers":[1,2,3,4]}
    return render(request,"index.html",content)

def process(request):
    return render(request,"process.html")

@login_required(login_url="user:login")
def plates(request):
    return render(request,"plates.html")

@login_required(login_url="user:login")
def dashboard(request):
    plates=Plate.objects.filter(attendant = request.user)
    context = {
        "plates": plates
    }
    return render(request, "dashboard.html", context)

@login_required(login_url="user:login")
def addPlate(request):
    form=PlateForm(request.POST or None,request.FILES or None)
    if form.is_valid():
        plate=form.save(commit=False)
        plate.attendant=request.user
        plate.save()
        messages.success(request,"Plaka Başarıyla Kayıt Edildi!")
        return redirect("index")
    return render(request,"addplate.html",{"form":form})

@login_required(login_url="user:login")
def detail(request,id):
    #plate=Plate.objects.filter(id=id).first()
    plate=get_object_or_404(Plate,id=id)
    return render(request,"detail.html",{"plate":plate})


@login_required(login_url="user:login")
def updatePlate(request,id):
    plate=get_object_or_404(Plate,id=id)
    form=PlateForm(request.POST or None,request.FILES or None,instance=plate)
    if form.is_valid():
        plate = form.save(commit=False)
        plate.attendant = request.user
        plate.save()
        messages.success(request, "Plaka Başarıyla Güncellenmiştir!")
        return redirect("plate:dashboard")
    return  render(request,"update.html",{"form":form})

@login_required(login_url="user:login")
def deletePlate(request,id):
    plate=get_object_or_404(Plate,id=id)
    plate.delete()
    messages.success(request,"Kayıt Başarıyla Silinmiştir!")
    return redirect("plate:dashboard")   # Plate adındaki uygulamanın altındaki dashboard sayfasına git

