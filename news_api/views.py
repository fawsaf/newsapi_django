import requests
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import ArticleSerializer

@api_view(['GET'])
def get_news(request):
    item = request.query_params.get('item')
    category = request.query_params.get('category')
    countries = 'us,gb,ca, au'; # Example countries: United States, United Kingdom, Canada
    
    print('Received category:', category)
    print('Received item:', item)
    api_key = 'fb6fe28c95034d3fb87ffb52e70f474b'
    if category:
        url = f'https://newsapi.org/v2/top-headlines?country=us&category={category}&apiKey={api_key}'
    else:
        url = f'https://newsapi.org/v2/everything?q={item}&from=2023-06-22&to=2023-06-22&sortBy=popularity&apiKey={api_key}'
    response = requests.get(url)
    data = response.json()

    articles = data['articles']  # Extract the list of articles from the response

    serializer = ArticleSerializer(articles, many=True)
    return Response(serializer.data)
