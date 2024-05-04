
from haystack import Pipeline
from haystack.components.writers import DocumentWriter
from haystack.components.preprocessors import DocumentSplitter
from haystack.components.embedders import SentenceTransformersDocumentEmbedder
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
from haystack.components.converters import PyPDFToDocument
from pathlib import Path # type: ignore
import os
from dotenv import load_dotenv
from QASystem.utility import pinecone_config

def ingest(document_store):

	#creating a pipeline object
	indexing = Pipeline()

	#adding the components in pipeline
	indexing.add_component("converter", PyPDFToDocument())
	indexing.add_component("splitter", DocumentSplitter(split_by="sentence", split_length=2))
	indexing.add_component("embedder", SentenceTransformersDocumentEmbedder())
	indexing.add_component("writer", DocumentWriter(document_store))

	#coneecting all the components of pipeline
	indexing.connect("converter", "splitter")
	indexing.connect("splitter", "embedder")
	indexing.connect("embedder", "writer")

	#stroing the data as a embedding in the database
	indexing.run({"converter": {"sources": [Path("C:\\Users\\Tharindu\\OneDrive\\Desktop\\Intellihack\\Chatbot\\data\\Retrieval-Augmented-Generation-for-NLP.pdf")]}})
 
 
if __name__ == "__main__":
    document_store=pinecone_config()
    ingest(document_store)