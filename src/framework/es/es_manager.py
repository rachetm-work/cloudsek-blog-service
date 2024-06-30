from elasticsearch import helpers, Elasticsearch, NotFoundError

from src.framework.es.mappings import get_mappings_for_index
from src.framework.settings.settings import settings


class ESManager:

    def __init__(self, index_name_suffix):
        self.es = Elasticsearch(hosts=[{"host": settings.es_host, "port": 9200}], max_retries=30, retry_on_timeout=True,
                                request_timeout=30)
        self.index_name_suffix = index_name_suffix
        self.index = self._get_index_name()
        self.create_index()

    def _get_index_name(self):
        prefix = 'cloudsek_assignment'

        return f'{prefix}_{self.index_name_suffix}'

    def does_index_exist(self):
        return self.es.indices.exists(index=self.index)

    def index_single(self, record):
        self.es.index(index=self.index, document=record)

    def create_index(self):
        self.es.indices.create(index=self.index, ignore=[400, 409], mappings=get_mappings_for_index(self.index))

    def get_result_by_id(self, identifier):
        query = {
            "query": {
                "terms": {
                    "id": [identifier]
                }
            }
        }

        try:
            res = self.es.search(index=self.index, body=query)['hits']['hits']
        except NotFoundError:
            return None

        if len(res) > 0:
            return res[0].get('_source')
        return None

    def get_search_results(self, query, size=10000):
        res = helpers.scan(self.es, index=self.index, query=query, size=size)

        return [{**item['_source']} for item in res]
