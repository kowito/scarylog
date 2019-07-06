# index.py
import algoliasearch_django as algoliasearch
from .models import Story
algoliasearch.register(Story)
