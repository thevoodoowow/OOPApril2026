import hashlib, secrets


class PasswordHasher:

    @staticmethod
    def verify(plain: str, hashed: str) -> bool:
        return hashlib.sha256(plain.encode()).hexdigest() == hashed


class TokenGenerator:

    @staticmethod
    def generate() -> str:
        return secrets.token_hex(32)


class SessionRepository:

    def save(self, user_id: int, token: str):
        print(f"[DB] Сессия сохранена: user_id={user_id}, token={token[:8]}...")


class AuthService:

    def __init__(
        self,
        hasher: PasswordHasher,
        generator: TokenGenerator,
        repository: SessionRepository,
    ):
        self.hasher = hasher
        self.generator = generator
        self.repository = repository

    def login(self, user_id: int, password: str, stored_hash: str) -> str:
        if not self.hasher.verify(password, stored_hash):
            raise Exception("Неверный пароль")

        token = self.generator.generate()
        self.repository.save(user_id, token)
        return token


hasher = PasswordHasher()
token_gen = TokenGenerator()
repo = SessionRepository()
auth = AuthService(hasher, token_gen, repo)

stored_hash = hashlib.sha256("secret".encode()).hexdigest()
token = auth.login(42, "secret", stored_hash)
print(f"Токен: {token[:8]}...")
