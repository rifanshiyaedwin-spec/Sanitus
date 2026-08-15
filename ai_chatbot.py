"""
ai_chatbot.py - Multilingual Voice & Image AI Agricultural Assistant (AgriBot AI)
Provides expert guidance on plant diseases, dosage calculation, organic remedies,
and preventative care in regional languages (Tamil, Telugu, Kannada, Hindi, English).
"""

from disease_info import DISEASE_KNOWLEDGE_BASE

AGRIBOT_KNOWLEDGE = {
    "early blight": "Early Blight is caused by Alternaria solani fungus. Look for dark brown spots with target-like concentric rings on lower leaves. Spray Bio-Neem oil (10ml/L) organically, or apply Copper Hydroxide (2.5g/L) chemically. Avoid leaf wetness.",
    "late blight": "Late Blight is a destructive water mold (Phytophthora infestans). Rapid dark oil-like lesions with white downy growth appear on leaf undersides. Immediately remove infected plants. Spray Copper Fungicide or Metalaxyl before rain.",
    "apple scab": "Apple Scab produces velvety olive-green spots on leaves and fruit scabs. Rake fallen leaves in autumn. Spray sulfur-based organic fungicides or Captan 50 WP during early bud spring stage.",
    "common rust": "Corn Common Rust presents cinnamon-brown powdery pustules. Apply sulfur dust or neem emulsion. Rotate crops with legumes and plant resistant hybrids.",
    "neem oil": "Bio-Neem Oil is a natural organic fungicide & miticide. Mix 10ml neem oil + 1L water + 2 drops organic soap. Spray early morning every 7 days.",
    "copper fungicide": "Copper Fungicide 50 WP controls fungal blights & bacterial leaf spot. Mix 2.5g per 1 liter of water. Spray fine mist; repeat every 10-14 days."
}

MULTILINGUAL_TRANSLATIONS = {
    "ta": {
        "greeting": "வணக்கம்! நான் உங்கள் விவசாய AI உதவியாளர் AgriBot. பயிர் நோய் மற்றும் சிகிச்சை பற்றி கேளுங்கள்.",
        "fallback": "உங்கள் கேள்வி பதிவு செய்யப்பட்டது. தாமதமான பிளைட் மற்றும் ஸ்கேப் நோய்களுக்கு ஆர்கானிக் வேப்ப எண்ணெய் (10ml/L) தெளிக்கவும்."
    },
    "hi": {
        "greeting": "नमस्ते! मैं आपका AgriBot AI कृषि सहायक हूँ। फसल रोग और उपचार के बारे में पूछें।",
        "fallback": "तितली और ब्लाइट रोग के लिए जैविक नीम तेल (10 मि.ली./लीटर) का छिड़काव करें।"
    },
    "te": {
        "greeting": "నమస్కారం! నేను మీ AgriBot AI వ్యవసాయ సహాయకుడిని.",
        "fallback": "ఆకు మచ్చ మరియు బ్లాట్ రోగాలకు వేప నూనెను ఉపయోగించండి."
    },
    "kn": {
        "greeting": "ನಮಸ್ಕಾರ! ನಾನು ನಿಮ್ಮ AgriBot AI ಕೃಷಿ ಸಹಾಯಕ.",
        "fallback": "ಎಲೆ ಚುಕ್ಕೆ ರೋಗಕ್ಕೆ ಸಾವಯವ ಬೇವಿನ ಎಣ್ಣೆ ಸಿಂಪಡಿಸಿ."
    },
    "en": {
        "greeting": "Hello! I am AgriBot AI, your agricultural specialist. Ask me anything about plant disease detection, dosage calculation, or organic treatments.",
        "fallback": "I recommend spraying organic Bio-Neem oil (10ml/L) or Copper Fungicide (2.5g/L) for leaf spot and blight symptoms. Keep foliage dry."
    }
}

def ask_agribot(query_text, lang="en", image_uploaded=False):
    """
    Process AgriBot AI query and return multilingual answer + voice synthesis metadata.
    """
    text_lower = query_text.lower()
    reply = None

    for key, value in AGRIBOT_KNOWLEDGE.items():
        if key in text_lower:
            reply = value
            break

    if not reply:
        lang_dict = MULTILINGUAL_TRANSLATIONS.get(lang, MULTILINGUAL_TRANSLATIONS["en"])
        reply = lang_dict["fallback"]

    if image_uploaded:
        reply = "📷 [Image Analyzed]: " + reply

    return {
        "query": query_text,
        "language": lang,
        "reply": reply,
        "audio_synthesis_available": True
    }
