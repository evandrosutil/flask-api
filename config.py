import os


class Config:
    """Classe com as configurações do REDIS."""
    CACHE_TYPE = os.environ.get('CACHE_TYPE', 'RedisCache')
    CACHE_REDIS_HOST = os.environ.get('CACHE_REDIS_HOST', 'localhost')
    CACHE_REDIS_PORT = os.environ.get('CACHE_REDIS_PORT', '6379')
    CACHE_REDIS_URL = os.environ.get(
        'CACHE_REDIS_URL', f'redis://{CACHE_REDIS_HOST}:{CACHE_REDIS_PORT}/0')
    CACHE_DEFAULT_TIMEOUT = '604800'  # 7 dias
