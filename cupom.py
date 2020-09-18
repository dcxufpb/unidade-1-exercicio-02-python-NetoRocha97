nome_loja = "Arcos Dourados Com. de Alimentos LTDA"
logradouro = "Av. Projetada Leste"
numero = 500
complemento = "EUC F32/33/34"
bairro = "Br. Sta Genebra"
municipio = "Campinas"
estado = "SP"
cep = "13080-395"
telefone = "(19) 3756-7408"
observacao = "Loja 1317 (PDP)"
cnpj = "42.591.651/0797-34"
inscricao_estadual = "244.898.500.113"

def imprime_dados_loja():
  dados_loja = f"{nome_loja}\n"
  dados_loja += f"{logradouro}, {numero} {complemento}\n"
  dados_loja += f"{bairro} - {municipio} - {estado}\n"
  dados_loja += f"CEP:{cep} Tel {telefone}\n"
  dados_loja += f"{observacao}\n"
  dados_loja += f"CNPJ: {cnpj}\n"
  dados_loja += f"IE: {inscricao_estadual}\n"
  return dados_loja