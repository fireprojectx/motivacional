from fastapi import FastAPI
import random

app = FastAPI()

versiculos = [
    {"livro": "Salmos", "capitulo": 23, "versiculo": 1, "texto": "O Senhor é o meu pastor, nada me faltará."},
    {"livro": "Filipenses", "capitulo": 4, "versiculo": 13, "texto": "Posso todas as coisas naquele que me fortalece."},
    {"livro": "Isaías", "capitulo": 41, "versiculo": 10, "texto": "Não temas, porque eu sou contigo; não te assombres, porque eu sou o teu Deus."},
    {"livro": "Jeremias", "capitulo": 29, "versiculo": 11, "texto": "Porque eu bem sei os pensamentos que penso de vós, diz o Senhor; pensamentos de paz, e não de mal."},
    {"livro": "Romanos", "capitulo": 8, "versiculo": 28, "texto": "Sabemos que todas as coisas cooperam para o bem daqueles que amam a Deus."}
]

@app.get("/")
def raiz():
    return {"mensagem": "API Bíblica Motivacional - Acesse /versiculo para receber um versículo aleatório."}

@app.get("/versiculo")
def versiculo():
    v = random.choice(versiculos)
    return {
        "texto": v["texto"],
        "referencia": f'{v["livro"]} {v["capitulo"]}:{v["versiculo"]}'
    }
