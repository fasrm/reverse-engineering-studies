import subprocess

def analyze_binary(binary_path):
    # Executa o comando objdump para desassemblar o binário
    try:
        result = subprocess.run(
            ['objdump', '-M', 'intel', '-D', binary_path], 
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        
        if result.returncode != 0:
            print(f"Erro ao executar objdump: {result.stderr}")
            return
        
        # Filtro da função 'main' para obter suas instruções
        # Aqui estamos filtrando com base na função 'main'
        objdump_output = result.stdout
        main_analysis = []
        in_main = False

        # Faz a varredura da saída procurando a função main
        for line in objdump_output.splitlines():
            if "<main>" in line:
                in_main = True
            if in_main:
                main_analysis.append(line)
                if line.strip().endswith("ret"):  # Quando o 'ret' é encontrado, termina a função
                    break

        # Imprime o resultado da análise
        if main_analysis:
            print("Instruções da função 'main':")
            for line in main_analysis:
                print(line)
        else:
            print("Função 'main' não encontrada no binário.")
    
    except FileNotFoundError:
        print("Comando 'objdump' não encontrado. Verifique se está instalado no seu sistema.")
    except Exception as e:
        print(f"Ocorreu um erro: {e}")

# Exemplo de uso
binary_path = 'a.out'  # Caminho para o binário que deseja analisar
analyze_binary(binary_path)
