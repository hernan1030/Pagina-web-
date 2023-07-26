from django.db import models
from django.dispatch import receiver
import os
from PIL import Image

# Create your models here.


class Project(models.Model):

    title = models.CharField(max_length=100, verbose_name="Titulo")
    description = models.TextField(verbose_name="Descripcion")
    image = models.ImageField(verbose_name="Imagen", upload_to='projectss')
    link = models.URLField(verbose_name="Link", null=True, blank=True)
    created = models.DateTimeField(
        auto_now_add=True, verbose_name="Fechade creacion")
    update = models.DateTimeField(
        auto_now=True, verbose_name="fecha de actualizacion")

    class Meta:
        verbose_name = "proyecto"
        verbose_name_plural = "proyectos"

        ordering = ['-created']

    def __str__(self) -> str:
        return f"titulo:{self.title}"

    # este metodo guarda imagenes con un tamaño y ancho deseado
    def save(self, *args, **kware):
        # redimesiona la imagen antes de guardar
        if self.image:
            # Guarda el objeto antes de redimensionar para obtener la ruta de la imagen
            super(Project, self).save(*args, **kware)
            img = Image.open(self.image.path)
            width, heigth = 300, 300
            img.thumbnail((width, heigth), Image.ANTIALIAS)
            img.save(self.image.path)
        else:
            super(Project, self).save(*args, **kware)


# con este decorador y este metodo se elimnan las fotos del directorios al eliminar del admin
@receiver(models.signals.post_delete, sender=Project)
def eliminar_imagen_post_delete(sender, instance, **kware):

    if instance.image:
        ruta_image = instance.image.path
        if os.path.exists(ruta_image):
            os.remove(ruta_image)
