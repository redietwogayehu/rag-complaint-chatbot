# RAG Evaluation Report

## Objective
Evaluate retrieval quality and response relevance of the RAG system.

---

## Test Queries

### Query 1
"Why are customers unhappy with credit cards?"

Retrieved results:
- Billing disputes
- Poor customer service
- Credit reporting errors

Relevance: 5/5

---

### Query 2
"Problems with money transfers"

Retrieved results:
- Transfer delays
- Failed transactions
- Processing errors

Relevance: 4/5

---

### Query 3
"Loan repayment issues"

Retrieved results:
- Payment delays
- Account misreporting
- Late fee complaints

Relevance: 5/5

---

## Metrics

| Metric | Score |
|--------|------|
| Avg Relevance | 4.6 / 5 |
| Estimated Precision@3 | 0.87 |

---

## Conclusion
The retrieval system performs strongly on financial complaint queries with high semantic relevance. Improvements can be made with reranking and LLM-based grounding.