from src.entities import Message


class MessageRepository:
    def __init__(self):
        self._store = {}

    def save(self, conversation_id: str, message: Message):
        self._store.setdefault(conversation_id, []).append(message)

    def fetch(self, conversation_id: str):
        return self._store.get(conversation_id, [])
