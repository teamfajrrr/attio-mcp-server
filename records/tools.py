import httpx
from typing import Optional, List, Dict, Any
from config import BASE_URL, API_KEY # Adjusted import


async def get_record(
    object_id_or_slug: str,
    record_id: str
) -> Dict[str, Any]:
    """
    Retrieves a specific record from a specified Attio object.

    Args:
        object_id_or_slug: The ID or slug of the Attio object.
        record_id: The ID of the record to retrieve.

    Returns:
        A dictionary containing the API response for the record or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
    }

    url = f"{BASE_URL}/v2/objects/{object_id_or_slug}/records/{record_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error getting record (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error getting record (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error getting record (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}


async def update_record_overwrite(
    object_id_or_slug: str,
    record_id: str,
    record_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Updates a specific record, overwriting existing values (uses PUT).

    Args:
        object_id_or_slug: The ID or slug of the Attio object.
        record_id: The ID of the record to update.
        record_data: A dictionary containing the new values for the record.
                     Example: {"values": {"attribute_id": "new_value"}}

    Returns:
        A dictionary containing the API response for the updated record or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {"data": record_data}
    url = f"{BASE_URL}/v2/objects/{object_id_or_slug}/records/{record_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.put(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error updating record (PUT) (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error updating record (PUT) (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error updating record (PUT) (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}


async def update_record_append(
    object_id_or_slug: str,
    record_id: str,
    record_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Updates a specific record, appending to multiselect values (uses PATCH).

    Args:
        object_id_or_slug: The ID or slug of the Attio object.
        record_id: The ID of the record to update.
        record_data: A dictionary containing the values to append or update.
                     Example: {"values": {"multiselect_attr_id": ["new_option"]}}

    Returns:
        A dictionary containing the API response for the updated record or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {"data": record_data}
    url = f"{BASE_URL}/v2/objects/{object_id_or_slug}/records/{record_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.patch(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error updating record (PATCH) (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error updating record (PATCH) (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error updating record (PATCH) (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}


async def delete_record(
    object_id_or_slug: str,
    record_id: str
) -> Dict[str, Any]:
    """
    Deletes a specific record from a specified Attio object.

    Args:
        object_id_or_slug: The ID or slug of the Attio object.
        record_id: The ID of the record to delete.

    Returns:
        A dictionary with a success message or an error message.
        Attio API returns a 204 No Content on successful deletion.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
    }

    url = f"{BASE_URL}/v2/objects/{object_id_or_slug}/records/{record_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url, headers=headers)
            response.raise_for_status()
            # For DELETE, a 204 No Content is a success
            if response.status_code == 204:
                return {"status": "success", "message": f"Record {record_id} deleted successfully."}
            return response.json() # Should not happen for a 204, but as a fallback
        except httpx.HTTPStatusError as e:
            # If it's a 204, it's a success despite being raised as an error by default by httpx for non-200s
            if e.response.status_code == 204:
                return {"status": "success", "message": f"Record {record_id} deleted successfully."}
            error_details_text = e.response.text
            print(f"Error deleting record (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error deleting record (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error deleting record (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}


async def list_record_entries(
    object_id_or_slug: str,
    record_id: str,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """
    Lists all entries, across all lists, for which this record is the parent.

    Args:
        object_id_or_slug: The ID or slug of the Attio object.
        record_id: The ID of the record.
        limit: The maximum number of entries to return. Defaults to 50.
        offset: The number of entries to skip. Defaults to 0.

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

    url = f"{BASE_URL}/v2/objects/{object_id_or_slug}/records/{record_id}/entries"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, headers=headers, params=params)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error listing record entries (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error listing record entries (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error listing record entries (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}


async def list_records(
    object_id_or_slug: str,
    filter_criteria: Optional[Dict[str, Any]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    limit: int = 500,
    offset: int = 0
) -> Dict[str, Any]:
    """
    Queries records from a specified Attio object.

    Args:
        object_id_or_slug: The ID or slug of the Attio object to query records from.
        filter_criteria: A dictionary defining the filter for the query.
                         Example: {"and": [{"attribute": "name", "condition": "eq", "value": "Test Company"}]}
        sorts: A list of dictionaries defining the sort order.
               Example: [{"attribute": "created_at", "direction": "desc"}]
        limit: The maximum number of records to return (default 500).
        offset: The number of records to skip (for pagination, default 0).

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload_data = {"limit": limit, "offset": offset}
    if filter_criteria:
        payload_data["filter"] = filter_criteria
    if sorts:
        payload_data["sorts"] = sorts
    
    payload = {"data": payload_data}

    url = f"{BASE_URL}/v2/objects/{object_id_or_slug}/records/query"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error querying records (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error querying records (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error querying records (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}

async def create_record(
    object_id_or_slug: str,
    record_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Creates a new record in a specified object.

    Args:
        object_id_or_slug: The ID or slug of the object where the record will be created.
        record_data: A dictionary containing the data for the new record.
                     It should typically be structured with a 'values' key holding attribute_id-value pairs.
                     Example:
                     {
                         "values": {
                             "name": "New Company Name",
                             "custom_text_attribute_id": "Some text"
                         }
                     }

    Returns:
        A dictionary containing the API response for the created record or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {
        "Authorization": f"Bearer {API_KEY}",
        "Content-Type": "application/json",
    }

    payload = {"data": record_data}

    url = f"{BASE_URL}/v2/objects/{object_id_or_slug}/records"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.post(url, headers=headers, json=payload)
            response.raise_for_status()
            return response.json()
        except httpx.HTTPStatusError as e:
            error_details_text = e.response.text
            print(f"Error creating record (HTTPStatusError): {error_details_text}")
            try:
                error_details = e.response.json()
            except ValueError:
                error_details = error_details_text
            return {
                "error": f"API request failed with status {e.response.status_code}",
                "details": error_details
            }
        except httpx.RequestError as e:
            print(f"Error creating record (RequestError): {e}")
            return {"error": f"Request to {e.request.url} failed: {str(e)}"}
        except Exception as e:
            print(f"Error creating record (Exception): {e}")
            return {"error": f"An unexpected error occurred: {str(e)}"}
