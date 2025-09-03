import re

def classify_question(question: str) -> str:
    """Classify question into factual, opinion, or math."""
    # Check if it's a math question
    if re.search(r'[0-9\+\-\*/\^=]', question):
        return "math"
    
    # Opinion keywords
    opinion_keywords = ["think", "feel", "opinion", "believe", "best", "should", "prefer"]
    if any(word in question.lower() for word in opinion_keywords):
        return "opinion"
    
    # Default: factual
    return "factual"


def respond(question: str) -> str:
    q_type = classify_question(question)
    
    if q_type == "math":
        try:
            answer = eval(question)
            return f"Math Question → Answer: {answer}"
        except:
            return "Math Question → Unable to compute safely."
    
    elif q_type == "opinion":
        return "Opinion Question → That depends on personal perspective!"
    
    else:  # factual
        return "Factual Question → Here’s a fact-based answer (stubbed)."

if __name__ == "__main__":
    while True:
        user_q = input("Ask me a question (or type 'exit'): ")
        if user_q.lower() == "exit":
            break
        print(respond(user_q))
