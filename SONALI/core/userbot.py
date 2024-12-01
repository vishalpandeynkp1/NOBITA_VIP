from typing import Callable, Optional
import pyrogram
from pyrogram import Client, filters, errors
import config
from ..logging import LOGGER

assistants = []
assistantids = []
clients = []


class Userbot:
    def __init__(self):
        # Initialize all clients
        self.one = self.create_client("RAUSHANAss1", config.STRING1)
        self.two = self.create_client("RAUSHANAss2", config.STRING2)
        self.three = self.create_client("RAUSHANAss3", config.STRING3)
        self.four = self.create_client("RAUSHANAss4", config.STRING4)
        self.five = self.create_client("RAUSHANAss5", config.STRING5)

    def create_client(self, session_name, session_string):
        """Create a pyrogram client if the session string exists."""
        if session_string:
            return Client(session_name, api_id=config.API_ID, api_hash=config.API_HASH, session_string=session_string)
        return None

    async def start(self):
        """Start all configured clients and join required chats."""
        LOGGER(__name__).info("Starting Assistant Clients")
        clients_to_start = [
            (self.one, 1),
            (self.two, 2),
            (self.three, 3),
            (self.four, 4),
            (self.five, 5),
        ]

        for client, index in clients_to_start:
            if client:
                try:
                    await client.start()
                    await self.join_chats(client)
                    assistants.append(index)
                    clients.append(client)
                    await self.send_start_message(client, index)
                    await self.log_client_info(client, index)
                except errors.RPCError as e:
                    LOGGER(__name__).error(f"Assistant {index} failed to start: {e}")

    async def join_chats(self, client):
        """Make clients join the necessary chats."""
        try:
            chat_list = [
                "ll_NOBITA_BOT_DEVLOPER_ll",
                "NOBITA_BOT_MAKER_STATUS",
                "NOBITA_SUPPORT",
                "NOBITA_ALL_BOT",
            ]
            for chat in chat_list:
                await client.join_chat(chat)
        except errors.FloodWait as e:
            LOGGER(__name__).warning(f"Flood wait triggered while joining chats: {e}")
        except errors.RPCError as e:
            LOGGER(__name__).warning(f"Failed to join chats: {e}")

    async def send_start_message(self, client, index):
        """Send a start message to the log group."""
        try:
            await client.send_message(config.LOG_GROUP_ID, f"Assistant {index} Started")
        except errors.RPCError as e:
            LOGGER(__name__).error(
                f"Assistant {index} could not send a message to the log group. "
                f"Ensure it's added and promoted. Error: {e}"
            )

    async def log_client_info(self, client, index):
        """Log the details of the started client."""
        get_me = await client.get_me()
        client.username = get_me.username
        client.id = get_me.id
        client.mention = get_me.mention
        assistantids.append(get_me.id)
        client.name = f"{get_me.first_name} {get_me.last_name}" if get_me.last_name else get_me.first_name
        LOGGER(__name__).info(f"Assistant {index} Started as {client.name}")

    async def stop(self):
        """Stop all running clients."""
        LOGGER(__name__).info("Stopping Assistant Clients")
        for client in clients:
            try:
                await client.stop()
            except errors.RPCError as e:
                LOGGER(__name__).error(f"Error while stopping client: {e}")


def on_cmd(filters: Optional[pyrogram.filters.Filter] = None, group: int = 0) -> Callable:
    """Decorator to add a command handler to all clients."""
    def decorator(func: Callable) -> Callable:
        for client in clients:
            client.add_handler(pyrogram.handlers.MessageHandler(func, filters), group)
        return func

    return decorator
