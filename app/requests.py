import urllib.request,json
from .models import Source,Article
# from newsapi.newsapi_client import NewsApiClient 
# from ..config import Config


#Getting api key
my_api_key = None

#Getting the news source base url
base_url = None

#Getting the article url
article_url = None

def configure_request(app):
    global base_url,my_api_key,article_url
    base_url = app.config["NEWS_API_BASE_URL"]
    my_api_key = app.config['API_KEY']
    article_url = app.config['ARTICLE_URL']


# def get_sources():
#     '''
#     Function that requests for data of all news sources.
#     '''
#     get_sources_url = base_url.format(my_api_key)
#     source_results = [] 
#     with urllib.request.urlopen(get_sources_url) as data:
#         data = json.loads(data)
#         source_list = data.get('sources')
#         source_results = []
#         for source in source_list:
#             id = source.get('id')
#             name = source.get('name')
#             description = source.get('description')
#             url = source.get('url')
#             language = source.get('language')

#             source_object = Source(id,name,description,url,language)
#             source_results.append(source_object)
#     return source_results

def get_sources():
    '''
    Function that gets the json response to our url request
    '''
    get_sources_url = base_url.format(my_api_key)
    sources_results = []
    try:
        with urllib.request.urlopen(get_sources_url) as response:
            if response.status == 200:
                data_ = response.read()
                response_ = json.loads(data_)
                sources_ = response_.get('sources')
                sources_results = process_sources(sources_)
    except urllib.error.URLError as e:
        print("HTTP ERROR: ", e)
    return sources_results
def process_sources(sources_list):
    '''
    Function  that processes the movie result and transform them to a list of Objects
    Args:
        movie_list: A list of dictionaries that contain movie details
    Returns :
        movie_results: A list of movie objects
    '''
    sources = []
    for source in sources_list:
        id_ = source.get('id')
        name = source.get('name')
        description = source.get('description')
        url = source.get('url')
        
        language = source.get('language')
       
        source_object = Source(id_,name,description,url,language,)
        sources.append(source)
    return sources












def get_articles(source):
    '''
    Function that gets a list of articles from a particular source

    Args: 
        source_id: The id of a specific result.
    Returns:
        article_results: list of news articles in the specific news source.
    '''

    with urllib.get(article_url.format(source,my_api_key))as data:
        data = data.json()
        article_list =data.get('articles')
        articles_results = []
        for article in article_list:
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            publishedAt = article.get('publishedAt')

    article_object = Article(author,title,description,url,urlToImage,publishedAt)
    articles_results.append(article_object)

    return articles_results

def search_article(q):
    search_article_url = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
    with urllib.get(search_article_url.format(q,my_api_key))as data:
        data = data.json()
        search_article_list =data.get('articles')
        search_articles_results = []
        for article in search_article_list:
            author = article.get('author')
            title = article.get('title')
            description = article.get('description')
            url = article.get('url')
            urlToImage = article.get('urlToImage')
            publishedAt = article.get('publishedAt')

    search_article_object = Article(author,title,description,url,urlToImage,publishedAt)
    search_articles_results.append(search_article_object)

    return search_articles_results

# def healthArticles():
#     newsapi = NewsApiClient(api_key= Config.API_KEY)

#     health_articles = newsapi.get_top_headlines(category='health')
#     all_articles = health_articles['articles']
#     health_articles_results = []

#     source = []
#     title = []
#     desc = []
#     author = []
#     img = []
#     p_date = []
#     url = []

#     for i in range(len(all_articles)):
#         article = all_articles[i]

#         source.append(article['source'])
#         title.append(article['title'])
#         desc.append(article['description'])
#         author.append(article['author'])
#         img.append(article['urlToImage'])
#         p_date.append(article['publishedAt'])
#         url.append(article['url'])

#         article_object = Article(source, title, desc, author, img, p_date, url)
#         health_articles_results.append(article_object)
#         contents = zip(source, title, desc, author, img, p_date, url)

#     return  contents

