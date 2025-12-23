from langchain_openai import ChatOpenAI
from orchestrator.langgraph_supervisor import build_workflow


def main():
    model = ChatOpenAI(model="gpt-4o")

    workflow = build_workflow(model)
    app = workflow.compile()

    # App is ready to be used (FastAPI / CLI / scripts)


if __name__ == "__main__":
    main()
