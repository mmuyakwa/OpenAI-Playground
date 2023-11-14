# Text to Speech Documentation

This document explains the code found in `text-to-speech.py` which generates speech from text using the text-to-speech model from OpenAI.

## Overview

The script uses the OpenAI Python client to convert a given text prompt into speech. The generated speech is saved as an MP3 file.

## Code Explanation

1. **Import Statements:**
   The script imports `Path` from the `pathlib` library for file path operations, and the `OpenAI` class from the `openai` library.

2. **OpenAI Client Initialization:**
   An instance of the `OpenAI` client is created.

3. **File Path Creation:**
   A file path for the generated speech is created using the `Path` class.

4. **Generating Speech:**
   The `audio.speech.create` method is called on the client instance, passing in the model name (`tts-1`), the voice (`nova`), and the input text.

5. **Saving the Speech File:**
   The generated speech is saved to the specified file path using the `stream_to_file` method.

6. **Output:**
   The saved MP3 file contains the generated speech from the input text.

## Example Usage

The script can be used to generate speech from text, which can be useful for creating audio content from written material or for accessibility purposes.
