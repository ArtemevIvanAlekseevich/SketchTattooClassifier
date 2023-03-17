import io

import numpy as np
from PIL import Image

from app.model.settings import MEAN
from app.model.settings import STD


def norm_numpy(array):
    array = array.transpose(-1, 0, 1)
    array = (array - MEAN[:, None, None]) / STD[:, None, None]
    return array


def get_padding_inference(image: np.array) -> tuple:

    imsize = image.size
    max_w = max_h = max(max(imsize), 256)
    h_padding = (max_w - imsize[0]) / 2
    v_padding = (max_h - imsize[1]) / 2
    l_pad = h_padding if h_padding % 1 == 0 else h_padding+0.5
    t_pad = v_padding if v_padding % 1 == 0 else v_padding+0.5
    r_pad = h_padding if h_padding % 1 == 0 else h_padding-0.5
    b_pad = v_padding if v_padding % 1 == 0 else v_padding-0.5
    padding = (int(l_pad), int(t_pad), int(r_pad), int(b_pad))

    return padding


def padding(image: Image.Image) -> Image.Image:

    left, top, right, bottom = get_padding_inference(image)
    width, height = image.size
    new_width = width + right + left
    new_height = height + top + bottom
    result = Image.new(image.mode, (new_width, new_height))
    result.paste(image, (left, top))

    return result


def image_preprocessing_inference(image) -> np.array:

    bytes_im = io.BytesIO(image)
    image = Image.open(bytes_im).convert('RGB')
    image = padding(image)
    image.thumbnail(size=(256, 256))
    image = np.array(image)
    image = norm_numpy(image / 255.)
    image = image.reshape(1, 3, 256, 256)
    return image.astype(np.float32)
