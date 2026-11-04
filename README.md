# material de estudos em python

python foi o meu começo na programação. aqui está tudo o que aprendi em sala de aula: os conceitos, com as minhas anotações nos comentários, e os exercícios que fiz para treinar.

## como está organizado

as pastas estão numeradas na ordem em que eu aprendi cada assunto. dentro de cada uma ficam os arquivos com a explicação do conceito e uma pasta `exercícios/` com a prática daquele assunto.

| pasta | o que aprendi |
| --- | --- |
| [01 · variáveis e tipos](01-variáveis-e-tipos) | `print`, variáveis, tipos de dados (string, int, float, bool), `input`, operações e f-string |
| [02 · condicionais](02-condicionais) | `if`, `elif` e `else` com operadores relacionais (`>=`, `==`) e lógicos (`and`, `or`) |
| [03 · laços de repetição](03-laços-de-repetição) | `for`, `range`, `while`, `break` e validação do que o usuário digita |
| [04 · listas e matrizes](04-listas-e-matrizes) | `append`, `insert`, `pop`, `remove`, `sort`, `min`, `max`, `sum`, `len` e matrizes |
| [05 · dicionários e arquivos](05-dicionários-e-arquivos) | dicionários (chave e valor) e um cadastro de alunos que lê um arquivo `.txt` |
| [06 · funções e bibliotecas](06-funções-e-bibliotecas) | `def`, `return` e `import` de bibliotecas (`math`, `random`, `time`) |
| [07 · classes e objetos](07-classes-e-objetos) | orientação a objetos: classes, `__init__`, atributos e métodos |
| [08 · chatbots com ia](08-chatbots-com-ia) | do chatbot feito só com `if`/`else` até a inteligência artificial com LangChain |

## chatbots com ia, passo a passo

| etapa | o que aprendi |
| --- | --- |
| [01 · chatbot tradicional](08-chatbots-com-ia/01-chatbot-tradicional) | chatbot com respostas fixas em `if`/`else` e histórico guardado em lista |
| [02 · primeiro chat com ia](08-chatbots-com-ia/02-primeiro-chat-com-ia-groq) | primeira conversa com um modelo de ia (llama 3 pela groq) |
| [03 · ia local com ollama](08-chatbots-com-ia/03-ia-local-com-ollama) | rodando a ia no meu próprio computador, sem internet |
| [04 · rag com pdf](08-chatbots-com-ia/04-rag-com-pdf) | a ia respondendo com base no conteúdo de um pdf (embeddings + faiss) |
| [05 · prompt e intenção](08-chatbots-com-ia/05-prompt-e-intenção) | engenharia de prompt, classificar a intenção da mensagem e responder conforme o assunto |
| [06 · interface com streamlit](08-chatbots-com-ia/06-interface-com-streamlit) | uma página web para conversar com o chatbot, com histórico e configurações |

## como rodar

os arquivos das pastas 01 a 07 só precisam do python instalado:

```bash
python "02-condicionais/cond_lógica.py"
```

os chatbots da pasta 08 usam bibliotecas extras:

```bash
pip install langchain langchain-groq langchain-community streamlit
```

- nos arquivos que usam a groq, troque o texto `"GROQ_API_KEY"` pela sua chave, que dá para criar de graça em [console.groq.com](https://console.groq.com)
- a etapa 03 precisa do [ollama](https://ollama.com) aberto e do modelo `llama3.1:8b` baixado
- a etapa 04 precisa também de `langchain-classic`, `pypdf`, `faiss-cpu` e `sentence-transformers`, e de um arquivo `documento.pdf` na mesma pasta
- a etapa 06 roda com `streamlit run chat_interface.py`, de dentro da pasta dela

## o que aprendi

- a lógica de programação desde o começo
- a tomar decisões no código com `if` e `else`
- a repetir tarefas com `for` e `while`
- a guardar dados em listas, matrizes e dicionários
- a organizar o código em funções e classes
- a criar chatbots com inteligência artificial
- a resolver problemas passo a passo e treinar com exercícios
