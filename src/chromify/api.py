from fastapi import FastAPI, File, UploadFile
import chromify.model as model
from contextlib import asynccontextmanager
from PIL import Image
import numpy as np
import torch
from io import BytesIO
import base64

@asynccontextmanager
async def lifespan(app: FastAPI):
    global my_model
    my_model = model.MainModel()

    yield
    
    del my_model

app = FastAPI(lifespan=lifespan)

# Add CORS middleware
from fastapi.middleware.cors import CORSMiddleware

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Replace with your frontend URL
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

@app.post("/infer")
async def infer(data: UploadFile = File(...)):
    input_image = Image.open(data.file).convert("L")
    input_tensor = torch.tensor(np.array(input_image)).unsqueeze(0).unsqueeze(0).float() / 255.0

    my_model.setup_input({'L': input_tensor, 'ab': torch.zeros_like(input_tensor)})
    my_model.forward()
    output_tensor = my_model.fake_color.squeeze(0).detach().cpu().numpy()
    
    output_image = np.transpose(output_tensor, (1, 2, 0))
    output_image = (output_image * 255).astype(np.uint8)
    output_image = Image.fromarray(output_image)
    
    buffered = BytesIO()
    output_image.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    
    return {"colorized_image": img_str}