import asyncio
from boilerpipe.extract import Extractor
from helpers.extractors import extractors

url = "https://dpstele.com"
extractor = extractors["article_sentences"]

ext = Extractor(extractor=extractor, url=url)

print(ext.getText())
