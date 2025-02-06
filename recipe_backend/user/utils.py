from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

GENDER_CHOICES = [
    ("Male", "Male"),
    ("Female", "Female"),
]

def validate_choices(value, choices):
    if not all(item in choices for item in value):
        raise ValidationError(_("Invalid choice: %(value)s"), params={"value": value})

class DietaryRestrictions(models.TextChoices):
    VEGETARIAN = "Vegetarian", _("Vegetarian")
    VEGAN = "Vegan", _("Vegan")
    GLUTEN_FREE = "Gluten-free", _("Gluten-free")
    LACTOSE_INTOLERANT = "Lactose Intolerant", _("Lactose Intolerant")
    HALAL = "Halal", _("Halal")
    KOSHER = "Kosher", _("Kosher")

def validate_dietary_restrictions(value):
    validate_choices(value, [choice.value for choice in DietaryRestrictions])

class HealthConditions(models.TextChoices):
    DIABETES = "Diabetes", _("Diabetes")
    HIGH_BLOOD_PRESSURE = "High Blood Pressure", _("High Blood Pressure")
    HIGH_CHOLESTEROL = "High Cholesterol", _("High Cholesterol")
    FOOD_ALLERGIES = "Food Allergies", _("Food Allergies")

def validate_health_conditions(value):
    validate_choices(value, [choice.value for choice in HealthConditions])


class NutritionalGoals(models.TextChoices):
    WEIGHT_LOSS = "Weight Loss", _("Weight Loss")
    WEIGHT_GAIN = "Weight Gain", _("Weight Gain")
    MUSCLE_BUILDING = "Muscle Building", _("Muscle Building")
    ENDURANCE_TRAINING = "Endurance Training", _("Endurance Training")

def validate_nutritional_goals(value):
    validate_choices(value, [choice.value for choice in NutritionalGoals])

class LifestylePreferences(models.TextChoices):
    BUSY_SCHEDULE = "Busy Schedule", _("Busy Schedule")
    BEGINNER_COOKING_SKILLS = "Beginner Cooking Skills", _("Beginner Cooking Skills")
    INTERMEDIATE_COOKING_SKILLS = (
        "Intermediate Cooking Skills",
        _("Intermediate Cooking Skills"),
    )
    ADVANCED_COOKING_SKILLS = "Advanced Cooking Skills", _("Advanced Cooking Skills")
    SPICY_FOOD = "Spicy Food", _("Spicy Food")
    SWEET_FOOD = "Sweet Food", _("Sweet Food")
    SAVORY_FOOD = "Savory Food", _("Savory Food")

def validate_lifestyle_preferences(value):
    validate_choices(value, [choice.value for choice in LifestylePreferences])


def validate_email_address(value):
    if "@" not in value or "." not in value.split("@")[1]:
        raise ValidationError(_("Invalid email address"))
    elif " " in value:
        raise ValidationError(_("Email address cannot contain spaces"))

    local_part, domain_part = value.split("@")
    domain_name = domain_part.split(".")[0]

    if "gmail" not in domain_name and "email" not in domain_name:
        raise ValidationError(
            _("Email address must contain 'gmail' or 'email' in the domain part")
        )