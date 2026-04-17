import typing

def is_prime(number: int) -> bool:
    """
    Verifica se um número é primo.
    
    Args:
        number (int): Um número inteiro a ser verificado.
        
    Returns:
        bool: True se o número é primo, False caso contrário.
        
    Raises:
        TypeError: Se o input não for um inteiro.
    """
    if not isinstance(number, int):
        raise TypeError("O input deve ser um inteiro.")
    
    if number < 2:
        return False
    
    if number == 2:
        return True
    
    if number % 2 == 0:
        return False
    
    for i in range(3, int(number ** 0.5) + 1, 2):
        if number % i == 0:
            return False
    
    return True

# Constantes para melhorar legibilidade e manutenção
HEADER = "=" * 50
TITLE = "VERIFICADOR DE NÚMEROS PRIMOS"
PRIME_MSG = "✓ É PRIMO"
NOT_PRIME_MSG = "✗ NÃO é primo"
PROMPT_MSG = "Digite um número inteiro para verificar se é primo: "
INVALID_INPUT_MSG = "Entrada inválida. Por favor, digite um número inteiro."

def main():
    """Função principal que solicita um número ao usuário e verifica se é primo."""
    print(HEADER)
    print(TITLE)
    print(HEADER)
    
    while True:
        try:
            user_input = input(PROMPT_MSG)
            number = int(user_input)
            break
        except ValueError:
            print(INVALID_INPUT_MSG)
    
    result = is_prime(number)
    status = PRIME_MSG if result else NOT_PRIME_MSG
    print(f"\n{number} -> {status}")

if __name__ == "__main__":
    main()
