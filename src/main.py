from fastapi import FastAPI
import uvicorn
import hydra
from core.config import Config

@hydra.main(version_base= "1.2.0" ,config_path="core", config_name="config")
def main(cfg: Config) -> FastAPI:
    instance = FastAPI(title="Title", debug=True)
    return instance

app = main()

if __name__ == "__main__":
    uvicorn.run(
        'main:app',
        host="127.0.0.1",
        port=8000,
        debug=True
        )