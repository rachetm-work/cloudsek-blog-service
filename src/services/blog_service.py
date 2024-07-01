import uuid

from src.framework.es.es_manager import ESManager
from src.framework.producers.producer import publish_to_queue
from src.framework.responses import ApiSuccessResponse


def submit_blog(blog_entry):
    entry_data = blog_entry.dict()
    entry_data["id"] = str(uuid.uuid4())
    entry_data["index_name_suffix"] = "blogs"
    publish_to_queue(entry_data)
    return ApiSuccessResponse(data={"status": "submitted", "id": entry_data["id"]})


def search_blogs(search_term: str):
    data = ESManager(index_name_suffix='blogs').get_search_results(query={
        "query": {
            "multi_match": {
                "query": search_term,
                "fields": ["title", "content"]
            }
        }
    })

    return ApiSuccessResponse(data=data)
