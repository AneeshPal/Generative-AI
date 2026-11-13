Generative-AI

My learning journal for Generative AI. I'm a CS student trying to actually understand how LLM apps work instead of just copy-pasting from tutorials, so this repo is where I try things out, break them, and fix them.

Everything here is Python, and most folders are just small experiments I wrote while learning that topic. The code isn't production-grade, but it runs, and the commit messages show how my understanding grew over time.

What's inside

I've numbered the folders in the order I studied them.

Folder	What I worked on
1.LLMs	Basics of working with LLM models and calling them from code
2.ChatModels	Chat models, and also trying to run a Hugging Face model locally
3.EmbeddedModels	Embeddings, plus a small document similarity search app
4.Prompts	Prompt templates, and a small research tool built with Streamlit
5.Structured_output	Getting structured responses back from models
6.output_parser	Output parsers, including the string output parser
7.chains	Chaining components together
8.runnables	The different types of runnables in LangChain
10.document_loaders	Loading data from different sources
11.text_splitters	Length based, markdown based and plain text splitting
LangGraph	Currently learning (see below)
Where I'm at right now

I've finished the LangChain fundamentals and the RAG building blocks (loaders, splitters, embeddings), and I'm currently learning LangGraph, specifically how to build workflows with nodes, edges and state instead of just linear chains.

The LangGraph folder is a work in progress and will keep growing as I learn.

Running it yourself
bash
# clone the repo
git clone https://github.com/AneeshPal/Generative-AI.git
cd Generative-AI

# make a virtual environment
python -m venv venv
source venv/bin/activate      # on Windows: venv\Scripts\activate

# install dependencies
pip install -r requirements.txt

Create a .env file in the root and add whatever API keys the scripts need (OpenAI, Hugging Face, etc). It's in .gitignore, so it won't get pushed.

OPENAI_API_KEY=your_key_here
HUGGINGFACEHUB_API_TOKEN=your_token_here

Then just run any script from its folder:

bash
python filename.py

When you're done, type deactivate to leave the virtual environment.

What I plan to add next
 LangGraph: state, nodes, edges and conditional routing
 LangGraph: workflows with loops and tool use
 A complete RAG app that ties loaders, splitters, embeddings and retrieval together
 Notes on things that confused me, so I (and maybe you) don't get stuck on them twice
Tech used
Python
LangChain
LangGraph
Streamlit
Hugging Face models
A note

I'm learning in public, so if you spot a mistake or know a better way to do something, feel free to open an issue or a PR. Always happy to learn.

Made with &hearts; by Aneesh