# Realiza a importação da biblioteca referente à criptografi sha-256
from hashlib import sha256

#Abre o arquivo no modo somente leitura e o referencia para futuras operações como "f"
#Inserir local do arquivo o qual deseja-se encriptar seu conteúdo
with open('<Insira o caminho do arquivo o qual é desejado que seja aplicado o hash sha-256>', 'r') as f:
    
    #atribui o valor do conteúdo do aquivo à "original_data" e o printa
    original_data = f.read()
    print("This is the original data: "  +original_data)
    
    #Aplica o hash sha-256 no conteúdo do arquivo e printa o conteúdo pós ação do hash
    hashed_data = sha256(original_data.encode('utf-8')).hexdigest()
    print("This is the hashed data: "  +hashed_data)
