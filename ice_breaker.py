from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama
from langchain_core.output_parsers import StrOutputParser

information = """
    John is a software engineer with 5 years of experience in Python and Java. He loves hiking and has climbed Mount Everest.
"""

if __name__ == '__main__':
    print("hello LangChain!")

    summary_template = """
        given the information {information} about a person from I want you to create:
        1. a short summary
        2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"],
        template=summary_template,
    )

    # llm = ChatOpenAI(
    #     model="gpt-3.5-turbo",
    #     temperature=0,
    # )

    llm = ChatOllama(
        model="llama3.2",
        temperature=0
    )

    chain = summary_prompt_template | llm | StrOutputParser()

    res = chain.invoke(input={"information": information})
    print(res)
