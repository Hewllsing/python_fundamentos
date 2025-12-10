# Importa todo o módulo chamado "converter"
import converter  # converte tudo no arquivo

# Mostra o objeto da função euro_dollar (não executa, apenas imprime a referência da função)
print(converter.euro_dollar)  # euro para o dolar

# Mostra o objeto da função dollar_euro (mesma coisa, apenas referência)
print(converter.dollar_euro)  # dolar para o euro

# Importa somente as funções euro_dollar e dollar_euro diretamente do módulo
from converter import euro_dollar, dollar_euro  # importa somente as funcoes selecionadas no arquivo
