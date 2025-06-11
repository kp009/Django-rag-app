from django.shortcuts import render
from .forms import UploadForm
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import Chroma
from langchain.text_splitter import CharacterTextSplitter
from langchain.llms import OpenAI
from langchain.chains import RetrievalQA
from langchain.docstore.document import Document
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

def rag_view(request):
    result = ""
    if request.method == 'POST':
        form = UploadForm(request.POST)
        if form.is_valid():
            content = form.cleaned_data['content']
            query = form.cleaned_data['query']

            try:
                # Create document
                doc = Document(page_content=content)
                
                # Split text
                splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=100)
                docs = splitter.split_documents([doc])
                
                # Create vector store and retriever
                embeddings = OpenAIEmbeddings()
                db = Chroma.from_documents(docs, embeddings)
                retriever = db.as_retriever()
                
                # Run query
                qa = RetrievalQA.from_chain_type(
                    llm=OpenAI(temperature=0), 
                    chain_type="stuff", 
                    retriever=retriever
                )
                result = qa.run(query)
                
                # Clean up (optional)
                db.delete_collection()
                
            except Exception as e:
                result = f"An error occurred: {str(e)}"
    else:
        form = UploadForm()

    return render(request, 'index.html', {'form': form, 'result': result})