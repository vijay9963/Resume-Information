from langfuse import Langfuse
import os

langfuse = Langfuse(
    public_key=os.getenv("LANGFUSE_PUBLIC_KEY"),
    secret_key=os.getenv("LANGFUSE_SECRET_KEY"),
    host="https://cloud.langfuse.com"
)

def create_trace(user_input):
    trace = langfuse.trace(
        name="resume_extraction",
        input=user_input
    )
    return trace