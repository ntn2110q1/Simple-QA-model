from pyngrok import conf, ngrok
import uvicorn
import nest_asyncio
from app import *

conf.get_default().auth_token = "ngrok_token"

# Tạo tunnel tới port 8000
public_url = ngrok.connect(8000)
print("Public URL:", public_url)

nest_asyncio.apply()

# Chạy FastAPI
uvicorn.run(app, host="0.0.0.0", port=8000)