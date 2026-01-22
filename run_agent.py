from decision_engine.agent import should_ai_speak
from decision_engine.retrieval import RetrievalConfidence

# Simple knowledge base (same as notebook)
knowledge_base = [
    "Kubernetes is a container orchestration system used to deploy, scale, and manage containerized applications.",
    "Production deployments should be handled carefully and often require human approval.",
    "System outages are critical incidents and should be handled by on-call engineers."
]

retriever = RetrievalConfidence(knowledge_base)

tests = [
    "Explain Kubernetes networking",
    "Explain it",
    "What should we do?",
    "asdfghjkl"
]

for query in tests:
    confidence = retriever.estimate(query)

    result = should_ai_speak(
        user_query=query,
        context={"user_busy": False},
        confidence=confidence
    )

    print(result)
