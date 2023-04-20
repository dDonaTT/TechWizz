from django.db import models
class Product(models.Model):
    LAPTOP = 'laptop'
    MONITOR = 'monitor'
    KOMPJUTER = 'kompjuter'
    LLOJI_CHOICES = [
        (LAPTOP, 'Laptop'),
        (MONITOR, 'Monitor'),
        (KOMPJUTER, 'Kompjuter'),
    ]

    id = models.AutoField(primary_key=True)
    emri_produktit = models.CharField(max_length=255)
    modeli = models.CharField(max_length=255)
    lloji = models.CharField(
        max_length=10,
        choices=LLOJI_CHOICES,
        default=LAPTOP,
    )
    procesori = models.CharField(max_length=255, blank=True, null=True)
    kartela_grafike = models.CharField(max_length=255, blank=True, null=True)
    memoria = models.CharField(max_length=255, blank=True, null=True)
    rami = models.CharField(max_length=255, blank=True, null=True)
    ekrani = models.CharField(max_length=255, blank=True, null=True)
    rezolucion = models.CharField(max_length=255, blank=True, null=True)
    pesha= models.CharField(max_length=255, blank=True, null=True)
    lloji_panelit = models.CharField(
        max_length=10,
        choices=[('IPS', 'IPS'), ('VA', 'VA'), ('TN', 'TN'),('OLED','OLED')],
        blank=True,
    )
    ngjyra = models.CharField(max_length=255)
    qmimi = models.IntegerField()
    fotografia = models.ImageField(upload_to='foto/%Y/%m/%d/')
    foto1 = models.ImageField(upload_to='foto/%Y/%m/%d/', blank=True)
    foto2 = models.ImageField(upload_to='foto/%Y/%m/%d/', blank=True)
    foto3 = models.ImageField(upload_to='foto/%Y/%m/%d/', blank=True)
    foto4 = models.ImageField(upload_to='foto/%Y/%m/%d/', blank=True)
    is_featured = models.BooleanField(default=False)
   

    def clean(self):
        if self.lloji == self.LAPTOP:
            self.rezolucion = None
            self.lloji_i_panelit = None
        elif self.lloji == self.MONITOR:
            self.procesori = None
            self.kartela_grafike = None
            self.rami = None
        elif self.lloji == self.KOMPJUTER:
            self.rezolucion = None
            self.lloji_i_panelit = None
            
    def __str__(self):
        return self.emri_produktit
