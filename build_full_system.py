# PULSE AUDIO - Complete Mobile-First Dynamic Store Generator
import os
import json

# 1. Generate Supplementary SVG Images
images = {
    'charger-black.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e293b"/></linearGradient>
    <linearGradient id="bodyGrad" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#27272a"/><stop offset="100%" stop-color="#09090b"/></linearGradient>
  </defs>
  <rect width="600" height="600" fill="url(#bgGrad)"/>
  <circle cx="300" cy="300" r="220" fill="#6366f1" opacity="0.07"/>
  <rect x="180" y="160" width="240" height="280" rx="36" fill="url(#bodyGrad)" stroke="#3f3f46" stroke-width="4"/>
  <rect x="230" y="100" width="28" height="60" rx="8" fill="#71717a"/>
  <rect x="342" y="100" width="28" height="60" rx="8" fill="#71717a"/>
  <rect x="220" y="340" width="160" height="36" rx="10" fill="#09090b" stroke="#f59e0b" stroke-width="2"/>
  <text x="300" y="363" fill="#f59e0b" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">TYPE-C 33W GaN</text>
  <rect x="240" y="390" width="120" height="24" rx="6" fill="#09090b" stroke="#6366f1" stroke-width="2"/>
  <text x="300" y="407" fill="#6366f1" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">USB-A 18W QC3.0</text>
  <text x="300" y="240" fill="#ffffff" font-family="sans-serif" font-size="24" font-weight="900" text-anchor="middle" letter-spacing="4">PULSE</text>
  <text x="300" y="265" fill="#a1a1aa" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2">HYPERCHARGE 33W</text>
</svg>''',

    'charger-white.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgGradW" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#f8fafc"/><stop offset="100%" stop-color="#e2e8f0"/></linearGradient>
    <linearGradient id="bodyGradW" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#ffffff"/><stop offset="100%" stop-color="#f1f5f9"/></linearGradient>
  </defs>
  <rect width="600" height="600" fill="url(#bgGradW)"/>
  <circle cx="300" cy="300" r="220" fill="#6366f1" opacity="0.08"/>
  <rect x="180" y="160" width="240" height="280" rx="36" fill="url(#bodyGradW)" stroke="#cbd5e1" stroke-width="4"/>
  <rect x="230" y="100" width="28" height="60" rx="8" fill="#94a3b8"/>
  <rect x="342" y="100" width="28" height="60" rx="8" fill="#94a3b8"/>
  <rect x="220" y="340" width="160" height="36" rx="10" fill="#0f172a" stroke="#f59e0b" stroke-width="2"/>
  <text x="300" y="363" fill="#f59e0b" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle">TYPE-C 33W GaN</text>
  <rect x="240" y="390" width="120" height="24" rx="6" fill="#0f172a" stroke="#6366f1" stroke-width="2"/>
  <text x="300" y="407" fill="#6366f1" font-family="sans-serif" font-size="11" font-weight="bold" text-anchor="middle">USB-A 18W QC3.0</text>
  <text x="300" y="240" fill="#0f172a" font-family="sans-serif" font-size="24" font-weight="900" text-anchor="middle" letter-spacing="4">PULSE</text>
  <text x="300" y="265" fill="#64748b" font-family="sans-serif" font-size="12" font-weight="700" text-anchor="middle" letter-spacing="2">HYPERCHARGE 33W</text>
</svg>''',

    'powerbank-black.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgPB" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#09090b"/><stop offset="100%" stop-color="#18181b"/></linearGradient>
    <linearGradient id="pbBody" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#27272a"/><stop offset="100%" stop-color="#18181b"/></linearGradient>
  </defs>
  <rect width="600" height="600" fill="url(#bgPB)"/>
  <circle cx="300" cy="300" r="230" fill="#06b6d4" opacity="0.08"/>
  <rect x="170" y="110" width="260" height="380" rx="28" fill="url(#pbBody)" stroke="#3f3f46" stroke-width="3"/>
  <rect x="230" y="150" width="140" height="50" rx="12" fill="#09090b" stroke="#06b6d4" stroke-width="1.5"/>
  <text x="300" y="183" fill="#06b6d4" font-family="monospace" font-size="26" font-weight="bold" text-anchor="middle">100%</text>
  <text x="300" y="290" fill="#ffffff" font-family="sans-serif" font-size="28" font-weight="900" text-anchor="middle" letter-spacing="5">PULSE</text>
  <text x="300" y="325" fill="#06b6d4" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" letter-spacing="2">POWERMAX 20000mAh</text>
  <text x="300" y="350" fill="#71717a" font-family="sans-serif" font-size="12" text-anchor="middle">22.5W Two-Way Fast Charge</text>
  <rect x="210" y="430" width="40" height="20" rx="4" fill="#09090b" stroke="#f59e0b" stroke-width="1"/>
  <rect x="280" y="430" width="40" height="20" rx="4" fill="#09090b" stroke="#06b6d4" stroke-width="1"/>
  <rect x="350" y="430" width="40" height="20" rx="4" fill="#09090b" stroke="#f59e0b" stroke-width="1"/>
</svg>''',

    'cable-black.svg': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 600 600" width="100%" height="100%">
  <defs>
    <linearGradient id="bgCab" x1="0%" y1="0%" x2="100%" y2="100%"><stop offset="0%" stop-color="#0f172a"/><stop offset="100%" stop-color="#1e293b"/></linearGradient>
  </defs>
  <rect width="600" height="600" fill="url(#bgCab)"/>
  <circle cx="300" cy="300" r="200" fill="#8b5cf6" opacity="0.1"/>
  <circle cx="300" cy="300" r="130" fill="none" stroke="#334155" stroke-width="22" stroke-dasharray="14 6"/>
  <circle cx="300" cy="300" r="100" fill="none" stroke="#1e293b" stroke-width="22" stroke-dasharray="14 6"/>
  <rect x="380" y="210" width="90" height="36" rx="10" fill="#475569" stroke="#8b5cf6" stroke-width="3" transform="rotate(35 425 228)"/>
  <rect x="130" y="350" width="90" height="36" rx="10" fill="#475569" stroke="#8b5cf6" stroke-width="3" transform="rotate(35 175 368)"/>
  <text x="300" y="295" fill="#ffffff" font-family="sans-serif" font-size="24" font-weight="900" text-anchor="middle" letter-spacing="4">PULSE</text>
  <text x="300" y="320" fill="#8b5cf6" font-family="sans-serif" font-size="14" font-weight="bold" text-anchor="middle" letter-spacing="1">100W TYPE-C TO C</text>
</svg>'''
}

