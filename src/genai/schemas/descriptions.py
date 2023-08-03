# flake8: noqa


class Descriptions:
    # LengthPenalty
    DECAY_FACTOR = "Represents the factor of exponential decay and must be > 1.0. Larger values correspond to more aggressive decay."
    START_INDEX = "A number of generated tokens after which this should take effect."

    # Return
    RETURN = "key-value pairs."
    INPUT_TEXT = "Include input text."
    GENERATED_TOKEN = "Include list of individual generated tokens. 'Extra' token information is included based on the other flags below."
    INPUT_TOKEN = "Include list of input tokens. 'Extra' token information is included based on the other flags here, but only for decoder-only models."
    TOKEN_LOGPROBS = "Include logprob for each returned token. Applicable only if generated_tokens == true and/or input_tokens == true."
    TOKEN_RANKS = (
        "Include rank of each returned token. Applicable only if generated_tokens == true and/or input_tokens == true."
    )
    TOP_N_TOKENS = "Include top n candidate tokens at the position of each returned token. The maximum value permitted is 5, but more may be returned if there is a tie for nth place. Applicable only if generated_tokens == true and/or input_tokens == true."

    # Params.Token
    RETURN_TOKEN = "Return tokens with the response. Defaults to false."

    # Params.History
    LIMIT = "Specifies the maximum number of items in the collection that should be returned. Defaults to 100. Maximum is 100."
    OFFSET = "Specifies the starting position in the collection. Defaults to 0."
    STATUS = "Filters the items to be returned based on their status. Possible values are SUCCESS and ERROR."
    ORIGIN = "Filters the items to be returned based on their origin. Possible values are API and UI."


class TunesAPIDescriptions:
    # Params.CreateTune
    NAME = "Name of the tune."
    SEARCH = "Filters the items to be returned based on their name."
    MODEL_ID = "The ID of the model to be used for this request."
    METHOD_ID = "The ID of the tuning method to be used for this request."
    TASK_ID = "Task ID that determines format of the training data. Possible values are generic, classification, or summarization."
    TRAINING_FILE_IDS = "The IDs of uploaded files that contain training data."
    VALIDATION_FILE_IDS = "The IDs of uploaded files that contain validation data."
    PARAMETERS = "key-value pairs"
    ACCUMULATE_STEPS = "Number of training steps to use to combine gradients. This helps overcome the limitation of smaller batch sizes due to GPU memory limitations. The range is 1 to 128, defaults to 16."
    BATCH_SIZE = "The number of samples to work through before updating the internal model parameters. Optimal batch size set points are based on a combination of the number of examples you’ve uploaded as well as other parameters. If you’ve uploaded a smaller training data set, you should set your batch size lower. The range is 1 to 16, defaults to 16."
    LEARNING_RATE = "Learning rate to be used while tuning prompt vectors. The range is 0.01 to 0.5, defaults to 0.3."
    MAX_INPUT_TOKENS = "The maximum number of tokens that are accepted in the input field for each example. If any of the input rows in your training data set exceed this value, the input data will be truncated at the set maximum value. The range is 1 to 256, defaults to 256."
    MAX_OUTPUT_TOKENS = "The maximum number of tokens that are accepted in the output field for each example. If any of the output rows in your training data set exceed this value, the output data will be truncated at the set maximum value. The range is 1 to 128, defaults to 128."
    NUM_EPOCHS = "The number of times to cycle through the training data set. If you have a large training data set, a high number of epochs will take a very long time to finish tuning. The range is 1 to 50, defaults to 20."
    NUM_VIRTUAL_TOKENS = "Number of virtual tokens to be used for training. This is purely experimental. If the default value doesn’t provide good results, you may want to try selecting another value. Possible values are 20, 50, or 100, defaults to 100."
    VERBALIZER = "Verbalizer template to be used for formatting data at train and inference time. This template may use double brackets to indicate where fields from training data should be rendered. The template can contain one or both of {{input}} and {{output}}. Defaults to {{input}}."
    OFFSET = "Specifies the starting position in the collection. Defaults to 0."
    LIMIT = "Specifies the maximum number of items in the collection that should be returned. Defaults to 100. Maximum is 100."
    SEARCH = "Filters the items to be returned based on their name."
    STATUS = "Filters the items to be returned based on their status. Possible values are: INITIALIZING, NOT_STARTED, PENDING, HALTED, RUNNING, QUEUED, COMPLETED, FAILED."
    INIT_METHOD = "Initialization method to be used. Possible values are RANDOM or TEXT. Defaults to RANDOM. Used only if the method_id is 'pt' = Prompt Tuning."
    INIT_TEXT = "Initialization text to be used. This is only applicable if init_method == TEXT. Used only if the method_id is 'pt' = Prompt Tuning."


class FilesAPIDescriptions:
    OFFSET = "Specifies the starting position in the collection. Defaults to 0."  # noqa
    LIMIT = "Specifies the maximum number of items in the collection that should be returned. Defaults to 100. Maximum is 100."  # noqa
    SEARCH = "Filters the items to be returned based on their name."
    PURPOSE = "The intended purpose of the uploaded document. Currently only tune or template are supported."  # noqa
    TASK_ID = "Task ID that determins format of the training data. Possible values are generation, classification, or summarization. This field is required if purpose == 'tune'."  # noqa
    FILE = "The file to be uploaded."
