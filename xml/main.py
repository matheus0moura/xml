import xml.etree.ElementTree as ET

class Contato:
  def __init__(self, nome, telefone, email):
    self.nome = nome
    self.telefone = telefone
    self.email = email

def escrever_contato(arquivo, contato):
  root = ET.Element("contatos")
  contato_node = ET.SubElement(root, "contato")
  ET.SubElement(contato_node, "nome").text = contato.nome
  ET.SubElement(contato_node, "telefone").text = contato.telefone
  ET.SubElement(contato_node, "email").text = contato.email
  arquivo.write(ET.tostring(root, encoding="utf-8"))

def ler_contato(arquivo):
  root = ET.fromstring(arquivo.read())
  contatos = []
  for contato_node in root:
    contato = Contato(contato_node.find("nome").text,
                       contato_node.find("telefone").text,
                       contato_node.find("email").text)
    contatos.append(contato)
  return contatos

def main():
  arquivo = open("contatos.xml", "wb")

  # Loop para inserir contatos
  while True:
    nome = input("Nome: ")
    telefone = input("Telefone: ")
    email = input("E-mail: ")

    contato = Contato(nome, telefone, email)
    escrever_contato(arquivo, contato)

    # Perguntando se deseja inserir outro contato
    opcao = input("Deseja inserir outro contato? (1 - Sim | 2 - Não): ")
    if opcao == "2":
      break

  arquivo.close()

if __name__ == "__main__":
  main()