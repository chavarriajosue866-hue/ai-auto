from langchain_openai import ChatOpenAI
from langchain_core.tools import tool
from app.core.config import settings
from app.automation.web import automator

@tool
async def navigate_and_read(url: str) -> str:
    """Navega a una URL web y devuelve el texto de la página."""
    return await automator.go_to(url)

@tool
async def click_element(selector: str) -> str:
    """Haz clic en un elemento usando selector CSS."""
    return await automator.click(selector)

@tool
async def fill_input(selector: str, text: str) -> str:
    """Escribe texto en un input usando selector CSS."""
    return await automator.type_text(selector, text)

tools = [navigate_and_read, click_element, fill_input]

llm = ChatOpenAI(model="gpt-4o", temperature=0, api_key=settings.OPENAI_API_KEY)
llm_with_tools = llm.bind_tools(tools)

async def run_agent(prompt: str):
    messages = [
        {"role": "system", "content": "Eres un asistente de automatización web. Usa las herramientas para completar la tarea. Primero navega y lee la página para entender su estructura."},
        {"role": "user", "content": prompt}
    ]
    
    for _ in range(10):
        response = await llm_with_tools.ainvoke(messages)
        messages.append(response)
        
        if not response.tool_calls:
            break
            
        for tool_call in response.tool_calls:
            tool_name = tool_call["name"]
            selected_tool = {t.name: t for t in tools}[tool_name]
            tool_msg = await selected_tool.ainvoke(tool_call["args"])
            messages.append({"role": "tool", "content": str(tool_msg), "tool_call_id": tool_call["id"]})
            
    return messages[-1].content