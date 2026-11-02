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
    * [Connect to remote MCP Servers](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-remote-servers/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-remote-servers/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/develop/connect-remote-servers/)



  * Light 

  * Dark 

  * System 




On this page

  * Understanding Remote MCP Servers
  * What are Custom Connectors?
  * Connecting to a Remote MCP Server
  * Navigate to Connector Settings
  * Add a Custom Connector
  * Complete Authentication
  * Access Resources and Prompts
  * Configure Tool Permissions
  * Best Practices for Using Remote MCP Servers
  * Next Steps
  * Build your own remote server
  * Explore available servers
  * Connect local servers
  * Understand the architecture



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

Connect to remote MCP Servers

# Connect to remote MCP Servers

Source: [MCP d998c804](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/d998c8049b8850d49d1fe3389ebf0e4a63262ab5/docs/docs/2026-07-28/develop/connect-remote-servers.mdx)

## Remote connections: establish the endpoint and permissions first

The `example-server.modelcontextprotocol.io` URL below is an attributed source example. This run did not check its availability, operator or capabilities and does not offer it as a public test service. Obtain a URL from a trusted service operator, then confirm HTTPS, the full path, supported revisions and authentication method. Never send account credentials to an unknown endpoint.

### Reachable HTTP is not sufficient

Use [the Inspector CLI lab](https://modelcontextprotocol.info/tools/inspector/) against an endpoint you control before opening a connector UI. On 2026-10-30, pinned Inspector `2.12.0` produced these results against local HTTP fixtures. They are controlled failure cases, not public service measurements.

Controlled response| Observed result| Next check  
---|---|---  
Working legacy MCP server| `auto` fell back and listed tools; `modern` failed| Protocol era before account permissions  
`404`| Inspector connection failed| `/mcp` path, reverse-proxy prefix and method  
`200 text/html` login page| Inspector connection failed| Redirects and login gateways; HTTP 200 does not establish an MCP result  
`401` with Bearer challenge| Inspector connection failed| PRM, authorization server and the client's supported login flow  
`403`| Inspector connection failed| Scope, policy and Origin; this status alone cannot identify the cause  
  
### Use a successful security control

[The best-practices article](https://modelcontextprotocol.info/docs/best-practices/) embeds `auth_ref_server.py` and `probe_http.py`. Its synthetic `good-token` and `other-audience-token` are loopback fixture values, not real OAuth credentials. This run checked the Python SDK `mcp==2.3.0` resource server: valid credentials returned a discovery result; missing, invalid and wrong-resource credentials returned 401 with no MCP result. Holding the same valid credentials fixed, the allowed `http://127.0.0.1:8001` Origin succeeded and an untrusted Origin returned 403. An arbitrary 4xx response cannot prove all of these boundaries.

Copy the two embedded files, start `python3 auth_ref_server.py` in an environment with the pinned SDK, then run in another terminal:
    
    
    python3 probe_http.py http://127.0.0.1:8001/mcp --token good-token --expect-auth --bad-audience-token other-audience-token

The probe carries valid credentials for its protocol and Origin negative cases, so an authentication failure cannot masquerade as Origin validation. It does not cover an allowed-Origin positive case; also send allowed, untrusted and absent Origin with the same valid credentials against your configuration and inspect the MCP results. Non-browser requests without Origin still need authentication. A synthetic token verifier does not validate JWT signatures, issuer, PKCE or an end-to-end OAuth flow.

Then configure the connector: check your client's Custom Connector support, exact redirect URI, organization policy and tool permissions. Source screenshots, shortcuts and generic mentions of API keys or passwords do not guarantee a current client's input methods. This run did not operate a real desktop UI, sign in remotely or exercise an OAuth callback; use [the authorization tutorial](https://modelcontextprotocol.info/docs/2026-07-28/tutorials/security/authorization/) to verify those stages separately.

Remote MCP servers extend AI applications' capabilities beyond your local environment, providing access to internet-hosted tools, services, and data sources. By connecting to remote MCP servers, you transform AI assistants from helpful tools into informed teammates capable of handling complex, multi-step projects with real-time access to external resources.

Many clients now support remote MCP servers, enabling a wide range of integration possibilities. This guide demonstrates how to connect to remote MCP servers using [Claude](https://claude.ai/) as an example, one of the many clients that support MCP. While we focus on Claude's implementation through Custom Connectors, the concepts apply broadly to other MCP-compatible clients.

## Understanding Remote MCP Servers

Remote MCP servers function similarly to local MCP servers but are hosted on the internet rather than your local machine. They expose tools, prompts, and resources that Claude can use to perform tasks on your behalf. These servers can integrate with various services such as project management tools, documentation systems, code repositories, and any other API-enabled service.

The key advantage of remote MCP servers is their accessibility. Unlike local servers that require installation and configuration on each device, remote servers are available from any MCP client with an internet connection. This makes them ideal for web-based AI applications, integrations that emphasize ease of use, and services that require server-side processing or authentication.

## What are Custom Connectors?

Custom Connectors serve as the bridge between Claude and remote MCP servers. They allow you to connect Claude directly to the tools and data sources that matter most to your workflows, enabling Claude to operate within your favorite software and draw insights from the complete context of your external tools.

With Custom Connectors, you can:

  * [Connect Claude to existing remote MCP servers](https://support.anthropic.com/en/articles/11175166-getting-started-with-custom-connectors-using-remote-mcp) provided by third-party developers
  * [Build your own remote MCP servers to connect with any tool](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)



## Connecting to a Remote MCP Server

The process of connecting Claude to a remote MCP server involves adding a Custom Connector through the [Claude interface](https://claude.ai/). This establishes a secure connection between Claude and your chosen remote server.

### Navigate to Connector Settings

Open Claude Desktop or Claude in your browser, then navigate to the settings page:

  * **Desktop** : Either use the keyboard shortcut `Ctrl+Comma` or click the top-left menu icon  , hover over "File", and select "Settings"
  * **Browser** : Either use the keyboard shortcut `⌘⇧,` (_macOS_) or click on your profile icon, and select "Settings" from the menu



Once you're in the settings page, click "Connectors" in the sidebar. This displays your currently configured connectors and provides options for adding new ones.

### Add a Custom Connector

In the Connectors section, click the "Add" button at the top-right of the window, then select "Add custom connector" from the dropdown. This begins the connection process. To follow along, copy/paste the URL below:
    
    
    https://example-server.modelcontextprotocol.io/mcp

A dialog will appear prompting you to enter the remote MCP server URL. This URL should be provided by the server developer or administrator. Enter the complete URL, ensuring it includes the proper protocol (https://) and any necessary path components.

After entering the URL, click "Add" to proceed with the connection.

### Complete Authentication

Most remote MCP servers require authentication to ensure secure access to their resources. The authentication process varies depending on the server implementation but commonly involves OAuth, API keys, or username/password combinations.

Follow the authentication prompts provided by the server. This may redirect you to a third-party authentication provider or display a form within Claude. Once authentication is complete, Claude will establish a secure connection to the remote server.

### Access Resources and Prompts

After successful connection, the remote server’s resources and prompts become available in your Claude conversations. You can access these by clicking the "Add files, connectors, and more /" indicator  in the bottom-left corner of the message input area. Then hover over "Connectors", move the cursor over "Add to Example Remote Server", where hovering displays the attachment menu.

The menu displays all available resources and prompts from your connected server. Select the items you want to include in your conversation. These resources provide Claude with context and information from your external tools.

### Configure Tool Permissions

Remote MCP servers often expose multiple tools with varying capabilities. You can control which tools Claude is allowed to use by configuring permissions in the connector settings. This ensures Claude only performs actions you've explicitly authorized.

Navigate back to the Connectors settings and click on your connected server. Here you can enable or disable specific tools, set usage limits, and configure other security parameters according to your needs.

## Best Practices for Using Remote MCP Servers

When working with remote MCP servers, consider these recommendations to ensure a secure and efficient experience:

**Security considerations** : Always verify the authenticity of remote MCP servers before connecting. Only connect to servers from trusted sources, and review the permissions requested during authentication. Be cautious about granting access to sensitive data or systems.

**Managing multiple connectors** : You can connect to multiple remote MCP servers simultaneously. Organize your connectors by purpose or project to maintain clarity. Regularly review and remove connectors you no longer use to keep your workspace organized and secure.

## Next Steps

Now that you've connected Claude to a remote MCP server, you can explore its capabilities in your conversations. Try using the connected tools to automate tasks, access external data, or integrate with your existing workflows.

### [Build your own remote server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/)

Create custom remote MCP servers to integrate with proprietary tools and services

### [Explore available servers](https://github.com/modelcontextprotocol/servers)

Browse our collection of official and community-created MCP servers

### [Connect local servers](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/)

Learn how to connect Claude Desktop to local MCP servers for direct system access

### [Understand the architecture](https://modelcontextprotocol.info/docs/2026-07-28/learn/architecture/)

Dive deeper into how MCP works and its architecture

Remote MCP servers unlock powerful possibilities for extending Claude's capabilities. As you become familiar with these integrations, you'll discover new ways to streamline your workflows and accomplish complex tasks more efficiently.

[Connect to local MCP servers](https://modelcontextprotocol.info/docs/2026-07-28/develop/connect-local-servers/ "Connect to local MCP servers")[Debugging](https://modelcontextprotocol.info/docs/2026-07-28/tools/debugging/ "Debugging")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
