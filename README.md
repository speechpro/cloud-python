# Распознавание речи в Облаке ЦРТ

## Начало работы
Установите клиентскую библиотеку с помощью pip
```
pip install speechpro-cloud-python
```

Задайте данные вашей учетной записи [Облака ЦРТ](https://cp.speechpro.com) с помощью переменных среды, например
```
export SPEECHPRO_USERNAME=username
export SPEECHPRO_DOMAIN_ID=200
export SPEECHPRO_PASSWORD=password
```

Код распознавания WAV файла на русском языке моделью GENERAL выглядит следующим образом
```python
import os

from speechpro.cloud.speech.recognition import RecognitionClient
from speechpro.cloud.speech.recognition import enums

recognitionClient = RecognitionClient(
    os.environ['SPEECHPRO_USERNAME'],
    os.environ['SPEECHPRO_DOMAIN_ID'],
    os.environ['SPEECHPRO_PASSWORD']
)

with open('pepsi16kHz.wav', "rb") as f:
    content = f.read()

config = {
    'language': enums.Language.RU,
    'model': enums.Model.GENERAL,
    'encoding': enums.AudioEncoding.WAV,
    'response_type': enums.ResponseType.WORD_LIST,
}

word_list = recognitionClient.recognize(config, content)
for w in word_list:
    print(w.word)
```

Аналогичная операция с помощью командной строки
```
speechpro recognize-word-list --model GENERAL --filename //path_to_audio
```

## Полная документация API
Полная документация API распознавания речи доступна на сайте Облака ЦРТ по адресу https://cp.speechpro.com/doc/asr
