from fastapi import FastAPI
from fastapi.responses import RedirectResponse
from langserve import add_routes
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate

app = FastAPI()


@app.get("/")
async def redirect_root_to_docs():
    return RedirectResponse("/docs")

prompt = ChatPromptTemplate.from_template("tell me a story about {topic}")
model = ChatOpenAI()

# Edit this to add the chain you want to add
add_routes(app,
           prompt | model,
           path ="/story"
           )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
