from tools.search_tool import get_search_tool

search_tool = get_search_tool()

result = search_tool.run("What's the capital of Norway?")
print("🔎 Search result:", result)

