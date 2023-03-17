import requests

import numpy as np
import onnxruntime as ort
from fastapi import FastAPI, UploadFile, File


from app.model.settings import NUM_TO_TYPE
from app.model.image_preprocessing import image_preprocessing_inference

app = FastAPI()

ort_sess = ort.InferenceSession('app/model/model.onnx')


def outputs2ans(outputs: np.array):
    top_3_list = np.argsort(outputs, axis=1,)[:, :-4:-1].tolist()[0]
    probas = (np.exp(outputs) / np.exp(outputs).sum()).tolist()[0]

    ans = {
        'top_1': NUM_TO_TYPE[top_3_list[0]],
        'top_3': [NUM_TO_TYPE[number] for number in top_3_list],
        'probabilities': {
            NUM_TO_TYPE[num]: proba for num, proba in enumerate(probas)
        }
    }
    return ans


@app.post('/file')
async def file2type(
        image: UploadFile = File(),
):

    image = await image.read()
    image = image_preprocessing_inference(image)
    outputs = np.array(ort_sess.run(None, {'modelInput': image}))[0]
    ans = outputs2ans(outputs)
    return ans


@app.post('/link')
def link2type(
        url: str,
):
    response = requests.get(url)
    image = response.content
    image = image_preprocessing_inference(image)

    outputs = np.array(ort_sess.run(None, {'modelInput': image}))[0]
    ans = outputs2ans(outputs)
    return ans
