from src.entities import User
from src.services import ChatServer

if __name__ == "__main__":
    server = ChatServer()

    alice = User("u1", "Alice")
    bob = User("u2", "Bob")
    carol = User("u3", "Carol")

    # Create a group conversation
    chat = server.create_conversation("group", "c1")
    chat.add_participant(alice)
    chat.add_participant(bob)
    chat.add_participant(carol)

    print("--- Real-time Broadcast ---")
    server.send_message("c1", "u1", "Hello everyone")
    server.send_message("c1", "u2", "Hi Alice")
    server.send_message("c1", "u3", "Hey folks!")

    print("\n--- History ---")
    history = server.get_history("c1")
    for msg in history:
        print(f"{msg.sender_id}: {msg.content}")
