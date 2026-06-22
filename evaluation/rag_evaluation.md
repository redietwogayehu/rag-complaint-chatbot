# RAG Evaluation

## Evaluation Method

The RAG system was tested using representative business questions related to customer complaints across financial products. For each query, the retriever returned the most relevant complaint chunks from ChromaDB, and the generator produced a summarized response.

| Question                                                 | Generated Answer Summary                                                          | Retrieved Source Example                       | Quality Score (1-5) | Comments                                 |
| -------------------------------------------------------- | --------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------- | ---------------------------------------- |
| Why are customers unhappy with credit cards?             | Customers frequently complain about billing disputes, fees, and interest charges. | "Unexpected charges appeared on my account..." | 4                   | Relevant retrieval and accurate summary. |
| What are common money transfer complaints?               | Delayed transfers and missing funds are recurring issues.                         | "My transfer never reached the recipient..."   | 4                   | Good retrieval quality.                  |
| What issues occur with personal loans?                   | Customers report loan servicing problems and payment processing issues.           | "Payments were applied incorrectly..."         | 4                   | Response aligned with retrieved context. |
| What complaints are common in savings accounts?          | Unauthorized fees and account access issues were frequently reported.             | "My account was charged fees unexpectedly..."  | 5                   | Strong retrieval and response quality.   |
| Which product category has the highest complaint volume? | Credit card complaints appeared most frequently in the filtered dataset.          | Product metadata from retrieved records.       | 5                   | Answer matched dataset trends.           |

## Observations

* Retrieval quality was generally strong when complaints contained detailed narratives.
* Chunk size of 500 characters with 50-character overlap preserved context effectively.
* The all-MiniLM-L6-v2 embedding model provided semantically relevant matches.
* Future improvements include testing larger embedding models and adding metadata filtering by product category.
