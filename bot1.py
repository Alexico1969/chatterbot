from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chatbot = ChatBot(name='MyBot', read_only=True, logic_adapters=['chatterbot.logic.MathematicalEvaluation', 'chatterbot.logic.BestMatch'])


conversation = [
    "Hello",
    "Hi there!",
    "How are you doing?",
    "I'm doing great.",
    "What is the best school in Queens?",
    "Archbishop Molloy High School",
]

trainer = ListTrainer(chatbot)

trainer.train(conversation)

while True:
    msg = input("You: ")
    if msg.strip() != 'Bye':
        print("Bot: ", chatbot.get_response(msg))
    else:
        break
