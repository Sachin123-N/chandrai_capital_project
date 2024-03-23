from django.db import models


class Flat(models.Model):
    PAYMENT_MODE = [('ON', 'ONLINE PAYMENT'), ("EMI", "MONTHLY INSTALLMENT")]
    ROOM_QUANTITY = [("1BHK", '1bed room'), ("2BHK", '2bed room'), ("3BHK", '3bed room')]
    flat_owner_name = models.CharField(max_length=20)
    flat_price = models.IntegerField()
    flat_no = models.IntegerField()
    maintaince_price = models.IntegerField()
    payment_mode = models.CharField(max_length=10, choices=PAYMENT_MODE)
    room_quantity = models.CharField(max_length=10, choices=ROOM_QUANTITY)
