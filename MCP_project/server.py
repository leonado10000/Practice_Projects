from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add_two_numbers(a:int, b:int) -> int:
    """Add two numbers"""
    print(f"adding {a} and {b}")
    return a + b

if __name__ == "__main__":
    mcp.run(transport="sse")