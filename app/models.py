from django.db import models
from django.contrib.auth.models import User

class CustomerOrders(models.Model):
    alpha_numeric_unique_id = models.CharField(max_length=255, verbose_name='Alpha Numeric Unique ID', null=True, blank=True)
    name = models.CharField(max_length=255, verbose_name='Name')
    mobile = models.CharField(max_length=255, verbose_name='Mobile', null=True, blank=True)
    email = models.CharField(max_length=255, verbose_name='Email', null=True, blank=True)
    address_line_1 = models.CharField(max_length=255, verbose_name='Address Line 1', null=True, blank=True)
    address_line_2 = models.CharField(max_length=255, verbose_name='Address Line 2', null=True, blank=True)
    near_by = models.CharField(max_length=255, verbose_name='Near By', null=True, blank=True)
    village = models.CharField(max_length=255, verbose_name='Village', null=True, blank=True)
    mandal = models.CharField(max_length=255, verbose_name='Mandal', null=True, blank=True)
    district = models.CharField(max_length=255, verbose_name='District', null=True, blank=True)
    state = models.CharField(max_length=255, verbose_name='State', null=True, blank=True)
    country = models.CharField(max_length=255, verbose_name='Country', null=True, blank=True)
    device_type = models.CharField(max_length=255, verbose_name='Device Type', null=True, blank=True)
    assembled = models.CharField(max_length=255, verbose_name='Assembled', null=True, blank=True)
    brand = models.CharField(max_length=255, verbose_name='Brand', null=True, blank=True)
    notes = models.TextField(verbose_name='Notes', null=True, blank=True)

    created_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='customer_order_created_by',
        null=True,
        blank=True,
        verbose_name='Created By'
    )

    updated_by = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='customer_order_updated_by',
        null=True,
        blank=True,
        verbose_name='Updated By'
    )

    created_datetime = models.DateTimeField(auto_now_add=True, verbose_name='Created Datetime', null=True, blank=True)
    updated_datetime = models.DateTimeField(auto_now=True, verbose_name='Updated Datetime', null=True, blank=True)

    service_engineer = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='customer_order_service_engineer',
        null=True,
        blank=True,
        verbose_name='Service Engineer'
    )
    
    operational_manager = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        related_name='customer_order_operational_manager',
        null=True,
        blank=True,
        verbose_name='Operational Manager'
    )

    class Meta:
        verbose_name = 'Customer Order'
        verbose_name_plural = 'Customer Order'

    def __str__(self):
        return self.name
