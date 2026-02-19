1) It registers a URL and tells flask that when someone visits this URL, run this function.
2) Flask keeps a URL map, which is a dictionary of paths and functions.
3) Route parameters are part of the URL path and query parameters come after the ? and are part of the query string.
4) Because of the place where the data is being sent. GET sends data in the URL, and POST sends data in the request body
5) Flask will raise a RuntimeError 