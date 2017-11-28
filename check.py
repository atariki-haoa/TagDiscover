try:
    import requests
    from bs4 import BeautifulSoup
    from bs4 import Comment
except ImportError:
    sys.exit("""Falta instalar algunos paquetes.
                Instalar mediante pip install -r requirements.txt""")