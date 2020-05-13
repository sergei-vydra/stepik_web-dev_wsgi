def wsgi_app(environ, start_response):
    status = "200 OK"
    headers = [('Content-Type', 'text/plain')]
    body = "\r\n".join(environ["QUERY_STRING"].split("&"))
    start_response(status, headers)
    return [bytes(body, encoding="utf-8")]

