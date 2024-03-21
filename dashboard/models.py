from django.db import models


class ItemLot(models.Model):
    id = models.AutoField(primary_key=True)
    numLot = models.CharField(max_length=13, help_text="Número do Lote")
    contractLot = models.CharField(max_length=19)
    descriptionLot = models.CharField(max_length=250)
    priceLot = models.CharField(max_length=13)
    #create_at = models.DateField(auto_now_add=True)

    #def __str__(self):
     #   return f'{self.numLot} {self.contractLot} {self.descriptionLot} {self.priceLot}'

    def __int__(self):
        return (self.numLot)
