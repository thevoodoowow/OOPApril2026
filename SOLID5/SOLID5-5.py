from abc import abstractmethod


class Cache:
    @abstractmethod
    def get(self, key: str):
        pass

    @abstractmethod
    def set(self, key: str, value):
        pass


class RedisCache(Cache):
    def __init__(self):
        self._store = {}

    def get(self, key: str):
        return self._store.get(key)

    def set(self, key: str, value):
        self._store[key] = value
        print(f"[Redis] Сохранено: {key}")


class MemoryCache(Cache):
    def __init__(self):
        self._data = {}

    def get(self, key: str):
        return self._data.get(key)

    def set(self, key: str, value):
        self._data[key] = value
        print(f"[Memory] Сохранено: {key}")


class ArticleService:
    def __init__(self, cache: Cache):
        self.cache = cache

    def get_article(self, article_id: int) -> dict:
        key = f"article:{article_id}"
        cached = self.cache.get(key)
        if cached:
            return cached

        article = {"id": article_id, "title": f"Статья #{article_id}"}
        self.cache.set(key, article)
        return article


prod_service = ArticleService(RedisCache())
prod_service.get_article(21)

test_service = ArticleService(MemoryCache())
test_service.get_article(52)
