from django.contrib import admin
from .models import Program
from import_export.admin import ImportExportModelAdmin

class ProgramAdmin(ImportExportModelAdmin, admin.ModelAdmin):
    list_display = ('Year', 'Organized_By', 'Region', 'Local_Area', 'Programmatic_Theme', 'Programmatic_Subtheme', 'Programme_Name', 'Total_Participants', 'Program_Start_Date', 'user', 'Duration_In_Hours')
    list_filter = ('Year', 'Organized_By', 'Region', 'Local_Area', 'Programmatic_Theme')
    search_fields = ('Programmatic_Subtheme',)
    readonly_fields = ('user', 'Total_Participants', 'Total_Activity_Expense')
    exclude = ('Region', 'Local_Area', 'Programmatic_Subtheme')

admin.site.register(Program, ProgramAdmin)