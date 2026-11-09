[ Model Context Protocol （MCP） ](https://modelcontextprotocol.info/)[Home ](https://modelcontextprotocol.info/)[Get Started ](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)[Develop ](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)[Connect and Run ](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)[Protocol and Versions ](https://modelcontextprotocol.info/specification/)[Reference ](https://modelcontextprotocol.info/tools/)[Blog ](https://modelcontextprotocol.info/blog/)[About](https://modelcontextprotocol.info/about/)

`CTRL K`




`CTRL K`




  * [Get Started](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)

    * [What is MCP?](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)
    * [Architecture and roles](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/)
    * [Servers and primitives](https://modelcontextprotocol.info/docs/2026-07-28/learn/server-concepts/)
    * [Hosts and clients](https://modelcontextprotocol.info/docs/2026-07-28/learn/client-concepts/)

  * [Develop](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)

    * [Build a server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)
    * [Build a client](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-client/)
    * [Choose an SDK](https://modelcontextprotocol.info/docs/2026-07-28/sdk/)
    * [Build with agent skills](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-with-agent-skills/)
    * [Node.js client: calls and failures without a model](https://modelcontextprotocol.info/docs/tutorials/building-a-client-node/)
    * [Design and check effective tools](https://modelcontextprotocol.info/docs/tutorials/writing-effective-tools/)

  * [Connect and Run](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)

    * [Connect a local server](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)
    * [Connect a remote server](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-remote-servers/)
    * [Authorization with OAuth 2.1](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/authorization/)
    * [Local server security defaults](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/local-server-security/)
    * [Security checklist before launch](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/security_best_practices/)
    * [Host applications at scale](https://modelcontextprotocol.info/docs/2026-07-28/develop/clients/client-best-practices/)
    * [Troubleshoot connections and calls](https://modelcontextprotocol.info/docs/2026-07-28/tools/debugging/)
    * [Inspector: test a server interactively](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/)
    * [Inspector CLI: scripted checks and CI](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/cli/)
    * [Inspector recipes: transports, Docker, config import](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/recipes/)
    * [Inspector lab: reproducible calls and failure diagnosis](https://modelcontextprotocol.info/tools/inspector/)

  * [Protocol and Versions](https://modelcontextprotocol.info/specification/)

    * [Version negotiation rules](https://modelcontextprotocol.info/docs/2026-07-28/learn/versioning/)
    * [Revision and method matrix](https://modelcontextprotocol.info/specification/)
    * [Key changes in 2026-07-28](https://modelcontextprotocol.info/specification/2026-07-28/changelog/)
    * [Deprecated features](https://modelcontextprotocol.info/specification/2026-07-28/deprecated/)
    * [Legacy and modern protocol eras](https://modelcontextprotocol.info/docs/2026-07-28/tools/inspector/protocol-eras/)
    * [Client extension support matrix](https://modelcontextprotocol.info/extensions/client-matrix/)

  * [Reference](https://modelcontextprotocol.info/tools/)

    * [Tools and Registry overview](https://modelcontextprotocol.info/tools/)
    * [Production checklist](https://modelcontextprotocol.info/docs/best-practices/)
    * [Client capability matrix](https://modelcontextprotocol.info/docs/clients/)
    * [Tools: definitions and version differences](https://modelcontextprotocol.info/docs/concepts/tools/)
    * [Resources: definitions and version differences](https://modelcontextprotocol.info/docs/concepts/resources/)
    * [Prompts: definitions and trade-offs](https://modelcontextprotocol.info/docs/concepts/prompts/)
    * [Sampling: deprecated server requests for client model calls](https://modelcontextprotocol.info/docs/concepts/sampling/)
    * [Current transports: stdio and Streamable HTTP](https://modelcontextprotocol.info/specification/2026-07-28/basic/transports/)
    * [Publish a server to the Registry](https://modelcontextprotocol.info/tools/registry/publishing/)
    * [Official SEP status index](https://modelcontextprotocol.info/seps/)
    * [SEP impact and method lifecycle guide](https://modelcontextprotocol.info/docs/reference/sep-impact-guide/)
    * [FAQ: revisions, authorization and failure handling](https://modelcontextprotocol.info/docs/faqs/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/getting-started/intro/)



  * Light 

  * Dark 

  * System 




On this page

  * What can MCP enable?
  * Why does MCP matter?
  * Broad ecosystem support
  * Start Building
  * Build servers
  * Build clients
  * Build MCP Apps
  * Learn more
  * Architecture
  * Security
  * Community
  * Contributing



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

What is the Model Context Protocol (MCP)?

# What is the Model Context Protocol (MCP)?

Source: [MCP b491e568](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/b491e56832ce09207d6d7bb2aae186ce55fdf172/docs/docs/2026-07-28/getting-started/intro.mdx)

## New to MCP: route yourself first

MCP is an open protocol standard, not a software package: it defines how an AI application (a client) exchanges capabilities with external systems (servers). When either side says it "supports MCP", the practical meaning is whatever protocol revision and extensions it actually implements — confirm both sides' declared version sets before building (see [Versioning](https://modelcontextprotocol.info/docs/2026-07-28/learn/versioning/)).

Your goal| Read first| Then  
---|---|---  
Use an existing server in Claude, your editor, etc.| [Connect local servers](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/) / [connect remote servers](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-remote-servers/)| Register the server in your client's config  
Build a server that exposes data or tools| [Build a server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)| Use the [Inspector guide](https://modelcontextprotocol.info/tools/inspector/) to check the connection and the capabilities your server actually exposes  
Build an app that talks to MCP servers| [Build a client](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-client/)| Check [Architecture](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/) for the three-party roles  
Understand the protocol itself| [Architecture](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/) / [Versioning](https://modelcontextprotocol.info/docs/2026-07-28/learn/versioning/)| Read the spec tree for the revision you target  
  
This page is pinned to the upstream commit in its front matter; the current protocol revision is 2026-07-28.

MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems.

Using MCP, AI applications like Claude or ChatGPT can connect to data sources (e.g. local files, databases), tools (e.g. search engines, calculators) and workflows (e.g. specialized prompts)—enabling them to access key information and perform tasks.

Think of MCP like a USB-C port for AI applications. Just as USB-C provides a standardized way to connect electronic devices, MCP provides a standardized way to connect AI applications to external systems.

## What can MCP enable?

  * Agents can access your Google Calendar and Notion, acting as a more personalized AI assistant.
  * Claude Code can generate an entire web app using a Figma design.
  * Enterprise chatbots can connect to multiple databases across an organization, empowering users to analyze data using chat.
  * AI models can create 3D designs on Blender and print them out using a 3D printer.



## Why does MCP matter?

Depending on where you sit in the ecosystem, MCP can have a range of benefits.

  * **Developers** : MCP reduces development time and complexity when building, or integrating with, an AI application or agent.
  * **AI applications or agents** : MCP gives them access to an ecosystem of data sources, tools and apps, which enhances their capabilities and improves the end-user experience.
  * **End-users** : MCP results in more capable AI applications or agents that can access user data and take actions on the user's behalf when necessary.



## Broad ecosystem support

MCP is an open protocol supported across a wide range of clients and servers. AI assistants like [Claude](https://claude.com/docs/connectors/building) and [ChatGPT](https://developers.openai.com/api/docs/mcp/), development tools like [Visual Studio Code](https://code.visualstudio.com/docs/copilot/chat/mcp-servers), [Cursor](https://cursor.com/docs/context/mcp), [MCPJam](https://docs.mcpjam.com/getting-started), and many others all support MCP — making it easy to build once and integrate everywhere.

## Start Building

### [Build servers](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)

Create MCP servers to expose your data and tools

### [Build clients](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-client/)

Develop applications that connect to MCP servers

### [Build MCP Apps](https://modelcontextprotocol.info/extensions/apps/overview/)

Build interactive apps that run inside AI clients

## Learn more

### [Architecture](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/)

Learn the core concepts and architecture of MCP

### [Security](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/security_best_practices/)

Understand the security considerations and best practices for MCP

## Community

### [Contributing](https://modelcontextprotocol.info/community/contributing/)

Learn how to get involved and contribute to MCP

[Understanding MCP servers](https://modelcontextprotocol.info/docs/2026-07-28/learn/server-concepts/ "Understanding MCP servers")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
