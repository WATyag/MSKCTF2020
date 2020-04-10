Исследуя таск замечаем, что подключеный к странице not-a-flag.js, который блокируется правилами csp. Также делается запрос на /csp-reports, где помимо прочего передается uri заблокированного файла. Ответ на этот запрос таков:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Fri, 10 Apr 2020 12:12:58 GMT
Content-Type: text/plain
Content-Length: 96
Connection: close
Content-Security-Policy: script-src 'self' 'unsafe-inline' https://code.jquery.com/ https://cdnjs.cloudflare.com/ https://maxcdn.bootstrapcdn.com/; report-uri /csp-reports

DEBUG: the js /not-a-flag.js with content 'This file does not contain a flag' is blocked by CSP
```

Стоит отметить, что при попытке перейти на /not-a-flag.js таск возвращает 404. Попробуем перехватить запрос через burp и заменить "not-a-flag.js" на что-то более интересное. 

Пробуем 'flag.txt', получаем:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Fri, 10 Apr 2020 12:22:43 GMT
Content-Type: text/plain
Content-Length: 58
Connection: close
Content-Security-Policy: script-src 'self' 'unsafe-inline' https://code.jquery.com/ https://cdnjs.cloudflare.com/ https://maxcdn.bootstrapcdn.com/; report-uri /csp-reports

DEBUG: the js /flag.txt with content '' is blocked by CSP
```

Быть может, flag.js? Ведь изначально к странице подключался javascript файл. Ответ:

![burp request](https://github.com/WATyag/MSKCTF2020/blob/master/Incident/burp.jpg)


#### Флаг: MSKCTF{CSP_IS_COOK1EZ_CR3AM_POPT4RT}


