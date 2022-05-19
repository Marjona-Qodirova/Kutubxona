from django.db import models

class Student(models.Model):
    ism=models.CharField(max_length=30)
    guruh=models.CharField(max_length=10)
    guvohnoma=models.CharField(max_length=10,blank=True)
    kitob_soni=models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.ism}"
class Muallif(models.Model):
    Tanlov=(
        ("Man","Man"),
        ("Woman","Woman")
    )
    ism=models.CharField(max_length=30)
    yosh=models.PositiveSmallIntegerField()
    tirik=models.BooleanField(blank=True)
    jins=models.CharField(max_length=20, choices=Tanlov)
    kitob_soni = models.PositiveSmallIntegerField(default=0)

    def __str__(self):
        return f"{self.ism}"
class Kitob(models.Model):
    JANR=(
        ("Badiiy", "Badiiy"),
        ("Ilmiy", "Ilmiy"),
        ("Hujjatli", "Hujjatli"),
        ("Detektiv", "Detektiv"),

          )
    nom=models.CharField(max_length=30)
    sahifa=models.PositiveSmallIntegerField()
    janr=models.CharField(max_length=20,choices=JANR)
    muallif=models.ForeignKey(Muallif,on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.nom}"
class Record(models.Model):
    student=models.ForeignKey(Student, on_delete=models.CASCADE)
    kitob =models.ForeignKey(Kitob, on_delete=models.CASCADE)
    sana=models.DateField()
    qaytardi=models.CharField(max_length=5,choices=(("ha","ha"),("yoq","yoq")))
    qaytarilgan_sana=models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.student.ism}, {self.kitob.nom}"












