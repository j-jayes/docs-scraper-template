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

  * In this section

    * [MCP Docs](https://modelcontextprotocol.info/docs/)
    * [SDKs](https://modelcontextprotocol.info/docs/2026-07-28/sdk/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/sdk/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/sdk/)



  * Light 

  * Dark 

  * System 




On this page

  * Available SDKs
  * Getting Started
  * Next Steps
  * Build a Server
  * Build a Client



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

SDKs

# SDKs

Source: [MCP 89153404](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/891534049ae842de72190fe4af7ce9a0f7c045e6/docs/docs/2026-07-28/sdk.mdx)

## Before choosing an SDK: three distinct things — tier, SDK version, protocol revision

Tiers signal maintenance commitment and support level; they are not a feature switch. The tier-3 Swift, PHP and Kotlin SDKs can still implement the full protocol — the difference is the maintainers' pledged support level and governance participation (see "SDK Tiers").

Easy to conflate| Actual relationship| What to do before integrating  
---|---|---  
SDK package version vs protocol revision| Each SDK adopts revisions on its own cadence; upgrading an SDK does not mean the other end supports the same revision| Check "supported protocol revision" in your SDK's docs and intersect it with your peer's  
Tier level vs capability ceiling| Tiers do not cap what you can implement| Don't abandon a language over tier 3; weigh ecosystem and sample depth  
Official SDK vs the spec text| SDKs are tools; the spec is the contract| Settle behavior disputes against the spec for the revision in play  
  
Suggested path: run the pinned quickstart example for your language first, then swap in your real tools.

Build MCP servers and clients using our official SDKs. SDKs are classified into tiers based on feature completeness, protocol support, and maintenance commitment. Learn more about [SDK tiers](https://modelcontextprotocol.info/community/sdk-tiers/).

## Available SDKs

SDK| Repository| Tier  
---|---|---  
[TypeScript](https://ts.sdk.modelcontextprotocol.io)| [modelcontextprotocol/typescript-sdk](https://github.com/modelcontextprotocol/typescript-sdk)| Tier 1  
[Python](https://py.sdk.modelcontextprotocol.io)| [modelcontextprotocol/python-sdk](https://github.com/modelcontextprotocol/python-sdk)| Tier 1  
[C#](https://csharp.sdk.modelcontextprotocol.io)| [modelcontextprotocol/csharp-sdk](https://github.com/modelcontextprotocol/csharp-sdk)| Tier 1  
[Go](https://go.sdk.modelcontextprotocol.io)| [modelcontextprotocol/go-sdk](https://github.com/modelcontextprotocol/go-sdk)| Tier 1  
[Rust](https://rust.sdk.modelcontextprotocol.io)| [modelcontextprotocol/rust-sdk](https://github.com/modelcontextprotocol/rust-sdk)| Tier 1  
[Ruby](https://ruby.sdk.modelcontextprotocol.io)| [modelcontextprotocol/ruby-sdk](https://github.com/modelcontextprotocol/ruby-sdk)| Tier 1  
[Java](https://java.sdk.modelcontextprotocol.io)| [modelcontextprotocol/java-sdk](https://github.com/modelcontextprotocol/java-sdk)| Tier 2  
Swift| [modelcontextprotocol/swift-sdk](https://github.com/modelcontextprotocol/swift-sdk)| Tier 3  
[PHP](https://php.sdk.modelcontextprotocol.io)| [modelcontextprotocol/php-sdk](https://github.com/modelcontextprotocol/php-sdk)| Tier 3  
[Kotlin](https://kotlin.sdk.modelcontextprotocol.io)| [modelcontextprotocol/kotlin-sdk](https://github.com/modelcontextprotocol/kotlin-sdk)| Tier 3  
  
See [SDK Tiering System](https://modelcontextprotocol.info/community/sdk-tiers/) for details on what each tier means.

## Getting Started

Each SDK follows the idioms and best practices of its language. SDKs adopt new protocol revisions on their own schedules, so check each SDK's documentation for the revisions it supports. All SDKs support:

  * Creating MCP servers that expose tools, resources, and prompts
  * Building MCP clients that can connect to any MCP server
  * Local and remote transport protocols
  * Protocol compliance with type safety



Visit the SDK page for your chosen language to find installation instructions, documentation, and examples.

## Next Steps

Ready to start building with MCP? Choose your path:

### [Build a Server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)

Learn how to create your first MCP server

### [Build a Client](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-client/)

Create applications that connect to MCP servers

[MCP SEP Impact Guide: What Each Proposal Changed and Where It Landed](https://modelcontextprotocol.info/docs/reference/sep-impact-guide/ "MCP SEP Impact Guide: What Each Proposal Changed and Where It Landed")[Security Best Practices](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/security_best_practices/ "Security Best Practices")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
