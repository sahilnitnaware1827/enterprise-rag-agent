# chat end point to handle user queries and generate responses

from src.graph import agent


class ChatService:

    def ask(self, question: str):

        response = agent.invoke(
            {
                "messages": [
                    {
                        "role": "user",
                        "content": question
                    }
                ]
            }
        )

        return response["messages"][-1].text()
    