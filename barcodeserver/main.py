from io import BytesIO

from fastapi import FastAPI, Query
from fastapi.responses import StreamingResponse

from barcode import generate
from barcode.writer import ImageWriter

app = FastAPI()


@app.get("/barcode/{file_path:path}")
async def generate_barcode(
    file_path: str,
    value: str,
    barcode_type: str = Query(alias="type"),
    text: str = None
):

    generated_image = BytesIO()
    generate(name=barcode_type, code=value, writer=ImageWriter(), output=generated_image)
    generated_image.seek(0)

    return StreamingResponse(generated_image, media_type="image/png")
