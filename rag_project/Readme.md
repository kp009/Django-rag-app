# Django RAG (Retrieval-Augmented Generation) Application

## Overview

This Django application implements a Retrieval-Augmented Generation (RAG) system using:
- OpenAI's language models
- Chroma vector database
- LangChain framework

Users can submit text content and ask questions, with the system providing answers by retrieving relevant information from the submitted content.

## Features

- Text content upload form
- Question input field
- AI-powered question answering
- Vector embeddings storage with Chroma
- Text chunking for efficient retrieval

## Installation

### Prerequisites

- Python 3.8+
- Django 4.0+
- OpenAI API key

### Setup

1. Clone the repository:
   ```bash
   git clone [your-repository-url]
   cd your-project
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Linux/Mac
   venv\Scripts\activate  # Windows
   ```

3. Install dependencies:
   ```bash
   pip install django langchain openai chromadb python-dotenv
   ```

4. Set up environment variables:
   Create a `.env` file in your project root:
   ```
   OPENAI_API_KEY=your_api_key_here
   ```

## Project Structure

```
project/
├── your_app/  
│   ├── __init__.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   └── views.py
├── project/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── templates/
│   │___ index.html
├── .env
└── manage.py
```

## Configuration

1. Add your app to `INSTALLED_APPS` in `settings.py`:
   ```python
   INSTALLED_APPS = [
       # ...
       'your_app',
   ]
   ```

2. Configure templates in `settings.py`:
   ```python
   TEMPLATES = [
       {
           'BACKEND': 'django.template.backends.django.DjangoTemplates',
           'DIRS': [os.path.join(BASE_DIR, 'templates')],
           'APP_DIRS': True,
           # ...
       },
   ]
   ```

## Usage

1. Run the development server:
   ```bash
   python manage.py runserver
   ```

2. Access the application at `http://localhost:8000`

3. In the web interface:
   - Paste your text content in the text area
   - Enter your question
   - Click "Ask" to get the AI-generated answer

## Customization

### Adjusting Chunk Sizes

Modify the chunk parameters in `views.py`:
```python
splitter = CharacterTextSplitter(
    chunk_size=500,      # Size of each text chunk
    chunk_overlap=100    # Overlap between chunks
)
```

### Changing AI Model

Replace the OpenAI model in `views.py`:
```python
qa = RetrievalQA.from_chain_type(
    llm=OpenAI(temperature=0.7),  # Adjust temperature for creativity
    chain_type="stuff",
    retriever=retriever
)
```

## Troubleshooting

### Template Errors
- Ensure `APP_DIRS=True` in settings
- Verify template is in `your_app/templates/your_app/`
- Check app is in `INSTALLED_APPS`

### API Key Issues
- Confirm `.env` file exists with `OPENAI_API_KEY`
- Restart server after adding API key

### Vector Database Problems
- Check Chroma DB is installed (`pip install chromadb`)
- Verify text chunks are being created properly

## License

[MIT License](LICENSE)
