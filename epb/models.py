import pandas as pd
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator
from datetime import datetime

def get_last_two_years():
    current_year = datetime.now().year
    return [(year, year) for year in range(current_year, current_year - 2, -1)]

organized_by_df = pd.read_excel('table.xlsx', sheet_name='OrganizedBy')
ORGANIZED_BY_CHOICES = [(row['name'], row['name']) for _, row in organized_by_df.iterrows()]

regions_df = pd.read_excel('table.xlsx', sheet_name='Regions')
REGION_CHOICES = [(row['name'], row['name']) for _, row in regions_df.iterrows()]

program_theme_df = pd.read_excel('table.xlsx', sheet_name='ProgramTheme')
PROGRAM_THEME_CHOICES = [(row['name'], row['name']) for _, row in program_theme_df.iterrows()]

program_subtheme_df = pd.read_excel('table.xlsx', sheet_name='ProgramSubtheme')
PROGRAM_SUBTHEME_CHOICES = [(row['name'], row['name']) for _, row in program_subtheme_df.iterrows()]

category_df = pd.read_excel('table.xlsx', sheet_name='Category')
CATEGORY_CHOICES = [(row['name'], row['name']) for _, row in category_df.iterrows()]

collaboration_df = pd.read_excel('table.xlsx', sheet_name='Collaboration')
COLLABORATION_CHOICES = [(row['name'], row['name']) for _, row in collaboration_df.iterrows()]

program_type_df = pd.read_excel('table.xlsx', sheet_name='ProgramType')
PROGRAM_TYPE_CHOICES = [(row['name'], row['name']) for _, row in program_type_df.iterrows()]

mode_df = pd.read_excel('table.xlsx', sheet_name='Mode')
MODE_CHOICES = [(row['name'], row['name']) for _, row in mode_df.iterrows()]

funding_type_df = pd.read_excel('table.xlsx', sheet_name='FundingType')
FUNDING_TYPE_CHOICES = [(row['name'], row['name']) for _, row in funding_type_df.iterrows()]

venue_df = pd.read_excel('table.xlsx', sheet_name='Venue')
VENUE_CHOICES = [(row['name'], row['name']) for _, row in venue_df.iterrows()]

budget_df = pd.read_excel('table.xlsx', sheet_name='Budget')
BUDGET_CHOICES = [(row['name'], row['name']) for _, row in budget_df.iterrows()]

funding_source_df = pd.read_excel('table.xlsx', sheet_name='FundingSource')
FUNDING_SOURCE_CHOICES = [(row['name'], row['name']) for _, row in funding_source_df.iterrows()]

