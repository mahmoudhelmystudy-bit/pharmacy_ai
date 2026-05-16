DRUGS = {
    "paracetamol": {
    "generic_name": "Paracetamol (Acetaminophen)",
    "brand_names": [
    "Panadol",
    "Adol",
    "Paramol",
    "Fevadol",
    "Cetal",
    "Calpol",
    "Pacimol",
    "Doliprane",
    "Abimol",
    "Acetalgan",
    "Anzoptima",
    "Augicetamide",
    "Awadist",
    "Cetamol",
    "Efferalgan",
    "Febrinil",
    "Glasmol",
    "Grandemol",
    "Grippo",
    "Injectmol",
    "Medalegic",
    "Novecetamol",
    "Panacetagen",
    "Paracetamol B.P."
],

"arabic_names": [
    "بنادول",
    "أدول",
    "بارامول",
    "فيفادول",
    "سيتال",
    "كالبول",
    "باسيمول",
    "دوليبران",
    "أبيمول",
    "أسيتالجان",
    "أنزوبتيما",
    "أوجيسيتاميد",
    "أواديست",
    "سيتامول",
    "إيفيرالجان",
    "فبرينيل",
    "جلاسمول",
    "جرانديمول",
    "جريبو",
    "إنجكت مول",
    "ميداليجيك",
    "نوفيسيتامول",
    "باناسيتاجين"
],
    "class": "Analgesic and Antipyretic",
    "moa": "Inhibits central prostaglandin synthesis.",
    "indications": "Fever, headache, mild to moderate pain.",
    "strengths": [
        "Oral Drops: 100 mg/mL",
        "Suspension: 120 mg/5 mL, 125 mg/5 mL, 150 mg/5 mL, 250 mg/5 mL",
        "Suppositories: 125 mg, 250 mg, 300 mg, 500 mg",
        "Tablets: 500 mg, 1000 mg",
        "Caplets: 500 mg",
        "Modified Release Tablets: 665 mg",
        "Effervescent Tablets: 500 mg, 1000 mg",
        "Sachets: 250 mg, 500 mg, 1000 mg",
        "IV Infusion: 1 g/100 mL"
    ],
    "side_effects": "Hepatotoxicity in overdose, nausea, vomiting, rash."
},

"ibuprofen": {
    "generic_name": "Ibuprofen",
    "brand_names": [
        "Brufen",
        "Brufen Cold",
        "Nurofen",
        "Nurofen for Children",
        "Advil",
        "Advil Cold & Sinus",
        "I-Profen",
        "Ibuprof",
        "Doloraz",
        "Mofen"
    ],
    "arabic_names": [
        "ايبوبروفين",
        "بروفين",
        "بروفين كولد",
        "نوروفين",
        "نوروفين للاطفال",
        "أدفيل",
        "اي بروفين",
        "موفين"
    ],
    "class": "NSAID (Non-Steroidal Anti-Inflammatory Drug)",
    "moa": "Reversible inhibition of COX-1 and COX-2, reducing prostaglandin synthesis.",
    "indications": "Pain, fever, inflammation.",
    "strengths": [
        "Drops 40 mg/mL",
        "Suspension 100 mg/5 mL",
        "Suspension Forte 200 mg/5 mL",
        "Tablet 200 mg",
        "Tablet 400 mg",
        "Tablet 600 mg",
        "Tablet 800 mg",
        "Capsule 200 mg"
    ],
    "side_effects": "Gastritis, nausea, renal impairment, fluid retention, GI bleeding.",
    "pregnancy_category": "Avoid in third trimester",
    "renal_warning": "Use with caution in dehydration and renal impairment.",
    "dose_rules": {
        "pediatric": "5-10 mg/kg/dose every 6-8 hours as needed",
        "max_daily": "40 mg/kg/day"
    }
},
}

INTERACTIONS = {
    ("warfarin", "aspirin"): {
        "severity": "Major",
        "mechanism": "Increased bleeding risk.",
        "recommendation": "Avoid combination unless clinically necessary."
    }
}
