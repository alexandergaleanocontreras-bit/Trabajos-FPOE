from django.db import models


class Manzana(models.Model):
    FORMAS = [
        ("redonda", "Redonda"),
        ("ovalada", "Ovalada"),
        ("conica", "Cónica"),
        ("achatada", "Achatada"),
    ]
    TAMANOS = [
        ("pequeno", "Pequeño"),
        ("mediano", "Mediano"),
        ("grande", "Grande"),
    ]
    COLORES = [
        ("roja", "Roja"),
        ("verde", "Verde"),
        ("amarilla", "Amarilla"),
        ("bicolor", "Bicolor"),
    ]

    forma = models.CharField(max_length=20, choices=FORMAS)
    tamano = models.CharField(max_length=20, choices=TAMANOS)
    peso_g = models.DecimalField(max_digits=6, decimal_places=2)
    color_cascara = models.CharField(max_length=20, choices=COLORES)

    def __str__(self):
        return f"Manzana {self.color_cascara} {self.tamano} ({self.peso_g} g)"