from django.db import models

# About Model
class About(models.Model):
    title = models.CharField(max_length=100, verbose_name="About title")
    short_description = models.TextField()
    description = models.TextField(verbose_name="About description")
    image = models.ImageField(upload_to="about")

    class Meta:
        verbose_name = "About me"
        verbose_name_plural = "About me"

    def __str__(self):
        return self.title


# Skill  Model
class Skill(models.Model):
    name = models.CharField(max_length=50, verbose_name="Skill name")
    level = models.IntegerField(default=0, verbose_name="Skill level")

    class Meta:
        verbose_name = "Skill name"
        verbose_name_plural = "Skills name"

    def __str__(self):
        return self.name



# Service Model
class Service(models.Model):
    name = models.CharField(max_length=100, verbose_name="Service name")
    description = models.TextField(verbose_name="service description")
    image = models.ImageField(upload_to="service")

    def __str__(self):
        return self.name


# Category Model
class ProjectCategory(models.Model):
    name = models.CharField(max_length=15, verbose_name="ProjectCategory name")

    def __str__(self):
        return self.name


# Recent Work Model
class RecentWork(models.Model):
    title = models.CharField(max_length=100, verbose_name="Project title")
    category = models.ForeignKey(ProjectCategory, on_delete=models.CASCADE)
    short_description = models.CharField(max_length=150, verbose_name="Project short_description")
    description = models.TextField(verbose_name="Project description")
    image = models.ImageField(upload_to="works")

    def __str__(self):
        return self.title


# Client Model
class Client(models.Model):
    name = models.CharField(max_length=100, verbose_name="Client name")
    description = models.TextField(verbose_name="Client description")
    image = models.ImageField(upload_to="clients", default="default.png")

    def __str__(self):
        return self.name





