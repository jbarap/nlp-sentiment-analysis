from src.models import rnn


def inference(sentences):
    processed_sentences = sentences  # replace with function_to_preprocess_sentences

    predictions = {}

    rnn_predictions = rnn.inference(processed_sentences)
    predictions.update(rnn_predictions)

    return combine_predictions(predictions)


def combine_predictions(predictions, positive_threshold=0.5):
    _check_same_length(predictions)

    final_predictions = []
    for models_prediction in zip(*predictions.values()):
        avg = sum(models_prediction) / len(models_prediction)
        if avg >= positive_threshold:
            final_predictions.append(1)
        else:
            final_predictions.append(0)

    return final_predictions


def _check_same_length(predictions):
    n = len(next(predictions.values().__iter__()))

    same_length = True
    for value in predictions.values():
        if value != n:
            same_length = False

    if not same_length:
        raise ValueError("Not all predictions are the same length.")