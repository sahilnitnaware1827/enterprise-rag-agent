# chat end point to handle user queries and generate responses

from src.graph import agent
from src.logger import logger

class ChatService:

    def ask(self, question: str):

        logger.info(f"User query: {question}")

        try:

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

            answer = response["messages"][-1].text()

            logger.info("Response generated successfully.")

            return answer

        except Exception as e:

            logger.error(f"Chat service failed: {e}")

            raise
    