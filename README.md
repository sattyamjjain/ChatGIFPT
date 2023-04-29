# ChatGIFPT

ChatGIFPT is a Python package and Flask API that generates GIFs based on the given text input using OpenAI ChatGPT. The package utilizes the GIPHY API to search and retrieve GIFs related to the given text input.

## Installation

You can install ChatGIFPT using pip:

`pip install ChatGIFPT`

## Usage

### Using the package

To generate a GIF using the ChatGIFPT package, simply import the `generate_gif` function and pass the text input as an argument:

```python
from ChatGIFPT import generate_gif

gif_url = generate_gif("Hello world!")
```



