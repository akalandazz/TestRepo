from django.db import models

class ShiftsField(models.ForeignKey):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)