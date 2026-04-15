from django.db import models


class Tweak(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField()
    download_link = models.URLField(max_length=500)
    icon_image = models.ImageField(upload_to='tweak_icons/', blank=True, null=True)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.name
