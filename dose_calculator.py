# =========================
# PEDIATRIC DOSE CATEGORIES
# =========================

# Analgesics / Antipyretics
# - Paracetamol
# - Ibuprofen

# Antibiotics
# - Amoxicillin
# - Amoxicillin/Clavulanate (Augmentin)
# - Azithromycin
# - Cefixime
# - Metronidazole

# Antihistamines
# - Cetirizine

# Respiratory
# - Salbutamol

# Corticosteroids
# - Prednisolone

# Gastrointestinal
# - Omeprazole
from drug_info import get_drug_info


def estimate_weight_from_age(age):
    """
    age is provided in YEARS.

    Age < 1 year:
        Weight (kg) = 3.5 + (age in months × 0.6)

    Age 1 to 10 years:
        Weight (kg) = (2 × age) + 8

    Age > 10 years:
        Weight (kg) = (3 × age) + 7
    """

    # أقل من سنة
    if age < 1:
        age_months = age * 12
        return 3.5 + (age_months * 0.6)

    # من سنة إلى 10 سنوات
    elif age <= 10:
        return (2 * age) + 8

    # أكبر من 10 سنوات
    else:
        return (3 * age) + 7

def calculate_paracetamol_dose(weight):
    dose_mg = weight * 15
    max_daily_dose = weight * 75

    return {
        "dose_mg": dose_mg,
        "frequency": "Every 4-6 hours as needed",
        "max_doses_per_day": 5,
        "max_daily_dose_mg": max_daily_dose
    }


from drug_info import get_drug_info


def calculate_drug_dose(drug_name, weight=None, age=None):
    # الحصول على بيانات الدواء من قاعدة البيانات
    info = get_drug_info(drug_name)

    if not info:
        return None

    # استخراج المادة الفعالة
    generic = info["generic_name"].lower()

    # إذا لم يتم إدخال الوزن لكن تم إدخال العمر
    if weight is None and age is not None:
        weight = estimate_weight_from_age(age)

    # إذا ما زال الوزن غير معروف
    if weight is None:
        return None

    # Paracetamol / Acetaminophen
    if "paracetamol" in generic or "acetaminophen" in generic:
        return calculate_paracetamol_dose(weight)

    # Ibuprofen
    elif "ibuprofen" in generic:
        dose_mg = weight * 10

        return {
            "dose_mg": dose_mg,
            "frequency": "Every 6-8 hours as needed",
            "max_doses_per_day": 4,
            "max_daily_dose_mg": weight * 40
        }

    # لا توجد قاعدة جرعات لهذا الدواء
    else:
        return None
   