class Program(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    Year = models.PositiveIntegerField(choices=get_last_two_years(), null=True,blank=False)
    Organized_By = models.CharField(max_length=100, choices=ORGANIZED_BY_CHOICES, null=True, blank=False, help_text='Activity initiated/planned by') 
    Select_Region = models.CharField(max_length=100, choices=REGION_CHOICES, null=True, blank=False, help_text='Select your region along with Local Area')
    Region = models.CharField(max_length=100, null=True, blank=True) # auto
    Local_Area = models.CharField(max_length=100, null=True, blank=True) # auto
    Programmatic_Theme = models.CharField(max_length=100, choices=PROGRAM_THEME_CHOICES, null=True, blank=False)
    Select_Programmatic_Subtheme = models.CharField(max_length=200, choices=PROGRAM_SUBTHEME_CHOICES, null=True, blank=True, help_text='Select your Sub-Theme based on Programmatic Portfolio')
    Programmatic_Subtheme = models.CharField(max_length=100, null=True, blank=True) # auto
    Programmatic_Category = models.CharField(max_length=100, choices=CATEGORY_CHOICES, null=True, blank=False)
    Collaboration= models.CharField(max_length=100, choices=COLLABORATION_CHOICES, null=True, blank=False, help_text='Select if any collaboration with other entity')
    Programme_Name = models.CharField(max_length=200, null=True, blank=False)
    Programme_Objective = models.TextField(null=True, blank=False, help_text='Provide details of the key program outputs with objectives')
    Male_Participants = models.PositiveIntegerField(null=True, blank=False)
    Female_Participants = models.PositiveIntegerField(null=True, blank=False)
    Total_Participants = models.PositiveIntegerField(null=True, blank=False) # auto
    Program_Type = models.CharField(max_length=100, choices=PROGRAM_TYPE_CHOICES, null=True, blank=False)
    Program_Start_Date = models.DateField(null=True, blank=False)
    Program_End_Date = models.DateField(null=True, blank=False)
    Duration_In_Hours = models.PositiveSmallIntegerField(null=True, blank=False, help_text='Total Duration of Activity/Program/Training in hours')
    Facilitator_Name = models.CharField(max_length=200, null=True, blank=False, help_text='Name of Speaker/Trainer/Institution, NA if not applicable')
    Facilitator_Contact_Number = models.CharField(max_length=200, null=True, blank=False, help_text='Contact Number of Speaker/Trainer/Institution, NA if not applicable')
    Type_Of_Venue = models.CharField(max_length=100, choices=VENUE_CHOICES, null=True, blank=False)
    Venue_Name = models.CharField(max_length=200, null=True, blank=False, help_text='e.g. Institution Name, JK Name, School Name, Office Name')
    Mode_Of_Activity = models.CharField(max_length=100, choices=MODE_CHOICES, null=True, blank=False)
    Budget_Category = models.CharField(max_length=100, choices=BUDGET_CHOICES, null=True, blank=False, help_text='Budgeted means allocated by National & Non-Budgeted means managed through other means')
    Funding_Source = models.CharField(max_length=100, choices=FUNDING_SOURCE_CHOICES, null=True, blank=False)
    National_Contribution = models.PositiveIntegerField(null=True, blank=False, help_text='Type amount', validators=[MaxValueValidator(5000000, message='Budget cannot exceed 5,000,000')])
    Beneficiary_Contribution = models.PositiveIntegerField(null=True, blank=False, help_text='Type amount', validators=[MaxValueValidator(5000000, message='Budget cannot exceed 5,000,000')])
    Donation = models.PositiveIntegerField(null=True, blank=False, help_text='Type amount', validators=[MaxValueValidator(5000000, message='Budget cannot exceed 5,000,000')])
    Ak_Agency = models.PositiveIntegerField(null=True, blank=False, help_text='Type amount', validators=[MaxValueValidator(5000000, message='Budget cannot exceed 5,000,000')])
    Govt_Funded = models.PositiveIntegerField(null=True, blank=False, help_text='Type amount', validators=[MaxValueValidator(5000000, message='Budget cannot exceed 5,000,000')])
    Impact_Of_Programme = models.TextField(null=True, blank=False, help_text='Provide outcome of programme with action plans and timelines')
    Attendance_Upload = models.FileField(upload_to='attendance/', null=True, blank=False)
    Picture_Upload = models.ImageField(upload_to='pictures/', null=True, blank=False, help_text='Attached aleast 3 best photos of the programme')
    Proposal_Upload = models.FileField(upload_to='proposals/', null=True, blank=False)
    Total_Activity_Expense = models.CharField(max_length=200, null=True, blank=False) # auto
    user = models.CharField(max_length=200, null=True, blank=False) # auto

    def save(self, *args, request=None, **kwargs):

        self.Total_Participants = self.Male_Participants + self.Female_Participants
        self.Total_Activity_Expense = self.National_Contribution + self.Beneficiary_Contribution + self.Donation + self.Ak_Agency + self.Govt_Funded
        
        if not self.pk and request and request.user.is_authenticated:
            self.user = request.user.first_name

        parts = self.Select_Region.split('_')

        if len(parts) == 2:
            self.Region = parts[0]
            self.Local_Area = parts[1]

        parts = self.Select_Programmatic_Subtheme.split('_')

        if len(parts) == 2:
            self.Programmatic_Subtheme = parts[1]

        super().save(*args, **kwargs)

    def __str__(self):
        return self.Programme_Name
    
    class Meta:
        verbose_name = "Programmatic Tracking"
        verbose_name_plural = "Programmatic Tracking"