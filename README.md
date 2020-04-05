# MSKCTF2020
#### More-less [PPC]
Простая задача на бинарный поиск.

#### Funny Farm [PPC]
Прочитав условие задачи можно понять, что это знаменитая игра быки и коровы (она же Mastermind). Существует много способов решения, здесь использовано дерево исходов.

#### Simple [RE]
В этой задаче можно было просто перебирать флаг посимвольно, сверяясь с содержимым файла `output.txt`.

#### Keycap [MISC]
##### По условие имеем файл dump.pcap. 
##### Заглянув, внутрь с помощью wireshark - убеждаемся в том, что перед нами находится usb capture.
##### C помощью скрипта (найден по запросу "ctf usb capture" - https://ctf-wiki.github.io/ctf-wiki/misc/traffic/protocols/USB/)
##### Запускаем этот скрипт с помощью команды `python ./script.py dump.pcap`
##### Получаем вывод: `[+] Found : keycap.tasks.2020.ctf.cs.msu.ru<RET>eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzZXRGbGFnIjoiVHJ1ZSIsInNob3dGbGFnIjoiRmFsc2UifQ.<RET>`
##### Видим url и какой-то. Пробуем отправить токен в форму на http://keycap.tasks.2020.ctf.cs.msu.ru и получаем ответ `Flag is already set!`
##### Разбираемся в чем дело. Пробуем раздекодить токен в base64 - `{"typ":"JWT","alg":"none"}￿{"setFlag":"True","showFlag":"False"}`. 
##### Раскодировав ее из base64, становится известно, что JWT ничем не подписан и его можно изменять как хочется. Если установить `{"setFlag":"False","showFlag":"True"}` и сдать вновь полученный токен, изменив "\" на "." полученный токен, сервис отдаст флаг.
