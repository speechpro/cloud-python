# Распознавание и синтез речи в Облаке ЦРТ

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

## Распознавание речи из файла
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

with open('path_to_wav_file', "rb") as f:
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

### Полная документация API распознавания речи
Полная документация API распознавания речи доступна на сайте Облака ЦРТ по адресу https://cp.speechpro.com/doc/asr

## Синтез речи
Код для синтеза текста голосом *Юлия* выглядит следующим образом:
```python
from speechpro.cloud.speech import synthesis

synthesisClient = synthesis.SynthesisClient(
    os.environ['SPEECHPRO_USERNAME'],
    os.environ['SPEECHPRO_DOMAIN_ID'],
    os.environ['SPEECHPRO_PASSWORD']
)

text = 'Привет, я - синтезированный голос от компании ЦРТ'
audio = synthesisClient.synthesize(synthesis.enums.Voice.JULIA, synthesis.enums.PlaybackProfile.SPEAKER, text)

with open('output.wav', 'wb') as f:
    f.write(audio)
```

### Полная документация API синтеза речи
Полная документация API синтеза речи доступна на сайте Облака ЦРТ по адресу https://cp.speechpro.com/doc/tts

## TODO
* Добавить оставшиеся методы API распознавания речи
* Добавить методы API синтеза речи
* Больше примеров
