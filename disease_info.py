"""
disease_info.py - Comprehensive Plant Disease Knowledge Base
Contains detailed medical guidelines, symptoms, organic remedies, chemical treatments,
and preventive measures for 38 PlantVillage crop & disease classes.
"""

DISEASE_KNOWLEDGE_BASE = {
    "Apple___Apple_scab": {
        "crop": "Apple",
        "disease": "Apple Scab",
        "scientific_name": "Venturia inaequalis",
        "status": "Diseased",
        "severity": "Moderate to High",
        "symptoms": [
            "Olive-green to brown velvety spots on leaf surface.",
            "Yellowing and premature leaf fall (defoliation).",
            "Cracked, corky lesions on fruit surface."
        ],
        "cause": "Fungal infection thriving in cool, wet spring weather (60-70°F).",
        "organic_treatment": [
            "Apply liquid copper or sulfur-based organic fungicides early in spring.",
            "Spray neem oil (0.5% - 1%) at early bud formation.",
            "Apply compost tea sprays to enhance leaf surface beneficial microbes."
        ],
        "chemical_treatment": [
            "Apply Myclobutanil or Captan 50 WP during pre-bloom stage.",
            "Alternate with Difenoconazole or Mancozeb to prevent fungicide resistance."
        ],
        "prevention": [
            "Rake and destroy fallen leaves in autumn to remove overwintering fungal spores.",
            "Prune tree canopy to maximize sunlight penetration and air movement.",
            "Plant scab-resistant cultivars like 'Liberty', 'Prima', or 'Enterprise'."
        ]
    },
    "Apple___Black_rot": {
        "crop": "Apple",
        "disease": "Black Rot (Frog-Eye Leaf Spot)",
        "scientific_name": "Botryosphaeria obtusa",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Small purple spots expanding into 'frog-eye' lesions with light brown centers.",
            "Black rotting areas on fruit starting from blossom end.",
            "Cankers on branches causing limb dieback."
        ],
        "cause": "Fungal spores overwintering in dead wood, mummified fruits, and bark cankers.",
        "organic_treatment": [
            "Prune out dead or infected wood 6 inches below visible infection.",
            "Apply copper octanoate spray during dormant season.",
            "Remove mummified fruits from trees and ground."
        ],
        "chemical_treatment": [
            "Spray Captan mixed with Ziram or Thiophanate-methyl.",
            "Apply Pyraclostrobin during petal fall."
        ],
        "prevention": [
            "Sterilize pruning shears with 70% isopropyl alcohol between cuts.",
            "Maintain balanced fertilization; avoid excess nitrogen.",
            "Avoid wounding bark during mechanical cultivation."
        ]
    },
    "Apple___Cedar_apple_rust": {
        "crop": "Apple",
        "disease": "Cedar Apple Rust",
        "scientific_name": "Gymnosporangium juniperi-virginianae",
        "status": "Diseased",
        "severity": "Moderate",
        "symptoms": [
            "Bright orange-yellow spots on upper leaf surfaces.",
            "Tube-like fungal fruiting bodies (aecia) under the leaf underside.",
            "Defoliation and stunted fruit growth."
        ],
        "cause": "Heteroecious fungus requiring both Eastern Red Cedar/Juniper and Apple trees to complete life cycle.",
        "organic_treatment": [
            "Spray sulfur or copper soap solutions at tight cluster stage.",
            "Apply Bacillus subtilis bio-fungicide weekly during spring wet periods."
        ],
        "chemical_treatment": [
            "Spray Myclobutanil (Immunox) or Propiconazole at pink bud stage.",
            "Apply Triadimefon if rust gall gelatinous horns appear on nearby cedars."
        ],
        "prevention": [
            "Remove nearby Eastern Red Cedar trees within a 1-mile radius if feasible.",
            "Grow rust-immune apple varieties like 'Redfree', 'Freedom', or 'Priscilla'."
        ]
    },
    "Apple___healthy": {
        "crop": "Apple",
        "disease": "Healthy",
        "scientific_name": "Malus domestica",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Vibrant green leaf blade without spots, discoloration, or leaf margin burning.",
            "Smooth texture and normal stomatal development."
        ],
        "cause": "Optimal plant health and environmental conditions.",
        "organic_treatment": [
            "Maintain current organic soil enrichment routine with balanced compost.",
            "Use seaweed extract spray to enhance immunity against stress."
        ],
        "chemical_treatment": [
            "No chemical treatment required."
        ],
        "prevention": [
            "Continue regular monitoring for early pest or disease signs.",
            "Ensure consistent trickle/drip irrigation avoiding foliage wetting."
        ]
    },
    "Blueberry___healthy": {
        "crop": "Blueberry",
        "disease": "Healthy",
        "scientific_name": "Vaccinium corymbosum",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Deep green glossy leaves without chlorosis or leaf spots.",
            "Vigorous shoot growth."
        ],
        "cause": "Optimal soil acidity (pH 4.5-5.5) and good drainage.",
        "organic_treatment": [
            "Apply pine needle or oak leaf mulch to maintain soil acidity."
        ],
        "chemical_treatment": [
            "No chemical intervention required."
        ],
        "prevention": [
            "Maintain soil pH between 4.5 and 5.2 using elemental sulfur if necessary."
        ]
    },
    "Cherry_(including_sour)___Powdery_mildew": {
        "crop": "Cherry",
        "disease": "Powdery Mildew",
        "scientific_name": "Podosphaera clandestina",
        "status": "Diseased",
        "severity": "Moderate",
        "symptoms": [
            "White powdery fungal patches on new leaves and young shoots.",
            "Leaves curling upward and becoming distorted or brittle.",
            "Stunted terminal shoot growth."
        ],
        "cause": "Fungus favored by warm, dry daytime temperatures accompanied by high nighttime humidity.",
        "organic_treatment": [
            "Spray potassium bicarbonate or neem oil solution (1 tbsp/gallon).",
            "Apply diluted milk spray (1 part milk to 9 parts water) in full sun."
        ],
        "chemical_treatment": [
            "Apply Myclobutanil, Quinoxyfen, or Tebuconazole fungicide.",
            "Rotate with sulfur formulations."
        ],
        "prevention": [
            "Prune inner canopy branches to increase sunlight and air flow.",
            "Avoid overhead irrigation."
        ]
    },
    "Cherry_(including_sour)___healthy": {
        "crop": "Cherry",
        "disease": "Healthy",
        "scientific_name": "Prunus avium",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Lush green, oval leaves with serrated edges and clean surface."
        ],
        "cause": "Good care and optimal growing environment.",
        "organic_treatment": ["Maintain balanced mulching and hydration."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Routine winter pruning and fruit fly monitoring."]
    },
    "Corn_(maize)___Cercospora_leaf_spot_Gray_leaf_spot": {
        "crop": "Corn (Maize)",
        "disease": "Gray Leaf Spot",
        "scientific_name": "Cercospora zeae-maydis",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Rectangular tan to gray lesions delimited by leaf veins.",
            "Lesions merge causing severe leaf blight and premature drying.",
            "Stalk lodging and reduced grain fill."
        ],
        "cause": "Fungal pathogen overwintering in corn crop residue under high humidity (>90%).",
        "organic_treatment": [
            "Spray Trichoderma viride or Bacillus amyloliquefaciens bio-control agents.",
            "Apply copper hydroxide spray during early vegetative stage."
        ],
        "chemical_treatment": [
            "Apply Pyraclostrobin, Azoxystrobin, or Propiconazole at tasseling stage (VT)."
        ],
        "prevention": [
            "Practice 2-year crop rotation with non-host crops like soybean or alfalfa.",
            "Use tillage to decompose crop residue in high-risk areas."
        ]
    },
    "Corn_(maize)___Common_rust_": {
        "crop": "Corn (Maize)",
        "disease": "Common Rust",
        "scientific_name": "Puccinia sorghi",
        "status": "Diseased",
        "severity": "Moderate to High",
        "symptoms": [
            "Oval to elongate cinnamon-brown pustules scattered across both leaf surfaces.",
            "Pustules rupture exposing powdery reddish-brown spores.",
            "Leaf yellowing and chlorosis around dense pustule clusters."
        ],
        "cause": "Airborne fungal spores blown northwards from warm southern regions.",
        "organic_treatment": [
            "Apply sulfur dust or liquid sulfur early at first sign of pustules.",
            "Use neem oil emulsion to suppress spore germination."
        ],
        "chemical_treatment": [
            "Spray Triazole or Strobis (e.g., Azoxystrobin + Difenoconazole) if rust reaches 5% leaf area prior to silking."
        ],
        "prevention": [
            "Plant rust-resistant corn hybrids.",
            "Plant early in the season to avoid peak spore loads."
        ]
    },
    "Corn_(maize)___Northern_Leaf_Blight": {
        "crop": "Corn (Maize)",
        "disease": "Northern Corn Leaf Blight",
        "scientific_name": "Exserohilum turcicum",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Long, elliptical cigar-shaped grayish-green lesions (1 to 6 inches long).",
            "Dark olive-green dark spores blooming inside lesions during humid weather.",
            "Extensive leaf necrosis leading to premature plant death."
        ],
        "cause": "Fungus surviving in infected corn debris under moderate temperatures (65-80°F) and wet conditions.",
        "organic_treatment": [
            "Apply copper-based sprays at boot stage.",
            "Spray bio-fungicides containing Bacillus subtilis."
        ],
        "chemical_treatment": [
            "Apply Mancozeb, Prothioconazole, or Metconazole at early tassel stage."
        ],
        "prevention": [
            "Use NCLB-resistant hybrid seeds.",
            "Rotate crops annually and bury infected crop residue."
        ]
    },
    "Corn_(maize)___healthy": {
        "crop": "Corn (Maize)",
        "disease": "Healthy",
        "scientific_name": "Zea mays",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Long, vibrant dark green leaves with clean veins and strong central midrib."
        ],
        "cause": "Adequate nitrogen, moisture, and sunshine.",
        "organic_treatment": ["Apply side-dress nitrogen fertilizer during knee-high stage."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Maintain weed control and proper crop spacing."]
    },
    "Grape___Black_rot": {
        "crop": "Grape",
        "disease": "Black Rot",
        "scientific_name": "Guignardia bidwellii",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Small reddish-brown circular spots on leaves with dark borders.",
            "Infected berries turn brown, shrivel, and transform into hard black mummies.",
            "Black specks (pycnidia) inside leaf spots."
        ],
        "cause": "Fungal spores spreading via splashing rain during warm wet weather.",
        "organic_treatment": [
            "Prune and destroy all mummified grape clusters and infected canes during winter.",
            "Apply liquid copper or lime-sulfur during shoot development."
        ],
        "chemical_treatment": [
            "Spray Myclobutanil, Tebuconazole, or Mancozeb from immediate pre-bloom until 4 weeks after bloom."
        ],
        "prevention": [
            "Maintain open canopy architecture using canopy management and shoot positioning.",
            "Keep vineyard floor clean of fallen debris."
        ]
    },
    "Grape___Esca_(Black_Measles)": {
        "crop": "Grape",
        "disease": "Esca (Black Measles)",
        "scientific_name": "Phaeomoniella chlamydospora / Phaeoacremonium aleophilum",
        "status": "Diseased",
        "severity": "Very High",
        "symptoms": [
            "'Tiger-stripe' patterns of interveinal yellowing and necrosis on leaves.",
            "Small dark spots ('measles') on berry skins.",
            "Sudden canopy collapse (apoplexy) during hot weather."
        ],
        "cause": "Complex wood-decay fungal infection entering through winter pruning wounds.",
        "organic_treatment": [
            "Paint fresh pruning wounds with Trichoderma-based wound protectants.",
            "Sanitize all pruning tools regularly."
        ],
        "chemical_treatment": [
            "Apply wound sealants (e.g. thiophanate-methyl paste) immediately following pruning."
        ],
        "prevention": [
            "Delayed winter pruning to drier weather conditions.",
            "Remove severely infected vine trunks from the vineyard."
        ]
    },
    "Grape___Leaf_blight_(Isariopsis_Leaf_Spot)": {
        "crop": "Grape",
        "disease": "Leaf Blight (Isariopsis Leaf Spot)",
        "scientific_name": "Pseudocercospora vitis",
        "status": "Diseased",
        "severity": "Moderate",
        "symptoms": [
            "Irregular brown spots on leaves with distinct yellow halos.",
            "Dark velvet fungal growth on leaf undersides.",
            "Premature defoliation before fruit ripening."
        ],
        "cause": "Fungus flourishing under high humidity and poor vine aeration.",
        "organic_treatment": [
            "Apply copper hydroxide or Bordeaux mixture.",
            "Spray neem oil extracts."
        ],
        "chemical_treatment": [
            "Apply Chlorothalonil or Azoxystrobin at early infection onset."
        ],
        "prevention": [
            "Leaf pulling around fruit zones to maximize air movement.",
            "Avoid overhead sprinkler irrigation."
        ]
    },
    "Grape___healthy": {
        "crop": "Grape",
        "disease": "Healthy",
        "scientific_name": "Vitis vinifera",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Broad lobed green leaves without lesions or leaf margin discoloration."
        ],
        "cause": "Optimal vineyard management.",
        "organic_treatment": ["Apply foliar zinc/boron micronutrient sprays if needed."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Maintain vine training trellis system and proper irrigation."]
    },
    "Orange___Haunglongbing_(Citrus_greening)": {
        "crop": "Orange / Citrus",
        "disease": "Huanglongbing (Citrus Greening)",
        "scientific_name": "Candidatus Liberibacter asiaticus",
        "status": "Diseased",
        "severity": "Critical",
        "symptoms": [
            "Asymmetrical blotchy mottle yellowing across leaf blades.",
            "Small, misshapen fruit that remains green at stem end and tastes bitter.",
            "Twig dieback and rapid tree decline."
        ],
        "cause": "Bacterial pathogen vectored by the Asian Citrus Psyllid (Diaphorina citri).",
        "organic_treatment": [
            "Spray horticultural oils or insecticidal soaps to suppress psyllid vector populations.",
            "Release biological predators like Tamarixia radiata wasps."
        ],
        "chemical_treatment": [
            "Apply systemic insecticides (Imidacloprid, Thiamethoxam) to control psyllids.",
            "Foliar nutritional sprays (Zinc, Iron, Manganese) to prolong tree life."
        ],
        "prevention": [
            "Plant only certified disease-free nursery stock.",
            "Promptly eradicate infected trees to prevent vector transmission."
        ]
    },
    "Peach___Bacterial_spot": {
        "crop": "Peach",
        "disease": "Bacterial Spot",
        "scientific_name": "Xanthomonas arboricola pv. pruni",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Small angular purple-brown spots that fall out, giving a 'shot-hole' appearance.",
            "Sunken, pitted dark lesions on fruit emitting gummy ooze.",
            "Severe leaf drop leading to sunburned fruit."
        ],
        "cause": "Bacterial infection entering through stomata or mechanical leaf wounds during warm wet spring.",
        "organic_treatment": [
            "Spray low-rate fixed copper formulations during dormant season and early spring.",
            "Apply Oxytetracycline bactericide under emergency agricultural approval."
        ],
        "chemical_treatment": [
            "Apply Oxytetracycline or Copper Hydroxide + Mancozeb starting at shuck-split."
        ],
        "prevention": [
            "Avoid high nitrogen applications that create succulent leaf tissue.",
            "Plant bacterial spot resistant varieties like 'Candor' or 'Bounty'."
        ]
    },
    "Peach___healthy": {
        "crop": "Peach",
        "disease": "Healthy",
        "scientific_name": "Prunus persica",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Long, lanceolate deep green leaves without shot-holes or spots."
        ],
        "cause": "Good soil conditions and proper tree pruning.",
        "organic_treatment": ["Maintain mulching ring around root zone."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Regular orchard inspection."]
    },
    "Pepper,_bell___Bacterial_spot": {
        "crop": "Pepper (Bell)",
        "disease": "Bacterial Spot",
        "scientific_name": "Xanthomonas euvesicatoria",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Small water-soaked dark spots on lower leaf surface expanding to dark brown.",
            "Leaves turn yellow and drop prematurely.",
            "Raised scab-like spots on green pepper fruits."
        ],
        "cause": "Seed-borne or soil-borne bacteria spread by wind-driven rain.",
        "organic_treatment": [
            "Spray copper soap bactericide mixed with neem oil.",
            "Soak seeds in hot water (122°F for 25 mins) prior to planting."
        ],
        "chemical_treatment": [
            "Apply Copper Sulfate combined with Mancozeb to overcome copper resistance."
        ],
        "prevention": [
            "Use certified pathogen-free seeds.",
            "Practice 3-year crop rotation avoiding Solanaceae family plants."
        ]
    },
    "Pepper,_bell___healthy": {
        "crop": "Pepper (Bell)",
        "disease": "Healthy",
        "scientific_name": "Capsicum annuum",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Smooth, dark green shiny leaves with upright robust stems."
        ],
        "cause": "Optimal soil moisture, warmth, and balanced fertilization.",
        "organic_treatment": ["Apply calcium nitrate foliar spray to prevent blossom end rot."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Use drip irrigation."]
    },
    "Potato___Early_blight": {
        "crop": "Potato",
        "disease": "Early Blight",
        "scientific_name": "Alternaria solani",
        "status": "Diseased",
        "severity": "Moderate to High",
        "symptoms": [
            "Dark brown concentric rings forming a 'target-board' pattern on older leaves.",
            "Yellow chlorotic halo surrounding leaf spots.",
            "Sunken dark brown spots on potato tubers."
        ],
        "cause": "Fungus surviving in soil and crop debris, favored by alternating wet and dry weather.",
        "organic_treatment": [
            "Apply copper octanoate or copper hydroxide spray every 7-10 days.",
            "Apply Bacillus subtilis bio-fungicide."
        ],
        "chemical_treatment": [
            "Spray Chlorothalonil, Mancozeb, or Azoxystrobin upon initial symptom detection."
        ],
        "prevention": [
            "Ensure proper nitrogen fertilization; stressed plants are more susceptible.",
            "Rotate crops with non-solanaceous species like corn or legumes."
        ]
    },
    "Potato___Late_blight": {
        "crop": "Potato",
        "disease": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "status": "Diseased",
        "severity": "Critical",
        "symptoms": [
            "Large water-soaked dark brown to black spots with pale green borders.",
            "White cottony fungal growth on leaf undersides in humid conditions.",
            "Rapid collapse of entire plant foliage and rot of tubers in storage."
        ],
        "cause": "Oomycete pathogen responsible for the Irish Potato Famine; spreads rapidly in cool, rainy weather.",
        "organic_treatment": [
            "Destroy and bury severely infected plants immediately.",
            "Apply preventative heavy copper hydroxide sprays before rainfall."
        ],
        "chemical_treatment": [
            "Apply systemic fungicides such as Metalaxyl, Dimethomorph, or Cyazofamid.",
            "Spray fluazinam protectant."
        ],
        "prevention": [
            "Plant certified disease-free seed potatoes.",
            "Eliminate cull piles and volunteer potato plants near fields."
        ]
    },
    "Potato___healthy": {
        "crop": "Potato",
        "disease": "Healthy",
        "scientific_name": "Solanum tuberosum",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Compound deep green leaves without concentric rings or dark decay spots."
        ],
        "cause": "Good soil aeration, proper hilling, and balanced nutrition.",
        "organic_treatment": ["Hill soil around stem bases."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Monitor foliage weekly."]
    },
    "Raspberry___healthy": {
        "crop": "Raspberry",
        "disease": "Healthy",
        "scientific_name": "Rubus idaeus",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Vibrant green serrated leaves with silvery underside."
        ],
        "cause": "Optimal cane management and soil moisture.",
        "organic_treatment": ["Mulch with wood chips."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Prune old fruited floricanes after harvest."]
    },
    "Soybean___healthy": {
        "crop": "Soybean",
        "disease": "Healthy",
        "scientific_name": "Glycine max",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Trifoliate clean green leaves with firm pod growth."
        ],
        "cause": "Good crop establishment and pest management.",
        "organic_treatment": ["Ensure Rhizobium inoculation at seeding."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Rotate with corn."]
    },
    "Squash___Powdery_mildew": {
        "crop": "Squash",
        "disease": "Powdery Mildew",
        "scientific_name": "Podosphaera xanthii",
        "status": "Diseased",
        "severity": "Moderate",
        "symptoms": [
            "Talculm-like white powdery dust spreading over upper and lower leaf surfaces.",
            "Leaves turn yellow, dry out, and become crisp.",
            "Sunburn on squash fruits due to lost leaf canopy cover."
        ],
        "cause": "Airborne fungal spores thriving in dry shade with high air humidity.",
        "organic_treatment": [
            "Spray baking soda solution (1 tbsp baking soda + 1 tsp liquid soap + 1 gal water).",
            "Spray potassium bicarbonate or neem oil."
        ],
        "chemical_treatment": [
            "Apply Myclobutanil, Trifloxystrobin, or Sulfur sprays."
        ],
        "prevention": [
            "Plant in full sun location with adequate plant spacing.",
            "Select resistant cultivars."
        ]
    },
    "Strawberry___Leaf_scorch": {
        "crop": "Strawberry",
        "disease": "Leaf Scorch",
        "scientific_name": "Diplocarpon earlianum",
        "status": "Diseased",
        "severity": "Moderate",
        "symptoms": [
            "Numerous small dark purple spots without light centers.",
            "Leaf margins turn brown and dry up, looking scorched by fire.",
            "Weakened plants and lower berry yield."
        ],
        "cause": "Fungus spreading by rain splashes in warm spring season.",
        "organic_treatment": [
            "Remove and burn spotted old leaves after harvest.",
            "Apply bio-fungicide Bacillus subtilis."
        ],
        "chemical_treatment": [
            "Spray Captan, Thiram, or Pyraclostrobin during spring growth."
        ],
        "prevention": [
            "Maintain narrow row width for rapid drying after rain.",
            "Use straw mulch to prevent soil splashing onto leaves."
        ]
    },
    "Strawberry___healthy": {
        "crop": "Strawberry",
        "disease": "Healthy",
        "scientific_name": "Fragaria × ananassa",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Trifoliate shiny dark green leaves with clean crown growth."
        ],
        "cause": "Optimal soil moisture and solar radiation.",
        "organic_treatment": ["Apply clean straw mulch around plants."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Replace strawberry beds every 3-4 years."]
    },
    "Tomato___Bacterial_spot": {
        "crop": "Tomato",
        "disease": "Bacterial Spot",
        "scientific_name": "Xanthomonas vesicatoria",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Small water-soaked dark brown spots with yellow borders on leaves.",
            "Blister-like dark scabs on green tomato fruit.",
            "Severe leaf drop exposing fruit to sunscald."
        ],
        "cause": "Bacteria surviving on seed, crop residue, or weeds.",
        "organic_treatment": [
            "Apply copper octanoate or fixed copper early in the morning.",
            "Spray bio-bactericide formulations."
        ],
        "chemical_treatment": [
            "Spray Copper Hydroxide combined with Mancozeb."
        ],
        "prevention": [
            "Use disease-free certified tomato seeds.",
            "Avoid handling foliage when plants are wet."
        ]
    },
    "Tomato___Early_blight": {
        "crop": "Tomato",
        "disease": "Early Blight",
        "scientific_name": "Alternaria solani",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Dark brown spots with concentric ring 'target' patterns on lower leaves first.",
            "Yellowing around lesions leading to leaf drop.",
            "Sunken leathery black spots at stem end of tomato fruit."
        ],
        "cause": "Soil-borne fungus favored by warm temperatures (75-85°F) and wet leaves.",
        "organic_treatment": [
            "Prune lower leaves up to 12 inches from ground level.",
            "Apply copper-based fungicides weekly.",
            "Mulch heavily around base with straw to block soil-to-leaf splashing."
        ],
        "chemical_treatment": [
            "Apply Chlorothalonil, Mancozeb, or Difenoconazole at initial symptom appearance."
        ],
        "prevention": [
            "Stake and cage tomato plants for vertical growth and air flow.",
            "Rotate tomato plots every 3 years."
        ]
    },
    "Tomato___Late_blight": {
        "crop": "Tomato",
        "disease": "Late Blight",
        "scientific_name": "Phytophthora infestans",
        "status": "Diseased",
        "severity": "Critical",
        "symptoms": [
            "Large irregular water-soaked dark gray-green oil spots on leaves.",
            "White fluffy downy mildew growth under the leaf surface.",
            "Firm brown greasy rot on tomato fruits."
        ],
        "cause": "Highly destructive water-mold pathogen spreading through wind and moisture.",
        "organic_treatment": [
            "Remove and bag infected plants immediately; do not compost.",
            "Apply heavy preventative copper soap formulations before rainfall events."
        ],
        "chemical_treatment": [
            "Apply Metalaxyl, Mandipropamid, or Chlorothalonil."
        ],
        "prevention": [
            "Avoid overhead irrigation; use drip tape exclusively.",
            "Destroy volunteer tomato and potato plants."
        ]
    },
    "Tomato___Leaf_Mold": {
        "crop": "Tomato",
        "disease": "Leaf Mold",
        "scientific_name": "Passalora fulva",
        "status": "Diseased",
        "severity": "Moderate",
        "symptoms": [
            "Pale green to yellow spots on upper leaf surface.",
            "Olive-green to velvety brown mold growth underneath the leaf.",
            "Leaves turn brown, curl, and wither."
        ],
        "cause": "Fungus prevalent in high humidity (>85%) greenhouse environments.",
        "organic_treatment": [
            "Increase ventilation and heating in greenhouses to reduce relative humidity.",
            "Spray copper-based organic fungicides."
        ],
        "chemical_treatment": [
            "Spray Difenoconazole, Chlorothalonil, or Copper Hydroxide."
        ],
        "prevention": [
            "Space plants generously to promote rapid drying.",
            "Grow resistant tomato cultivars."
        ]
    },
    "Tomato___Septoria_leaf_spot": {
        "crop": "Tomato",
        "disease": "Septoria Leaf Spot",
        "scientific_name": "Septoria lycopersici",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Numerous small circular spots (1/16 to 1/8 inch) with dark borders and tan centers.",
            "Tiny black specks (pycnidia) inside lesion centers.",
            "Leaves turn yellow and fall, starting from lower stems upward."
        ],
        "cause": "Fungus surviving in Solanaceous weed hosts and crop debris.",
        "organic_treatment": [
            "Remove infected lower leaves promptly.",
            "Spray copper soap fungicide every 7 days."
        ],
        "chemical_treatment": [
            "Spray Chlorothalonil, Mancozeb, or Azoxystrobin."
        ],
        "prevention": [
            "Mulch heavily around plant base.",
            "Keep foliage dry with drip irrigation."
        ]
    },
    "Tomato___Spider_mites Two-spotted_spider_mite": {
        "crop": "Tomato",
        "disease": "Two-Spotted Spider Mites",
        "scientific_name": "Tetranychus urticae",
        "status": "Diseased",
        "severity": "Moderate to High",
        "symptoms": [
            "Tiny yellow or white stippling dots across upper leaf surface.",
            "Fine silky webbing on leaf undersides and shoot tips.",
            "Leaves turn bronze, dry up, and drop off."
        ],
        "cause": "Arachnid pests thriving in hot, dry, dusty environmental conditions.",
        "organic_treatment": [
            "Release predatory mites (Phytoseiulus persimilis).",
            "Spray insecticidal soap, neem oil, or rosemary oil sprays targeting leaf undersides."
        ],
        "chemical_treatment": [
            "Apply Abamectin, Bifenazate, or Spiromesifen miticides."
        ],
        "prevention": [
            "Hose down dusty plant foliage periodically with water.",
            "Avoid overuse of broad-spectrum synthetic insecticides that kill natural predators."
        ]
    },
    "Tomato___Target_Spot": {
        "crop": "Tomato",
        "disease": "Target Spot",
        "scientific_name": "Corynespora cassiicola",
        "status": "Diseased",
        "severity": "Moderate",
        "symptoms": [
            "Small pinpoint necrotic spots expanding into circular lesions with light brown centers.",
            "Concentric rings resembling a target board on leaves and stems.",
            "Sunken rubbery lesions on mature fruit."
        ],
        "cause": "Fungus favored by warm temperatures (68-90°F) and high relative humidity.",
        "organic_treatment": [
            "Apply copper hydroxide fungicides.",
            "Prune lower infected foliage."
        ],
        "chemical_treatment": [
            "Apply Chlorothalonil, Azoxystrobin, or Fluxapyroxad."
        ],
        "prevention": [
            "Ensure proper crop spacing and weed management."
        ]
    },
    "Tomato___Tomato_Yellow_Leaf_Curl_Virus": {
        "crop": "Tomato",
        "disease": "Tomato Yellow Leaf Curl Virus (TYLCV)",
        "scientific_name": "Begomovirus TYLCV",
        "status": "Diseased",
        "severity": "Severe",
        "symptoms": [
            "Leaves curl dramatically upward and inward with yellow (chlorotic) margins.",
            "Severe plant stunting and bushy top appearance.",
            "Complete flower drop resulting in zero fruit yield."
        ],
        "cause": "Plant virus transmitted exclusively by the Silverleaf Whitefly (Bemisia tabaci).",
        "organic_treatment": [
            "Use yellow sticky traps to catch whitefly vectors.",
            "Spray neem oil or horticultural oil to smother whiteflies.",
            "Cover young transplants with insect exclusion mesh screens."
        ],
        "chemical_treatment": [
            "Apply Imidacloprid, Acetamiprid, or Dinotefuran systemic insecticides to control whitefly vector population."
        ],
        "prevention": [
            "Plant TYLCV-resistant tomato hybrids (e.g. 'Tycoon', 'Inbar').",
            "Remove viral-infected plants immediately to prevent vector pickup."
        ]
    },
    "Tomato___Tomato_mosaic_virus": {
        "crop": "Tomato",
        "disease": "Tomato Mosaic Virus (ToMV)",
        "scientific_name": "Tobamovirus ToMV",
        "status": "Diseased",
        "severity": "High",
        "symptoms": [
            "Light and dark green mottled 'mosaic' pattern on leaves.",
            "Leaf distortion, blistering, and fern-like leaf growth.",
            "Internal brown necrosis inside fruit tissue."
        ],
        "cause": "Extremely stable virus spread mechanically via hands, tools, and tobacco products.",
        "organic_treatment": [
            "No chemical cure exists for viral plant infections.",
            "Remove and burn infected plants immediately."
        ],
        "chemical_treatment": [
            "Disinfect hands and tools with 20% non-fat dry milk solution or 10% trisodium phosphate."
        ],
        "prevention": [
            "Prohibit smoking or tobacco use near tomato plants.",
            "Plant mosaic-resistant tomato varieties."
        ]
    },
    "Tomato___healthy": {
        "crop": "Tomato",
        "disease": "Healthy",
        "scientific_name": "Solanum lycopersicum",
        "status": "Healthy",
        "severity": "None",
        "symptoms": [
            "Lush deep green compound leaves without spots, curling, or yellow mottling."
        ],
        "cause": "Optimal care, nutrition, and pest control.",
        "organic_treatment": ["Apply organic fish emulsion fertilizer every 2 weeks."],
        "chemical_treatment": ["None needed."],
        "prevention": ["Maintain consistent drip watering schedule."]
    }
}

DEFAULT_INFO = {
    "crop": "Unknown Plant",
    "disease": "Unclassified Leaf Condition",
    "scientific_name": "Flora incertae sedis",
    "status": "Requires Review",
    "severity": "Unknown",
    "symptoms": ["Unusual leaf discoloration or texture detected."],
    "cause": "Potential environmental stress or rare fungal/bacterial strain.",
    "organic_treatment": ["Isolate plant and apply broad-spectrum organic neem oil spray."],
    "chemical_treatment": ["Consult local agricultural extension center for tissue sampling."],
    "prevention": ["Ensure proper soil drainage and avoid foliage moisture."]
}

def get_disease_info(label_key):
    """Retrieve full disease details from knowledge base key."""
    return DISEASE_KNOWLEDGE_BASE.get(label_key, DEFAULT_INFO)
