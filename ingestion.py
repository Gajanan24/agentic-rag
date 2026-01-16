from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
# from langchain_community.vectorstores import Chroma

from langchain_pinecone import PineconeVectorStore

from pinecone import Pinecone, ServerlessSpec
import os

load_dotenv()

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENV = os.getenv("PINECONE_ENVIRONMENT")
INDEX_NAME = os.getenv("PINECONE_INDEX_NAME")



urls = [
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    "https://lilianweng.github.io/posts/2023-03-15-prompt-engineering/",
    "https://lilianweng.github.io/posts/2023-10-25-adv-attack-llm/",
]

docs = [WebBaseLoader(url).load() for url in urls]

docs_list = [ item for sublist in docs for item in sublist ]
text_splitter = RecursiveCharacterTextSplitter(chunk_size=250, chunk_overlap=0)

docs_splits = text_splitter.split_documents(docs_list)

# vectorstore = Chroma.from_documents(
#     documents=docs_splits,
#     collection_name="rag-chroma-collection",
#     embedding=OpenAIEmbeddings(),
#     persist_directory="./.chroma_db"
# )
# retriver = Chroma(
#     collection_name="rag-chroma-collection",
#     embedding_function=OpenAIEmbeddings(),
#     persist_directory="./.chroma_db"
# ).as_retriever()


pc = Pinecone(api_key=PINECONE_API_KEY)

# # 5️⃣ Create index if it doesn't exist
# if INDEX_NAME not in pc.list_indexes().names():
#     pc.create_index(
#         name=INDEX_NAME,
#         dimension=1536,  # OpenAI embedding dimension
#         metric="cosine",
#         spec=ServerlessSpec(
#             cloud="gcp",
#             region=PINECONE_ENV
#         )
#     )

# 6️⃣ Create vector store + upsert
vectorstore = PineconeVectorStore.from_documents(
    documents=docs_splits,
    embedding=OpenAIEmbeddings(model="text-embedding-3-small"),
    index_name=INDEX_NAME
)

# 7️⃣ Create retriever
retriever = vectorstore.as_retriever()


