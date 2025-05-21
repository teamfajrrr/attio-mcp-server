<center>
<img src="attio.svg" alt="Attio Logo" height="48" align=center>
</center>
<h1 align=center>Attio MCP Server</h1>

<p align=center>This project provides a <a href="https://gofastmcp.com">FastMCP</a> server with tools to interact with the Attio API. It allows you to manage resources within your Attio workspace.</p>

---

## Setup

1. **Clone the repository (if applicable):**

   ```bash
   git clone <repository-url>
   cd attio-mcp
   ```
2. **Create and activate a virtual environment:**

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```
4. **Configure environment variables:**
   Create a `.env` file in the project root directory (`attio-mcp/`) with the following content:

   ```env
   BASE_URL=https://api.attio.com
   API_KEY=your_attio_api_key_here
   ```

   Replace `your_attio_api_key_here` with your actual Attio API key.

## Running the Server

```bash
python main.py
```

The server will run on `http://0.0.0.0:8000` (or as configured in `.env`).
SSE transport is used by default available at `http://0.0.0.0:8000/sse`, you can change the transport by setting the `TRANSPORT` ('stdio', 'streamable-http' or 'sse', more info [here](https://gofastmcp.com/deployment/running-server#transport-options)).
