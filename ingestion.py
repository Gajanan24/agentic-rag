from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

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
retriver = Chroma(
    collection_name="rag-chroma-collection",
    embedding_function=OpenAIEmbeddings(),
    persist_directory="./.chroma_db"
).as_retriever()


