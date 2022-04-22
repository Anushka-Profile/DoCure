# from xml.etree.ElementTree import Comment
from django.contrib import admin


from .models import User
from .models import Cbc
from  .models import Comments
from .models import Doctor,ViewDoctor,ConfirmDoctor

#Register your models here.
admin.site.register(User)
admin.site.register(Cbc)
admin.site.register(Doctor)
admin.site.register(ViewDoctor)
admin.site.register(ConfirmDoctor)
admin.site.register(Comments)

# from django.http import HttpResponse
# import csv

# I usually prefer an action for this in the admin. This is the snippet:

# def download_csv(modeladmin, request, queryset):
#     # if not request.user.is_staff:
#     #     raise PermissionDenied
#     opts = queryset.model._meta
#     model = queryset.model
#     response = HttpResponse(mimetype='text/csv')
#     # force download.
#     response['Content-Disposition'] = 'attachment;filename=export.csv'
#     # the csv writer
#     writer = csv.writer(response)
#     field_names = [field.name for field in opts.fields]
#     # Write a first row with header information
#     writer.writerow(field_names)
#     # Write data rows
#     for obj in queryset:
#         writer.writerow([getattr(obj, field) for field in field_names])
#     return response
# download_csv.short_description = "Download selected as csv"
