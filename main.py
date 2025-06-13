import random
from fastapi import FastAPI, Query
from typing import Annotated
from pydantic import AfterValidator

app = FastAPI()

data = {
    "isbn-9781529046137": "The Hitchhiker's Guide to the Galaxy",
    "imdb-tt0371724": "The Hitchhiker's Guide to the Galaxy",
    "isbn-9781439512982": "Isaac Asimov: The Complete Stories, Vol. 2",
}


def check_valid_id(id: str):
    if not id.startswith(("isbn-", "imdb-")):
        raise ValueError('Invalid ID format, it must start with "isbn-" or "imdb-"')
    return id


"""
@app.get("/items/")
async def read_items(q: str | None = None):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results
"""


# async def read_items(q: Annotated[str | None, Query(max_length=10)] = None):
"""
async def read_items(
    q: Annotated[str | None, Query(min_length=3, max_length=50)] = None,
):
"""
"""
async def read_items(
    q: Annotated[
        str | None, Query(min_length=3, max_length=50, pattern="^fixedquery$")
    ] = None,
):
"""
# async def read_items(q: Annotated[str, Query(min_length=3)] = "fixedquery"):
# async def read_items(q: Annotated[str, Query(min_length=3)]):
# async def read_items(q: Annotated[list[str] | None, Query()] = None):
#async def read_items(q: Annotated[list[str], Query()] = ["foo", "bar"]):
# async def read_items(q: Annotated[list, Query()] = []):
"""
async def read_items(
    q: Annotated[str | None, Query(title="Query string", min_length=3)] = None,
):
"""
"""
async def read_items(
    q: Annotated[
        str | None,
        Query(
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
        ),
    ] = None,
):
"""
#async def read_items(q: Annotated[str | None, Query(alias="item-query")] = None):
"""
async def read_items(
    q: Annotated[
        str | None,
        Query(
            alias="item-query",
            title="Query string",
            description="Query string for the items to search in the database that have a good match",
            min_length=3,
            max_length=50,
            pattern="^fixedquery$",
            deprecated=True,
        ),
    ] = None,
):
"""
@app.get("/items/")
async def read_items(
    id: Annotated[str | None, AfterValidator(check_valid_id)] = None,
):
    results = {"items": [{"item_id": "Foo"}, {"item_id": "Bar"}]}
    if q:
        results.update({"q": q})
    return results