### LangChain Expression Language (LCEL)

- Easy way to compose chains together using the Runnable Interface.
  
Provides:

- Streaming
- Async
- Parallel Execution
- Retries and Fallbacks
- Input and Output Schemas
- Integration with langsmith

#### Runnable Interface

- `stream`
- `invoke`
- `batch`

Async:

- `astream`
- `ainvoke`
- `abatch`

[LCEL Reference](https://python.langchain.com/docs/expression_language/interface)

## Runnable Interface

1. **Runnable Parallel:** Used to define and run multiple values and operations in parallel.

2. **Runnable Passthrough:** Used to take the input and pass it through.

3. **Runnable Lambda:** Used to turn the Python functions into pipe-compatible functions.

```python
from dotenv import load_dotenv
load_dotenv()

# LLM Chain
from langchain.chat_models.openai import ChatOpenAI
model = ChatOpenAI(model='gpt-3.5-turbo', temperature=0.0)

# DeepInfra
from langchain.llms.deepinfra import DeepInfra
from langchain_experimental.chat_models import Llama2Chat
llm = DeepInfra(model_id="meta-llama/Llama-2-70b-chat-hf")
model = Llama2Chat(llm=llm)

# Chat Prompt Template
from langchain.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage
from langchain.prompts import HumanMessagePromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a code assistant that generates code for users' input"),
        HumanMessagePromptTemplate.from_template("provide code for {text} in {language}")
    ]
)

# LLM Chain
from langchain_core.output_parsers import StrOutputParser
parser = StrOutputParser()
chain = prompt | model | parser
chain.invoke({'text':'print prime numbers', 'language':'python'})
```

### Simple Sequential Chain

![Simple Sequential Chain](./images/SimpleSequentialChain.PNG)

```python
company_name_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are an assistant that provides a single company name based on the description provided by the user"),
        HumanMessagePromptTemplate.from_template("{text}")
    ]
)

slogan_prompt_template = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="generate a slogan from the company name provided by the user and print it along with the name of the company"),
        HumanMessagePromptTemplate.from_template("{company_name}")
    ]
)

from langchain_core.runnables import RunnableParallel
chain = RunnableParallel(
    company_name = company_name_prompt | model,
    company_slogan = {'company_name' : company_name_prompt | model} | slogan_prompt_template | model | parser 
)
chain.invoke({'text':'a company that sells flying cars'})
```

### Sequential Chain

![Sequential Chain](./images/SequentialChain.PNG)

```python
code_generation_prompt = ChatPromptTemplate.from_messages(
   [
       SystemMessage(content="You are a code assistant that generates code for users' input"),
       HumanMessagePromptTemplate.from_template("generate code for {text} in {language}")
   ] 
)

time_complexity_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a code assistant that evaluates the time and space complexity of code for users' input"),
        HumanMessagePromptTemplate.from_template("{code}")
    ]
)

code_summary_chain = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="you are a code assistant that prints the time complexity of the code and code provided by the user and an explanation for the code"),
        HumanMessagePromptTemplate.from_template("{code} and {time_complexity} ")
    ]
)

from langchain_core.runnables import RunnableParallel, RunnablePassthrough
chain = RunnableParallel(
    code_generation = code_generation_prompt | model,
    code_complexity = RunnablePassthrough.assign(code = (code_generation_prompt | model))| time_complexity_prompt | model,
    code_comparison = {'code' : (code_generation_prompt | model), 'time_complexity': ({'code' : code_generation_prompt | model} | time_complexity_prompt | model)} | code_summary_chain | model
)
chain.invoke({'text':'print prime numbers', 'language':'python'})
```

### Router Chain

![Router Chain](./images/RouterChain.PNG)

```python
sales_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a helpful, honest sales assistant for a telecom company called brightspeed"),
        HumanMessagePromptTemplate.from_template("{text}")
    ]
)

service_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="You are a helpful, honest service assistant for a telecom company called brightspeed, guide the user to resolve the issues."),
        HumanMessagePromptTemplate.from_template("{text}")
    ]
)

router_prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="Categorize the user input to sales or service along with actual text"),
        HumanMessagePromptTemplate.from_template("{text}")
    ]
)

from langchain_core.runnables import RunnableLambda
from langchain_core.output_parsers import StrOutputParser
from transformers import pipeline

# classifier = pipeline('zero-shot-classification', candidate_labels=['sales', 'service'])
parser = StrOutputParser()

chain = router_prompt | model | parser

def categorize_text(text):
    if("sales" in text):
        return sales_prompt
    else:
        return service_prompt

router_chain = RunnablePassthrough.assign(text=(router_prompt | model | parser)) | RunnableLambda(lambda text: categorize_text(text)) | model
router_chain.invoke({'text':"What are the broadband plans available?"})
```

### Transform Chain

- Used to transform the input before it is passed to the prompt or model.

```python
def to_upper(input):
    return {'text': str(input).upper()}

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(content="you are a helpful assistant"),
        HumanMessagePromptTemplate.from_template("{text}, print the actual text")
    ]  
) 

chain = RunnableLambda(lambda text: to_upper(text)) | prompt | model
chain.invoke({"text":"Its me Hi!"})
```

### Math Chain

```python
! pip install numexpr
from langchain.chains import LLMMathChain

chain = LLMMathChain.from_llm(llm)
chain.invoke({"What is 2+2?"})
```

### LangChain Legacy Chains

#### Sequential Chains

```python
from langchain.chains import SimpleSequentialChain, LLMChain

first_prompt = ChatPromptTemplate.from_template("What is the best name to describe a company that makes {product}?")

chain_one = LLMChain(llm=llm, prompt=first_prompt)

second_prompt = ChatPromptTemplate.from_template("Provide a slogan for the company {company_name}")

chain_two = LLMChain(llm=llm, prompt=second_prompt)

simple_seq_chain = SimpleSequentialChain(chains=[chain_one, chain_two], verbose=True)

simple_seq_chain.run("invisible car")
```

#### Sequential Chain

```python
from langchain.chains import SequentialChain

language_translation_prompt = ChatPromptTemplate.from_template("translate the {review} to english")

review_prompt = ChatPromptTemplate.from_template("provide a summary for the

 {english_review} in 20 words")

language_recognition_prompt = ChatPromptTemplate.from_template("what language is the review {review} in?")

final_response_prompt = ChatPromptTemplate.from_template(
    """write a follow up response to the following
    summary in the specific language: {summary} \n language : {language}
    """
)

from langchain_core.runnables import RunnableParallel, RunnablePassthrough
chain = SequentialChain(
    chains=[
        LLMChain(llm=llm, prompt=language_translation_prompt, output_key="english_review"),
        LLMChain(llm=llm, prompt=review_prompt, output_key="summary"),
        LLMChain(llm=llm, prompt=language_recognition_prompt, output_key="language"),
        LLMChain(llm=llm, prompt=final_response_prompt, output_key="followup_message"),
    ],
    input_variables=["review"],
    output_variables=["english_review", "summary", "followup_message", "language"],
    verbose=True,
)
chain("text")
```

#### Router chain

```python
positive_review_prompt = "provide a response thanking the user for the {input}"

negative_review_prompt = "Provide a solution for the {input} and apologize to the customer"

prompt_info = [
    {
        "name": "thank you response",
        "description": "A thank you note for a positive review from the customer",
        "prompt_template": positive_review_prompt,
    },
    {
        "name": "apology",
        "description": "An apology message to the customer for a negative review or statement from the customer",
        "prompt_template": negative_review_prompt,
    },
]

from langchain.prompts import PromptTemplate

destination_chains = {}

for p in prompt_info:
    name = p['name']
    prompt = ChatPromptTemplate.from_template(template=p['prompt_template'])
    chain = LLMChain(prompt=prompt, llm=llm)
    destination_chains[name] = chain

destinations = [f"{p['name']}: {p['description']}" for p in prompt_info]
destination_str = "\n".join(destinations)
dedault_prompt = PromptTemplate.from_template("{input}")
default_chain = LLMChain(llm=llm, prompt=dedault_prompt)

MULTI_PROMPT_ROUTER_TEMPLATE = """Given a raw text input to a \
language model select the model prompt best suited for the input. \
You will be given the names of the available prompts and a \
description of what the prompt is best suited for. \
You may also revise the original input if you think that revising \
it will ultimately lead to a better response from the language model.

<< FORMATTING >>
Return a markdown code snippet with a JSON object formatted to look like:
```json
{
    "destination": string \ name of the prompt to use or "DEFAULT"
    "next_inputs": string \ a potentially modified version of the original input
}
```

REMEMBER: "destination" MUST be one of the candidate prompt \
names specified below OR it can be "DEFAULT" if the input is not \
well suited for any of the candidate prompts.
REMEMBER: "next_inputs" can just be the original input \
if you don't think any modifications are needed.

<< CANDIDATE PROMPTS >>
{destinations}

<< INPUT >>
{input}

<< OUTPUT (remember to include the ```json)>>
"""

from langchain.chains import MultiPromptChain
from langchain.chains.router.llm_router import LLMRouterChain, RouterOutputParser
from langchain.prompts import PromptTemplate

router_template = MULTI_PROMPT_ROUTER_TEMPLATE.format(destinations=destination_str)
router_prompt = PromptTemplate(template=router_template, input_variables=["input"], output_parser=RouterOutputParser())
llm_router_chain = LLMRouterChain.from_llm(llm=llm, prompt=router_prompt)
final_router_chain = MultiPromptChain(router_chain=llm_router_chain, default_chain=default_chain, verbose=True, destination_chains=destination_chains)

final_router_chain.run("Do you sell potatoes?")
```

#### Task: replace string output parser with JSON and Structured Output parser

```python
from langchain_core.pydantic_v1 import BaseModel, Field

class Code(BaseModel):
    text: str = Field(description="")
    # add necessary fields

from langchain_core.output_parsers import JsonOutputParser

output_parser = JsonOutputParser(pydantic_object=Code)
```

#### Structured Output Parser

```python
from langchain.output_parsers import StructuredOutputParser, ResponseSchema

response_schema = [ResponseSchema(
    # add necessary fields
)]

output_parser = StructuredOutputParser.from_response_schemas(response_schema)

output_parser.schema()
```

```python
! pip install pypdf
```

### PDF Loader

```python
from langchain.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:/TrainingMaterial/g

enerative-ai/genai-material/trng-1855/trng-git-repo/trng-1855/week-5/assets/the-velveteen-rabbit.pdf')

pages = loader.load_and_split()

pages
```

### Text Splitting Using Character Splitter

```python
from langchain.text_splitter import CharacterTextSplitter

text_splitter = CharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50,
    separator='\n'
)

documents = text_splitter.split_documents(pages)

documents
```

### Text Splitting Using Recursive Character Splitter

```python
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=50,
    separators=['\n', '\n\n']
)

documents = text_splitter.split_documents(pages)

documents
```

```python
! pip install numexpr
```

### Embedding Model from Hugging Face

```python
from langchain.vectorstores import Pinecone
from langchain.embeddings.huggingface import HuggingFaceEmbeddings

# embedding model from hf
embeddings = HuggingFaceEmbeddings(model_name='thenlper/gte-large')

index = 'trng-index'

result = [Pinecone.from_documents(documents, embeddings.embed_documents, index_name=index)]

result
```

```python
import pinecone
from pinecone import Pinecone
import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('PINECONE_API_KEY')

client = Pinecone(api_key=key)

index = client.Index('trng-index')
```

### Chain with Pinecone Retrieval

```python
from langchain.vectorstores.pinecone import Pinecone
from langchain.chains import RetrievalQA

vectordb = Pinecone(index, embeddings.embed_query, "text")

retriever = vectordb.as_retriever()

chain = RetrievalQA.from_chain_type(llm=model, chain_type="stuff", retriever=retriever)

chain.run("rabbit")
```

### Multi-Query Retriever

```python
from langchain.retrievers import MultiQueryRetriever

retriever = MultiQueryRetriever.from_llm(retriever=retriever, llm=model)

retriever.get_relevant_documents("the boy")
```