from django.db import models

class PortfolioImage(models.Model):
    image = models.ImageField(upload_to='portfolio_images/')
