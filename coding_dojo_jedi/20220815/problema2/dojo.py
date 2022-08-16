def index(palavra: str, pos: int) -> str:
    return palavra[pos % len(palavra)]



if __name__ == '__main__':
    print(index(input('Qual a palavra: '), int(input('Qual a posição: '))))
