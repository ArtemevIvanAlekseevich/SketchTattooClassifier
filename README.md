# Sketch Tattoo Classifier
---

## Description in English 
This service classifies tattoo sketches into 9 classes:
- Traditional
- New school
- Realism
- Engraving
- Japanese
- Chicano
- Minimalist
- Linework
- Other

### Get started with Sketch Tattoo Classifier
---
1. Clone the repository:
```bash
git clone https://github.com/ArtemevIvanAlekseevich/SketchTattooClassifier
```
2. [Download the model](https://drive.google.com/file/d/1dXTSdAaJOUXblimKGptV9px8wK-mFXh7/view?usp=sharing) and move it to the folder ```./SketchTattooClassifier/service/app/model```.
3. Create and start container:
```bash
docker compose up
```
4. Use service ([example of using](example_of_using/example_of_using.py)).

The service returns json like this:
```JSON
{
"top_1": "Minimalist",
"top_3": ["Minimalist", "Linework", "Traditional"],
"probability":
     {
     "Chicano": 0.0005174795514903963,
     "Engraving": 0.0012208480620756745,
     "Japanese": 0.001117055886425078,
     "Linework": 0.0035219548735767603,
     "Minimalist": 0.9846374988555908,
     "New school": 0.002163673983886838,
     "Other": 0.0022433940321207047,
     "Realism": 0.0022268760949373245,
     "Traditional": 0.002351153641939163
     },
}
```
where: 
- ```top_1``` is the most likely class, 
- ```top_3``` is the 3 most likely classes in descending order of the model's confidence, 
- ```probabilities``` is the model's confidence that the photo belongs to this class for all classes .
The client converts json to a dictionary.
## Описание на русском  
Данный сервис классифицирует эскизы татуировок на 9 классов:
- Traditional
- New school
- Realism
- Engraving
- Japanese
- Chicano
- Minimalist
- Linework
- Other

### Начать работать с Sketch Tattoo Classifier
---
1. Склонировать репозиторий:
```bash
git clone https://github.com/ArtemevIvanAlekseevich/SketchTattooClassifier
```
2. [Cкачать модель](https://drive.google.com/file/d/1dXTSdAaJOUXblimKGptV9px8wK-mFXh7/view?usp=sharing) и переместить ее в папку ```./SketchTattooClassifier/service/app/model```.
3. Поднять ```docker-compose```:
```bash
docker compose up
```
4. Начать использовать сервис ([пример использования](example_of_using/example_of_using.py)).

Сервис возвращает json вида:
```JSON
{ 
"top_1": "Minimalist",
"top_3": ["Minimalist", "Linework", "Traditional"],
"probabilities":
    {
    "Chicano": 0.0005174795514903963,
    "Engraving": 0.0012208480620756745,
    "Japanese": 0.001117055886425078,
    "Linework": 0.0035219548735767603,
    "Minimalist": 0.9846374988555908,
    "New school": 0.002163673983886838,
    "Other": 0.0022433940321207047,
    "Realism": 0.0022268760949373245,
    "Traditional": 0.002351153641939163
    },   
}
```
где: 
- ```top_1``` - наиболее вероятный класс, 
- ```top_3``` - 3 наиболее веротяных класса в порядке убывания уверенности модели, 
- ```probabilities``` - уверенность модели, что фото принадлежит данному классу для всех классов.
Клиент конвертирует json в словарь.