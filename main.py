from fastmcp import FastMCP
# Import tools from submodules
from entries import tools as entry_tools
from records import tools as record_tools
from lists import tools as list_tools
from attributes import tools as attribute_tools
from objects import tools as object_tools
from workspace_members import tools as workspace_member_tools
from notes import tools as note_tools
from tasks import tools as task_tools
from loguru import logger

# Create a server instance
mcp = FastMCP(
    name="AttioMCP", 
    instructions="""
        This server provides tools to interact with Attio's API.
    """
)

# Add a health check endpoint for Railway
@mcp.get("/")
async def health_check():
    """Health check endpoint for Railway and other monitoring services"""
    return {
        "status": "healthy",
        "service": "AttioMCP",
        "message": "Attio MCP Server is running",
        "endpoints": {
            "sse": "/sse",
            "health": "/"
        }
    }

# Add an additional health endpoint
@mcp.get("/health")
async def health():
    """Alternative health check endpoint"""
    return {"status": "ok", "service": "AttioMCP"}

# List entry
mcp.tool()(entry_tools.create_list_entry)
mcp.tool()(entry_tools.get_list_entry)
mcp.tool()(entry_tools.list_entries)
mcp.tool()(entry_tools.update_list_entry_overwrite)
mcp.tool()(entry_tools.update_list_entry_append)
mcp.tool()(entry_tools.delete_list_entry)
mcp.tool()(entry_tools.get_list_entry_attribute_values)

# Record
mcp.tool()(record_tools.create_record)
mcp.tool()(record_tools.list_records)
mcp.tool()(record_tools.get_record)
mcp.tool()(record_tools.update_record_overwrite)
mcp.tool()(record_tools.update_record_append)
mcp.tool()(record_tools.delete_record)
mcp.tool()(record_tools.list_record_entries)

# Lists
mcp.tool()(list_tools.list_lists)
mcp.tool()(list_tools.create_list)
mcp.tool()(list_tools.get_list)
mcp.tool()(list_tools.update_list)

# Attributes
mcp.tool()(attribute_tools.list_attributes)
mcp.tool()(attribute_tools.create_attribute)
mcp.tool()(attribute_tools.get_attribute)
mcp.tool()(attribute_tools.update_attribute)
mcp.tool()(attribute_tools.list_select_options)
mcp.tool()(attribute_tools.create_select_option)
mcp.tool()(attribute_tools.update_select_option)
mcp.tool()(attribute_tools.list_statuses)
mcp.tool()(attribute_tools.create_status)
mcp.tool()(attribute_tools.update_status)

# Objects
mcp.tool()(object_tools.list_objects)
mcp.tool()(object_tools.create_object)
mcp.tool()(object_tools.get_object)
mcp.tool()(object_tools.update_object)

# Workspace Members
mcp.tool()(workspace_member_tools.list_workspace_members)
mcp.tool()(workspace_member_tools.get_workspace_member)

# Notes
mcp.tool()(note_tools.list_notes)
mcp.tool()(note_tools.create_note)
mcp.tool()(note_tools.get_note)
mcp.tool()(note_tools.delete_note)

# Tasks
mcp.tool()(task_tools.list_tasks)
mcp.tool()(task_tools.create_task)
mcp.tool()(task_tools.get_task)
mcp.tool()(task_tools.update_task)
mcp.tool()(task_tools.delete_task)

if __name__ == "__main__":
    try:
        import config 
        if not config.API_KEY:
            logger.warning("API_KEY not found in environment. Please check your .env file.")
    except ImportError:
        logger.warning("Could not import config.py. API calls may fail.")
    
    mcp.run(transport=config.TRANSPORT, host="0.0.0.0", port=config.PORT)
