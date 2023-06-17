from langchain.indexes import VectorstoreIndexCreator
from langchain.document_loaders import CSVLoader

index = VectorstoreIndexCreator().from_loaders([CSVLoader("Dummy minutes.csv", encoding="utf-8")])

# result = index.query_with_sources("", chain_type="refine")



while True:
    query = input("Enter your query: ")
    result = index.query_with_sources(query, chain_type="refine")
    print(result["answer"])