from django.db import models


class Country(models.Model):
    # Basic Details
    name = models.CharField(max_length=100, unique=True)  # Country name
    code = models.CharField(max_length=10, unique=True)  # ISO country code
    gdp = models.DecimalField(max_digits=12, decimal_places=2, help_text="GDP in USD (Trillions)")  # GDP in trillions
    work_hours = models.IntegerField(help_text="Average work hours per week")  # Work hours per week

    # Education-Related Information
    literacy_rate = models.DecimalField(max_digits=5, decimal_places=2, help_text="Percentage of literacy rate") 
    top_universities_count = models.IntegerField(help_text="Number of universities in top global rankings")  # Number of top universities
    education_quality_index = models.DecimalField(max_digits=5, decimal_places=2, help_text="Education quality index (1-100)")  
    
    # Cost of Living
    living_cost_index = models.DecimalField(max_digits=5, decimal_places=2, help_text="Living cost index (1-100)")  
    average_tuition_fees = models.DecimalField(max_digits=10, decimal_places=2, help_text="Average tuition fees (USD)")  

    # Work and Immigration
    work_permit_availability = models.BooleanField(default=False, help_text="Can international students work while studying?")
    post_study_work_visa_duration = models.IntegerField(null=True, blank=True, help_text="Post-study work visa duration in months")  # Duration in months

    # Safety and Well-being
    safety_index = models.DecimalField(max_digits=5, decimal_places=2, help_text="Safety index (1-100)")  
    health_care_index = models.DecimalField(max_digits=5, decimal_places=2, help_text="Healthcare quality index (1-100)")  

    # Climate
    climate_type = models.CharField(max_length=50, choices=[
        ('Tropical', 'Tropical'),
        ('Dry', 'Dry'),
        ('Temperate', 'Temperate'),
        ('Continental', 'Continental'),
        ('Polar', 'Polar')
    ], help_text="Type of climate")
    average_temperature = models.DecimalField(max_digits=5, decimal_places=2, help_text="Average annual temperature (°C)")  # Temperature in Celsius

    # Miscellaneous
    language = models.CharField(max_length=100, help_text="Primary language(s) spoken")  
    currency = models.CharField(max_length=50, help_text="Currency used")  
    timezone = models.CharField(max_length=100, help_text="Timezone(s)")  

    # Additional Info
    created_at = models.DateTimeField(auto_now_add=True)  # Record creation timestamp
    updated_at = models.DateTimeField(auto_now=True)  # Record last updated timestamp

    def __str__(self):
        return self.name
