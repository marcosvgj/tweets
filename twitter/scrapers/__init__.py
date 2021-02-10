from enum import Enum
from twitter.scrapers.batch import Batch
from twitter.scrapers.stream import Streaming


class ScraperType(Enum):
    BATCH = dict(label="Batch", constructor=Batch)
    STREAMING = dict(label="Streaming", constructor=Streaming)