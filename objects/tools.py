import httpx
from typing import Optional, Dict, Any
from config import BASE_URL, API_KEY

async def list_objects(
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    Lists all objects in the workspace.

    Args:
        limit: The maximum number of objects to return. Defaults to 50.
        offset: The number of objects to skip. Defaults to 0.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {'limit': limit, 'offset': offset}
    url = f"{BASE_URL}/v2/objects"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"API request failed: {e.response.status_code}", "details": e.response.text}
        except httpx.RequestError as e:
            return {"error": f"Request failed: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}

async def create_object(
    object_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Creates a new object.

    Args:
        object_data: Dictionary containing the object's properties such as api_slug, singular_noun, and plural_noun.
            e.g. {"api_slug": "people", "singular_noun": "Person", "plural_noun": "People"}

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/objects"
    payload = {"data": object_data}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"API request failed: {e.response.status_code}", "details": e.response.text}
        except httpx.RequestError as e:
            return {"error": f"Request failed: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}

async def get_object(
    object_id_or_slug: str
) -> Dict[str, Any]:
    """
    Retrieves a specific object by its ID or slug.

    Args:
        object_id_or_slug: The ID or slug of the object.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/objects/{object_id_or_slug}"

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

async def update_object(
    object_id_or_slug: str,
    object_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Updates a specific object.

    Args:
        object_id_or_slug: The ID or slug of the object to update.
        object_data: Dictionary containing the object's properties to update.
            e.g. {"api_slug": "people", "singular_noun": "Person", "plural_noun": "People"}

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/objects/{object_id_or_slug}"
    payload = {"data": object_data}

    async with httpx.AsyncClient() as client:
        try:
            response = await client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"API request failed: {e.response.status_code}", "details": e.response.text}
        except httpx.RequestError as e:
            return {"error": f"Request failed: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}
