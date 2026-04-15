import json
from dataclasses import dataclass, field


@dataclass
class HttpRequest:
    method: str = ""
    url: str = ""
    headers: dict[str, str] = field(default_factory=dict)
    body: str = ""
    timeout: int = 30

    def __str__(self) -> str:
        return (
            f"Request\n"
            f"{self.method} {self.url}\n"
            f"Headers: {self.headers}\n"
            f"Body: {self.body[:50]}{'...' if len(self.body) > 50 else ''}\n"
            f"Timeout: {self.timeout}s\n"
        )


# Строитель


class HttpRequestBuilder:
    def __init__(self):
        self.reset()

    def reset(self):
        self._request = HttpRequest()
        return self

    def set_method(self, method: str):
        self._request.method = method.upper()
        return self

    def set_url(self, url: str):
        self._request.url = url
        return self

    def add_header(self, key: str, value: str):
        self._request.headers[key] = value
        return self

    def set_body(self, body: str):
        self._request.body = body
        return self

    def set_timeout(self, timeout: int):
        self._request.timeout = timeout
        return self

    def build(self) -> HttpRequest:
        product = self._request
        self.reset()
        return product


# Директор


class Director:
    def __init__(self, builder: HttpRequestBuilder):
        self.builder = builder

    def build_json_post(self, url: str, data: dict) -> HttpRequest:
        return (
            self.builder.set_method("POST")
            .set_url(url)
            .add_header("Content-Type", "application/json")
            .set_body(json.dumps(data))
            .build()
        )

    def build_auth_get(self, url: str, token: str) -> HttpRequest:
        return (
            self.builder.set_method("GET")
            .set_url(url)
            .add_header("Authorization", f"Bearer {token}")
            .build()
        )

    def build_multipart_upload(self, url: str, filename: str) -> HttpRequest:
        return (
            self.builder.set_method("POST")
            .set_url(url)
            .add_header("Content-Type", "multipart/form-data")
            .set_body(f"--boundary\nContent-Disposition: file; filename={filename}")
            .set_timeout(300)
            .build()
        )


# Клиентский код

director = Director(HttpRequestBuilder())

# Готовый рецепт
request = director.build_json_post("https://api.example.com/orders", {"item": "book"})
print(request)

# Авторизованный GET-запрос
auth_request = director.build_auth_get("https://example.com", "top-secret-token")
print(auth_request)
