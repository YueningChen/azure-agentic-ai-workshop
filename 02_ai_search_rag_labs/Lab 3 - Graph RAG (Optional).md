# Graph RAG (Optional)

This lab is optional and focuses on querying using a Graph RAG. It is designed for those who want to explore advanced RAG architectures that leverage graph databases for enhanced data retrieval and relationship mapping.

All the graphs needed for this Lab are already created. You can find them as Parquet files in the `graphrag/output` directory. Input files used to create the graphs are in the `graphrag/input` directory. And the prompts that are used to extract the entities, relationships, summaries, and other information from the documents are in the `graphrag/prompts` directory.

## Prerequisites

1. From a terminal, navigate to the `graphrag` directory.
2. Rename the `.env.example` file to `.env` and fill in the required values: (all values are already used in the previous labs)
    - `GRAPHRAG_API_URL`: The URL of the Azure OpenAI Endpoint you created in the previous lab.
    - `GRAPHRAG_API_KEY`: The API key for the Azure OpenAI Endpoint.
    - `AIService__DocumentIntelligence__Endpoint`: The URL of the Azure AI Document Intelligence service you created in the previous lab.
    - `AZURE_AI_DOCUMENT_INTELLIGENCE_KEY`: The API key for the Azure AI Document Intelligence service.

## Local Search

Run the following command to perform a local search using the Graph RAG:

```bash
python -m graphrag query -m local -c .\settings.yaml -d .\output -q "What are some of the very important things that Alliant has been achieveing?"  
```

This command will use the local graph database to search for the query and return the results. You can modify the query to search for the achievement of one of the other company documents that we have in the `input` directory (e.g. `ICCU`, `RBFCU`, `SFFCU` `Mountain America`, etc.).

Local search performs well on a pointed query like the one above. However, it may not perform well on a more complex query that requires obtaining information from a larger context.

Let's try a more generic query that requires the model to understand the context of many documents:

```bash
python -m graphrag query -m local -c .\settings.yaml -d .\output -q "What are the key achievements and milestones of all the companies in the past year?"
```

You can notice when the query is more open ended, the model is not able to provide a good answer. This is because the local search is limited to the context of the local graph that it picks based on the query.

## Global Search

Now let's try the same query using global search.

```bash
python -m graphrag query -m global -c .\settings.yaml -d .\output -q "What are the key achievements and milestones of all the companies in the past year?"
```

With global search you can see that it's able to obtain information from a lot more documents and provide a more comprehensive answer. This is because the global search try to traverse the entire graph and find the relevant nodes and relationships that match the query.

Some additional examples of queries you can try:

```bash
python -m graphrag query -m local -c .\settings.yaml -d .\output -q "What are the similarities and differences between BECU and RBFCU?"
```

```bash
python -m graphrag query -m global -c .\settings.yaml -d .\output -q "What are the top 5 companies with total assets?"
```
