import os
from dotenv import load_dotenv

from langchain_openai import AzureChatOpenAI

load_dotenv(dotenv_path=".env")

# load_dotenv(dotenv_path="Deloitte.Ca.DBotBeta.DjangoAPI\\DVoice\\.env") 

def instantiate_azure_chat_openai():
    """
    """
    
    model = AzureChatOpenAI(
            openai_api_version = os.environ["AZURE_OPENAI_API_VERSION"],
            temperature        = os.environ["TEMPERATURE"],
            deployment_name    = os.environ["AZURE_OPENAI_MODEL_NAME"],
            azure_endpoint     = os.environ["AZURE_OPENAI_ENDPOINT"],
            # azure_ad_token     = TOKEN.token, 
            api_key      =  os.environ["AZURE_OPENAI_API_KEY"], ## will be removed by azure_ad_token when we go to dev
            max_tokens         = os.environ["MAX_TOKEN_COMPLETION"],
            model              = os.environ["AZURE_OPEN_AI_MODEL"]
        )
    
    return model