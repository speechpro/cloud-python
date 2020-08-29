# Распознавание и синтез речи в Облаке ЦРТ
[![PyPI version](https://badge.fury.io/py/speechpro-cloud-python.svg)](https://badge.fury.io/py/speechpro-cloud-python)

## Начало работы
Установите клиентскую библиотеку с помощью pip
```shell
pip install speechpro-cloud-python
```

Создайте файл *~/.speechpro/credentials*, укажите в ней данные учетной записи в формате TOML в профиле (секции) *default*, например:
```toml
[default]
username = "username"
domain_id = 200
password = "password"
```
Узнайте больше об аутентификации в разделе [Аутентификация](#аутентификация).

## Распознавание речи из файла
Код распознавания WAV файла на русском языке моделью **GENERAL** выглядит следующим образом
```python
import os

from speechpro.cloud.speech.recognition import RecognitionClient
from speechpro.cloud.speech.recognition import enums

сlient = RecognitionClient()

with open('path_to_wav_file', "rb") as f:
    content = f.read()

config = {
    'language': enums.Language.RU,
    'model': enums.Model.GENERAL,
    'encoding': enums.AudioEncoding.WAV,
    'response_type': enums.ResponseType.WORD_LIST,
}

word_list = сlient.recognize(config, content)
for w in word_list:
    print(w.word)
```

Аналогичная операция с помощью командной строки
```shell
speechpro recognize-word-list --model GENERAL --filename //path_to_audio
```

### Полная документация API распознавания речи
Полная документация API распознавания речи доступна на сайте Облака ЦРТ по адресу https://cp.speechpro.com/doc/asr

## Синтез речи
Код для синтеза текста голосом **Юлия** выглядит следующим образом:
```python
import os
from speechpro.cloud.speech import synthesis

сlient = synthesis.SynthesisClient()

text = 'Привет, я - синтезированный голос от компании ЦРТ'
audio = сlient.synthesize(synthesis.enums.Voice.JULIA, synthesis.enums.PlaybackProfile.SPEAKER, text)

with open('output.wav', 'wb') as f:
    f.write(audio)
```

Аналогичная операция с помощью командной строки
```shell
speechpro synthesize --voice JULIA --input "Привет, я - синтезированный голос от компании ЦРТ" --output hi.wav
```

### Полная документация API синтеза речи
Полная документация API синтеза речи доступна на сайте Облака ЦРТ по адресу https://cp.speechpro.com/doc/tts

## Аутентификация

Данные для аутентификации можно задать несколькими способами - передать в качестве параметров в конструктор, сохранить в TOML формате, либо установить переменные среды.

### TOML

Предполагается, что TOML файл расположен по пути *~/.speechpro/credentials*, по умолчанию используется профиль (секция) *default*:

```toml
[default]
username = "username"
domain_id = 200
password = "password"
```
Для использования профиля с другим именем, установите его значение в переменную среду *SPEECHPRO_PROFILE*.

### Переменные среды

Задайте данные вашей учетной записи [Облака ЦРТ](https://cp.speechpro.com) с помощью переменных среды, их значения будут использованы в случае, если не удастся прочитать TOML файл.
```shell
export SPEECHPRO_USERNAME=username
export SPEECHPRO_DOMAIN_ID=200
export SPEECHPRO_PASSWORD=password
```

### Конструктор

Возможно также передать значения напрямую в конструктор, например:

```python
from speechpro.cloud.speech.recognition import RecognitionClient

сlient = RecognitionClient(
    'username',
    200,
    'password'
)
```

## TODO
* Добавить оставшиеся методы API распознавания речи
* Описания моделей и голосов
* Больше примеров
