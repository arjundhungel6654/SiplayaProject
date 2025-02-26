from django.contrib import admin
from .models import Course
from .models import Collegelist
# Register your models here.
@admin.register(Course)
class courseAdmin(admin.ModelAdmin):
    list_display=['id','faculty','amount','level']

@admin.register(Collegelist)
class CollegelistAdmin(admin.ModelAdmin):
    list_display=['id','collegename','enrollmentdate','level']


admin.site.site_header="Student Enrollment Data"