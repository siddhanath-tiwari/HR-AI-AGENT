import chromadb

client = chromadb.PersistentClient(path="./hr_data")
collection = client.get_or_create_collection("hr_policies")

def get_hr_policy(query: str):
    results = collection.query(query_texts=[query], n_results=1)
    return results["documents"][0] if results["documents"] else "Policy not found."