os.makedirs('frontend/assets/images', exist_ok=True)
for fname, content in images.items():
    with open(os.path.join('frontend/assets/images', fname), 'w', encoding='utf-8') as f:
        f.write(content)
print('Generated supplementary SVG assets.')

# 2. Update seed_data.py with rich multi-product catalogue
SEED_DATA_CODE = '''from backend.app.database import SessionLocal, engine, Base
from backend.app.models.product import Product

PINCODE_DATA = {
    '110001': {'city': 'New Delhi', 'state': 'Delhi', 'days': '2-3 business days'},
    '110020': {'city': 'South Delhi', 'state': 'Delhi', 'days': '2-3 business days'},
    '400001': {'city': 'Mumbai', 'state': 'Maharashtra', 'days': '2-3 business days'},
    '400050': {'city': 'Bandra, Mumbai', 'state': 'Maharashtra', 'days': '2-3 business days'},
    '560001': {'city': 'Bengaluru', 'state': 'Karnataka', 'days': '2-3 business days'},
    '560034': {'city': 'Koramangala, Bengaluru', 'state': 'Karnataka', 'days': '2-3 business days'},
    '560038': {'city': 'Indiranagar, Bengaluru', 'state': 'Karnataka', 'days': '2-3 business days'},
    '600001': {'city': 'Chennai', 'state': 'Tamil Nadu', 'days': '3-4 business days'},
    '700001': {'city': 'Kolkata', 'state': 'West Bengal', 'days': '3-4 business days'},
    '500001': {'city': 'Hyderabad', 'state': 'Telangana', 'days': '2-3 business days'},
    '380001': {'city': 'Ahmedabad', 'state': 'Gujarat', 'days': '2-3 business days'},
    '411001': {'city': 'Pune', 'state': 'Maharashtra', 'days': '2-3 business days'},
    '302001': {'city': 'Jaipur', 'state': 'Rajasthan', 'days': '3-4 business days'},
    '226001': {'city': 'Lucknow', 'state': 'Uttar Pradesh', 'days': '3-4 business days'},
    '682001': {'city': 'Kochi', 'state': 'Kerala', 'days': '3-5 business days'},
    '160017': {'city': 'Chandigarh', 'state': 'Punjab', 'days': '2-3 business days'}
}

PRODUCTS_SEED = [
    {
        'slug': 'pulse-sonic-pro',
        'sku': 'PA-TW3500-BLK',
        'name': 'Pulse Sonic Pro ANC True Wireless Earbuds',
        'tagline': '35dB Hybrid ANC • 13mm Titanium Drivers • 40H Monster Battery • 45ms Gaming',
        'brand': 'PULSE AUDIO',
        'category': 'TWS Earbuds',
        'mrp': 2999.0,
        'price': 1499.0,
        'discount_percent': 50,
        'stock': 28,
        'rating': 4.8,
        'review_count': 14820,
        'description': 'Experience studio-grade acoustic depth and powerful punchy bass with the Pulse Sonic Pro ANC Earbuds. Engineered with custom 13mm Titanium drivers, ultra-responsive smart touch sensors, 35dB Hybrid Active Noise Cancellation, Quad-Mic AI Environmental Noise Cancellation, and 40 hours of combined playtime. Designed for creators, gamers, and audiophiles.',
        'highlights': [
            '35dB Hybrid Active Noise Cancellation (ANC)',
            '13mm Titanium Dynamic Acoustic Drivers with PulseBass™',
            '40 Hours Total Playtime (8H Buds + 32H Fast Type-C Case)',
            'Quad-Mic ENC with AI Noise Reduction for Crystal Calls',
            '45ms Beast™ Ultra-Low Latency Dedicated Gaming Mode',
            'Bluetooth v5.3 + Insta-Wake N\\' Pair Instant Connection',
            'Type-C Turbo Fast Charge (10 Mins = 120 Mins Playtime)',
            'IPX4 Sweat & Splash Resistant Ergonomic Fit'
        ],
        'specifications': {
            'Acoustics & Sound': {
                'Driver Size': '13mm Titanium Dynamic Acoustic Drivers',
                'Frequency Response': '20Hz - 20,000Hz Ultra-Wide Audio Stage',
                'Active Noise Cancellation': 'Up to 35dB Hybrid ANC + Transparency Ambient Mode',
                'Microphone Array': '4 x MEMS Microphones with AI-ENC Noise Filter',
                'Audio Codecs': 'AAC, SBC High-Definition Decoding'
            },
            'Connectivity': {
                'Bluetooth Version': 'v5.3 + EDR (15m Unobstructed Range)',
                'Gaming Latency': '45ms Dedicated Ultra-Low Latency Mode',
                'Pairing Protocol': 'Insta-Wake N\\' Pair Hall Switch Sensor',
                'Compatibility': 'Universal (Android, iOS, Windows, macOS)'
            },
            'Battery & Charging': {
                'Earbud Playtime': 'Up to 8 Hours per charge (at 60% volume)',
                'Charging Case Playtime': 'Additional 32 Hours (4 full recharges)',
                'Total Battery': '40 Hours Playtime',
                'Fast Charging': '10 Mins Type-C Charge = 120 Mins Playtime',
                'Charging Port': 'USB Type-C (Cable Included)'
            },
            'Build & Warranty': {
                'Earbud Weight': '3.8g Featherlight Ergonomic Fit',
                'Water Resistance': 'IPX4 Splash & Sweat Proof',
                'Warranty': '1 Year Comprehensive Brand Replacement Warranty'
            }
        },
        'box_contents': [
            '1x Pair of Pulse Sonic Pro ANC Earbuds',
            '1x Pocket-friendly Smart Charging Case',
            '3x Pairs of Soft Silicone Eartips (S, M, L)',
            '1x Type-C Fast Charging Cable',
            '1x Quick Start Guide & Warranty Registration Card'
        ],
        'warranty_info': '1 Year Official Pulse Brand Replacement Warranty with Free Doorstep Pickup',
        'variants': [
            {
                'id': 'midnight-obsidian',
                'name': 'Midnight Obsidian (Matte Black)',
                'color_code': '#1a1b1e',
                'badge': 'Bestseller',
                'image': '/assets/images/earbuds-black.svg',
                'stock': 28,
                'in_stock': True
            },
            {
                'id': 'forest-emerald',
                'name': 'Forest Emerald (Deep Green)',
                'color_code': '#064e3b',
                'badge': 'Trending',
                'image': '/assets/images/earbuds-green.svg',
                'stock': 14,
                'in_stock': True
            },
            {
                'id': 'arctic-ivory',
                'name': 'Arctic Ivory (Ceramic White)',
                'color_code': '#f8fafc',
                'badge': 'Classic',
                'image': '/assets/images/earbuds-white.svg',
                'stock': 19,
                'in_stock': True
            }
        ],
        'gallery_images': [
            {'id': 'main', 'title': 'Overview', 'url': '/assets/images/earbuds-black.svg', 'caption': 'Pulse Sonic Pro ANC with Matte Charging Case'},
            {'id': 'case', 'title': 'Charging Case', 'url': '/assets/images/earbuds-case.svg', 'caption': '40H Monster Battery Case with Type-C'},
            {'id': 'driver', 'title': '13mm Driver', 'url': '/assets/images/earbuds-driver.svg', 'caption': 'Custom 13mm Titanium Diaphragm for Deep Bass'},
            {'id': 'anc', 'title': '35dB ANC', 'url': '/assets/images/earbuds-anc.svg', 'caption': '35dB Hybrid Noise Cancellation Waveforms'},
            {'id': 'ipx4', 'title': 'IPX4 Proof', 'url': '/assets/images/earbuds-ipx4.svg', 'caption': 'IPX4 Sweat and Splash Proof Protection'},
            {'id': 'lifestyle', 'title': 'Ergonomic Fit', 'url': '/assets/images/earbuds-lifestyle.svg', 'caption': '3.8g Ultra-lightweight Ergonomic Ear Fit'}
        ],
        'faq': [
            {'q': 'Does Active Noise Cancellation work on both Android and iOS?', 'a': 'Yes! The 35dB Hybrid ANC is hardware-powered directly on the earbuds. It functions seamlessly across all Bluetooth devices without third-party apps.'},
            {'q': 'How do I claim the 1-Year Doorstep Warranty?', 'a': 'Every Pulse Sonic Pro comes with a 1-Year Comprehensive Replacement Warranty. Simply email support@pulse-audio.in with your Order ID for hassle-free doorstep pickup.'},
            {'q': 'How does the PREPAID100 discount coupon work?', 'a': 'When you choose UPI or Online Payment at checkout, coupon PREPAID100 is automatically applied, reducing your total payable price by ₹100 from ₹1,499 down to ₹1,399.'}
        ],
        'reviews': [
            {'name': 'Aditya Kulkarni', 'city': 'Bengaluru', 'rating': 5, 'date': '2 days ago', 'variant': 'Midnight Obsidian', 'title': 'Absolute game changer for the price. ANC is remarkably effective!', 'body': 'I was skeptical about 35dB ANC at under ₹1,500, but these genuinely block out the bus AC and metro drone during my daily commute. Bass is punchy without distorting vocals. Highly recommend!'},
            {'name': 'Pooja Sharma', 'city': 'Delhi NCR', 'rating': 5, 'date': '5 days ago', 'variant': 'Forest Emerald', 'title': 'Super premium look and incredible mic quality for work calls', 'body': 'The Forest Emerald finish looks stunning in real life. I use it for daily 4-5 hours of Zoom and Microsoft Teams calls, and my colleagues report zero background ambient disturbance.'},
            {'name': 'Rahul Verma', 'city': 'Mumbai', 'rating': 5, 'date': '1 week ago', 'variant': 'Arctic Ivory', 'title': 'Gaming mode is phenomenal! Zero noticeable latency in BGMI', 'body': 'Triple-tap toggles Beast Gaming Mode. Gunshots and footsteps are perfectly synced with zero lag. Battery easily lasts 4-5 days of heavy use.'}
        ],
        'is_active': True
    },
    {
        'slug': 'pulse-hypercharge-33w',
        'sku': 'PA-CH33W-BLK',
        'name': 'Pulse HyperCharge 33W GaN Dual-Port Fast Charger',
        'tagline': 'Gallium Nitride (GaN) Tech • 33W Type-C Power Delivery • 18W QC3.0 USB-A • Ultra Compact',
        'brand': 'PULSE AUDIO',
        'category': 'Chargers',
        'mrp': 1799.0,
        'price': 899.0,
        'discount_percent': 50,
        'stock': 42,
        'rating': 4.9,
        'review_count': 6410,
        'description': 'Power up your smartphones, tablets, and TWS earbuds at lightning speed with the Pulse HyperCharge 33W GaN Fast Charger. Powered by next-gen Gallium Nitride semiconductors for 50% smaller size and superior thermal dissipation. Dual output ports let you charge two devices concurrently with full voltage protection.',
        'highlights': [
            'Next-Gen GaN III Technology for cool, efficient fast charging',
            '33W Max Power Delivery (PD 3.0) via Type-C Port',
            '18W Quick Charge (QC 3.0) via USB-A Port',
            'Charges iPhone & Android up to 60% in just 30 Minutes',
            'Multi-layer SafeCharge™ Surge, Overheat & Short-Circuit Protection',
            'BIS Certified for Indian Wall Sockets'
        ],
        'specifications': {
            'Power & Output': {
                'Total Wattage': '33W Maximum Output',
                'Type-C Output (PD 3.0)': '5V/3A, 9V/3A, 11V/3A, 12V/2.5A, 15V/2A, 20V/1.5A (33W Max)',
                'USB-A Output (QC 3.0)': '5V/3A, 9V/2A, 12V/1.5A (18W Max)',
                'Combined Dual Output': '5V/3.4A (Smart Power Distribution)'
            },
            'Compatibility & Certifications': {
                'Fast Charging Protocols': 'PD 3.0, QC 3.0, PPS, AFC, FCP, Apple 2.4A',
                'Supported Devices': 'iPhones, Samsung, OnePlus, Xiaomi, iPads, Earbuds, Smartwatches',
                'Certifications': 'BIS Certified (India), CE, FCC, RoHS'
            }
        },
        'box_contents': [
            '1x Pulse HyperCharge 33W GaN Charger',
            '1x User Manual & 1-Year Warranty Card'
        ],
        'warranty_info': '1 Year Official Pulse Brand Replacement Warranty',
        'variants': [
            {
                'id': 'matte-black',
                'name': 'Matte Black',
                'color_code': '#18181b',
                'badge': 'Popular',
                'image': '/assets/images/charger-black.svg',
                'stock': 42,
                'in_stock': True
            },
            {
                'id': 'glacier-white',
                'name': 'Glacier White',
                'color_code': '#f8fafc',
                'badge': 'Clean',
                'image': '/assets/images/charger-white.svg',
                'stock': 25,
                'in_stock': True
            }
        ],
        'gallery_images': [
            {'id': 'main', 'title': 'Overview', 'url': '/assets/images/charger-black.svg', 'caption': 'Pulse HyperCharge 33W GaN Dual Port'},
            {'id': 'white', 'title': 'Glacier White', 'url': '/assets/images/charger-white.svg', 'caption': 'Compact Portable Design'}
        ],
        'faq': [
            {'q': 'Can this charge iPhones at full 20W/27W speeds?', 'a': 'Yes! The Type-C port supports Power Delivery 3.0 and will fast charge iPhone 13, 14, 15, and 16 models at their maximum supported speeds.'}
        ],
        'reviews': [
            {'name': 'Vikram Mehra', 'city': 'Hyderabad', 'rating': 5, 'date': '3 days ago', 'variant': 'Matte Black', 'title': 'Extremely compact and charges phone in 30 mins!', 'body': 'Much smaller than my original phone brick and doesn\\'t heat up at all. Charges both my phone and watch at the same time.'}
        ],
        'is_active': True
    },
    {
        'slug': 'pulse-powermax-20k',
        'sku': 'PA-PB20K-BLK',
        'name': 'Pulse PowerMax 20000mAh 22.5W Fast Power Bank',
        'tagline': '20000mAh High-Density Polymer • 22.5W Two-Way Fast Charge • LED Digital Display',
        'brand': 'PULSE AUDIO',
        'category': 'Power Banks',
        'mrp': 3499.0,
        'price': 1699.0,
        'discount_percent': 51,
        'stock': 35,
        'rating': 4.8,
        'review_count': 4280,
        'description': 'Never run out of power on the go with the Pulse PowerMax 20000mAh Power Bank. Delivers 22.5W two-way fast charging with real-time numeric LED percentage display, dual USB-A + Type-C ports, and aircraft-safe flight compliance.',
        'highlights': [
            '20000mAh High-Density Lithium-Polymer Battery',
            '22.5W Super Fast Charging Output (PD + QC 3.0)',
            'Real-Time LED Numeric Battery Indicator Screen',
            'Triple Output (Charge 3 devices simultaneously)',
            'Aircraft Flight Safe Approved (Under 100Wh)',
            '12-Layer Smart IC Protection Circuitry'
        ],
        'specifications': {
            'Battery & Power': {
                'Battery Capacity': '20,000mAh / 74Wh (Aircraft Friendly)',
                'Input Ports': 'Type-C (18W Max) & Micro-USB (18W Max)',
                'Output Ports': '1x Type-C (20W PD) + 2x USB-A (22.5W SuperCharge)',
                'Recharge Time': 'Approx 4.5 Hours with 18W/33W fast adapter'
            }
        },
        'box_contents': [
            '1x Pulse PowerMax 20000mAh Power Bank',
            '1x Short Type-C Fast Charging Cable',
            '1x User Manual & Warranty Card'
        ],
        'warranty_info': '1 Year Comprehensive Brand Replacement Warranty',
        'variants': [
            {
                'id': 'stealth-black',
                'name': 'Stealth Black',
                'color_code': '#09090b',
                'badge': 'Bestseller',
                'image': '/assets/images/powerbank-black.svg',
                'stock': 35,
                'in_stock': True
            }
        ],
        'gallery_images': [
            {'id': 'main', 'title': 'Overview', 'url': '/assets/images/powerbank-black.svg', 'caption': 'Pulse PowerMax 20000mAh with LED Display'}
        ],
        'faq': [
            {'q': 'Can I carry this on domestic and international flights?', 'a': 'Yes! At 74Wh, it is fully compliant with DGCA and FAA airline regulations for carry-on cabin baggage.'}
        ],
        'reviews': [
            {'name': 'Sameer Joshi', 'city': 'Pune', 'rating': 5, 'date': '4 days ago', 'variant': 'Stealth Black', 'title': 'Charges my phone 4 times full!', 'body': 'The LED percentage display is super handy. Highly reliable during travel.'}
        ],
        'is_active': True
    },
    {
        'slug': 'pulse-armorcable-c',
        'sku': 'PA-CB100W-BLK',
        'name': 'Pulse ArmorCable 100W Braided Type-C to Type-C Fast Cable (1.5m)',
        'tagline': '100W Power Delivery (5A) • E-Marker Smart Chip • Double-Braided Military Grade Nylon',
        'brand': 'PULSE AUDIO',
        'category': 'Cables & Accessories',
        'mrp': 899.0,
        'price': 399.0,
        'discount_percent': 55,
        'stock': 85,
        'rating': 4.9,
        'review_count': 8920,
        'description': 'Built to outlast standard charging cords, the Pulse ArmorCable 100W is reinforced with military-grade ballistic nylon braiding, aluminum alloy connectors, and an intelligent E-Marker chip that safely manages up to 100W 5A fast charging for laptops, MacBooks, tablets, and phones.',
        'highlights': [
            '100W (20V/5A) Power Delivery Ultra Fast Charging',
            'Integrated E-Marker Smart Chip for optimal device negotiation',
            '30,000+ Bend Tested Ballistic Braided Nylon Jacket',
            'High-Speed 480Mbps Data Sync & Transfer',
            'Optimal 1.5m (5ft) Extended Reach Length'
        ],
        'specifications': {
            'Technical Details': {
                'Connector Types': 'Type-C to Type-C',
                'Max Power Rating': '100 Watts (20V / 5 Amps)',
                'Cable Length': '1.5 Meters (5 Feet)',
                'Material': 'Double-Braided Ballistic Nylon + Aluminum Alloy Shell'
            }
        },
        'box_contents': [
            '1x Pulse ArmorCable 100W Type-C to C (1.5m)',
            '1x Reusable Velcro Cable Organizer Strap'
        ],
        'warranty_info': '2 Years Unconditional Brand Replacement Warranty',
        'variants': [
            {
                'id': 'nylon-black',
                'name': 'Nylon Carbon Black',
                'color_code': '#1e293b',
                'badge': 'Popular',
                'image': '/assets/images/cable-black.svg',
                'stock': 85,
                'in_stock': True
            }
        ],
        'gallery_images': [
            {'id': 'main', 'title': 'Overview', 'url': '/assets/images/cable-black.svg', 'caption': 'Pulse ArmorCable 100W Braided Type-C to C'}
        ],
        'faq': [
            {'q': 'Can this charge a MacBook or Type-C Laptop?', 'a': 'Yes! It supports full 100W 5A Power Delivery and easily charges MacBooks, Dell XPS, Lenovo ThinkPads, iPads, and high-end smartphones.'}
        ],
        'reviews': [
            {'name': 'Tanmay Rao', 'city': 'Bengaluru', 'rating': 5, 'date': '6 days ago', 'variant': 'Nylon Carbon Black', 'title': 'Unbreakable build quality!', 'body': 'Thick braided wire that doesn\\'t tangle. Fast charges my laptop and phone without getting warm.'}
        ],
        'is_active': True
    }
]

def seed_database():
    Base.metadata.create_all(bind=engine)
    db = SessionLocal()
    try:
        for pdata in PRODUCTS_SEED:
            existing = db.query(Product).filter(Product.slug == pdata['slug']).first()
            if existing:
                for key, val in pdata.items():
                    setattr(existing, key, val)
                print(f"Updated product: {pdata['slug']}")
            else:
                p = Product(**pdata)
                db.add(p)
                print(f"Created product: {pdata['slug']}")
        db.commit()
        print('Database catalogue seeded successfully!')
    finally:
        db.close()
'''

