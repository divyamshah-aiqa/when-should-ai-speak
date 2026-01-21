def estimate_clarity(user_query):
    if len(user_query.strip()) < 10:
        return 0.2
    if "?" not in user_query:
        return 0.5
    return 0.8


def estimate_attention_cost(user_query, context=None):
    if context and context.get("user_busy"):
        return 0.8
    if "urgent" in user_query.lower():
        return 0.2
    return 0.5
