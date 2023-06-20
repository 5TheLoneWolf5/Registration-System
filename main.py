from datetime import date

# A variável "hoje" contém a data de hoje.
# Para o dia do mês, use:  hoje.day
# Para o mês, use:         hoje.month
# Para o ano, use:         hoje.year
hoje = date.today()

# Mantenha as linhas acima no início do arquivo

def register(dataset):

  print("--- Preencha os dados referentes ao cadastro ---")

  check = True

  while check:

    # Input do usuário.
    fillId = input("ID (número - opcional): ")
    fillFirstName = input("Primeiro Nome: ")
    fillLastName = input("Sobrenome: ")
    fillCpf = input("CPF: ")
    fillBirthdate = input("Data de Nascimento (DD/MM/AAAA): ")
    
    # Validação dos Dados (pt. 1).
    if fillFirstName.strip() == "" or fillCpf.strip() == "" or fillBirthdate.strip() == "":

      print("Erro: dados vazios.")

    else:

      # Validação dos Dados (pt. 2).
      
      if not check_id(fillId, register=True):
        continue
        
      fillFirstName, fillLastName, check = check_name(fillFirstName, fillLastName, check)
      
      fillCpf = check_cpf(fillCpf)
      
      if not fillCpf:
        continue
        
      if not check_date(fillBirthdate):
        continue

      # It needs to be below, otherwise it will append the data without verifying the others.

      sanitizedId = fillId.strip()

      if len(id) == 0 and sanitizedId == "":

        id.append(1)

      elif sanitizedId == "":

        id.append(id[-1] + 1)

      else:

        id.append(int(sanitizedId))

      if check:
        fullName.append(fillFirstName)
      else:
        fullName.append(fillFirstName + " " + fillLastName)
        cpf.append(fillCpf)
        birthDate.append(fillBirthdate)

    # id = sorted(id) # Also: .sort().

    # New occupations. Ordering.
    for i in range(
        len(id)
    ):  # It needs to be the length, since the actual array changes its position.
      for j in range(i + 1, len(id)):
        if id[i] >= id[
            j]:  # Ordering if id[i] is bigger or equal to id[j]. Ordering first, so the update adjust the old value thereafter.

          id[i], id[j] = id[j], id[i]
          fullName[i], fullName[j] = fullName[j], fullName[i]
          cpf[i], cpf[j] = cpf[j], cpf[i]
          birthDate[i], birthDate[j] = birthDate[j], birthDate[i]

        if id[i] == id[j]:  # Updating.
          id[j] += 1

      check = False

def show_db(dataset):

  # Output.
  print(f"--- Banco de Dados: ---\n\
  IDs: {dataset[0]}\n\
  Nomes completos: {dataset[1]}\n\
  CPFs: {dataset[2]}\n\
  Datas de Nascimento: {dataset[3]}")

def remove_register(dataset):

  # Reminder: Modifying a list while looping affects the loop.

  try:

    idRemove = int(input("Digite o ID que deseja remover: "))
    index = id.index(idRemove)
    
  except:
    
    print("Esse ID não existe.")
  # Using "else", the variable scope becomes the same.
  else:
    for i in id[:]:
      for i in id:
        if i == idRemove:
          id.remove(i)
  
    fullName.remove(fullName[index])
    cpf.remove(cpf[index])
    birthDate.remove(birthDate[index])
    
    for idx, i in enumerate(range(len(id))):

      if len(id) <= 1:
        id[idx] = 1
        break
      
      id[i] = idx + 1
  
    id.sort()

def change_cpf(dataset):

  # Mudando o CPF através do índex da array.
  idCpf = int(input("Digite o ID do cadastro a ser alterado: ")) 
  
  cpfChange = input("Digite o novo CPF: ")

  if not check_cpf(cpfChange):
    return

  if input("Confirme digitando \"sim\": ").lower() == "sim":

    try:
      cpf[id.index(idCpf)] = cpfChange
    except:
      print("Esse ID não existe.")

def switch_last_name(dataset):

  # Trocando os sobrenomes com os dois IDs informados.
  firstId = int(input("Informe o primeiro ID: "))
  secondId = int(input("Informe o segundo ID: "))

  if input("Confirme digitando \"sim\": ").lower() == "sim":

    try:
      firstPerson = fullName[id.index(firstId)]
      secondPerson = fullName[id.index(secondId)]
    except:
      print("ID(s) não existe(m).")
    else:
      firstLastName = firstPerson.split()
      secondLastName = secondPerson.split()
    
      firstLastName[1], secondLastName[1] = secondLastName[1], firstLastName[1]
    
      firstPerson = " ".join(firstLastName) 
      secondPerson = " ".join(secondLastName)
    
      fullName[id.index(firstId)] = firstPerson
      fullName[id.index(secondId)] = secondPerson

def age_in_days(dataset):

  ageId = int(input("Digite o ID que deseja obter: ")) # Input

  try:
    age = birthDate[id.index(ageId)]
  except:
    print("Esse ID não existe.")
  else:
    # In case user uses another type of formatting.
    age = age.replace("-", "/")
    age = age.strip().split("/")
    
    day = int(age[0])
    month = int(age[1])
    year = int(age[2])
  
    ageOfBirth = date(year, month, day)
  
    calc = ((hoje - ageOfBirth).days)
  
    print(f"{calc} dias decorridos.") # Output

