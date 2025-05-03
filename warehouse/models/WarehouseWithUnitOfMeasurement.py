from django.db import models
from django_countries.fields import CountryField

from accounts.models.company import Company


# Create your models here.
class PackType(models.TextChoices):
    BOX = 'box', 'box' # karobka
    BAG = 'bag', 'bag' # qop sumkka
    CONTAINER = 'container', 'container' # quti konatiner nazarida oq idiw


class Unit_type (models.TextChoices):
    BLISTER = 'blister', 'Blister'
    VIAL = 'vial', 'Flakon'
    AMPULE = 'ampule', 'Ampula'

class DosageForm(models.TextChoices):
    TABLET = ("tablet", "Tablet")
    CAPSULE = ("capsule", "Capsule")
    SYRUP = ("syrup", "Syrup")
    INJECTION = ("injection", "Injection")
    OINTMENT = ("ointment", "Ointment")
    CREAM = ("cream", "Cream")
    GEL = ("gel", "Gel")
    DROPS = ("drops", "Drops")
    POWDER = ("powder", "Powder")
    SPRAY = ("spray", "Spray")
    SUPPOSITORY = ("suppository", "Suppository")
    SUSPENSION = ("suspension", "Suspension")
    SOLUTION = ("solution", "Solution")


class DosageForm(models.TextChoices):
    TABLET = ("tablet", "Tablet (Tablet)")  # Tablet (Tablet)
    CAPSULE = ("capsule", "Capsule (Kapsula)")  # Capsule (Kapsula)
    SYRUP = ("syrup", "Syrup (Sirob)")  # Syrup (Sirob)
    INJECTION = ("injection", "Injection (Ukol)")  # Injection (Ukol)
    OINTMENT = ("ointment", "Ointment (Mast))")  # Ointment (Mast)
    CREAM = ("cream", "Cream (Krem)")  # Cream (Krem)
    GEL = ("gel", "Gel (Gel)")  # Gel (Gel)
    DROPS = ("drops", "Drops (Tomchi)")  # Drops (Tomchi)
    POWDER = ("powder", "Powder (Kukun)")  # Powder (Kukun)
    SPRAY = ("spray", "Spray (Sprey)")  # Spray (Sprey)
    SUPPOSITORY = ("suppository", "Suppository (Sham)")  # Suppository (Sham)
    SUSPENSION = ("suspension", "Suspension (Suyuq-qalin)")  # Suspension (Suyuq-qalin)
    SOLUTION = ("solution", "Solution (Eritma)")  # Solution (Eritma)


class Dosage_type(models.TextChoices):
    MG = ("mg", "Milligram")
    G = ("g", "Gram")
    KG = ("kg", "Kilogram")
    ML = ("ml", "Milliliter")
    L = ("l", "Liter")
    UNIT = ("unit", "Unit")
    IU = ("iu", "International Unit")
    PILL = ("pill", "Pill")
    DROP = ("drop", "Drop")
    TSP = ("tsp", "Teaspoon")
    TBSP = ("tbsp", "Tablespoon")
    OZ = ("oz", "Ounce")
    LB = ("lb", "Pound")
    GALLON = ("gallon", "Gallon")

#  O'lchov birligi bilan
class Warehouse(models.Model):  # С единицей измерения
    name = models.CharField(max_length=255)  # nomi
    country = CountryField(blank_label="(select country)")  # choices
    pack_type = models.CharField(choices=PackType.choices , default=PackType.BOX )
    unit_type = models.CharField(choices=Unit_type.choices , default=Unit_type.BLISTER, max_length=255) # Upakovka ichidagi birlik turi
    units_per_pack = models.IntegerField()  # Bir upakovkada nechta birlik bor
    tablets_per_blister = models.IntegerField() # Agar birlik blister bo‘lsa, blister ichida nechta tabletka bor (
    dosage = models.IntegerField() # dozasi
    dosage_type= models.CharField(choices=Dosage_type.choices , default=Dosage_type.MG)
    form = models.CharField(choices=DosageForm.choices , default=DosageForm.TABLET)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)



    class Meta:
        db_table = 'warehouse'
        ordering =  ["-id"]
        app_label = 'warehouse'





