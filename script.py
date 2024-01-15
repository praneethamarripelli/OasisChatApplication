from nltk.chat.util import Chat, reflections

pairs = [
    [r'hi', ['hiii']],
    [r'hii|hey|hello', ['hi there']],
    [r'how are you', ['I am fine, how about you?']],
    [r'what is your name', ['My name is Chatbot']],
    [r'who invented you', ['I am a creation of Praneetha']],
    [r'who is your boss', ['My boss is Praneetha']],
    [r'are you mad', ['Nice joke']],
    [r'sorry', ['Machines cannot have feelings, it\'s okay']],
    [r'what is Python', ['Python is an interpreted programming language']],
]

def quit1():
    print("Hi, I am Chatbot. Ask me something.")

if __name__ == "__main__":
    chat = Chat(pairs, reflections)
    quit1()
    chat.converse()
