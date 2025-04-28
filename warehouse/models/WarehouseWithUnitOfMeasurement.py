from django.db import models
from django_countries.fields import CountryField


# Create your models here.
class PackageType(models.TextChoices):
    BOX = ("box", "Box")
    PACKAGE = ("package", "Package")
    BLISTER = ("blister", "Blister")
    BOTTLE = ("bottle", "Bottle")
    VIAL = ("vial", "Vial")
    AMPULE = ("ampule", "Ampule")
    SACHET = ("sachet", "Sachet")
    TUBE = ("tube", "Tube")
    JAR = ("jar", "Jar")
    STRIP = ("strip", "Strip")


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
    BLISTER = ("blister", "Blister (Blister-pack)")  # Blister (Blister-qadoq)
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


class MeasureUnit(models.TextChoices):
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
class ProductWithUnit(models.Model):  # С единицей измерения
    name = models.CharField(max_length=255)  # nomi
    country = CountryField(blank_label="(select country)")  # choices
    Manufacturer = models.CharField(max_length=255)  # proizvodeitel
    Package_id = models.CharField(choices=PackageType.choices,  max_length=255, default=PackageType.BOX)  # tara karobka upakovka
    Dosage_form = models.CharField(choices=DosageForm.choices, max_length=255, default=DosageForm.TABLET)  # Formasi gel yoki blister choices
    Dosage_form_amount = models.IntegerField()  # 1 pochkani ichida nechi dona dori borligi
    Dosage = models.IntegerField()# 1ta dona tabletka nechi  gramligini soni
    Measure_unit = models.CharField(max_length=255,choices=MeasureUnit.choices, default=MeasureUnit.MG)  # choiches ml yoki


