# MSKCTF2020
#### More-less [PPC]
Простая задача на бинарный поиск.

#### Funny Farm [PPC]
Прочитав условие задачи можно понять, что это знаменитая игра быки и коровы (она же Mastermind). Существует много способов решения, здесь использовано дерево исходов.

#### Simple [RE]
В этой задаче можно было просто перебирать флаг посимвольно, сверяясь с содержимым файла `output.txt`.

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
Описание к этой задаче слишком большое, оно доступно по [ссылке](https://github.com/WATyag/MSKCTF2020/blob/master/pickle/solve.md).
