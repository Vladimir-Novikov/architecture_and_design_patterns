from wsgiref.simple_server import make_server

from application.urls import fronts, page_404

# импорт из view тк применяем декоратор AppRoute
from application.views import routes
from trinity_framework.main import Framework

application = Framework(routes, fronts, page_404)


with make_server("", 8000, application) as httpd:
    print("Сервер работает на порту 8000...")
    httpd.serve_forever()
