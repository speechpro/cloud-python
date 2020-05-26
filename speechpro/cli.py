import os
import sys

import click

from speechpro.cloud.speech import recognition
from speechpro.cloud.speech import synthesis


recognitionClient = recognition.RecognitionClient(
    os.environ['SPEECHPRO_USERNAME'],
    os.environ['SPEECHPRO_DOMAIN_ID'],
    os.environ['SPEECHPRO_PASSWORD']
)

synthesisClient = synthesis.SynthesisClient(
    os.environ['SPEECHPRO_USERNAME'],
    os.environ['SPEECHPRO_DOMAIN_ID'],
    os.environ['SPEECHPRO_PASSWORD']
)


def recognize(language, model, response_type, filename, audio_channel_count=1):
    with open(filename, "rb") as f:
        content = f.read()

    config = {
        'language': language,
        'model': model,
        'encoding': recognition.enums.AudioEncoding.WAV,
        'response_type': response_type,
        'audio_channel_count': audio_channel_count
    }
    return recognitionClient.recognize(config, content)


@click.group()
def cli():
    pass

@cli.command()
@click.option('--language', default=recognition.enums.Language.RU)
@click.option('--model', default=recognition.enums.Model.GENERAL)
@click.option('--filename', type=str,)
def recognize_plain_text(language, model, filename):
    result = recognize(language, model, recognition.enums.ResponseType.PLAIN_TEXT, filename)
    print(result.text)
    return 0


@cli.command()
@click.option('--language', default=recognition.enums.Language.RU)
@click.option('--model', default=recognition.enums.Model.GENERAL)
@click.option('--filename', type=str,)
def recognize_word_list(language, model, filename):
    result = recognize(language, model, recognition.enums.ResponseType.WORD_LIST, filename)
    for w in result:
        print(w.word)
    return 0


@cli.command()
@click.option('--language', default=recognition.enums.Language.RU)
@click.option('--model', default=recognition.enums.Model.GENERAL)
@click.option('--filename', type=str,)
@click.option('--audio_channel_count', type=int,)
def recognize_multichannel(language, model, filename, audio_channel_count):
    result = recognize(language, model, recognition.enums.ResponseType.MULTICHANNEL, filename, audio_channel_count)
    for ch in result:
        print(f'Channel {ch.channel_id}')
        for w in ch.result:
            print(w.word)
        print('\n')
    return 0


@cli.command()
@click.option('--voice', default=synthesis.enums.Voice.JULIA)
@click.option('--profile', default=synthesis.enums.PlaybackProfile.SPEAKER)
@click.option('--output', type=str)
@click.option('--input', type=str)
def synthesize(voice, profile, output, input):
    try:
        with open(input) as f:
            text = f.read()
    except:
        text = input
    audio = synthesisClient.synthesize(voice, profile, text)

    with open(output, 'wb') as outputfile:
        outputfile.write(audio)



if __name__ == "__main__":
    sys.exit(cli())  # pragma: no cover