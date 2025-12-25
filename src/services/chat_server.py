from .conversation_factory import ConversationFactory
from src.repositories import MessageRepository
from src.entities import Message


class ChatServer:
    def __init__(self):
        self.conversations = {}
        self.message_repo = MessageRepository()

    def create_conversation(self, conversation_type: str, conversation_id: str):
        if conversation_id not in self.conversations:
            convo = ConversationFactory.create(conversation_type, conversation_id)
            self.conversations[conversation_id] = convo
        return self.conversations[conversation_id]

    def send_message(self, conversation_id: str, sender_id: str, content: str):
        message = Message.create(sender_id, content)

        conversation = self.conversations.get(conversation_id)

        if conversation:
            conversation.broadcast(message)
            self.message_repo.save(conversation_id, message)
        else:
            raise ValueError(f"Conversation {conversation_id} not found")

    def get_history(self, conversation_id: str):
        return self.message_repo.fetch(conversation_id)
