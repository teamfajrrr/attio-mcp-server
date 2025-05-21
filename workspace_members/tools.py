import httpx
from typing import Optional, Dict, Any
from config import BASE_URL, API_KEY

async def list_workspace_members() -> Dict[str, Any]:
    """
    Lists all workspace members.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/workspace_members"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"API request failed: {e.response.status_code}", "details": e.response.text}
        except httpx.RequestError as e:
            return {"error": f"Request failed: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}

async def get_workspace_member(
    workspace_member_id: str
) -> Dict[str, Any]:
    """
    Retrieves a specific workspace member by their ID.

    Args:
        workspace_member_id: The ID of the workspace member.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/workspace_members/{workspace_member_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"API request failed: {e.response.status_code}", "details": e.response.text}
        except httpx.RequestError as e:
            return {"error": f"Request failed: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}
