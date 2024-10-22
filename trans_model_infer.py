

import numpy as np # linear algebra




# Use a pipeline as a high-level helper
from transformers import pipeline

def translate(text):
    pipe = pipeline("translation_en_to_fr", model="google-t5/t5-small", )

    # %% [code] {"execution":{"iopub.status.busy":"2024-10-21T08:12:52.355169Z","iopub.execute_input":"2024-10-21T08:12:52.355601Z","iopub.status.idle":"2024-10-21T08:12:52.612500Z","shell.execute_reply.started":"2024-10-21T08:12:52.355562Z","shell.execute_reply":"2024-10-21T08:12:52.611387Z"},"jupyter":{"outputs_hidden":false}}
    trans = pipe(f'translate English to French: {text}')

    # %% [code] {"execution":{"iopub.status.busy":"2024-10-21T08:12:55.089585Z","iopub.execute_input":"2024-10-21T08:12:55.090891Z","iopub.status.idle":"2024-10-21T08:12:55.096481Z","shell.execute_reply.started":"2024-10-21T08:12:55.090786Z","shell.execute_reply":"2024-10-21T08:12:55.095295Z"},"jupyter":{"outputs_hidden":false}}
    return trans[0]['translation_text']