# MSKCTF2020
#### More-less [PPC]
Простая задача на бинарный поиск.

#### Funny Farm [PPC]
Прочитав условие задачи можно понять, что это знаменитая игра быки и коровы (она же Mastermind). Существует много способов решения, здесь использовано дерево исходов.

#### Simple [RE]
В этой задаче можно было просто перебирать флаг посимвольно, сверяясь с содержимым файла `output.txt`.

#### Keycap [MISC]
... Можно получить строчку, очень похожую на JWT. Раскодировав ее из base64, становится известно, что JWT ничем не подписан и его можно изменять как хочется. Если установить `{"setFlag":"False","showFlag":"True"}` и сдать полученный токен, сервис отдаст флаг.
