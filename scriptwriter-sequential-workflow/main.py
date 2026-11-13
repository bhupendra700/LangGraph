from os import getenv
from dotenv import load_dotenv
load_dotenv()
from pydantic import BaseModel
from typing import Optional

# Step 1 -> State creation
class Pipeline(BaseModel):
    raw_input: str
    edited_text: Optional[str] = ""
    script_text: Optional[str] = ""
    final_output: Optional[str] = ""


from langchain_groq import ChatGroq
api_key = getenv("GROQ_API_KEY")
llm = ChatGroq(model="openai/gpt-oss-120b" , temperature=0.5 , api_key=api_key)


# Step 2 -> Creating nodes
def editor_node(state:Pipeline) -> dict:
    prompt = (
        "You are an expert copyeditor. Clean up the following raw text. "
        "Fix any grammatical errors, spelling mistakes, and smooth out the transition flow"
        "while keeping the core message intact. return only the edited text.\n\n"
        f"Text:\n{state.raw_input}"
    )

    response = llm.invoke(prompt)

    return {"edited_text": response.content.strip()}

def scriptwriter_node(state: Pipeline)-> dict:
    prompt = (
        "You are a charismatic YouTube content creator. Take this edited text and transform"
        "it init a highly engaging, puncy, conversational video script hook. Make it soun"
        "like a real person speaking passionately. Return only the script content.\n\n"
        f"Edited text:\n{state.edited_text}"
    )

    response = llm.invoke(prompt)

    return {"script_text" : response.content.strip()}

def translator_node(state: Pipeline) -> dict:
    prompt = (
        "You are an expert content localizer for the Indian market. Take the following script"
        "ans convert it into natural, flowing 'Hinglish'. Do not simply translator it sentance by sentence"
        "or repeat information. Alternating comfortably between Hindi and English pharses just like"
        "an intellectual tech educator would speak naturally on a live stream. Keep the energy high"
        "Return only the final Hinglish text.\n\n"
        f"Script:\n{state.script_text}"
    )

    response = llm.invoke(prompt)

    return {"final_output" : response.content.strip()}


# Step 3 -> Creating graph and connect node through edges and edges is imp to create workflow.


from langgraph.graph import StateGraph , START , END

graph = StateGraph(Pipeline)

# Connecting node with graph
graph.add_node("editor" , editor_node)
graph.add_node("scriptwriter" , scriptwriter_node)
graph.add_node("translator" , translator_node)

# Creating Edges (sequential - one after another)
graph.add_edge(START , "editor")
graph.add_edge("editor" , "scriptwriter")
graph.add_edge("scriptwriter" , "translator")
graph.add_edge("translator" , END)

app = graph.compile()

User_Input = input("Enter prompt here: ")
# AI agents are the future of tech. They can think, plan, and act on their own. LangGraph helps you build these agents with proper control and memory.
result = app.invoke({
    "raw_input" : User_Input
})

print(result['final_output'])