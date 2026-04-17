### Explicação Técnica e Didática do Código Otimizado em num_primo.py

O código foi refatorado aplicando princípios de clean code: nomes descritivos em inglês, type hints, validação de entrada, constantes para evitar magic numbers/strings, separação de responsabilidades e docstrings aprimoradas. Agora, o programa solicita ao usuário um número e verifica se é primo. Abaixo, explico linha a linha, destacando melhorias e conceitos.

1. **`import typing`**  
   Importa o módulo `typing` para usar type hints, melhorando a legibilidade e permitindo verificação estática de tipos (ex.: com mypy).

2. **`def is_prime(number: int) -> bool:`**  
   Define a função `is_prime` com type hints: `number` deve ser `int`, e retorna `bool`. Nome em inglês segue convenções globais; "is_" prefixo indica função booleana.

3-11. **Docstring aprimorada:**  
   ```
   """
   Verifica se um número é primo.
   
   Args:
       number (int): Um número inteiro a ser verificado.
       
   Returns:
       bool: True se o número é primo, False caso contrário.
       
   Raises:
       TypeError: Se o input não for um inteiro.
   """
   ```  
   Inclui type hints na docstring (seguindo Google style), descrição de exceções e formatação consistente. Facilita documentação automática e IDEs.

12. **`if not isinstance(number, int):`**  
   **`raise TypeError("O input deve ser um inteiro.")`**  
   Valida o tipo do input em runtime. Isso previne erros sutis (ex.: float) e segue defensive programming, lançando uma exceção clara.

13. **`if number < 2:`**  
   **`return False`**  
   Mantém a verificação de casos edge, agora com input validado.

14. **`if number == 2:`**  
   **`return True`**  
   Caso especial otimizado.

15. **`if number % 2 == 0:`**  
   **`return False`**  
   Eliminação de pares.

16. **`for i in range(3, int(number ** 0.5) + 1, 2):`**  
   Loop eficiente, sem mudanças.

17. **`if number % i == 0:`**  
   **`return False`**  
   Verificação de divisibilidade.

18. **`return True`**  
   Retorno positivo.

19-24. **Constantes:**  
   Define constantes para strings, evitando duplicação e facilitando manutenção (ex.: alterar mensagem sem procurar no código). Inclui mensagens para o usuário e validação de input.

25. **`def main():`**  
   **`"""Função principal que solicita um número ao usuário e verifica se é primo."""`**  
   Separa a lógica principal em uma função dedicada, seguindo SRP (Single Responsibility Principle). Docstring concisa.

26-40. **Corpo de main():**  
   Imprime cabeçalho. Entra em loop para solicitar input até que seja válido (inteiro). Usa try-except para capturar ValueError. Chama is_prime e imprime o resultado com status.

41. **`if __name__ == "__main__":`**  
   **`main()`**  
   Chama a função principal, mantendo o padrão Python para scripts executáveis.

**Observações Gerais:**  
- **Clean Code Aplicado:** Nomes expressivos, funções pequenas, constantes, validação, type hints e separação de concerns. Código mais legível, testável e manutenível.  
- **Interatividade:** Agora solicita input do usuário com validação robusta.  
- **Eficiência:** Mantida em O(√n).  
- **Robustez:** Lança exceções para inputs inválidos na função e valida input do usuário.  
- **Boas Práticas:** Segue PEP 8, Google docstring style e princípios SOLID.  
- **Limitações:** Ainda não trata números muito grandes (overflow), mas adequado para uso geral.

Se precisar de mais otimizações ou testes, informe!
