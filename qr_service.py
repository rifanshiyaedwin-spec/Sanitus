"""
qr_service.py - QR Code Generator Service for Agro-Medicines
Generates printable SVG/DataURI QR codes linking to usage guides and video tutorials on https://plantasanitus.com.
"""

import urllib.parse

DOMAIN_URL = "https://plantasanitus.com"

def generate_product_qr_code(product_id, product_name):
    """
    Generate Data URI QR Code URL pointing to product instruction page on plantasanitus.com.
    """
    target_url = f"{DOMAIN_URL}/product/{product_id}"
    encoded_url = urllib.parse.quote(target_url)
    qr_image_url = f"https://api.qrserver.com/v1/create-qr-code/?size=160x160&data={encoded_url}"
    return {
        "qr_image_url": qr_image_url,
        "target_url": target_url
    }
