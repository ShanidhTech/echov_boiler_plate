from broker.consumer import listen_to_topic
from services.business_logic import handle_user_created

if __name__ == "__main__":
    listen_to_topic("user.created", handle_user_created)
