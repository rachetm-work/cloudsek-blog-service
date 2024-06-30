_mappings_per_index = {
    "blogs": {
        "mappings": {
            "properties": {
                "title": {"type": "text"},
                "content": {"type": "text"},
                "user_id": {"type": "keyword"},
                "id": {"type": "keyword"}
            }
        }
    }
}


def get_mappings_for_index(index_name):
    return _mappings_per_index.get(index_name, None)
