from django.db import models

# Create your models here.

class Category(models.Model):
    class Meta:
        verbose_name_plural = "Categories"
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()

    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name

class CurrencyRate(models.Model):
    CURRENCIES = (
        ('usd', 'usd'),
        ('eur', 'eur')
    )
    currency = models.CharField(max_length=3, choices=CURRENCIES)
    rate = models.DecimalField(max_digits=10, decimal_places=6, default=1)

    def __str__(self):
        return "{} ({})".format(self.currency, self.rate)

    def save(self, *args, **kwargs):
        if not self.pk:
            try:
                rate = CurrencyRate.objects.get(currency=self.currency)
                self.pk = rate.pk
            except CurrencyRate.DoesNotExist:
                pass

        super().save(*args, **kwargs )






