import boto3
import uuid
from botocore.exceptions import ClientError

class DynamoDBClass:

    def __init__(self, dynamodb_table_name):

        # Define o nome da tabela DynamoDB
        self.dynamodb_table_name = dynamodb_table_name

        # Inicia a sessão do DynamoDB
        self.dynamodb = boto3.resource('dynamodb', region_name='us-west-2')

    # Serviço de DynamoDB para registro de log
    def log_register_dynamodb(self, is_liked, embedding_vector):
        """
        Registra um log no DynamoDB com as informações de requisição e resposta.
        :param user_id: ID do usuário que fez a consulta.
        :param chat_id: ID da conversa em que a consulta foi feita.
        :param is_liked: Flag booleana indicando se a consulta foi "curtida" ou foi positiva.
        :param embedding_vector: Vetor de embeddings (ou vetor de similaridade) associado à consulta.
        :return: None
        """
        # Inicia o serviço DynamoDB e acessa a tabela especificada
        table = self.dynamodb.Table(self.dynamodb_table_name)

        # Gerar um ID único para o log usando o timestamp atual
        unique_id = str(uuid.uuid4())

        # Configura os dados do log
        log_item = {
            'unique_id': unique_id,  # ID único gerado para o log
            'was_liked': is_liked,    # Flag indicando se a consulta foi "curtida"
            'was_copied': embedding_vector,  # Vetor de embeddings associado à consulta
        }

        try:
            # Insere os dados do log na tabela do DynamoDB
            table.put_item(Item=log_item)
            print("Dados do log inseridos no DynamoDB com sucesso")
        
        except ClientError as e:
            # Em caso de erro, imprime a mensagem de erro
            print(f"Erro ao inserir os dados do log no DynamoDB: {e}")
            raise
    
    def scan_table_dynamodb(self):
        """
        Realiza um scan na tabela DynamoDB e retorna todos os itens.
        :return: Lista de itens encontrados na tabela.
        """
        try:
            # Acessa a tabela DynamoDB
            table = self.dynamodb.Table(self.dynamodb_table_name)
            
            # Realiza o scan na tabela
            response = table.scan()
           
            # Obtém os itens retornados pelo scan
            items = response.get('Items', [])
            
            print(f"Scan bem-sucedido. Número de itens encontrados: {len(items)}")
            return items
        
        except ClientError as e:
            print(f"Erro ao realizar o scan na tabela DynamoDB: {e}")
            raise
    
    def update_item_dynamodb(self, unique_id, boolLike=None, boolCopy=None):
        """
        Atualiza o item no DynamoDB correspondente ao unique_id fornecido.
        Altera o valor da chave 'was_liked' ou incrementa o valor da chave 'was_copied'.
        Verifica se o unique_id existe antes de realizar a atualização.
        :param unique_id: ID único do item a ser atualizado.
        :param boolLike: Novo valor para a chave 'was_liked'.
        :param boolCopy: Se não for None, incrementa a chave 'was_copied'.
        :return: Mensagem de sucesso ou erro.
        """
        try:
            # Acessa a tabela DynamoDB
            table = self.dynamodb.Table(self.dynamodb_table_name)

            # Verifica se o unique_id existe na tabela
            response = table.get_item(Key={'unique_id': unique_id})
            
            if 'Item' not in response:
                # Caso o item não exista, lança uma exceção
                raise ValueError(f"O item com unique_id '{unique_id}' não existe na tabela.")

            # Atualiza o valor da chave 'was_liked'
            if boolLike is not None:
                response = table.update_item(
                    Key={'unique_id': unique_id},
                    UpdateExpression="SET was_liked = :liked_value",
                    ExpressionAttributeValues={
                        ':liked_value': boolLike
                    },
                    ReturnValues="UPDATED_NEW"
                )
                return print(f"Item atualizado com sucesso (was_liked): {response['Attributes']}")

            # Incrementa o valor da chave 'was_copied'
            if boolCopy is not None:
                response = table.update_item(
                    Key={'unique_id': unique_id},
                    UpdateExpression="SET was_copied = if_not_exists(was_copied, :default) + :increment",
                    ExpressionAttributeValues={
                        ':default': 0,
                        ':increment': 1
                    },
                    ReturnValues="UPDATED_NEW"
                )
                return print(f"Item atualizado com sucesso (was_copied): {response['Attributes']}")

            # Caso nenhum parâmetro tenha sido atualizado
            return print("Nenhuma operação foi realizada. Ambos os parâmetros são None.")

        except ValueError as errorValue:
            print(errorValue)
            raise

        except ClientError as e:
            print(f"Erro ao atualizar o item no DynamoDB: {e}")
            raise
