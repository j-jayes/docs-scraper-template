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
    * [Understanding MCP servers](https://modelcontextprotocol.info/docs/2026-07-28/learn/server-concepts/)

  * More
  * [Docs ↗](https://modelcontextprotocol.info/docs/)
  * [Specification ↗](https://modelcontextprotocol.info/specification/)
  * [About](https://modelcontextprotocol.info/about/)



English

  * [English](https://modelcontextprotocol.info/docs/2026-07-28/learn/server-concepts/)
  * [简体中文](https://mcpcn.com/docs/2026-07-28/learn/server-concepts/)



  * Light 

  * Dark 

  * System 




On this page

  * Core Server Features
  * Tools
  * How Tools Work
  * Example: Travel Booking
  * User Interaction Model
  * Resources
  * How Resources Work
  * Example: Getting Travel Planning Context
  * Parameter Completion
  * User Interaction Model
  * Prompts
  * How Prompts Work
  * Example: Streamlined Workflows
  * User Interaction Model
  * Bringing Servers Together
  * Example: Multi-Server Travel Planning
  * The Complete Flow



Scroll to top

[MCP Docs](https://modelcontextprotocol.info/docs/)

Understanding MCP servers

# Understanding MCP servers

Source: [MCP 29affa6b](https://github.com/modelcontextprotocol/modelcontextprotocol/blob/29affa6b11e2dbd5a8b5678e9b90aa4a336769a4/docs/docs/2026-07-28/learn/server-concepts.mdx)

## From server concepts to a running server

  * [Build a server](https://modelcontextprotocol.info/docs/2026-07-28/develop/build-server/) exercises this page's tools primitive with a pinned SDK lab — its fixture server exposes four tools and no resources or prompts — including the missing-argument and failure paths of `tools/call`.
  * [Design and check effective tools](https://modelcontextprotocol.info/docs/tutorials/writing-effective-tools/) covers the model-facing half of the tools row above: how a model chooses between similar tools, and how to check definitions without running a model.
  * Each primitive has a cross-revision reference on this site that goes beyond the current view: [tools](https://modelcontextprotocol.info/docs/concepts/tools/), [resources](https://modelcontextprotocol.info/docs/concepts/resources/) and [prompts](https://modelcontextprotocol.info/docs/concepts/prompts/) track field-level changes since 2024-11-05.
  * The multi-server flow at the end of this page is observed one server at a time with the [Inspector](https://modelcontextprotocol.info/tools/inspector/); when the composition fails, start at [troubleshooting](https://modelcontextprotocol.info/docs/2026-07-28/tools/debugging/).



MCP servers are programs that expose specific capabilities to AI applications through standardized protocol interfaces.

Common examples include file system servers for document access, database servers for data queries, GitHub servers for code management, Slack servers for team communication, and calendar servers for scheduling.

## Core Server Features

Servers provide functionality through three building blocks:

Feature| Explanation| Examples| Who controls it  
---|---|---|---  
**Tools**|  Functions that your LLM can actively call, and decides when to use them based on user requests. Tools can write to databases, call external APIs, modify files, or trigger other logic.| Search flights  
Send messages  
Create calendar events| Model  
**Resources**|  Passive data sources that provide read-only access to information for context, such as file contents, database schemas, or API documentation.| Retrieve documents  
Access knowledge bases  
Read calendars| Application  
**Prompts**|  Pre-built instruction templates that tell the model to work with specific tools and resources.| Plan a vacation  
Summarize my meetings  
Draft an email| User  
  
We will use a hypothetical scenario to demonstrate the role of each of these features, and show how they can work together.

### Tools

Tools enable AI models to perform actions. Each tool defines a specific operation with typed inputs and outputs. The model requests tool execution based on context.

#### How Tools Work

Tools are schema-defined interfaces that LLMs can invoke. MCP uses JSON Schema for validation. Each tool performs a single operation with clearly defined inputs and outputs. Tools may require user consent prior to execution, helping to ensure users maintain control over actions taken by a model.

**Protocol operations:**

Method| Purpose| Returns  
---|---|---  
`tools/list`| Discover available tools| Array of tool definitions with schemas  
`tools/call`| Execute a specific tool| Tool execution result  
  
**Example tool definition:**
    
    
    {
      name: "searchFlights",
      description: "Search for available flights",
      inputSchema: {
        type: "object",
        properties: {
          origin: { type: "string", description: "Departure city" },
          destination: { type: "string", description: "Arrival city" },
          date: { type: "string", format: "date", description: "Travel date" }
        },
        required: ["origin", "destination", "date"]
      }
    }

#### Example: Travel Booking

Tools enable AI applications to perform actions on behalf of users. In a travel planning scenario, the AI application might use several tools to help book a vacation:

**Flight Search**
    
    
    searchFlights(origin: "NYC", destination: "Barcelona", date: "2024-06-15")

Queries multiple airlines and returns structured flight options.

**Calendar Blocking**
    
    
    createCalendarEvent(title: "Barcelona Trip", startDate: "2024-06-15", endDate: "2024-06-22")

Marks the travel dates in the user's calendar.

**Email notification**
    
    
    sendEmail(to: "[[email protected]](/cdn-cgi/l/email-protection)", subject: "Out of Office", body: "...")

Sends an automated out-of-office message to colleagues.

#### User Interaction Model

Tools are model-controlled, meaning AI models can discover and invoke them automatically. However, MCP emphasizes human oversight through several mechanisms.

For trust and safety, applications can implement user control through various mechanisms, such as:

  * Displaying available tools in the UI, enabling users to define whether a tool should be made available in specific interactions
  * Approval dialogs for individual tool executions
  * Permission settings for pre-approving certain safe operations
  * Activity logs that show all tool executions with their results



### Resources

Resources provide structured access to information that the AI application can retrieve and provide to models as context.

#### How Resources Work

Resources expose data from files, APIs, databases, or any other source that an AI needs to understand context. Applications can access this information directly and decide how to use it - whether that's selecting relevant portions, searching with embeddings, or passing it all to the model.

Each resource has a unique URI (e.g., `file:///path/to/document.md`) and declares its MIME type for appropriate content handling.

Resources support two discovery patterns:

  * **Direct Resources** \- fixed URIs that point to specific data. Example: `calendar://events/2024` \- returns calendar availability for 2024
  * **Resource Templates** \- dynamic URIs with parameters for flexible queries. Example:
    * `travel://activities/{city}/{category}` \- returns activities by city and category
    * `travel://activities/barcelona/museums` \- returns all museums in Barcelona



Resource Templates include metadata such as title, description, and expected MIME type, making them discoverable and self-documenting.

**Protocol operations:**

Method| Purpose| Returns  
---|---|---  
`resources/list`| List available direct resources| Array of resource descriptors  
`resources/templates/list`| Discover resource templates| Array of resource template definitions  
`resources/read`| Retrieve resource contents| Resource data with metadata  
`subscriptions/listen`| Monitor resource changes| Stream of update notifications  
  
To watch specific resources for changes, a client sends a [`subscriptions/listen`](https://modelcontextprotocol.info/specification/2026-07-28/basic/patterns/subscriptions/) request with the resource URIs listed in the `resourceSubscriptions` filter. The server delivers `notifications/resources/updated` on the resulting stream whenever a watched resource changes.

#### Example: Getting Travel Planning Context

Continuing with the travel planning example, resources provide the AI application with access to relevant information:

  * **Calendar data** (`calendar://events/2024`) - Checks user availability
  * **Travel documents** (`file:///Documents/Travel/passport.pdf`) - Accesses important documents
  * **Previous itineraries** (`trips://history/barcelona-2023`) - References past trips and preferences



The AI application retrieves these resources and decides how to process them, whether selecting a subset of data using embeddings or keyword search, or passing raw data directly to the model.

In this case, it provides calendar data, weather information, and travel preferences to the model, enabling it to check availability, look up weather patterns, and reference past travel preferences.

**Resource Template Examples:**
    
    
    {
      "uriTemplate": "weather://forecast/{city}/{date}",
      "name": "weather-forecast",
      "title": "Weather Forecast",
      "description": "Get weather forecast for any city and date",
      "mimeType": "application/json"
    }
    
    {
      "uriTemplate": "travel://flights/{origin}/{destination}",
      "name": "flight-search",
      "title": "Flight Search",
      "description": "Search available flights between cities",
      "mimeType": "application/json"
    }

These templates enable flexible queries. For weather data, users can access forecasts for any city/date combination. For flights, they can search routes between any two airports. When a user has input "NYC" as the `origin` airport and begins to input "Bar" as the `destination` airport, the system can suggest "Barcelona (BCN)" or "Barbados (BGI)".

#### Parameter Completion

Dynamic resources support parameter completion. For example:

  * Typing "Par" as input for `weather://forecast/{city}` might suggest "Paris" or "Park City"
  * Typing "JFK" for `flights://search/{airport}` might suggest "JFK - John F. Kennedy International"



The system helps discover valid values without requiring exact format knowledge.

#### User Interaction Model

Resources are application-driven, giving them flexibility in how they retrieve, process, and present available context. Common interaction patterns include:

  * Tree or list views for browsing resources in familiar folder-like structures
  * Search and filter interfaces for finding specific resources
  * Automatic context inclusion or smart suggestions based on heuristics or AI selection
  * Manual or bulk selection interfaces for including single or multiple resources



Applications are free to implement resource discovery through any interface pattern that suits their needs. The protocol doesn't mandate specific UI patterns, allowing for resource pickers with preview capabilities, smart suggestions based on current conversation context, bulk selection for including multiple resources, or integration with existing file browsers and data explorers.

### Prompts

Prompts provide reusable templates. They allow MCP server authors to provide parameterized prompts for a domain, or showcase how to best use the MCP server.

#### How Prompts Work

Prompts are structured templates that define expected inputs and interaction patterns. They are user-controlled, requiring explicit invocation rather than automatic triggering. Prompts can be context-aware, referencing available resources and tools to create comprehensive workflows. Similar to resources, prompts support parameter completion to help users discover valid argument values.

**Protocol operations:**

Method| Purpose| Returns  
---|---|---  
`prompts/list`| Discover available prompts| Array of prompt descriptors  
`prompts/get`| Retrieve prompt details| Full prompt definition with arguments  
  
#### Example: Streamlined Workflows

Prompts provide structured templates for common tasks. In the travel planning context:

**" Plan a vacation" prompt:**
    
    
    {
      "name": "plan-vacation",
      "title": "Plan a vacation",
      "description": "Guide through vacation planning process",
      "arguments": [
        { "name": "destination", "type": "string", "required": true },
        { "name": "duration", "type": "number", "description": "days" },
        { "name": "budget", "type": "number", "required": false },
        { "name": "interests", "type": "array", "items": { "type": "string" } }
      ]
    }

Rather than unstructured natural language input, the prompt system enables:

  1. Selection of the "Plan a vacation" template
  2. Structured input: Barcelona, 7 days, $3000, ["beaches", "architecture", "food"]
  3. Consistent workflow execution based on the template



#### User Interaction Model

Prompts are user-controlled, requiring explicit invocation. The protocol gives implementers freedom to design interfaces that feel natural within their application. Key principles include:

  * Easy discovery of available prompts
  * Clear descriptions of what each prompt does
  * Natural argument input with validation
  * Transparent display of the prompt's underlying template



Applications typically expose prompts through various UI patterns such as:

  * Slash commands (typing "/" to see available prompts like /plan-vacation)
  * Command palettes for searchable access
  * Dedicated UI buttons for frequently used prompts
  * Context menus that suggest relevant prompts



## Bringing Servers Together

The real power of MCP emerges when multiple servers work together, combining their specialized capabilities through a unified interface.

### Example: Multi-Server Travel Planning

Consider a personalized AI travel planner application, with three connected servers:

  * **Travel Server** \- Handles flights, hotels, and itineraries
  * **Weather Server** \- Provides climate data and forecasts
  * **Calendar/Email Server** \- Manages schedules and communications



#### The Complete Flow

  1. **User invokes a prompt with parameters:**
         
         {
           "prompt": "plan-vacation",
           "arguments": {
             "destination": "Barcelona",
             "departure_date": "2024-06-15",
             "return_date": "2024-06-22",
             "budget": 3000,
             "travelers": 2
           }
         }

  2. **User selects resources to include:**

     * `calendar://my-calendar/June-2024` (from Calendar Server)
     * `travel://preferences/europe` (from Travel Server)
     * `travel://past-trips/Spain-2023` (from Travel Server)
  3. **AI processes the request using tools:**

The AI first reads all selected resources to gather context - identifying available dates from the calendar, learning preferred airlines and hotel types from travel preferences, and discovering previously enjoyed locations from past trips.

Using this context, the AI then executes the prompt provided by the AI application. In our example, the AI application exposes the weather tools from the connected MCP weather server to the model. Because weather can affect travel plans, the AI chooses to call `checkWeather()` when interpreting the prompt.

As a result the AI executes a series of tools:

     * `searchFlights()` \- Queries airlines for NYC to Barcelona flights
     * `checkWeather()` \- Retrieves climate forecasts for travel dates

The AI then uses this information to create the booking and following steps, requesting approval from the user where necessary:

     * `bookHotel()` \- Finds hotels within the specified budget
     * `createCalendarEvent()` \- Adds the trip to the user's calendar
     * `sendEmail()` \- Sends confirmation with trip details



**The result:** Through multiple MCP servers, the user researched and booked a Barcelona trip tailored to their schedule. The "Plan a Vacation" prompt guided the AI to combine Resources (calendar availability and travel history) with Tools (searching flights, booking hotels, updating calendars) across different servers—gathering context and executing the booking. A task that could have taken hours was completed in minutes using MCP.

[Understanding MCP clients](https://modelcontextprotocol.info/docs/2026-07-28/learn/client-concepts/ "Understanding MCP clients")[What is the Model Context Protocol (MCP)?](https://modelcontextprotocol.info/docs/2026-07-28/getting-started/intro/ "What is the Model Context Protocol \(MCP\)?")

[About](https://modelcontextprotocol.info/about/)[Privacy](https://modelcontextprotocol.info/privacy/)[Contact](https://modelcontextprotocol.info/contact/)[Official Sources](https://modelcontextprotocol.info/docs/#official-sources)

[Model Context Protocol Hub ](https://modelcontextprotocol.info "Model Context Protocol")[MCP 中文站 ](https://mcpcn.com "MCP 中文社区")[A2A Protocol ](https://a2acn.com "A2A Protocol Community")[AP2 Lab ](https://ap2lab.com "Agent Payments Protocol Community")[ACP Protocol ](https://acplib.com "Agentic Commerce Protocol Community")[Agent2Agent 文档 ](https://agent2agent.info "Agent2Agent Protocol")[AI to Sora ](https://aitosora.com "AI to Sora")[ChatGPT 中文 ](https://chatgptcn.com "ChatGPT 中文社区")[UCP 技术 ](https://ucp.md "UCP 技术站")[Clawd Bot ](https://clawdbot.sh/ "Clawd Bot 技术站")[moltBot Lab ](https://OpenClawLab.com/ "OpenClaw 技术站")[DSHx Community ](https://dshx.dev "DeepSeek Harness Developer Community")[DSH Plugins](https://plugin.dshx.dev "DeepSeek Harness Plugin Directory")

[Powered by ModelContextProtocol](https://github.com/imfing/hextra "Hextra GitHub Homepage")

© 2024 ModelContextProtocol.Info.
