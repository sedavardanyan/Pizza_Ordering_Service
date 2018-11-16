from django.db import models

PIZZA_SIZES = (
    (0, '30 cm'),
    (1, '50 cm')
               )


class Pizza(models.Model):
    type = models.CharField(max_length=250)
    size = models.IntegerField(choices=PIZZA_SIZES)

    def __str__(self):
        return self.type


class Customer(models.Model):
    name = models.CharField(max_length=250)
    address = models.CharField(max_length=400)
    phone = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, default=None)
    pizza = models.ForeignKey(Pizza, on_delete=models.SET_NULL, null=True)
    order_date = models.DateTimeField()

    def __str__(self):
        return str(self.id)
