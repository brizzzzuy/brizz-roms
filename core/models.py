from django.db import models


class TeamMember(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    avatar = models.ImageField(upload_to='team_avatars/', blank=True, null=True)

    def __str__(self):
        return self.name
