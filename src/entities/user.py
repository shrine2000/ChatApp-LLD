from src.entities.message import Message


class User:
    def __init__(self, user_id: str, name: str):
        self.user_id = user_id
        self.name = name

    def receive(self, conversation_id: str, message: Message):
        print(f"[{conversation_id}] {message.sender_id}: {message.content}")
