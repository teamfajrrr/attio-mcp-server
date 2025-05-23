import httpx
from typing import Optional, List, Dict, Any
from config import BASE_URL, API_KEY # Adjusted import

async def create_list_entry(
    list_id: str,
    entry_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Creates a new entry in a specified list.
    Args:
        list_id: The ID or slug of the list where the entry will be created.
        entry_data: A dictionary containing the data for the new entry.
                    Example:
                    {
                        "parent_record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d",
                        "parent_object": "people",
                        "entry_values": {
                            "41252299-f8c7-4b5e-99c9-4ff8321d2f96": "Text value",
                            "multiselect_attribute": [
                                "Select option 1",
                                "Select option 2"
                            ]
                        }
                    }
    Returns:
        A dictionary containing the API response for the created entry or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"data": entry_data}
    url = f"{BASE_URL}/v2/lists/{list_id}/entries"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error creating entry (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error creating entry (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error creating entry (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}

async def get_list_entry(
    list_id: str,
    entry_id: str
) -> Dict[str, Any]:
    """
    Retrieves a specific entry from a specified list.

    Args:
        list_id: The ID of the list.
        entry_id: The ID of the list entry to retrieve.

    Returns:
        A dictionary containing the API response for the list entry or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/lists/{list_id}/entries/{entry_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error getting list entry (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error getting list entry (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error getting list entry (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}

async def list_entries(
    list_id: str,
    filter_criteria: Dict[str, Any] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    limit: int = 10,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Queries entries from a specified list.

    Args:
        list_id: The ID or slug of the list to query.
        filter_criteria: A dictionary defining the filter for the query.
                         Example for a standard 'Name' attribute on a person list entry:
                         {"name": {"$eq": "Ada Lovelace"}}
                         Example for a custom attribute (replace with actual attribute ID):
                         {"attribute_id": {"$eq": "Some Value"}}
                         Example for filter on a parent's attribute (people):
                        {
                            "path":[
                                ["[list slug/list id]", "parent_record"],
                                ["people", "email_addresses"]
                            ],
                            "constraints": {
                                "email_address": "user@example.com"
                            }
                        }
        sorts: A list of dictionaries defining the sort order.
               Example for a standard 'Name' attribute:
               [{"attribute": "name", "direction": "asc"}]
               Example for a custom attribute (replace with actual attribute ID):
               [{"attribute_id": "custom_attribute_id_for_sorting", "direction": "asc"}]
        limit: The maximum number of entries to return. Defaults to 10.
        offset: The number of entries to skip before starting to collect the result set. Defaults to 0.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"limit": limit, "offset": offset}
    if filter_criteria:
        payload["filter"] = filter_criteria
    if sorts:
        payload["sorts"] = sorts
    url = f"{BASE_URL}/v2/lists/{list_id}/entries/query"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error querying list entries (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error querying list entries (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error querying list entries (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}

async def update_list_entry_overwrite(
    list_id: str,
    entry_id: str,
    entry_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Updates a specific list entry, overwriting existing values (uses PUT).

    Args:
        list_id: The ID of the Attio list.
        entry_id: The ID of the list entry to update.
        entry_data: A dictionary containing the new values for the entry.
                    This should contain the 'entry_values' key with attribute ID-value pairs.
                    Example:
                    {
                        "entry_values": {
                            "name_attribute_id": "Updated Name",
                            "status_attribute_id": "Closed"
                        }
                    }

    Returns:
        A dictionary containing the API response for the updated entry or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"data": entry_data}
    url = f"{BASE_URL}/v2/lists/{list_id}/entries/{entry_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error updating list entry (PUT) (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error updating list entry (PUT) (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error updating list entry (PUT) (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}

async def update_list_entry_append(
    list_id: str,
    entry_id: str,
    entry_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Updates a specific list entry, appending to multiselect values (uses PATCH).
    This is suitable for updating specific fields, especially for appending values to multiselect attributes
    without overwriting existing selections.

    Args:
        list_id: The ID of the Attio list.
        entry_id: The ID of the list entry to update.
        entry_data: A dictionary containing the values to append or update.
                    For multiselect, provide a list of values to append.
                    For other fields, it will update them.
                    Example:
                    {
                        "entry_values": {
                            "multiselect_attribute_id": ["New Option 3", "New Option 4"],
                            "description_attribute_id": "Updated description text."
                        }
                    }
    Returns:
        A dictionary containing the API response for the updated entry or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }
    payload = {"data": entry_data}
    url = f"{BASE_URL}/v2/lists/{list_id}/entries/{entry_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error updating list entry (PATCH) (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error updating list entry (PATCH) (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error updating list entry (PATCH) (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}

async def delete_list_entry(
    list_id: str,
    entry_id: str
) -> Dict[str, Any]:
    """
    Deletes a specific entry from a specified list.

    Args:
        list_id: The ID of the list.
        entry_id: The ID of the list entry to delete.

    Returns:
        A dictionary with a success message or an error message.
        API returns a 204 No Content on successful deletion.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/lists/{list_id}/entries/{entry_id}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error deleting list entry (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error deleting list entry (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error deleting list entry (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}

async def get_list_entry_attribute_values(
    list_id: str,
    entry_id: str,
    attribute_id_or_slug: str
) -> Dict[str, Any]:
    """
    Retrieves the values of a specific attribute for a given list entry.

    Args:
        list_id: The ID of the Attio list.
        entry_id: The ID of the list entry.
        attribute_id_or_slug: The ID or slug of the attribute whose values are to be retrieved.

    Returns:
        A dictionary containing the API response for the attribute values or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}
    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/lists/{list_id}/entries/{entry_id}/attributes/{attribute_id_or_slug}/values"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error getting attribute values (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error getting attribute values (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error getting attribute values (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}
