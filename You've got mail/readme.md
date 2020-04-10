## You've got mail

Нам дан файл без расширения. Открыв его в текстовом редакторе (notepad++ as example) видим перед собой, что-то по типу дампа почты.

Просмотрев дамп, находим base64 от архива:
```
 filename="attach.zip"

UEsDBBQACQAIAFZidVBv9f5ahwAAAHkAAAAIAAAAZmxhZy50eHQ45c3zHhuqVNivOf80djnC
tmkmwiSCTELSf0iFP6kEGDd3NlChMcSk0q/kN9oCTYH1NZSli0d2DS22xNVt/wLwLEwkwxdN
CXNajXmLRN5FxD3C2/Br6aCFvpylLx6y245zkB0cd8u9ICEVoiMhjITSIsAsnarMCK8IUwZX
MLNAehKGf0nkGkFQSwcIb/X+WocAAAB5AAAAUEsBAh8AFAAJAAgAVmJ1UG/1/lqHAAAAeQAA
AAgAJAAAAAAAAAAgAAAAAAAAAGZsYWcudHh0CgAgAAAAAAABABgAmQOVuGH/1QGE2Utw6v7V
AYTZS3Dq/tUBUEsFBgAAAAABAAEAWgAAAL0AAAAAAA==
--------------100AC5362A69E32B7F7DE353--
```

Достаем архив из base64 с помощью сайта https://base64.guru/converter/decode/file

В этом архиве видим один файл flag.txt, но он запаролен.

Однако в дампе было сообщение:

```
Content-Transfer-Encoding: 8bit

╨Э╨░╤Б╤В╤Г╨┐╨╕╨╗ ╤Б╨╡╨╖╨╛╨╜ ╨┐╨╡╤А╨╡╨▓╨╡╤А╨╜╤Г╨▓╤И╨╕╤Е╤Б╤П ╨┐╨╕╨╜╨│╨▓╨╕╨╜╨╛╨▓, ╨▓╤Л╨┤╨▓╨╕╨│╨░╤О╤Б╤М ╨╜╨░ ╨┐╨╛╨▒╨╡╤А╨╡╨╢╤М╨╡
╨┐╨╡╤А╨╡╨▓╨╛╤А╨░╤З╨╕╨▓╨░╤В╤М ╨╕╤Е ╨╛╨▒╤А╨░╤В╨╜╨╛.

╨С╨╡╤А╤Г ╨╝╨░╨╗╤Г╤О ╨╗╨╛╨┐╨░╤В╤Г ╨╕ ╨╗╤Л╨╢╨╕.

╨Я╤А╨╕╨╗╨░╨│╨░╤О ╤А╨╡╨╖╨╡╤А╨▓╨╜╤Г╤О ╨║╨╛╨┐╨╕╤О ╨╝╨╛╨╕╤Е ╨┤╨╛╨║╤Г╨╝╨╡╨╜╤В╨╛╨▓ ╨╜╨░ ╤Б╨╗╤Г╤З╨░╨╣, ╨╡╤Б╨╗╨╕ ╤Б╨╛ ╨╝╨╜╨╛╨╣ ╤З╤В╨╛-╤В╨╛
╤Б╨╗╤Г╤З╨╕╤В╤Б╤П. ╨Я╨░╤А╨╛╨╗╤М ╨║ ╨░╤А╤Е╨╕╨▓╤Г - ╨╕╤Б╤В╨╕╨╜╨░


╨Т╨░╤И╨░ ╨Э╨░╤В╨░╤И╨░.
```

С помощью сайта  http://www.online-decoder.com/ru переводим сообщение в utf-8:

```
Наступил сезон перевернувшихся пингвинов, выдвигаюсь на побережье
переворачивать их обратно.

Беру малую лопату и лыжи.

Прилагаю резервную копию моих документов на случай, если со мной что-то
случится. Пароль к архиву - истина


Ваша Наташа.
```

Вводим пароль `истина` и получаем файл с флагом.

Флаг: MSKCTF{the_truth_i$_0uT_tHeRe_haha}
