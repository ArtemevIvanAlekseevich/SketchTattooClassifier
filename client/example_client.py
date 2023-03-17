import os

from pprint import pprint

from client import ClientSketchTattooClassifier

if __name__ == '__main__':

    # Creating client
    client = ClientSketchTattooClassifier()

    # work with image path
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_path = os.path.join(dir_path, 'test.jpg')
    pprint(client.img_path2type(img_path))
    # result
    '''
    {'probabilities': {'Chicano': 0.0005174795514903963,
                   'Engraving': 0.0012208480620756745,
                   'Japanese': 0.001117055886425078,
                   'Linework': 0.0035219548735767603,
                   'Minimalist': 0.9846374988555908,
                   'New school': 0.002163673983886838,
                   'Other': 0.0022433940321207047,
                   'Realism': 0.0022268760949373245,
                   'Traditional': 0.002351153641939163},
     'top_1': 'Minimalist',
     'top_3': ['Minimalist', 'Linework', 'Traditional']}
    '''

    # work with image
    dir_path = os.path.dirname(os.path.realpath(__file__))
    img_path = os.path.join(dir_path, 'test.jpg')
    with open(img_path, 'rb') as file:
        image = file.read()
    pprint(client.img2type(image))
    # result
    '''
    {'probabilities': {'Chicano': 0.0005174795514903963,
                   'Engraving': 0.0012208480620756745,
                   'Japanese': 0.001117055886425078,
                   'Linework': 0.0035219548735767603,
                   'Minimalist': 0.9846374988555908,
                   'New school': 0.002163673983886838,
                   'Other': 0.0022433940321207047,
                   'Realism': 0.0022268760949373245,
                   'Traditional': 0.002351153641939163},
     'top_1': 'Minimalist',
     'top_3': ['Minimalist', 'Linework', 'Traditional']}
    '''
    # Work with url
    some_tattoo_url = 'https://i.pinimg.com/originals/71' +\
                      '/9d/d1/719dd1e3c24f6d89000d34053465f5a3.jpg'
    pprint(client.img_url2type(some_tattoo_url))
    # result
    '''
    {'probabilities': {'Chicano': 0.4754016697406769,
                   'Engraving': 0.1928965300321579,
                   'Japanese': 0.11786531656980515,
                   'Linework': 0.09553991258144379,
                   'Minimalist': 0.015211457386612892,
                   'New school': 0.018308987841010094,
                   'Other': 0.03690987825393677,
                   'Realism': 0.02684232033789158,
                   'Traditional': 0.021023869514465332},
     'top_1': 'Chicano',
     'top_3': ['Chicano', 'Engraving', 'Japanese']}
    '''
