from fastapi import FastAPI
import random

app = FastAPI()

frases = [
    "Acredite em você e tudo será possível.",
    "Você é mais forte do que imagina.",
    "Cada dia é uma nova chance de recomeçar.",
    "Não desista, o começo é sempre o mais difícil.",
    "Seu esforço de hoje constrói o seu sucesso de amanhã."
]

@app.get("/")
def raiz():
    return {"mensagem": "Bem-vindo à API Motivacional!"}

@app.get("/motivacao")
def motivacao():
    return {"frase": random.choice(frases)}
