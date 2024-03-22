import requests
import feedparser

def arXiv_scrapper():
    # arXiv API endpoint
    ARXIV_API_URL = "http://export.arxiv.org/api/query?"

    # Parameters for the API query  
    query_params = {
        'search_query': 'cat:cs.LG',  # Search in the Machine Learning category, change as needed
        'start': 0,  # Starting point of the results
        'max_results': 1,  # Number of results to return, adjust as needed
    }

    # Make the request to arXiv API
    response = requests.get(ARXIV_API_URL, params=query_params)

    # Parse the response using feedparser
    feed = feedparser.parse(response.content)

    return feed

print(arXiv_scrapper())
