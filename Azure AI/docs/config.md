# Configuração do Ambiente Azure

## Passo 1: Criar recursos no Azure

1. **Criar uma conta no Azure**:
   - Acesse [Azure Portal](https://portal.azure.com) e crie uma conta (se ainda não tiver uma).
2. **Configurar o Speech Studio**:
   - Vá até **Azure Cognitive Services** e crie um **Speech Resource**.
   - Copie a chave da API e o endpoint para uso posterior.
3. **Configurar o Language Studio**:
   - Crie um **Language Resource** no Azure Cognitive Services.
   - Copie a chave da API e o endpoint para usar em seu código.

## Passo 2: Instalando dependências

```bash
pip install azure-cognitiveservices-speech
pip install azure-ai-textanalytics
