# Speech to Text Documentation

This document explains the code found in `speech-to-text.py` and `speech-to-text_translate.py` which are responsible for converting speech to text using the OpenAI API.

## Overview

Both scripts use the OpenAI Python client to transcribe speech from an audio file to text. The `speech-to-text.py` script transcribes the speech as is, while `speech-to-text_translate.py` appears to be intended for translating the speech, although it incorrectly uses the same transcription method as `speech-to-text.py`.

## Code Explanation

### speech-to-text.py

1. **Import Statements:**
   The script imports the `OpenAI` class from the `openai` library.

2. **OpenAI Client Initialization:**
   An instance of the `OpenAI` client is created.

3. **File Handling:**
   The script specifies the path to an MP3 file and opens it in binary read mode.

4. **Transcription:**
   The `audio.transcriptions.create` method is called on the client instance, passing in the model name (`whisper-1`), the audio file, and the response format (`text`).

5. **Output:**
   The transcript is printed to the console.

### speech-to-text_translate.py

The code in `speech-to-text_translate.py` is almost identical to `speech-to-text.py`, with the exception of the variable names. It should be noted that the method used for transcription is not suitable for translation, and the script would need to be modified to perform translation.

## Example Usage

The scripts can be used to transcribe speech from an audio file, such as a recorded conversation or a speech, into text format.
