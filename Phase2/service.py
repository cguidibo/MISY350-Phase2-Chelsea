#AI assistant

class ShopAssistantBot:
    def __init__(self, api_key, inventory_context):
        self.client = OpenAI(api_key=api_key)
        self.inventory_context = inventory_context