from django.core.cache import cache

from catalog.models import Product
from config.settings import CACHE_ENABLED


def get_products_from_cache():
    """Получение данных из кеша о продуктах"""
    if CACHE_ENABLED:
        key = "products_list"
        products = cache.get(key)
        if products is None:
            products = Product.objects.all()
            cache.set(key, products)
    else:
        products = Product.objects.all()
    return products
