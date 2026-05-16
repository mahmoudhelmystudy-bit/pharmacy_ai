from data import INTERACTIONS


def check_interaction(drug1, drug2):
    drug1 = drug1.lower()
    drug2 = drug2.lower()

    key = (drug1, drug2)
    if key in INTERACTIONS:
        return INTERACTIONS[key]

    key = (drug2, drug1)
    if key in INTERACTIONS:
        return INTERACTIONS[key]

    return None