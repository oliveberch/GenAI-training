from langchain.prompts import PromptTemplate
from langchain.llms.huggingface_hub import HuggingFaceHub
from langchain_core.output_parsers import StrOutputParser
from langchain.chains import LLMChain
from dotenv import load_dotenv

load_dotenv()

prompt = PromptTemplate.from_template(template="Write a program in {language} for {task}")

llm = HuggingFaceHub(
    repo_id="google/flan-t5-xxl",
    model_kwargs={"temperature": 1.0, "max_length": 200}
)

output_parser = StrOutputParser()


chain = LLMChain(
    llm=llm,
    prompt=prompt,
    output_parser=output_parser
)

print(chain.invoke({"task": "function to take distance in meters and return in centimeter", "language": "python"}))

