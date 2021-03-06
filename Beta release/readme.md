## Beta release

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

#### Флаг: MSKCTF{l34v1g_g1t_f0ld3r_1s_t00_b4d_id34_l0l}
