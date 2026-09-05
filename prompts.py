SUMMARY_PROMPT = """You are a research assistant. Based only on the paper content below,
write a concise summary in 4-6 sentences for someone unfamiliar with the topic.

Paper content:
{context}
"""

CONTRIBUTIONS_PROMPT = """List the key contributions of this paper as 3-5 bullet points,
based only on the content below. Be specific and avoid generic statements.

Paper content:
{context}
"""

LIMITATIONS_PROMPT = """Identify the limitations or weaknesses the authors mention or that are
evident from the paper below. List them as bullet points. If none are explicitly stated,
say so honestly rather than inventing any.

Paper content:
{context}
"""

FUTURE_WORK_PROMPT = """Based on the paper below, list the future work directions the authors
suggest, or reasonable next steps if none are explicitly stated (label these as "suggested").

Paper content:
{context}
"""
