from django.db import models

# Create A blog model

#title, pub_date, body, image


class Blog(models.Model):
    title = models.CharField(max_length=30)
    pub_date = models.DateField()
    body = models.TextField(max_length=300)
    image = models.ImageField(
        height_field=100, width_field=200, upload_to='images/')


# Add the blog app to the settings

# Create a migration

# migrate

# Add to the Admin
