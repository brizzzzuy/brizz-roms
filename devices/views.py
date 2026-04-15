from django.shortcuts import render, get_object_or_404
from .models import Device


# This is your existing view for the list of all devices.
# It remains unchanged.
def device_list_view(request):
    brand_filter = request.GET.get('brand', 'All')
    brands = Device.objects.values_list('brand', flat=True).distinct().order_by('brand')

    if brand_filter == 'All':
        devices = Device.objects.all().order_by('name')
    else:
        devices = Device.objects.filter(brand=brand_filter).order_by('name')

    context = {
        'devices': devices,
        'brands': brands,
        'selected_brand': brand_filter,
    }
    return render(request, 'devices/device_list.html', context)


# This is the updated view for a single device's detail page.
def device_detail_view(request, codename):
    # Get the specific device using its codename, or show a 404 error.
    device = get_object_or_404(Device, codename=codename)

    # Get all 'Build' objects linked to this device, ordering by the newest first.
    builds = device.builds.all().order_by('-release_date')

    context = {
        'device': device,
        'builds': builds,
        'latest_build': builds.first(),  # Pass the most recent build for convenience
    }
    return render(request, 'devices/device_detail.html', context)

