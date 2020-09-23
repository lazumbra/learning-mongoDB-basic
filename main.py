from pymongo import MongoClient

client = MongoClient()
db = client.get_database('data_sciency_project')
collection = db.get_collection('files_order_sender')

document_1 = {"_id": 0, "name": "tim", "score": 5}

# Adicionar um documento na minha base de dados.
# collection.insert_one(document_1)

document_2 = {"_id": 5, "name": "joe"}
document_3 = {"_id": 6, "name": "bill"}

# Adicionar dois documentos de uma única vez
# collection.insert_many([document_2, document_3])

# Encontrar um resultado na minha base de dados
# LEMBRAR: eu posso colocar quantas querys eu quiser.
results = collection.find({"name": "bill"})
# Dessa forma eu não vou conseguir ver exatamente o documento.
# Dessa forma o que eu vou conseguir é printar o objeto.
print(results)

# Aqui eu vou pegar o iterador e vou conseguir percorrer cada elemento da minha
# Base de dados.
for result in results:
    print(result)

# Caso eu queira achar apenas um elemento na minha base de dados
# Eu posso fazer o seguinte.
result = collection.find_one({"_id": 0})
# Como neste caso eu usei o find_one, então o meu resultado
# Vai ser o documento em si e não o objeto.
print(result)
