import httpx
from typing import Optional, List, Dict, Any
from config import BASE_URL, API_KEY

async def list_attributes(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    Lists all attributes for a given target (object or list).

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        limit: The maximum number of attributes to return. Defaults to 50.
        offset: The number of attributes to skip. Defaults to 0.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {'limit': limit, 'offset': offset}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes"

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

async def create_attribute(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    attribute_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Creates a new attribute for a given target (object or list).

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        attribute_data: Dictionary containing the attribute's properties.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes"
    payload = {"data": attribute_data}

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

async def get_attribute(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    attribute_id_or_slug: str
) -> Dict[str, Any]:
    """
    Retrieves a specific attribute for a given target (object or list).

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        attribute_id_or_slug: The ID or slug of the attribute.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes/{attribute_id_or_slug}"

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

async def update_attribute(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    attribute_id_or_slug: str,
    attribute_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Updates a specific attribute for a given target (object or list).

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        attribute_id_or_slug: The ID or slug of the attribute to update.
        attribute_data: Dictionary containing the attribute's properties to update.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes/{attribute_id_or_slug}"
    payload = {"data": attribute_data}

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


async def list_select_options(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    attribute_id_or_slug: str,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    Lists all select options for a particular attribute on either an object or a list.

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        attribute_id_or_slug: The ID or slug of the attribute.
        limit: The maximum number of options to return. Defaults to 50.
        offset: The number of options to skip. Defaults to 0.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {'limit': limit, 'offset': offset}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes/{attribute_id_or_slug}/options"

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

async def create_select_option(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    attribute_id_or_slug: str,
    option_data: Dict[str, Any] # e.g. {"title": "Medium"}
) -> Dict[str, Any]:
    """
    Adds a select option to a select attribute on an object or a list.

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        attribute_id_or_slug: The ID or slug of the attribute.
        option_data: Dictionary containing the option's properties (e.g., title).

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes/{attribute_id_or_slug}/options"
    payload = {"data": option_data}

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

async def update_select_option(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    attribute_id_or_slug: str,
    option_id: str,
    option_data: Dict[str, Any] # e.g. {"title": "Medium", "is_archived": false}
) -> Dict[str, Any]:
    """
    Updates a select option for a particular attribute on either an object or a list.

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        attribute_id_or_slug: The ID or slug of the attribute.
        option_id: The ID of the select option to update.
        option_data: Dictionary containing the option's properties to update.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes/{attribute_id_or_slug}/options/{option_id}"
    payload = {"data": option_data}

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


async def list_statuses(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    attribute_id_or_slug: str,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    Lists all statuses for a particular attribute on either an object or a list.

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        attribute_id_or_slug: The ID or slug of the attribute.
        limit: The maximum number of statuses to return. Defaults to 50.
        offset: The number of statuses to skip. Defaults to 0.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    params = {'limit': limit, 'offset': offset}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes/{attribute_id_or_slug}/statuses"

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

async def create_status(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    attribute_id_or_slug: str,
    status_data: Dict[str, Any] # e.g. {"title": "Open", "color": "blue"}
) -> Dict[str, Any]:
    """
    Adds a status to a status attribute on an object or a list.

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        attribute_id_or_slug: The ID or slug of the attribute.
        status_data: Dictionary containing the status's properties (e.g., title, color).

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes/{attribute_id_or_slug}/statuses"
    payload = {"data": status_data}

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

async def update_status(
    target_type: str, # 'objects' or 'lists'
    target_identifier: str, # ID or slug of the object or list
    attribute_id_or_slug: str,
    status_id: str,
    status_data: Dict[str, Any] # e.g. {"title": "In Progress", "is_archived": false}
) -> Dict[str, Any]:
    """
    Updates a status for a particular attribute on either an object or a list.

    Args:
        target_type: The type of the target ('objects' or 'lists').
        target_identifier: The ID or slug of the target object or list.
        attribute_id_or_slug: The ID or slug of the attribute.
        status_id: The ID of the status to update.
        status_data: Dictionary containing the status's properties to update.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    if target_type not in ['objects', 'lists']:
        return {"error": "Invalid target_type. Must be 'objects' or 'lists'."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/{target_type}/{target_identifier}/attributes/{attribute_id_or_slug}/statuses/{status_id}"
    payload = {"data": status_data}

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
