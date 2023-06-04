from django.db import models

# Create your models here.

class Features(models.Model):
    val1 = models.FloatField(max_length=30)
    val2 = models.FloatField(max_length=30)
    val3 = models.FloatField(max_length=30)
    val4 = models.FloatField(max_length=30)
    val5 = models.FloatField(max_length=30)
    val6 = models.FloatField(max_length=30)
    val7 = models.FloatField(max_length=30)
    val8 = models.FloatField(max_length=30)
    val9 = models.FloatField(max_length=30)
    val10 = models.FloatField(max_length=30)

NP_TYPE = (
    ('AG', 'Ag'),
    ('NIFE', 'NiFe2O4'),
    ('AL', 'Al2O3'),
    ('BI', 'Bi2O3'),
    ('CO', 'CoO'),
    ('CR', 'Cr2O3'),
    ('FE', 'Fe2O3'),
    ('IN', 'In2O3'),
    ('LA', 'La2O3'),
    ('NO', 'NiO'),
    ('SB', 'Sb2O3'),
    ('SN', 'SnO2'),
    ('TI', 'TiO2'),
    ('V', 'V2O3'),
    ('W', 'WO3'),
    ('Y', 'Y2O3'),
    ('ZN', 'ZnO'),
    ('ZR', 'ZrO2'),
    ('PT', 'Pt')
)

TOX_MEASURE = (
    ('CC', 'CC50'),
    ('LC', 'LC50'),
    ('EC', 'EC50')
)

ENDPOINT = (
    ('RAW', 'RAW 264.7 (M)'),
    ('A', 'A549 (H)'),
    ('HACAT', 'HaCaT (H)'),
    ('DR', 'Danio rerio (embryos)'),
    ('PS', 'Pseudokirchneriella subcapitata')
)

SHAPE = (
    ('SPHERE', 'spherical'),
    ('IRREG', 'irregular'),
    ('POLY', 'polyhedral'),
    ('N/A', 'n/a')
)

CONDITION = (
    ('WATER', 'H2O'),
    ('DRY', 'Dry'),
    ('DULBECCO', 'DMEM')
)

ASSAY_TIME = (
    ('FOUR', '4'),
    ('TWOFOUR', '24'),
    ('FOUREIGHT', '48'),
    ('SEVENTWO', '72'),
    ('NINESIX', '96'),
    ('ONETWENTY', '120'),
    ('ONESIXTYEIGHT', '168')
)

COAT = (
    ('PDAD', 'PDADMAC'),
    ('U', 'UC'),
    ('OLE', 'oleate')
)

class Reference(models.Model):
    np = models.CharField(choices=NP_TYPE, max_length=15, null=False)
    me = models.CharField(choices=TOX_MEASURE, max_length=15, null=False)
    bt = models.CharField(choices=ENDPOINT, max_length=15, null=False)
    ns = models.CharField(choices=SHAPE, max_length=15, null=False)
    dm = models.CharField(choices=CONDITION, max_length=15, null=False)
    ta = models.CharField(choices=ASSAY_TIME, max_length=15, null=False)
    sc = models.CharField(choices=COAT, max_length=15, null=False)
    f1 = models.FloatField(max_length=100, null=False)
    f2 = models.FloatField(max_length=100, null=False)
    f3 = models.FloatField(max_length=100, null=False)
    f4 = models.FloatField(max_length=100, null=False)
    f5 = models.FloatField(max_length=100, null=False)
    f6 = models.FloatField(max_length=100, null=False)
    f7 = models.FloatField(max_length=100, null=False)
    f8 = models.FloatField(max_length=100, null=False)
    f9 = models.FloatField(max_length=100, null=False)
    f10 = models.FloatField(max_length=100, null=False)