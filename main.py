from fastmcp import FastMCP
import os
from loguru import logger
from typing import Optional, List, Dict, Any

# Import all tool modules
from attributes.tools import (
    list_attributes, create_attribute, get_attribute, update_attribute,
    list_select_options, create_select_option, update_select_option,
    list_statuses, create_status, update_status
)
from entries.tools import (
    create_list_entry, get_list_entry, list_entries,
    update_list_entry_overwrite, update_list_entry_append,
    delete_list_entry, get_list_entry_attribute_values
)
from lists.tools import list_lists, create_list, get_list, update_list
from notes.tools import list_notes, create_note, get_note, delete_note
from objects.tools import list_objects, create_object, get_object, update_object
from records.tools import (
    get_record, update_record_overwrite, update_record_append,
    delete_record, list_record_entries, list_records, create_record
)
from tasks.tools import list_tasks, create_task, get_task, update_task, delete_task
from workspace_members.tools import list_workspace_members, get_workspace_member

# Initialize FastMCP
mcp = FastMCP(name="AttioMCP")

# ============= ATTRIBUTE TOOLS =============

@mcp.tool()
async def attio_list_attributes(
    target_type: str,
    target_identifier: str,
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """Lists all attributes for a given target (object or list).
    
    Args:
        target_type: The type of the target ('objects' or 'lists')
        target_identifier: The ID or slug of the target object or list
        limit: Maximum number of attributes to return (default 50)
        offset: Number of attributes to skip (default 0)
    """
    return await list_attributes(target_type, target_identifier, limit, offset)

@mcp.tool()
async def attio_create_attribute(
    target_type: str,
    target_identifier: str,
    attribute_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Creates a new attribute for a given target (object or list).
    
    Args:
        target_type: The type of the target ('objects' or 'lists')
        target_identifier: The ID or slug of the target object or list
        attribute_data: Dictionary containing the attribute's properties
    """
    return await create_attribute(target_type, target_identifier, attribute_data)

@mcp.tool()
async def attio_get_attribute(
    target_type: str,
    target_identifier: str,
    attribute_id_or_slug: str
) -> Dict[str, Any]:
    """Retrieves a specific attribute for a given target (object or list).
    
    Args:
        target_type: The type of the target ('objects' or 'lists')
        target_identifier: The ID or slug of the target object or list
        attribute_id_or_slug: The ID or slug of the attribute
    """
    return await get_attribute(target_type, target_identifier, attribute_id_or_slug)

@mcp.tool()
async def attio_update_attribute(
    target_type: str,
    target_identifier: str,
    attribute_id_or_slug: str,
    attribute_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Updates a specific attribute for a given target (object or list).
    
    Args:
        target_type: The type of the target ('objects' or 'lists')
        target_identifier: The ID or slug of the target object or list
        attribute_id_or_slug: The ID or slug of the attribute to update
        attribute_data: Dictionary containing the attribute's properties to update
    """
    return await update_attribute(target_type, target_identifier, attribute_id_or_slug, attribute_data)

# ============= LIST ENTRY TOOLS =============

@mcp.tool()
async def attio_create_list_entry(
    list_id: str,
    entry_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Creates a new entry in a specified list.
    
    Args:
        list_id: The ID or slug of the list where the entry will be created
        entry_data: Dictionary containing the data for the new entry
    """
    return await create_list_entry(list_id, entry_data)

@mcp.tool()
async def attio_get_list_entry(
    list_id: str,
    entry_id: str
) -> Dict[str, Any]:
    """Retrieves a specific entry from a specified list.
    
    Args:
        list_id: The ID of the list
        entry_id: The ID of the list entry to retrieve
    """
    return await get_list_entry(list_id, entry_id)

@mcp.tool()
async def attio_list_entries(
    list_id: str,
    filter_criteria: Optional[Dict[str, Any]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    limit: int = 10,
    offset: int = 0
) -> Dict[str, Any]:
    """Queries entries from a specified list.
    
    Args:
        list_id: The ID or slug of the list to query
        filter_criteria: Dictionary defining the filter for the query
        sorts: List of dictionaries defining the sort order
        limit: Maximum number of entries to return (default 10)
        offset: Number of entries to skip (default 0)
    """
    return await list_entries(list_id, filter_criteria, sorts, limit, offset)

@mcp.tool()
async def attio_update_list_entry_overwrite(
    list_id: str,
    entry_id: str,
    entry_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Updates a specific list entry, overwriting existing values (uses PUT).
    
    Args:
        list_id: The ID of the Attio list
        entry_id: The ID of the list entry to update
        entry_data: Dictionary containing the new values for the entry
    """
    return await update_list_entry_overwrite(list_id, entry_id, entry_data)

@mcp.tool()
async def attio_update_list_entry_append(
    list_id: str,
    entry_id: str,
    entry_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Updates a specific list entry, appending to multiselect values (uses PATCH).
    
    Args:
        list_id: The ID of the Attio list
        entry_id: The ID of the list entry to update
        entry_data: Dictionary containing the values to append or update
    """
    return await update_list_entry_append(list_id, entry_id, entry_data)

@mcp.tool()
async def attio_delete_list_entry(
    list_id: str,
    entry_id: str
) -> Dict[str, Any]:
    """Deletes a specific entry from a specified list.
    
    Args:
        list_id: The ID of the list
        entry_id: The ID of the list entry to delete
    """
    return await delete_list_entry(list_id, entry_id)

# ============= LIST TOOLS =============

@mcp.tool()
async def attio_list_lists(
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """Retrieves all lists in the workspace.
    
    Args:
        limit: Maximum number of lists to return (default 50)
        offset: Number of lists to skip (default 0)
    """
    return await list_lists(limit, offset)

@mcp.tool()
async def attio_create_list(
    list_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Creates a new list.
    
    Args:
        list_data: Dictionary containing the data for the new list
    """
    return await create_list(list_data)

@mcp.tool()
async def attio_get_list(
    list_id_or_slug: str
) -> Dict[str, Any]:
    """Retrieves a specific list by its ID or slug.
    
    Args:
        list_id_or_slug: The ID or slug of the list to retrieve
    """
    return await get_list(list_id_or_slug)

@mcp.tool()
async def attio_update_list(
    list_id_or_slug: str,
    list_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Updates a specific list.
    
    Args:
        list_id_or_slug: The ID or slug of the list to update
        list_data: Dictionary containing the data to update
    """
    return await update_list(list_id_or_slug, list_data)

# ============= NOTE TOOLS =============

@mcp.tool()
async def attio_list_notes() -> Dict[str, Any]:
    """Lists all notes."""
    return await list_notes()

@mcp.tool()
async def attio_create_note(
    note_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Creates a new note.
    
    Args:
        note_data: Dictionary containing the note's properties
    """
    return await create_note(note_data)

@mcp.tool()
async def attio_get_note(
    note_id: str
) -> Dict[str, Any]:
    """Retrieves a specific note by its ID.
    
    Args:
        note_id: The ID of the note
    """
    return await get_note(note_id)

@mcp.tool()
async def attio_delete_note(
    note_id: str
) -> Dict[str, Any]:
    """Deletes a specific note by its ID.
    
    Args:
        note_id: The ID of the note to delete
    """
    return await delete_note(note_id)

# ============= OBJECT TOOLS =============

@mcp.tool()
async def attio_list_objects(
    limit: Optional[int] = 50,
    offset: Optional[int] = 0
) -> Dict[str, Any]:
    """Lists all objects in the workspace.
    
    Args:
        limit: Maximum number of objects to return (default 50)
        offset: Number of objects to skip (default 0)
    """
    return await list_objects(limit, offset)

@mcp.tool()
async def attio_create_object(
    object_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Creates a new object.
    
    Args:
        object_data: Dictionary containing the object's properties
    """
    return await create_object(object_data)

@mcp.tool()
async def attio_get_object(
    object_id_or_slug: str
) -> Dict[str, Any]:
    """Retrieves a specific object by its ID or slug.
    
    Args:
        object_id_or_slug: The ID or slug of the object
    """
    return await get_object(object_id_or_slug)

@mcp.tool()
async def attio_update_object(
    object_id_or_slug: str,
    object_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Updates a specific object.
    
    Args:
        object_id_or_slug: The ID or slug of the object to update
        object_data: Dictionary containing the object's properties to update
    """
    return await update_object(object_id_or_slug, object_data)

# ============= RECORD TOOLS =============

@mcp.tool()
async def attio_get_record(
    object_id_or_slug: str,
    record_id: str
) -> Dict[str, Any]:
    """Retrieves a specific record from a specified Attio object.
    
    Args:
        object_id_or_slug: The ID or slug of the Attio object
        record_id: The ID of the record to retrieve
    """
    return await get_record(object_id_or_slug, record_id)

@mcp.tool()
async def attio_create_record(
    object_id_or_slug: str,
    record_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Creates a new record in a specified object.
    
    Args:
        object_id_or_slug: The ID or slug of the object where the record will be created
        record_data: Dictionary containing the data for the new record
    """
    return await create_record(object_id_or_slug, record_data)

@mcp.tool()
async def attio_list_records(
    object_id_or_slug: str,
    filter_criteria: Optional[Dict[str, Any]] = None,
    sorts: Optional[List[Dict[str, Any]]] = None,
    limit: int = 10,
    offset: int = 0
) -> Dict[str, Any]:
    """Queries records from a specified Attio object.
    
    Args:
        object_id_or_slug: The ID or slug of the Attio object to query records from
        filter_criteria: Dictionary defining the filter for the query
        sorts: List of dictionaries defining the sort order
        limit: Maximum number of records to return (default 10)
        offset: Number of records to skip (default 0)
    """
    return await list_records(object_id_or_slug, filter_criteria, sorts, limit, offset)

@mcp.tool()
async def attio_update_record_overwrite(
    object_id_or_slug: str,
    record_id: str,
    record_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Updates a specific record, overwriting existing values (uses PUT).
    
    Args:
        object_id_or_slug: The ID or slug of the Attio object
        record_id: The ID of the record to update
        record_data: Dictionary containing the new values for the record
    """
    return await update_record_overwrite(object_id_or_slug, record_id, record_data)

@mcp.tool()
async def attio_update_record_append(
    object_id_or_slug: str,
    record_id: str,
    record_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Updates a specific record, appending to multiselect values (uses PATCH).
    
    Args:
        object_id_or_slug: The ID or slug of the Attio object
        record_id: The ID of the record to update
        record_data: Dictionary containing the values to append or update
    """
    return await update_record_append(object_id_or_slug, record_id, record_data)

@mcp.tool()
async def attio_delete_record(
    object_id_or_slug: str,
    record_id: str
) -> Dict[str, Any]:
    """Deletes a specific record from a specified Attio object.
    
    Args:
        object_id_or_slug: The ID or slug of the Attio object
        record_id: The ID of the record to delete
    """
    return await delete_record(object_id_or_slug, record_id)

# ============= TASK TOOLS =============

@mcp.tool()
async def attio_list_tasks() -> Dict[str, Any]:
    """Lists all tasks."""
    return await list_tasks()

@mcp.tool()
async def attio_create_task(
    task_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Creates a new task.
    
    Args:
        task_data: Dictionary containing the task's properties
    """
    return await create_task(task_data)

@mcp.tool()
async def attio_get_task(
    task_id: str
) -> Dict[str, Any]:
    """Retrieves a specific task by its ID.
    
    Args:
        task_id: The ID of the task
    """
    return await get_task(task_id)

@mcp.tool()
async def attio_update_task(
    task_id: str,
    task_data: Dict[str, Any]
) -> Dict[str, Any]:
    """Updates a specific task by its ID.
    
    Args:
        task_id: The ID of the task to update
        task_data: Dictionary containing the task properties to update
    """
    return await update_task(task_id, task_data)

@mcp.tool()
async def attio_delete_task(
    task_id: str
) -> Dict[str, Any]:
    """Deletes a specific task by its ID.
    
    Args:
        task_id: The ID of the task to delete
    """
    return await delete_task(task_id)

# ============= WORKSPACE MEMBER TOOLS =============

@mcp.tool()
async def attio_list_workspace_members() -> Dict[str, Any]:
    """Lists all workspace members."""
    return await list_workspace_members()

@mcp.tool()
async def attio_get_workspace_member(
    workspace_member_id: str
) -> Dict[str, Any]:
    """Retrieves a specific workspace member by their ID.
    
    Args:
        workspace_member_id: The ID of the workspace member
    """
    return await get_workspace_member(workspace_member_id)

# ============= SERVER STARTUP =============

if __name__ == "__main__":
    from config import PORT, TRANSPORT
    
    logger.info(f"Starting Attio MCP Server on port {PORT} with transport {TRANSPORT}")
    logger.info(f"Available tools: {len(mcp._tools)} tools registered")
    
    if TRANSPORT == "sse":
        mcp.run(transport="sse", host="0.0.0.0", port=PORT)
    elif TRANSPORT == "stdio":
        mcp.run(transport="stdio")
    elif TRANSPORT == "streamable-http":
        mcp.run(transport="streamable-http", host="0.0.0.0", port=PORT)
    else:
        logger.warning(f"Unknown transport {TRANSPORT}, defaulting to SSE")
        mcp.run(transport="sse", host="0.0.0.0", port=PORT)
