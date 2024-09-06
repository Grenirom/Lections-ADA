PROTOCOLS
HTTP - протокол, построенный на TCP/IP
HTTPS - более защищенная версия HTTP (там появилось шфирование данных и SSL сертификаты)


HTTP - hyper text transfer protocol
HTTP METHODS

1) GET - получение данных
2) POST - отправка данных на создание
3) PUT - полное обновление или создание новых данных
4) PATCH - частичное обновление
5) DELETE - удаление

- HEAD - получает Headers
- OPTIONS - получение списка допустимых методов для этого URL
- TRACE - трассировка (проверка связи)

HTTPS STATUS CODE
- 1XX - информационные статус коды
- 2XX - успешные статус коды
- 3XX - redirect (перенаправление)
- 4XX - ошибки со стороны клиента (front-end)
- 5XX - ошибки со стороны сервера (back-end)

URL - uniform resource locator (https://www.google.com/search?q=hello)
DOMAIN - уникальное название (google.com)
URI - кусочек URL (/search)
QUERY PARAMETRS - пары (ключ=значение) после ? (q=hello)
HOST - адрес на который мы отправляем запрос (ip address / domain) 32.123.222.2
PORT - номер сервиса в сервере (http-server:80, postgresql:5432, backend:8000, frontend:3000)
