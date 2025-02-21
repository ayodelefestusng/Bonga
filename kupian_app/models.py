from django.db import models

class PromoCode(models.Model):
    code = models.CharField(max_length=11)
    gift = models.IntegerField(default=0, null=False, blank=False)
    status = models.BooleanField(default=True)
    
    def __str__(self):
        return str(self.code)
    
    
    
    
    from django.db import models

class Product(models.Model):
    code_id = models.ForeignKey('PromoCode', on_delete=models.CASCADE)
    point = models.IntegerField(default=0, null=False, blank=False)
    gift_picture = models.ImageField(upload_to='static/')
    image = models.ImageField(null=True, blank=True)
    
    def __str__(self):
        return str(self.code_id)

class CreateGift(models.Model):
    gift_name = models.CharField(max_length=11)
    value = models.IntegerField(default=0, null=False, blank=False)
    QuantityProduced = models.IntegerField(default=0, null=False, blank=False)
    gift_picture = models.ImageField(null=True, blank=True,upload_to='static/')
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return str(self.gift_name)
    
class Winning_Code(models.Model):
    
    items_name = models.CharField(max_length=11)
    # Voucher_id = models.CharField(max_length=11)
    
    
    # items_name = models.ForeignKey('CreateGift', on_delete=models.CASCADE)
    Voucher_id = models.ForeignKey('PromoCode', on_delete=models.CASCADE)
    Wcode_point = models.IntegerField(default=0, null=False, blank=False)
 
    
    def __str__(self):
        return str(self.items_name)
    
