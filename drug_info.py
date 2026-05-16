from data import DRUGS
def get_drug_info(drug_name):
    search = drug_name.lower().strip()

    # البحث بالاسم العلمي
    if search in DRUGS:
        return DRUGS[search]

    # البحث بالأسماء التجارية الإنجليزية
    for drug in DRUGS.values():
        for brand in drug["brand_names"]:
            if search == brand.lower():
                return drug

    # البحث بالأسماء العربية
    for drug in DRUGS.values():
        for arabic_name in drug["arabic_names"]:
            if drug_name.strip() == arabic_name:
                return drug

    return None
