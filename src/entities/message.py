from dataclasses import dataclass
from datetime import datetime
from uuid import uuid4


@dataclass(frozen=True)
class Message:
    id: str
    sender_id: str
    content: str
    timestamp: datetime

    @staticmethod
    def create(sender_id: str, content: str) -> "Message":
        return Message(
            id=str(uuid4()),
            sender_id=sender_id,
            content=content,
            timestamp=datetime.utcnow(),
        )
