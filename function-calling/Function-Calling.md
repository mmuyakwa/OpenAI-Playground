# Function Calling Documentation

This document explains the code found in `function-calling.py` which demonstrates how to call a function using the OpenAI API.

## Overview

The script showcases an example of how to integrate external functions into a conversation with an OpenAI model. It simulates a conversation where a user asks about the weather in multiple cities, and the model calls a predefined function to get the weather data.

## Code Explanation

1. **Import Statements:**
   The script imports `json` for handling JSON data and the `OpenAI` class from the `openai` library.

2. **OpenAI Client Initialization:**
   An instance of the `OpenAI` client is created.

3. **Dummy Function Definition:**
   A dummy function `get_current_weather` is defined to simulate a weather API. It returns hardcoded weather data for Tokyo, San Francisco, and Paris.

4. **Conversation Simulation:**
   The `run_conversation` function sends a user message to the model and specifies the `get_current_weather` function as a tool that can be called.

5. **Function Call Handling:**
   The script checks if the model's response includes a request to call the `get_current_weather` function. If so, it calls the function with the provided arguments and sends the function's response back to the model.

6. **Output:**
   The final response from the model, which includes the weather data, is printed to the console.

## Example Usage

The script can be used to demonstrate how an OpenAI model can interact with external functions to provide dynamic responses based on external data or services.
