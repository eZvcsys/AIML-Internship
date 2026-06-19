import bs4
import requests
from langchain_core.documents import Document
import streamlit as st

from langchain_text_splitters import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,  # chunk size (characters)
    chunk_overlap=200,  # chunk overlap (characters)
    add_start_index=True,  # track index in original document
)


# Below is a minimal helper for demonstration purposes.


def load_web_page(url: str, bs_kwargs: dict | None = None) -> list[Document]:
    response = requests.get(url)
    response.raise_for_status()
    soup = bs4.BeautifulSoup(response.text, "html.parser", **(bs_kwargs or {}))
    return [Document(page_content=soup.get_text(), metadata={"source": url})]


# Only keep post title, headers, and content from the full HTML.
bs4_strainer = bs4.SoupStrainer(
    class_=("post-title", "post-header", "post-content"))
docs = load_web_page(
    "https://lilianweng.github.io/posts/2023-06-23-agent/",
    bs_kwargs={"parse_only": bs4_strainer},
)

assert len(docs) == 1
print(f"Total characters: {len(docs[0].page_content)}")

all_splits = text_splitter.split_documents(docs)

print(f"Split blog post into {len(all_splits)} sub-documents.")

st.write(f"STEP1::::LOAD DATA > {docs[0:100]}")

st.write(f"STEP2::::SPLIT OUTPUT > {len(all_splits)}")
