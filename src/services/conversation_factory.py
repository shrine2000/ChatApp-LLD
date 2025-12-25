from src.entities import Conversation, GroupConversation, OneToOneConversation


class ConversationFactory:
    @staticmethod
    def create(conversation_type: str, conversation_id: str) -> Conversation:
        if conversation_type == "one_to_one":
            return OneToOneConversation(conversation_id)
        elif conversation_type == "group":
            return GroupConversation(conversation_id)
        else:
            raise ValueError("Invalid conversation type")
