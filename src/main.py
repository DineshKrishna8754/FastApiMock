import os

import fastapi as _fastapi
import fastapi.encoders as _encoders
import fastapi.responses as _responses
import base64

from fastapi.openapi.models import Response
from pydantic import BaseModel
from starlette.responses import JSONResponse

import services as _services

app = _fastapi.FastAPI()

class Img2ImgReq(BaseModel):
    base64_image: str
    photo_name: str

class Txt2ImgReq(BaseModel):
    input_text: str


@app.get("/programmer-memes")
def get_programmer_meme():
    image_path = _services.select_random_image("ProgrammerHumor")
    return _responses.FileResponse(image_path)


@app.post("/programmer-memes")
def post_programmer_meme(image: _fastapi.UploadFile = _fastapi.File(...)):
    file_name = _services.upload_image("ProgrammerHumor", image)
    image_path = _services.select_random_image("ProgrammerHumor")
    if file_name is None:
        return _fastapi.HTTPException(status_code=409, detail="incorrect file type")
    return _responses.FileResponse(image_path)


@app.get("/cat-memes")
def get_cat_memes():
    image_path = _services.select_random_image("Catmemes")
    return _responses.FileResponse(image_path)


@app.get("/image")
def get_meme():
    return _responses.FileResponse("ProgrammerHumor/tq00bck4mov61.gif")


@app.post("/img2img")
async def post_base64Image2Image(img2img : Img2ImgReq):
    imgstr = img2img.base64_image
    imgdata = base64.b64decode(imgstr)
    filename = '%s.jpg' % img2img.photo_name
    with open("ProgrammerHumor/"+filename, 'wb') as f:
        f.write(imgdata)
    test = {"statusCodeValue": "200","statusCode":"OK"}
    base64_arr = []
    for images in os.listdir("GenImages"):
        if (images.endswith(".png")):
            with open("GenImages/"+images, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                base64_arr.append(encoded_string.decode("utf-8"))
                # a_dict = {'base64_'+str(count): encoded_string.decode("utf-8")}
    a_dict = {'base64_arr': base64_arr}

    test.update(a_dict)

    return JSONResponse(content=test, media_type="application/json")\



@app.post("/txt2img")
async def post_base64Text2Image(txt2img : Txt2ImgReq ):
    test = {"statusCodeValue": "200","statusCode":"OK"}
    base64_arr = []
    for images in os.listdir("GenImages"):
        if (images.endswith(".png")):
            with open("GenImages/"+images, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                base64_arr.append(encoded_string.decode("utf-8"))
                # a_dict = {'base64_'+str(count): encoded_string.decode("utf-8")}
    a_dict = {'base64_arr': base64_arr}

    test.update(a_dict)

    return JSONResponse(content=test, media_type="application/json")


@app.get("/getImages")
async def get_base64Images():
    test = {"statusCodeValue": "200","statusCode":"OK"}
    base64_arr = []
    for images in os.listdir("GenImages"):
        if (images.endswith(".png")):
            with open("GenImages/"+images, "rb") as image_file:
                encoded_string = base64.b64encode(image_file.read())
                base64_arr.append(encoded_string.decode("utf-8"))
                # a_dict = {'base64_'+str(count): encoded_string.decode("utf-8")}
    a_dict = {'base64_arr': base64_arr}

    test.update(a_dict)

    return JSONResponse(content=test, media_type="application/json")
