from langchain_google_genai import ChatGoogleGenerativeAI
from prompts import SUMMARY_PROMPT, CONTRIBUTIONS_PROMPT, LIMITATIONS_PROMPT, FUTURE_WORK_PROMPT

class ResearchAssistant:
    def __init__(self, full_text, qa_chain):
        self.full_text = full_text[:12000]  # keep prompt size reasonable
        self.qa_chain = qa_chain
        self.llm = ChatGoogleGenerativeAI(model="gemini-3.6-flash")

    def _run_fixed_prompt(self, template):
        prompt = template.format(context=self.full_text)
        response = self.llm.invoke(prompt)
        content = response.content
        if isinstance(content, list):
            # Newer Gemini models return content as a list of blocks — extract just the text
            return "".join(
                block.get("text", "") for block in content if isinstance(block, dict)
            )
        return content

    def summarize(self):
        return self._run_fixed_prompt(SUMMARY_PROMPT)

    def contributions(self):
        return self._run_fixed_prompt(CONTRIBUTIONS_PROMPT)

    def limitations(self):
        return self._run_fixed_prompt(LIMITATIONS_PROMPT)

    def future_work(self):
        return self._run_fixed_prompt(FUTURE_WORK_PROMPT)

    def ask(self, question: str):
        result = self.qa_chain.invoke({"query": question})
        answer = result["result"]
        sources = result.get("source_documents", [])
        page_numbers = sorted({s.metadata.get("page", "?") for s in sources})
        return answer, page_numbers

    def route(self, user_input: str):
        """Very simple intent router — the 'agent' decision layer."""
        text = user_input.lower().strip()
        if text in ("summary", "summarize"):
            return self.summarize()
        elif text in ("contributions", "key contributions"):
            return self.contributions()
        elif text in ("limitations",):
            return self.limitations()
        elif text in ("future work",):
            return self.future_work()
        else:
            answer, pages = self.ask(user_input)
            return f"{answer}\n\n(Source pages: {pages})"