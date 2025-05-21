import httpx
from typing import Optional, Dict, Any, List
from config import BASE_URL, API_KEY

async def list_tasks() -> Dict[str, Any]:
    """
    Lists all tasks.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/tasks"

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

async def create_task(
    task_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Creates a new task.

    Args:
        task_data: Dictionary containing the task's properties.
            e.g. {
                "content": "Follow up on current software solutions",
                "format": "plaintext",
                "deadline_at": "2023-01-01T15:00:00.000000000Z",
                "is_completed": false,
                "linked_records": [
                    {
                        "target_object": "people",
                        "target_record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d"
                    }
                ],
                "assignees": [
                    {
                        "referenced_actor_type": "workspace-member",
                        "referenced_actor_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b"
                    }
                ]
            }

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/tasks"
    payload = {"data": task_data}

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

async def get_task(
    task_id: str
) -> Dict[str, Any]:
    """
    Retrieves a specific task by its ID.

    Args:
        task_id: The ID of the task.

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/tasks/{task_id}"

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

async def update_task(
    task_id: str,
    task_data: Dict[str, Any]
) -> Dict[str, Any]:
    """
    Updates a specific task by its ID.

    Args:
        task_id: The ID of the task to update.
        task_data: Dictionary containing the task properties to update.
            e.g. {
                "deadline_at": "2023-01-01T15:00:00.000000000Z",
                "is_completed": false,
                "linked_records": [
                    {
                        "target_object": "people",
                        "target_record_id": "891dcbfc-9141-415d-9b2a-2238a6cc012d"
                    }
                ],
                "assignees": [
                    {
                        "referenced_actor_type": "workspace-member",
                        "referenced_actor_id": "50cf242c-7fa3-4cad-87d0-75b1af71c57b"
                    }
                ]
            }

    Returns:
        A dictionary containing the API response or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}
    url = f"{BASE_URL}/v2/tasks/{task_id}"
    payload = {"data": task_data}

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

async def delete_task(
    task_id: str
) -> Dict[str, Any]:
    """
    Deletes a specific task by its ID.

    Args:
        task_id: The ID of the task to delete.

    Returns:
        A dictionary containing a success message or an error message.
    """
    if not API_KEY:
        return {"error": "API_KEY environment variable not set."}

    headers = {"Authorization": f"Bearer {API_KEY}"}
    url = f"{BASE_URL}/v2/tasks/{task_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.delete(url, headers=headers)
            response.raise_for_status()
            if response.status_code == 204:
                return {"message": f"Task {task_id} deleted successfully."}
            return response.json()
        except httpx.HTTPStatusError as e:
            return {"error": f"API request failed: {e.response.status_code}", "details": e.response.text}
        except httpx.RequestError as e:
            return {"error": f"Request failed: {e}"}
        except Exception as e:
            return {"error": f"An unexpected error occurred: {e}"}
