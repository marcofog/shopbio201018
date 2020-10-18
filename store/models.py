from django.db import models
from django.urls import reverse


# I modelli sono sottoclassi di django.db.models.Model
# I campi dei modelli sono invece definiti in django.db.models.fields
# Campi dei Modelli: https://docs.djangoproject.com/en/2.0/ref/models/fields/
# ForeignKey: https://docs.djangoproject.com/en/2.0/ref/models/fields/#django.db.models.ForeignKey
# Making Queries: https://docs.djangoproject.com/en/2.0/topics/db/queries/

# Create your models here.

class Categoria(models.Model):
	categoria = models.CharField(max_length=30, db_index=True)
	slug=models.SlugField(max_length=200, unique=True)

	def __str__(self):
		return self.categoria

	class Meta:
		ordering=('categoria',)
		verbose_name="Categoria"
		verbose_name_plural="Categorie"

	@staticmethod
	def getAllCategory():
		return Categoria.objects.all()

	def get_absolute_url(self):
		return reverse('store:product_list_by_category', args=[self.slug])



class Prodotti (models.Model):
	categoria=models.ForeignKey(Categoria,on_delete=models.CASCADE,related_name='prodotti')
	produttore=models.CharField(max_length=30)
	nome_prodotto=models.CharField(max_length=30, db_index=True)
	slug=models.SlugField(max_length=200, db_index=True)
	descrizione_prodotto=models.CharField(max_length=100)
	prezzo_quantità=models.DecimalField(max_digits=7, decimal_places=2)
	prezzo_pezzi=models.DecimalField(max_digits=7, decimal_places=2)
	informazioni=models.CharField(max_length=300, null=True, blank=True)
	immagine=models.ImageField(null=True, blank=True)
	flag_pezzi=models.BooleanField(default=False,null=True, blank=True)
	unità_quantità=models.DecimalField(max_digits=7, decimal_places=2)
	unità_misura=models.CharField(max_length=10)
	disponibile=models.BooleanField(default=True)

	def __str__(self):
		return self.nome_prodotto


	class Meta:
		ordering=('nome_prodotto',)
		index_together=(('id','slug'),)
		verbose_name="Prodotti"
		verbose_name_plural="Prodotti"


	@property
	def imageURL(self):
		try:
			url = self.immagine.url
		except:
			url = ''
		return url

	def get_absolute_url(self):
		return reverse('store:product_detail', args=[self.id, self.slug])


class CostoConsegna (models.Model):
   Località=models.CharField(max_length=30)
   Importo=models.DecimalField(max_digits=7, decimal_places=2)

   def __str__(self):
	   return self.Località

   class Meta:
	   ordering=('Località',)
	   verbose_name="Località"
	   verbose_name_plural="Località"


class OrarioConsegna(models.Model):
	Orario=models.CharField(max_length=30)

	def __str__ (self):
		 return self.Orario

	class Meta:
	   	verbose_name="Orario"
	   	verbose_name_plural="Orari"


class Parametri(models.Model):
	Chiave=models.CharField(max_length=30)
	Valore=models.CharField(max_length=300, null=True, blank=True)

	def __str__(self):
		return self.Chiave

	class Meta:
	   	verbose_name="Parametri"
	   	verbose_name_plural="Parametri"
