
from haystack_integrations.document_stores.pinecone import PineconeDocumentStore
import os
from dotenv import load_dotenv
from pinecone import  Pinecone, PodSpec

load_dotenv()
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
os.environ['PINECONE_API_KEY'] = PINECONE_API_KEY

HF_TOKEN = os.getenv("HF_TOKEN")
os.environ['HF_API_TOKEN'] = HF_TOKEN
    
print("Import Successfully")

def pinecone_config():
  """Configures Pinecone database connection."""
  pc = Pinecone(api_key=PINECONE_API_KEY)

  pc.create_index(
      name="serverless-index",
      dimension=1536,
      metric="cosine",
       spec=PodSpec(
    environment="us-west1-gcp",
    pod_type="p1.x1",
    pods=1
  )
      
  )

  return pc