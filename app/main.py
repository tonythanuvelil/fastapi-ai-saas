from fastapi import FastAPI, HTTPException
from mangum import Mangum

from .copykitt import generate_branding_snippet, generate_keywords

app = FastAPI()
handler = Mangum(app)

MAX_INPUT_LENGTH = 12


@app.get("/")
async def root():
    return {"message": "Hello CopyKitt"}


@app.get("/generate-snippet")
async def generate_snippet_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    return {"snippet": snippet}


@app.get("/generate-keywords")
async def generate_keywords_api(prompt: str):
    validate_input_length(prompt)
    keywords = generate_keywords(prompt)
    return {"keywords": keywords}


@app.get("/generate-snippet-and-keywords")
async def generate_snippet_and_keywords_api(prompt: str):
    validate_input_length(prompt)
    snippet = generate_branding_snippet(prompt)
    keywords = generate_keywords(prompt)
    return {"snippet": snippet, "keywords": keywords}


def validate_input_length(prompt: str):
    if len(prompt) >= MAX_INPUT_LENGTH:
        raise HTTPException(
            status_code=400,
            detail=f"Input is too long, length must be under {MAX_INPUT_LENGTH}.",
        )
