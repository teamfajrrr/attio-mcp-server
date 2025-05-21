import httpx
from typing import Optional, Dict, Any, List
from config import BASE_URL, API_KEY

async def list_notes() -> Dict[str, Any]:
    """
    Lists all notes.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/notes"

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

async def create_note(
    note_data: Dict[str, Any] 
) -> Dict[str, Any]:
    """
    Creates a new note.

    Args:
        note_data: Dictionary containing the note's properties such as parent_object, 
                   parent_record_id, title, format, content, and created_at.
            e.g. {
                "parent_object": "people", 
                "parent_record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d", 
                "title": "Initial Prospecting Call Summary", 
                "format": "plaintext", 
                "content": "# Meeting Recap...", 
                "created_at": "2023-01-01T15:00:00.000000000Z"
            }

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/notes"
    payload = {"data": note_data}

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

async def get_note(
    note_id: str
) -> Dict[str, Any]:
    """
    Retrieves a specific note by its ID.

    Args:
        note_id: The ID of the note.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/notes/{note_id}"

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

async def delete_note(
    note_id: str
) -> Dict[str, Any]:
    """
    Deletes a specific note by its ID.

    Args:
        note_id: The ID of the note to delete.

    Returns:
        A dictionary containing a success message or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/notes/{note_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url, headers=headers)
            response.raise_for_status()
            if response.status_code == 204:
                return {"message": f"Note {note_id} deleted successfully."}
            return response.json() # Should ideally not happen for a 204
        except httpx.HTTPStatusError as e:
            return {"error": f"API request failed: {e.response.status_code}", "details": e.response.text}
        except httpx.RequestError as e:
            return {"error": f"Request failed: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}
