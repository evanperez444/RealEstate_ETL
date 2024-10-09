from django.db import models

class RealEstateData(models.Model):
    property_url = models.URLField()
    median_price = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    days_on_market = models.IntegerField(null=True)
    average_price_per_sqft = models.DecimalField(max_digits=10, decimal_places=2, null=True)
    fetched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.property_url
