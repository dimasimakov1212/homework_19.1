from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

# параметры подключения
hostName = "localhost"
serverPort = 8080


class MyServer(BaseHTTPRequestHandler):

    def __get_html_content(self):
        """
        Считывает содержимое html файла
        :return:
        """
        html_file = 'homework.html'
        with open(html_file, "r", encoding="utf-8") as file:
            html_content = file.read()

        return html_content

    def do_GET(self):
        """
        Обрабатывает запросы на сервер
        :return:
        """

        shop_html = self.__get_html_content()

        self.send_response(200)
        self.send_header("Content-type", "text/html")  # Тип данных, передаваемых в запросе
        self.end_headers()
        self.wfile.write(bytes(shop_html, "utf-8"))  # Вывод информации


if __name__ == "__main__":
    # Инициализация веб-сервера, который будет по заданным параметрам в сети
    # принимать запросы и отправлять их на обработку в классе MyServer
    webServer = HTTPServer((hostName, serverPort), MyServer)
    print("Server started http://%s:%s" % (hostName, serverPort))

    try:
        webServer.serve_forever()  # Cтарт веб-сервера в бесконечном цикле запросов
    except KeyboardInterrupt:
        pass

    # Остановка веб-сервера, чтобы он освободил адрес и порт в сети, которые занимал
    webServer.server_close()
    print("Server stopped.")
