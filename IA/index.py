from chatterbot.trainers import ListTrainer
from chatterbot import ChatBot

bot = ChatBot('CGD Chat Bot')

conversa = ['Oi', 'Olá', 'Tudo bem?', 'Tudo ótimo', 'Você gosta de programar?', 'Sim, eu programo em Python']

bot.set_trainer(ListTrainer)
bot.train(conversa)

while True:
    pergunta = input("Usuário")
    resposta = bot.get_response(pergunta)
    if float(resposta.confidence) > 0.5:
        print('CGD Bot: ', resposta)
    else: 
        print('CGD Bot: Ainda não sei responder esta pergunta')