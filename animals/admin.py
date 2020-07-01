from django.contrib import admin

from animals.models import Animal, Cat, Dog
from registry.models import Passport
from .forms import CatAdminForm, DogAdminForm


@admin.register(Animal)
class AnimalAdmin(admin.ModelAdmin):
    pass


@admin.register(Cat)
class CatAdmin(admin.ModelAdmin):

    form = CatAdminForm


@admin.register(Dog)
class DogAdmin(admin.ModelAdmin):

    form = DogAdminForm


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    pass
