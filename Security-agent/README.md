# 🛡️ Security Guardian Agent for Multi-Agent Travel Assistant

A Security AI agent to monitor, block agent interactions &amp; delegations. 

![screenshjto1](https://github.com/user-attachments/assets/078cff64-7efc-4be8-b3a9-e527a01fdd08)



![screenshjto2](https://github.com/user-attachments/assets/0fb9fb6f-9e64-4006-949f-6bfaa2f77163)




A modular, secure travel assistant system built with Chainlit, supporting agent handoffs, prompt injection defense (LlamaFirewall & LLM-Guard), and contextual security checks.

---

## Features

- **Multi-agent orchestration:** Hotel, Activities, and Coordinator agents.
- **SecurityGuardian:** Modular security layer with contextual, static, and AI-powered checks.
- **Prompt injection & output scanning:** Integrates [LLM-Guard](https://github.com/protectai/llm-guard).
- **Chainlit UI:** Interactive web chat.
- **Session-based context:** Per-user chat history and security context.

---


## 🛠️ Installation Steps

### Step 1: Clone the GitHub Repository

```bash
git clone https://github.com/vsn411/security-agent.git
cd security-agent
```

### Step 2: Create and Activate a Virtual Environment

```bash
python -m venv venvmcp
source venvmcp/bin/activate  # On Windows use: venvmcp\Scripts\activate
```

### Step 3: Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

### Step 4: Configure environment variables
- For OpenAI or other LLMs, add your API keys to a `.env` file.

---

### Step 5: 

Start the Chainlit app: 

chainlit run main.py --port 8000

- **Dependency Issues:**  
  Ensure all packages are up-to-date and compatible.

- **Debugging:**  
  Debug print statements are included throughout the code for agent and security flow tracing.

---

## Credits

- [ProtectAI LLM-Guard](https://github.com/protectai/llm-guard)
- [Chainlit](https://www.chainlit.io/)
- [OpenAI, Hugging Face, and other LLM providers]

---

## License

Apache License 

---

## Contributing
Pull requests and issues welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for details.


