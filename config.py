"""
Configuration file for Whoppah scraper
=====================================
"""

# Base configuration
BASE_URL = "https://www.whoppah.com"
DEFAULT_DELAY = 2  # seconds between requests
DEFAULT_TIMEOUT = 30  # seconds

# Main categories to scrape
MAIN_CATEGORIES = [
    '/furniture',
    '/lighting', 
    '/decoration',
    '/art',
    '/tableware'
]

# Style categories
STYLE_CATEGORIES = [
    '/style/vintage',
    '/style/mid-century-modern',
    '/style/italian-design', 
    '/style/scandinavian',
    '/style/memphis',
    '/style/hollywood-regency'
]

# Furniture subcategories
FURNITURE_SUBCATEGORIES = [
    '/furniture/chairs',
    '/furniture/sofas',
    '/furniture/cabinets',
    '/furniture/tables',
    '/furniture/beds',
    '/furniture/garden-furniture',
    '/furniture/office-furniture'
]

# Detailed furniture categories
DETAILED_FURNITURE_CATEGORIES = [
    '/furniture/chairs/dining-chairs',
    '/furniture/chairs/armchairs',
    '/furniture/chairs/office-chairs',
    '/furniture/chairs/bar-stools',
    '/furniture/chairs/rocking-chairs',
    '/furniture/chairs/folding-chairs',
    '/furniture/chairs/bean-bags',
    '/furniture/sofas/2-seaters',
    '/furniture/sofas/3-5-seaters',
    '/furniture/sofas/corner-sofas',
    '/furniture/sofas/chaise-longues',
    '/furniture/sofas/benches',
    '/furniture/cabinets/bookcases',
    '/furniture/cabinets/sideboards',
    '/furniture/cabinets/dressers',
    '/furniture/cabinets/shelving-unit',
    '/furniture/cabinets/chest-of-drawers',
    '/furniture/cabinets/wall-furniture',
    '/furniture/cabinets/tv-furniture',
    '/furniture/cabinets/display-cabinets',
    '/furniture/cabinets/liquor-cabinets',
    '/furniture/cabinets/wardrobes',
    '/furniture/cabinets/nightstands',
    '/furniture/tables/dining-tables',
    '/furniture/tables/coffee-tables',
    '/furniture/tables/side-tables',
    '/furniture/tables/consoles',
    '/furniture/tables/bar-carts',
    '/furniture/tables/dressing-tables',
    '/furniture/beds/single-beds',
    '/furniture/beds/double-beds',
    '/furniture/beds/sofa-beds'
]

# Lighting subcategories
LIGHTING_SUBCATEGORIES = [
    '/lighting/pendant-lamps',
    '/lighting/table-lamps',
    '/lighting/floor-lights',
    '/lighting/wall-lights',
    '/lighting/ceiling-lights',
    '/lighting/chandeliers',
    '/lighting/spot-lights',
    '/lighting/reading-lamp',
    '/lighting/childrens-lights'
]

# Decoration subcategories
DECORATION_SUBCATEGORIES = [
    '/decoration/vases',
    '/decoration/decorative-objects',
    '/decoration/mirrors',
    '/decoration/wall-decoration',
    '/decoration/candle-holders',
    '/decoration/coat-racks',
    '/decoration/bowls',
    '/decoration/clocks',
    '/decoration/pillows',
    '/decoration/room-screens',
    '/decoration/wine-racks',
    '/decoration/frames',
    '/decoration/coffee-table-books'
]

# Art subcategories
ART_SUBCATEGORIES = [
    '/art/paintings-drawings',
    '/art/lithographs-screen-prints',
    '/art/sculptures',
    '/art/glass-art',
    '/art/posters',
    '/art/photography',
    '/art/art-prints'
]

# Collections
COLLECTIONS = [
    '/collections/curators-favourites',
    '/collections/sofas-under-1000',
    '/collections/lighting-under-250',
    '/collections/armchairs-from-300',
    '/collections/dining-chairs-under-250',
    '/collections/showroom-furniture',
    '/collections/dining-tables-from-250',
    '/collections/dutch-design-deals'
]

# Brand pages (sample - there are many more)
SAMPLE_BRANDS = [
    '/brands/leolux',
    '/brands/vitra',
    '/brands/artifort',
    '/brands/pastoe',
    '/brands/fritz-hansen',
    '/brands/knoll',
    '/brands/cassina',
    '/brands/b-b-italia'
]

# Content extraction settings
CONTENT_SELECTORS = [
    'main',
    '.content',
    '.description', 
    '.category-description',
    '.seo-content',
    'article',
    '.page-content'
]

# Headers for requests
REQUEST_HEADERS = {
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'Connection': 'keep-alive',
    'Upgrade-Insecure-Requests': '1',
}

# Output settings
DEFAULT_OUTPUT_FORMAT = 'csv'
LOG_LEVEL = 'INFO'
LOG_FORMAT = '%(asctime)s - %(levelname)s - %(message)s'

# Minimum content length to be considered substantial
MIN_PARAGRAPH_LENGTH = 50
MIN_HEADING_LENGTH = 3

# Rate limiting
MAX_RETRIES = 3
RETRY_DELAY = 5  # seconds to wait before retrying