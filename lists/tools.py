import httpx
from typing import Optional, List, Dict, Any
from config import BASE_URL, API_KEY # Adjusted import


async def list_lists(
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    Retrieves all lists in the workspace.

    Args:
        limit: The maximum number of lists to return. Defaults to 50.
        offset: The number of lists to skip. Defaults to 0.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
    }
    params = {}
    if limit is not None:
        params['limit'] = limit
    if offset is not None:
        params['offset'] = offset

    url = f"{BASE_URL}/v2/lists"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error listing lists (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error listing lists (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error listing lists (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}


async def create_list(
    list_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Creates a new list.

    Args:
        list_data: A dictionary containing the data for the new list.
                   Example:
                   {
                       "name": "Enterprise Sales",
                       "api_slug": "enterprise_sales",
                       "parent_object": "people",
                       "workspace_access": "read-and-write",
                       "workspace_member_access": [
                           {
                               "workspace_member_id": "member_id_example",
                               "level": "read-and-write"
                           }
                       ]
                   }

    Returns:
        A dictionary containing the API response for the created list or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {"data": list_data}
    url = f"{BASE_URL}/v2/lists"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error creating list (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error creating list (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error creating list (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}


async def get_list(
    list_id_or_slug: str
) -> Dict[str, Any]:
    """
    Retrieves a specific list by its ID or slug.

    Args:
        list_id_or_slug: The ID or slug of the list to retrieve.

    Returns:
        A dictionary containing the API response for the list or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
    }

    url = f"{BASE_URL}/v2/lists/{list_id_or_slug}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error getting list (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error getting list (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error getting list (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}


async def update_list(
    list_id_or_slug: str,
    list_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Updates a specific list.

    Args:
        list_id_or_slug: The ID or slug of the list to update.
        list_data: A dictionary containing the data to update.

    Returns:
        A dictionary containing the API response for the updated list or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {"data": list_data}
    url = f"{BASE_URL}/v2/lists/{list_id_or_slug}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error updating list (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error updating list (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error updating list (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}
