"""
generate_samples.py - Utility to generate sample leaf images for instant 1-click UI demos.
"""

import os
import numpy as np
from PIL import Image, ImageDraw

SAMPLES_DIR = os.path.join(os.path.dirname(__file__), "static", "samples")
os.makedirs(SAMPLES_DIR, exist_ok=True)

def create_leaf_sample(filename, bg_color, vein_color, spot_color=None, spots_count=0):
    img = Image.new("RGB", (400, 400), (245, 247, 248))
    draw = ImageDraw.Draw(img)
    
    # Draw realistic leaf shape (ellipse / polygon)
    leaf_shape = [(200, 40), (320, 160), (340, 260), (200, 360), (60, 260), (80, 160)]
    draw.polygon(leaf_shape, fill=bg_color, outline=(30, 80, 40))
    
    # Draw central midrib stem and side veins
    draw.line([(200, 40), (200, 375)], fill=vein_color, width=4)
    for y in range(80, 340, 40):
        draw.line([(200, y), (130, y - 30)], fill=vein_color, width=2)
        draw.line([(200, y), (270, y - 30)], fill=vein_color, width=2)
        
    # Draw disease spots if specified
    if spot_color and spots_count > 0:
        np.random.seed(42)
        for _ in range(spots_count):
            rx = np.random.randint(120, 280)
            ry = np.random.randint(90, 310)
            radius = np.random.randint(6, 20)
            draw.ellipse([rx - radius, ry - radius, rx + radius, ry + radius], fill=spot_color, outline=(20, 20, 20))

    img_path = os.path.join(SAMPLES_DIR, filename)
    img.save(img_path, "JPEG", quality=92)
    print(f"[Generated] Sample leaf image: {img_path}")

if __name__ == "__main__":
    # Apple Scab: Dark olive leaf with brownish-black velvet spots
    create_leaf_sample("apple_scab.jpg", bg_color=(75, 110, 50), vein_color=(45, 75, 30), spot_color=(50, 40, 30), spots_count=22)
    
    # Tomato Late Blight: Mid-green leaf with dark brown/black oil spots
    create_leaf_sample("tomato_late_blight.jpg", bg_color=(85, 135, 60), vein_color=(55, 95, 40), spot_color=(40, 30, 25), spots_count=18)
    
    # Corn Common Rust: Elongated green leaf with cinnamon reddish-brown rust pustules
    create_leaf_sample("corn_common_rust.jpg", bg_color=(90, 140, 50), vein_color=(60, 100, 30), spot_color=(180, 65, 30), spots_count=35)
    
    # Potato Healthy: Vibrant lush dark green leaf without spots
    create_leaf_sample("potato_healthy.jpg", bg_color=(34, 139, 34), vein_color=(20, 90, 20), spot_color=None, spots_count=0)
