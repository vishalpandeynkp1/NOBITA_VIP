import aiohttp
import socket
from asyncio import get_running_loop
from functools import partial

# Method 1: Netcat-based pastebin (ezup.dev)
def _netcat(host, port, content):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((host, port))
        s.sendall(content.encode())
        s.shutdown(socket.SHUT_WR)
        response = []
        while True:
            data = s.recv(4096).decode("utf-8").strip("\n\x00")
            if not data:
                break
            response.append(data)
        s.close()
        return "\n".join(response)
    except Exception as e:
        return f"Error: {e}"


async def paste(content):
    """Uploads content to ezup.dev using a socket connection."""
    loop = get_running_loop()
    link = await loop.run_in_executor(None, partial(_netcat, "ezup.dev", 9999, content))
    return link

# Method 2: Batbin-based pastebin (batbin.me)
BASE = "https://batbin.me/"


async def post(url: str, *args, **kwargs):
    """Helper function to perform an HTTP POST request."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.post(url, *args, **kwargs) as resp:
                try:
                    return await resp.json()
                except Exception:
                    return {"error": await resp.text()}
    except Exception as e:
        return {"error": str(e)}


async def Bin(text):
    """Uploads content to batbin.me using HTTP POST."""
    data = {"content": text}
    resp = await post(f"{BASE}api/v2/paste", data=data)
    if not resp.get("success"):
        return f"Error: {resp.get('error', 'Unknown error')}"
    return BASE + resp["message"]

# Unified Interface
async def NOBIBin(content, method="batbin"):
    """
    Unified function to upload content to pastebin services.
    :param content: The text content to upload.
    :param method: Choose between "batbin" or "ezup".
    """
    if method == "ezup":
        return await paste(content)
    elif method == "batbin":
        return await Bin(content)
    else:
        raise ValueError("Invalid method specified. Choose 'ezup' or 'batbin'.")
