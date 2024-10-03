from django.db import models
import qrcode
from io import BytesIO
from django.core.files import File
from PIL import Image, ImageDraw

SEXE = (
    ('homme', 'Homme'),
    ('femme', 'Femme'),
)

class Carte(models.Model):
    nom = models.CharField(max_length=100)
    postnom = models.CharField(max_length=100)
    prenom = models.CharField(max_length=100)
    sexe = models.CharField(choices=SEXE, max_length=10)
    telephone = models.CharField(max_length=100)
    date_naissance = models.CharField(max_length=20)
    photo = models.ImageField(upload_to='photo/', blank=True)
    adresse = models.CharField(max_length=100)
    filiere = models.CharField(max_length=100, blank=True)
    promotion = models.CharField(max_length=100)
    
    email = models.CharField(max_length=100)
    lieu_naissance = models.CharField(max_length=50)

    annee_academique = models.CharField(max_length=100)
    nom_pere = models.CharField(max_length=100)
    contact_pere = models.CharField(max_length=100)
    nom_mere = models.CharField(max_length=100)
    contact_mere = models.CharField(max_length=100)
    nom_tuteur = models.CharField(max_length=100)
    contact_tuteur = models.CharField(max_length=100)

    nom_urgence = models.CharField(max_length=100)
    contact_urgence = models.CharField(max_length=100)

    qr_code = models.ImageField(upload_to="qr_code", blank=True)

    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'{self.nom} {self.postnom} {self.prenom}'
    
    def save(self, *args, **kwargs):
        qr_image = qrcode.make(f"Nom: {self.nom}\nPost-nom: {self.postnom}\nPrenom: {self.prenom}\nTélephone: {self.telephone}\nFilière: {self.filiere}\nPromotion: {self.promotion}")
        canvas = Image.new('RGB', (qr_image.pixel_size, qr_image.pixel_size), 'white')
        draw = ImageDraw.Draw(canvas)
        canvas.paste(qr_image)
        file_name = f"qr_code-{self.nom}-{self.postnom}-{self.prenom}.png"
        buffer = BytesIO()
        canvas.save(buffer, 'PNG')
        self.qr_code.save(file_name, File(buffer), save=False)
        canvas.close()
        return super().save(*args, **kwargs)