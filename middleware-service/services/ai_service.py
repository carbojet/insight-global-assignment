from uuid import uuid4
from datetime import datetime, timezone
from models.insight import Insight

def generate_insights(prompt: str):
    insights = []
    now = datetime.now(timezone.utc)
    for i in range(37):
        insights.append(
            Insight(
                id=uuid4(),
                title=f"Insight {i+1}",
                content=f"Generated insight based on: {prompt}",
                category="General",
                confidenceScore=0.8,
                createdAt=now,
                updatedAt=now
            )
        )
    return insights
