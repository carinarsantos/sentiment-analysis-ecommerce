# Importações no topo do seu arquivo
import requests
from bs4 import BeautifulSoup
import pandas as pd

# --- NOVA FUNÇÃO AUXILIAR ---
def get_element_text(parent_element, tag, class_name):
    """
    Busca um elemento dentro de um 'parent' e retorna seu texto.
    Se o elemento não for encontrado, retorna None para evitar erros.
    """
    element = parent_element.find(tag, class_=class_name)
    if element:
        return element.text.strip()
    return None

def scrape_ml_reviews(url):
    """
    Função para extrair reviews de uma URL de produto do Mercado Livre.
    VERSÃO ROBUSTA que lida com campos ausentes.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        if response.status_code != 200:
            print(f"Erro ao acessar a página. Status: {response.status_code}")
            return None
    except requests.exceptions.RequestException as e:
        print(f"Ocorreu um erro na requisição: {e}")
        return None

    soup = BeautifulSoup(response.content, 'html.parser')
    
    review_containers = soup.find_all('article', class_='ui-review-capability-comments__comment')
    reviews_data = []

    print(f"Encontrados {len(review_containers)} reviews na página.")

    if not review_containers:
        print("Nenhum container de review foi encontrado.")
        return None

    # --- LOOP REATORADO PARA SER ROBUSTO ---
    for review in review_containers:
        # Usamos nossa nova função para cada campo.
        # Se um campo não for encontrado, a variável receberá 'None'.
        title = get_element_text(review, 'h3', 'ui-review-capability-comments__content__title')
        text = get_element_text(review, 'p', 'ui-review-capability-comments__comment__content')
        date = get_element_text(review, 'span', 'ui-review-capability-comments__comment__date')
        
        # Só adicionamos o review se pelo menos o texto principal existir.
        if text:
            reviews_data.append({
                'title': title,
                'text': text,
                'date': date
            })
        else:
            print("Review ignorado por não conter o texto principal.")
            
    return reviews_data


# --- Execução do Script ---
if __name__ == '__main__':
    # **SUA TAREFA:** Substitua pela URL do produto do Mercado Livre
    # Dica: Pegue a URL da página que lista TODAS as opiniões do produto.
    # Geralmente termina com "#reviews" ou algo similar.
    PRODUCT_URL = "https://produto.mercadolivre.com.br/noindex/catalog/reviews/MLB3997031239?noIndex=true&access=view_all&modal=true&show_fae=true"

    print("Iniciando o scraping do Mercado Livre...")
    reviews = scrape_ml_reviews(PRODUCT_URL)

    if reviews:
        df = pd.DataFrame(reviews)
        
        # Vamos salvar com um nome específico
        output_path = '../data/ml_reviews_raw.csv'
        df.to_csv(output_path, index=False, encoding='utf-8-sig')
        
        print(f"\nScraping finalizado com sucesso!")
        print(f"{len(df)} reviews foram salvos em '{output_path}'")
        print("\nAmostra dos dados:")
        print(df.head())