def check_id(id, register=False):

  if not id.strip() and register:
    return True
  
  try:
    id = int(id)
  except ValueError:
    print("O ID deve ser um número inteiro.")
    return False
  else:

    checkSameId = False 
    
    for i in dataset[0]:
      if id == i:
        checkSameId = True
    
    if id != dataset[0][-1] + 1 and not checkSameId:
      print("O ID deve corresponder à posição de cada cadastro na estrutura, que é de forma sucessiva. Se estiver criando um campo ID, ele deve ser deixado em branco, ou ser um ID já em uso, ou ser o próximo ID que não estiver em uso (lembrando que a sequência de IDs começa em 1).")
      return False
      
    return True

def check_name(name, surname, check):

  check = False
  name = name.lower().capitalize()

  if not surname.strip():
    print("Nome é composto por uma única palavra.")
    check = True
  
  surname = surname.lower().capitalize()

  return name, surname, check

def check_cpf(unsanitizedCpf):

  cpf = unsanitizedCpf.replace(".", "")
  cpf = cpf.replace("-", "")

  length_cpf = len(cpf)
  
  if cpf.isnumeric() and length_cpf == 11: # Not converting directly the variable, so it doesn't give out an error. It checks if characters in a string are numeric, and every CPF comes as a string.

    regiaoFiscal  = int(cpf[8])
    
    if regiaoFiscal == 6 or regiaoFiscal == 7 or regiaoFiscal == 8:
      
      print("O sistema não aceita CPFs emitidos na Região Sudeste (ES, MG, RJ e SP).")
      return False
  
    validFirstNum = False
    validSecondNum = False
  
    result = 0
    counter = 0
    
    # First Num.
  
    for i in range(length_cpf - 1, 1, -1):
      result += int(cpf[counter]) * i
      counter = counter + 1
  
    calc = result * 10 % 11 # Or subtracting by 11 instead of multiplying by 10 (apparently).
  
    if calc == 10:
        calc = 0
    elif calc == 11:
        calc = 0
  
    if calc == int(cpf[-2]):
      validFirstNum = True
  
    ###################################
  
    # Second Num.
    
    # Cleansing.
    result = 0
    counter = 0
    
    for j in range(length_cpf, 1, -1):
  
      result += int(cpf[counter]) * j
      counter = counter + 1
  
    calc = 11 - (result % 11)
    
    if calc == 10:
        calc = 0
    elif calc == 11:
        calc = 0
        
    if calc == int(cpf[-1]):
      validSecondNum = True
    
    if validFirstNum and validSecondNum:
  
      insertChars = [str(x) for x in str(cpf)]
      
      insertChars.insert(3, ".")
      insertChars.insert(7, ".")
      insertChars[10] += "-"
      
      cpf = "".join(insertChars)
      
      return cpf
      
    else:
  
      print("CPF inválido.")
      return False
  else:
    print("CPF inválido.")
    return False

def check_date(birthdate):

  birthdate = birthdate.replace("-", "/")
  birthdate = birthdate.strip().split("/")
  
  try:
    
    day = int(birthdate[0])
    month = int(birthdate[1])
    year = int(birthdate[2])
  
    birthdate = date(year, month, day) # If using the same name, it will show Typeerror: ‘list’ object is not callable.
  
  except:
    print("Erro: a data de nascimento deve estar no formato dd/mm/aaaa, e deve ser uma data válida.")
    return False
    
  else:

    calc = (hoje - birthdate).days
    
    # Not allowed (as understood): date.strptime(birthdate, '%d-%m-%Y').
    if calc < 0:
      print("Esta é uma data de nascimento futura. Não estamos aceitando cadastros de viajantes do tempo no momento.")
      return False
      
    return True

# Armazenamento dos cadastros
id = [
  1, 2, 3
]  # Number of IDs must be the same amount to the number of users (and its required fields).
fullName = ["Adam Stones", "David Parker", "John Smith"]
cpf = ["714.748.550-59", "071.494.980-94", "307.266.840-07"]
birthDate = ["30/03/2000", "23/07/2004", "03/05/1980"]

dataset = (id, fullName, cpf, birthDate)

def main(dataset):

  answer = None

  while answer != "7":

    print("--- Tela Inicial do Cadastro ---\n\
  Digite a tecla:\n\n\
  1: Para inserir um cadastro;\n\
  2: Para mostrar os registros;\n\
  3: Para remover um registro;\n\
  4: Para alterar o CPF;\n\
  5: Para trocar sobrenomes;\n\
  6: Para obter a idade em dias;\n\
  7: Para sair.")

    answer = input()

    if answer == "1":

      register(dataset)

    elif answer == "2":

      check = True
      
      for i in dataset:
        if len(i) < 1:
          print("Não há registros no banco de dados.")
          check = False
          break

      if check: 
        show_db(dataset)

    elif answer == "3":

      remove_register(dataset)

    elif answer == "4":
      
      change_cpf(dataset)

    elif answer == "5":

      switch_last_name(dataset)

    elif answer == "6":
      
      age_in_days(dataset)

    elif not answer.strip() or not (int(answer) >= 1 and int(answer) <= 7):

      print(f"Desculpe! A funcionalidade \"{answer}\" ainda não foi implementada.")

  print("Sistema finalizado com sucesso.")

main(dataset)