## Keycap [MISC]
Изучив `dump.pcap` с помощью wireshark, понимаем, что перед нами находится usb capture. По запросу "ctf usb capture" находим скрипт https://ctf-wiki.github.io/ctf-wiki/misc/traffic/protocols/USB/ и запускаем: `python ./script.py dump.pcap`.
Вывод:


`[+] Found : keycap.tasks.2020.ctf.cs.msu.ru<RET>eyJ0eXAiOiJKV1QiLCJhbGciOiJub25lIn0.eyJzZXRGbGFnIjoiVHJ1ZSIsInNob3dGbGFnIjoiRmFsc2UifQ.<RET>`


Видим url и JWT токен. Пробуем отправить токен в форму на http://keycap.tasks.2020.ctf.cs.msu.ru и получаем ответ


>Flag is already set!


Разбираемся в чем дело. Пробуем раздекодить токен в base64 - `{"typ":"JWT","alg":"none"}.{"setFlag":"True","showFlag":"False"}`. Видим, что токен ничем не подписан и его можно изменять как хочется. Если установить `{"setFlag":"False","showFlag":"True"}` и сдать вновь полученный токен, сервис отдаст флаг.
