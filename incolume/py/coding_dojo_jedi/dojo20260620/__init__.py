"""dojo module."""

from __future__ import annotations

from pathlib import Path

import whisper
from icecream import ic


def transcrever(audio: Path | str, model_name: str = 'turbo') -> str:
    """Dojo solution."""
    if audio:
        audio = Path(audio)
    else:
        msg = f'Expected str or Path for `audio`, got {type(audio)}'
        raise TypeError(msg)

    model = whisper.load_model(model_name)

    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio.as_posix())
    audio = whisper.pad_or_trim(audio.as_posix())

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio, n_mels=model.dims.n_mels).to(
        model.device,
    )

    # detect the spoken language
    _, probs = model.detect_language(mel)
    ic(f'Detected language: {max(probs, key=probs.get)}')

    # decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # return recognized text
    return result.text


def dojo(**kwargs: str) -> dict[str]:
    """Dojo solution."""
    result = transcrever(
        kwargs.get('audio'),
        kwargs.get('model_name', 'turbo'),
    )
    return {'translate': result}


def main():
    """Main function."""
    ic('Hello from dojo20260620!')
    dojo(audio=Path('insumos', '17_06_2020 20.34.m4a'))


if __name__ == '__main__':
    main()
