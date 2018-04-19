from django.shortcuts import render, get_object_or_404
from .models import Device
# Create your views here.

def index(request):
	return render(request, "home.html")


def devices(request):
	if request.method == "POST":
		search_by = request.POST.get("search_by")
		num = request.POST.get("num")
		if search_by == "device_id":
			devices = Device.objects.filter(id=num)
		else:
			devices = Device.objects.filter(pin_code=num)
		print(devices)
	else:
		devices = Device.objects.all()
	context = {
			"devices": devices,
		}
	return render(request, "devices.html", context)


def about_us(request):
	return render(request, "about_us.html")


def device(request, id):
	dev = get_object_or_404(Device, id=id)
	context = {
		"device": dev,
	}
	return render(request, "device.html", context)