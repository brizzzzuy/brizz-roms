from django.db import models
from django.utils import timezone

class Device(models.Model):
    name = models.CharField(max_length=100)
    codename = models.CharField(max_length=100, unique=True)
    brand = models.CharField(max_length=50)
    maintainer = models.CharField(max_length=100)
    maintainer_avatar = models.ImageField(upload_to='avatars/', blank=True, null=True)
    image = models.ImageField(upload_to='device_images/', blank=True, null=True)
    latest_version = models.CharField(max_length=50, blank=True, default='N/A')
    size = models.CharField(max_length=50, blank=True, default='N/A')
    released_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.name

class Build(models.Model):
    # Link each build to a specific device
    device = models.ForeignKey(Device, on_delete=models.CASCADE, related_name='builds')

    # Build-specific information
    android_version = models.CharField(max_length=20) # e.g., "16", "15"
    build_version = models.CharField(max_length=20) # e.g., "11.2"
    build_type = models.CharField(max_length=50, default="userdebug") # e.g., "userdebug"
    size = models.CharField(max_length=20) # e.g., "2.93 GB"
    is_maintained = models.BooleanField(default=True)
    release_date = models.DateField(default=timezone.now)

    # Links for the buttons
    download_link = models.URLField()
    changelog_link = models.URLField(blank=True)
    install_guide_link = models.URLField(blank=True)

    def __str__(self):
        return f"{self.device.name} - Android {self.android_version}"