with open('backend/app/services/seed_data.py', 'w', encoding='utf-8') as f:
    f.write(SEED_DATA_CODE)
print('Updated seed_data.py')

# 3. Update backend/app/main.py for direct product routing
MAIN_PY_CODE = '''import os
from fastapi import FastAPI, HTTPException
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
from backend.app.database import engine, Base
from backend.app.services.seed_data import seed_database
from backend.app.routes import products, checkout, orders

Base.metadata.create_all(bind=engine)
seed_database()

app = FastAPI(
    title='PULSE AUDIO E-Commerce Store Engine',
    description='Production-grade mobile-first e-commerce API for Indian electronics consumers with Razorpay and Meta CAPI integration.',
    version='2.0.0'
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=['*'],
    allow_headers=['*']
)

app.include_router(products.router, prefix='/api')
app.include_router(checkout.router, prefix='/api')
app.include_router(orders.router, prefix='/api')

frontend_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'frontend')
app.mount('/assets', StaticFiles(directory=os.path.join(frontend_dir, 'assets')), name='assets')
app.mount('/css', StaticFiles(directory=os.path.join(frontend_dir, 'css')), name='css')
app.mount('/js', StaticFiles(directory=os.path.join(frontend_dir, 'js')), name='js')

@app.get('/')
def read_index():
    return FileResponse(os.path.join(frontend_dir, 'index.html'))

@app.get('/product/{slug}')
def read_product_page(slug: str):
    return FileResponse(os.path.join(frontend_dir, 'index.html'))

@app.get('/checkout.html')
@app.get('/checkout')
def read_checkout():
    return FileResponse(os.path.join(frontend_dir, 'checkout.html'))

@app.get('/success.html')
@app.get('/success')
def read_success():
    return FileResponse(os.path.join(frontend_dir, 'success.html'))
'''

with open('backend/app/main.py', 'w', encoding='utf-8') as f:
    f.write(MAIN_PY_CODE)
print('Updated main.py')

print('Backend updates applied successfully!')

