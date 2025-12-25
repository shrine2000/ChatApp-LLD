from abc import ABC, abstractmethod

from .message import Message
from .user import User


class Conversation(ABC):
    def __init__(self, conversation_id: str):
        self.conversation_id = conversation_id
        self.participants = {}
        self.messages = []

    def add_participant(self, user: User):
        self.participants[user.user_id] = user

    def remove_participant(self, user_id: str):
        self.participants.pop(user_id, None)

    def get_history(self):
        return list(self.messages)

    @abstractmethod
    def broadcast(self, message: Message):
        pass


class OneToOneConversation(Conversation):
    def broadcast(self, message: Message):
        self.messages.append(message)
        for user in self.participants.values():
            user.receive(self.conversation_id, message)


class GroupConversation(Conversation):
    def broadcast(self, message: Message):
        self.messages.append(message)
        for user in self.participants.values():
            user.receive(self.conversation_id, message)
