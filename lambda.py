import os
from dotenv import load_dotenv
from log_register.dynamo_services import DynamoDBClass

# Carregar variáveis de ambiente do arquivo .env
load_dotenv()

# Nome da tabela DynamoDB e bucket S3 onde os logs serão registrados
DYNAMODB_TABLE = os.getenv('DYNAMODB_TABLE')

# --------------------------------------------------------------------
# Função Lambda que processa o evento e registra o log
# --------------------------------------------------------------------
def lambda_handler(event, context):
    """
    Função Lambda que processa o evento e registra um log no DynamoDB.
    :param event: Dados do evento recebido (contendo os parâmetros do log).
    :param context: Contexto de execução da Lambda.
    :return: Resposta com o status do processamento (sucesso ou erro).
    """
    try:
        # Extrai os dados do evento
        answer_id = event['answer_id']  # ID da conversa
        bool_liked = event['like']    # Valor booleano representando "like"
        bool_copy = event['copy']  # Valor booleano representando "copy"
        
        # Cria instância do DynamoDBClass
        dynamodb = DynamoDBClass(DYNAMODB_TABLE)
        
        # Registra o log no DynamoDB com os parâmetros extraídos
        dynamodb.update_item_dynamodb(answer_id, bool_liked, bool_copy)
        
        # Retorna sucesso com código 200
        return {'statusCode': 200, 'body': 'Log atualizado com sucesso!'}
    
    except Exception as e:
        # Loga e retorna erro genérico, incluindo detalhes do erro
        print(f"Erro ao processar o evento: {str(e)}")
        return {'statusCode': 500, 'body': f'Erro ao processar o evento: {str(e)}'}