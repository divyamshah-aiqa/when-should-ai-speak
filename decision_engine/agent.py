from decision_engine.signals import (
    estimate_clarity,
    estimate_attention_cost
)
from decision_engine.decision import decide_action


def should_ai_speak(user_query, context=None, confidence=0.0):
    clarity = estimate_clarity(user_query)
    attention_cost = estimate_attention_cost(user_query, context)

    decision, reason = decide_action(
        confidence=confidence,
        clarity=clarity,
        attention_cost=attention_cost
    )


    decision_log = {
    "query": user_query,
    "decision": decision,
    "clarity_score": clarity,
    "confidence_score": confidence,
    "attention_cost": attention_cost,
    "failure_reason": None if decision == "RESPOND" else reason
}
    print(decision_log)
    
    return {
        "query": user_query,
        "signals": {
            "clarity": clarity,
            "confidence": confidence,
            "attention_cost": attention_cost
        },
        "decision": decision,
        "reason": reason
    }
