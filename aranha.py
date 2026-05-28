import importlib #essa blibioteca acrssa arquivos

while True:
    n = input("\nQual questão testar? (0 para sair): ")
    if n == '0': #serve para fazer uma verificação ou condição e para encerrar o progama
        break
    
    try:#serve para tentar executar um código que pode dar algum erro
       
        modulo = importlib.import_module(f"questao_{n}") # serve para importar um módulo automaticamente usando o valor da variável
        getattr(modulo, f"q_{n}")() #serve para pegar e executar uma função pelo nome dela
    except Exception:
        print("[!] Questão não encontrada ou erro na execução.")
        
        #O erro foi que não estava com o mesmo nome que estava na minha pasta