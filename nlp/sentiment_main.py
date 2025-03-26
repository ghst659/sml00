#!/usr/bin/env python3

import argparse
import collections
import logging
import os
import pathlib
import sys

import tensorflow as tf

def main(argv: collections.abc.Sequence[str]) -> int:
    """Hello-world application to use a pre-trained NLP model stored in a .keras file."""
    # Parse command-line flags
    parser = argparse.ArgumentParser(description=main.__doc__)
    parser.add_argument("--model", type=pathlib.Path, default="/tmp/tweet_model.keras", dest="model",
                        help="Path to the .keras model file")
    parser.add_argument("--prompt", type=str, default="Enter a string", dest="prompt",
                        help="Prompt string for each round of user input.")
    args = parser.parse_args(args=argv[1:])

    # Read the model from the file.
    nlp_model = read_model_from_file(args.model)
    nlp_model.summary()  # prints a summary of the model.

    # Repeatedly get a string from the user, and run it through the model.
    prompt = args.prompt + " (Ctrl-D to end): "
    while True:
        try:
            user_text = input(prompt)
        except EOFError as e:
            print("Done.")
            break
        logging.info("user entry: %s", user_text)

        # TODO: call the model with the string and show the result.
        #       The current model does not take a string as input.
        # predicted_sentiment = nlp_model(tf.constant([user_text]))
        # print("prediction:", predicted_sentiment)
    return 0


def read_model_from_file(path: os.PathLike) -> tf.keras.Model:
    """Reads a previously-trained Model from a disc file in .keras format.

    The model file should have been saved with keras.Model.save()
       https://www.tensorflow.org/api_docs/python/tf/keras/Model#save

    The model saved by
      https://github.com/ghst659/sml00/blob/main/nlp/Tutorial_Emotion.ipynb
    is self-sufficient, but has not been converted to take strings as input.

    The model should be constructed to take strings as an input, like
    the end_to_end_model in
      https://github.com/ghst659/sml00/blob/main/nlp/text_classify.ipynb
    but that model has a dependency on a function not saved in the file.
    """
    logging.info("reading model: %s", path)
    model = tf.keras.models.load_model(path)
    return model
    


if __name__ == "__main__":
    sys.exit(main(sys.argv))
