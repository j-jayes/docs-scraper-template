# AgentConfig

  


The config for the YAML schema to create an agent.

##  Any of

  * LlmAgentConfig
  * LoopAgentConfig
  * ParallelAgentConfig
  * SequentialAgentConfig
  * BaseAgentConfig



root  anyOf LlmAgentConfig

#### LlmAgentConfig

Type: object  


The config for the YAML schema of a LlmAgent.

No Additional Properties

##  agent_class

root  anyOf LlmAgentConfig agent_class

#### Agent Class

Type: enum (of string) Default: "LlmAgent"  


The value is used to uniquely identify the LlmAgent class. If it is empty, it is by default an LlmAgent.

#### Must be one of:

  * "LlmAgent"
  * ""



##  name Required

root  anyOf LlmAgentConfig name

#### Name

Type: string  


Required. The name of the agent.

##  description

root  anyOf LlmAgentConfig description

#### Description

Type: string Default: ""  


Optional. The description of the agent.

##  sub_agents

root  anyOf LlmAgentConfig sub_agents

#### Sub Agents

Default: null  


Optional. The sub-agents of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig sub_agents anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig sub_agents anyOf item 0 AgentRefConfig

#### AgentRefConfig

Type: object  


The config for the reference to another agent.

No Additional Properties

##  config_path

root  anyOf LlmAgentConfig sub_agents anyOf item 0 AgentRefConfig config_path

#### Config Path

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig sub_agents anyOf item 0 AgentRefConfig config_path anyOf item 0

Type: string  


root  anyOf LlmAgentConfig sub_agents anyOf item 0 AgentRefConfig config_path anyOf item 1

Type: null  


##  code

root  anyOf LlmAgentConfig sub_agents anyOf item 0 AgentRefConfig code

#### Code

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig sub_agents anyOf item 0 AgentRefConfig code anyOf item 0

Type: string  


root  anyOf LlmAgentConfig sub_agents anyOf item 0 AgentRefConfig code anyOf item 1

Type: null  


root  anyOf LlmAgentConfig sub_agents anyOf item 1

Type: null  


##  before_agent_callbacks

root  anyOf LlmAgentConfig before_agent_callbacks

#### Before Agent Callbacks

Default: null  


Optional. The before _agent_ callbacks of the agent.

Example:  

    
    
    before_agent_callbacks:
      - name: my_library.security_callbacks.before_agent_callback  
    
      

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

No Additional Properties

##  name Required

root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig name

#### Name

Type: string  


##  args

root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig args

#### Args

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig args anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig args anyOf item 0 ArgumentConfig

#### ArgumentConfig

Type: object  


An argument passed to a function or a class's constructor.

No Additional Properties

##  name

root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig args anyOf item 0 ArgumentConfig name

#### Name

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig args anyOf item 0 ArgumentConfig name anyOf item 0

Type: string  


root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig args anyOf item 0 ArgumentConfig name anyOf item 1

Type: null  


##  value Required

root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig args anyOf item 0 ArgumentConfig value

#### Value

Type: object  


root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 0 CodeConfig args anyOf item 1

Type: null  


root  anyOf LlmAgentConfig before_agent_callbacks anyOf item 1

Type: null  


##  after_agent_callbacks

root  anyOf LlmAgentConfig after_agent_callbacks

#### After Agent Callbacks

Default: null  


Optional. The after _agent_ callbacks of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig after_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig after_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf LlmAgentConfig after_agent_callbacks anyOf item 1

Type: null  


##  model

root  anyOf LlmAgentConfig model

#### Model

Default: null  


Optional. LlmAgent.model. If not set, the model will be inherited from the ancestor.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig model anyOf item 0

Type: string  


root  anyOf LlmAgentConfig model anyOf item 1

Type: null  


##  instruction Required

root  anyOf LlmAgentConfig instruction

#### Instruction

Type: string  


Required. LlmAgent.instruction.

##  disallow_transfer_to_parent

root  anyOf LlmAgentConfig disallow_transfer_to_parent

#### Disallow Transfer To Parent

Default: null  


Optional. LlmAgent.disallow _transfer_ to_parent.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig disallow_transfer_to_parent anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig disallow_transfer_to_parent anyOf item 1

Type: null  


##  disallow_transfer_to_peers

root  anyOf LlmAgentConfig disallow_transfer_to_peers

#### Disallow Transfer To Peers

Default: null  


Optional. LlmAgent.disallow _transfer_ to_peers.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig disallow_transfer_to_peers anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig disallow_transfer_to_peers anyOf item 1

Type: null  


##  input_schema

root  anyOf LlmAgentConfig input_schema

Default: null  


Optional. LlmAgent.input_schema.

##  Any of

  * CodeConfig
  * Option 2



root  anyOf LlmAgentConfig input_schema anyOf CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf LlmAgentConfig input_schema anyOf item 1

Type: null  


##  output_schema

root  anyOf LlmAgentConfig output_schema

Default: null  


Optional. LlmAgent.output_schema.

##  Any of

  * CodeConfig
  * Option 2



root  anyOf LlmAgentConfig output_schema anyOf CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf LlmAgentConfig output_schema anyOf item 1

Type: null  


##  output_key

root  anyOf LlmAgentConfig output_key

#### Output Key

Default: null  


Optional. LlmAgent.output_key.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig output_key anyOf item 0

Type: string  


root  anyOf LlmAgentConfig output_key anyOf item 1

Type: null  


##  include_contents

root  anyOf LlmAgentConfig include_contents

#### Include Contents

Type: enum (of string) Default: "default"  


Optional. LlmAgent.include_contents.

#### Must be one of:

  * "default"
  * "none"



##  tools

root  anyOf LlmAgentConfig tools

#### Tools

Default: null  


Optional. LlmAgent.tools.

Examples:

For ADK built-in tools in `google.adk.tools` package, they can be referenced  
directly with the name:  

    
    
    tools:
      - name: google_search
      - name: load_memory  
    
        

For user-defined tools, they can be referenced with fully qualified name:  

    
    
    tools:
      - name: my_library.my_tools.my_tool  
    
        

For tools that needs to be created via functions:  

    
    
    tools:
      - name: my_library.my_tools.create_tool
        args:
          - name: param1
            value: value1
          - name: param2
            value: value2  
    
        

For more advanced tools, instead of specifying arguments in config, it's  
recommended to define them in Python files and reference them. E.g.,  

    
    
    # tools.py
    my_mcp_toolset = MCPToolset(
        connection_params=StdioServerParameters(
            command="npx",
            args=["-y", "@notionhq/notion-mcp-server"],
            env={"OPENAPI_MCP_HEADERS": NOTION_HEADERS},
        )
    )  
    
        

Then, reference the toolset in config:  

    
    
    tools:
      - name: tools.my_mcp_toolset  
    
      

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig tools anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig tools anyOf item 0 ToolConfig

#### ToolConfig

Type: object  


The configuration for a tool.

The config supports these types of tools:  
1\. ADK built-in tools  
2\. User-defined tool instances  
3\. User-defined tool classes  
4\. User-defined functions that generate tool instances  
5\. User-defined function tools

For examples:

  1. For ADK built-in tool instances or classes in `google.adk.tools` package,  
they can be referenced directly with the `name` and optionally with  
`args`.
         
         tools:
           - name: google_search
           - name: AgentTool
             args:
               agent: ./another_agent.yaml
               skip_summarization: true
         

  2. For user-defined tool instances, the `name` is the fully qualified path  
to the tool instance.
         
         tools:
           - name: my_package.my_module.my_tool
         

  3. For user-defined tool classes (custom tools), the `name` is the fully  
qualified path to the tool class and `args` is the arguments for the tool.
         
         tools:
           - name: my_package.my_module.my_tool_class
             args:
               my_tool_arg1: value1
               my_tool_arg2: value2
         

  4. For user-defined functions that generate tool instances, the `name` is  
the fully qualified path to the function and `args` is passed to the  
function as arguments.
         
         tools:
           - name: my_package.my_module.my_tool_function
             args:
               my_function_arg1: value1
               my_function_arg2: value2
         

The function must have the following signature:
         
         def my_function(args: ToolArgsConfig) -> BaseTool:
           ...
         

  5. For user-defined function tools, the `name` is the fully qualified path  
to the function.
         
         tools:
           - name: my_package.my_module.my_function_tool
         

If the above use cases don't suffice, users can define a custom tool config  
by extending BaseToolConfig and override from_config() in the custom tool.




No Additional Properties

##  name Required

root  anyOf LlmAgentConfig tools anyOf item 0 ToolConfig name

#### Name

Type: string  


The name of the tool.

For ADK built-in tools, `name` is the name of the tool, e.g. `google_search`  
or `AgentTool`.

For user-defined tools, the name is the fully qualified path to the tool, e.g.  
`my_package.my_module.my_tool`.

##  args

root  anyOf LlmAgentConfig tools anyOf item 0 ToolConfig args

Default: null  


The args for the tool.

##  Any of

  * ToolArgsConfig
  * Option 2



root  anyOf LlmAgentConfig tools anyOf item 0 ToolConfig args anyOf ToolArgsConfig

#### ToolArgsConfig

Type: object  


Config to host free key-value pairs for the args in ToolConfig.

##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig tools anyOf item 0 ToolConfig args anyOf ToolArgsConfig additionalProperties

Type: object  


root  anyOf LlmAgentConfig tools anyOf item 0 ToolConfig args anyOf item 1

Type: null  


root  anyOf LlmAgentConfig tools anyOf item 1

Type: null  


##  before_model_callbacks

root  anyOf LlmAgentConfig before_model_callbacks

#### Before Model Callbacks

Default: null  


Optional. LlmAgent.before _model_ callbacks.

Example:  

    
    
    before_model_callbacks:
      - name: my_library.callbacks.before_model_callback  
    
      

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig before_model_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig before_model_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf LlmAgentConfig before_model_callbacks anyOf item 1

Type: null  


##  after_model_callbacks

root  anyOf LlmAgentConfig after_model_callbacks

#### After Model Callbacks

Default: null  


Optional. LlmAgent.after _model_ callbacks.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig after_model_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig after_model_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf LlmAgentConfig after_model_callbacks anyOf item 1

Type: null  


##  before_tool_callbacks

root  anyOf LlmAgentConfig before_tool_callbacks

#### Before Tool Callbacks

Default: null  


Optional. LlmAgent.before _tool_ callbacks.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig before_tool_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig before_tool_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf LlmAgentConfig before_tool_callbacks anyOf item 1

Type: null  


##  after_tool_callbacks

root  anyOf LlmAgentConfig after_tool_callbacks

#### After Tool Callbacks

Default: null  


Optional. LlmAgent.after _tool_ callbacks.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig after_tool_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig after_tool_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf LlmAgentConfig after_tool_callbacks anyOf item 1

Type: null  


##  generate_content_config

root  anyOf LlmAgentConfig generate_content_config

Default: null  


Optional. LlmAgent.generate _content_ config.

##  Any of

  * GenerateContentConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig

#### GenerateContentConfig

Type: object  


Optional model configuration parameters.

For more information, see `Content generation parameters <https://cloud.google.com/vertex-ai/generative-ai/docs/multimodal/content-generation-parameters>`_.

No Additional Properties

##  httpOptions

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions

Default: null  


Used to override HTTP request options.

##  Any of

  * HttpOptions
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions

#### HttpOptions

Type: object  


HTTP options to be used in each of the requests.

No Additional Properties

##  baseUrl

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions baseUrl

#### Baseurl

Default: null  


The base URL for the AI platform service endpoint.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions baseUrl anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions baseUrl anyOf item 1

Type: null  


##  apiVersion

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions apiVersion

#### Apiversion

Default: null  


Specifies the version of the API to use.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions apiVersion anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions apiVersion anyOf item 1

Type: null  


##  headers

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions headers

#### Headers

Default: null  


Additional HTTP headers to be sent with the request.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions headers anyOf item 0

Type: object  


##  _Additional Properties_

Each additional property must conform to the following schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions headers anyOf item 0 additionalProperties

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions headers anyOf item 1

Type: null  


##  timeout

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions timeout

#### Timeout

Default: null  


Timeout for the request in milliseconds.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions timeout anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions timeout anyOf item 1

Type: null  


##  clientArgs

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions clientArgs

#### Clientargs

Default: null  


Args passed to the HTTP client.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions clientArgs anyOf item 0

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions clientArgs anyOf item 0 additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions clientArgs anyOf item 1

Type: null  


##  asyncClientArgs

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions asyncClientArgs

#### Asyncclientargs

Default: null  


Args passed to the async HTTP client.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions asyncClientArgs anyOf item 0

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions asyncClientArgs anyOf item 0 additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions asyncClientArgs anyOf item 1

Type: null  


##  extraBody

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions extraBody

#### Extrabody

Default: null  


Extra parameters to add to the request body.  
The structure must match the backend API's request structure.  
\- VertexAI backend API docs: https://cloud.google.com/vertex-ai/docs/reference/rest  
\- GeminiAPI backend API docs: https://ai.google.dev/api/rest

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions extraBody anyOf item 0

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions extraBody anyOf item 0 additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions extraBody anyOf item 1

Type: null  


##  retryOptions

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions

Default: null  


HTTP retry options for the request.

##  Any of

  * HttpRetryOptions
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions

#### HttpRetryOptions

Type: object  


HTTP retry options to be used in each of the requests.

No Additional Properties

##  attempts

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions attempts

#### Attempts

Default: null  


Maximum number of attempts, including the original request.  
If 0 or 1, it means no retries.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions attempts anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions attempts anyOf item 1

Type: null  


##  initialDelay

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions initialDelay

#### Initialdelay

Default: null  


Initial delay before the first retry, in fractions of a second.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions initialDelay anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions initialDelay anyOf item 1

Type: null  


##  maxDelay

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions maxDelay

#### Maxdelay

Default: null  


Maximum delay between retries, in fractions of a second.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions maxDelay anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions maxDelay anyOf item 1

Type: null  


##  expBase

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions expBase

#### Expbase

Default: null  


Multiplier by which the delay increases after each attempt.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions expBase anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions expBase anyOf item 1

Type: null  


##  jitter

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions jitter

#### Jitter

Default: null  


Randomness factor for the delay.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions jitter anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions jitter anyOf item 1

Type: null  


##  httpStatusCodes

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions httpStatusCodes

#### Httpstatuscodes

Default: null  


List of HTTP status codes that should trigger a retry.  
If not specified, a default set of retryable codes may be used.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions httpStatusCodes anyOf item 0

Type: array of integer  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions httpStatusCodes anyOf item 0 item 0 items

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf HttpRetryOptions httpStatusCodes anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf HttpOptions retryOptions anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig httpOptions anyOf item 1

Type: null  


##  systemInstruction

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction

#### Systeminstruction

Default: null  


Instructions for the model to steer it toward better performance.  
For example, "Answer as concisely as possible" or "Don't use technical  
terms in your response".

##  Any of

  * Content
  * Option 2
  * File
  * Part
  * Option 5
  * Option 6



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content

#### Content

Type: object  


Contains the multi-part content of a message.

No Additional Properties

##  parts

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts

#### Parts

Default: null  


List of parts that constitute a single message. Each part may have  
a different IANA MIME type.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part

#### Part

Type: object  


A datatype containing media content.

Exactly one field within a Part should be set, representing the specific type  
of content being conveyed. Using multiple fields within the same `Part`  
instance is considered invalid.

No Additional Properties

##  videoMetadata

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata

Default: null  


Metadata for a given video.

##  Any of

  * VideoMetadata
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata

#### VideoMetadata

Type: object  


Describes how the video in the Part should be used by the model.

No Additional Properties

##  fps

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata fps

#### Fps

Default: null  


The frame rate of the video sent to the model. If not specified, the  
default value will be 1.0. The fps range is (0.0, 24.0].

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata fps anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata fps anyOf item 1

Type: null  


##  endOffset

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata endOffset

#### Endoffset

Default: null  


Optional. The end offset of the video.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata endOffset anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata endOffset anyOf item 1

Type: null  


##  startOffset

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata startOffset

#### Startoffset

Default: null  


Optional. The start offset of the video.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata startOffset anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf VideoMetadata startOffset anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part videoMetadata anyOf item 1

Type: null  


##  thought

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part thought

#### Thought

Default: null  


Indicates if the part is thought from the model.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part thought anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part thought anyOf item 1

Type: null  


##  inlineData

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData

Default: null  


Optional. Inlined bytes data.

##  Any of

  * Blob
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob

#### Blob

Type: object  


Content blob.

No Additional Properties

##  displayName

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob displayName

#### Displayname

Default: null  


Optional. Display name of the blob. Used to provide a label or filename to distinguish blobs. This field is not currently used in the Gemini GenerateContent calls.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob displayName anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob displayName anyOf item 1

Type: null  


##  data

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob data

#### Data

Default: null  


Required. Raw bytes.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob data anyOf item 0

Type: stringFormat: base64url  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob data anyOf item 1

Type: null  


##  mimeType

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob mimeType

#### Mimetype

Default: null  


Required. The IANA standard MIME type of the source data.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob mimeType anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf Blob mimeType anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part inlineData anyOf item 1

Type: null  


##  fileData

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData

Default: null  


Optional. URI based data.

##  Any of

  * FileData
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData

#### FileData

Type: object  


URI based data.

No Additional Properties

##  displayName

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData displayName

#### Displayname

Default: null  


Optional. Display name of the file data. Used to provide a label or filename to distinguish file datas. It is not currently used in the Gemini GenerateContent calls.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData displayName anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData displayName anyOf item 1

Type: null  


##  fileUri

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData fileUri

#### Fileuri

Default: null  


Required. URI.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData fileUri anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData fileUri anyOf item 1

Type: null  


##  mimeType

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData mimeType

#### Mimetype

Default: null  


Required. The IANA standard MIME type of the source data.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData mimeType anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf FileData mimeType anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part fileData anyOf item 1

Type: null  


##  thoughtSignature

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part thoughtSignature

#### Thoughtsignature

Default: null  


An opaque signature for the thought so it can be reused in subsequent requests.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part thoughtSignature anyOf item 0

Type: stringFormat: base64url  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part thoughtSignature anyOf item 1

Type: null  


##  codeExecutionResult

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part codeExecutionResult

Default: null  


Optional. Result of executing the [ExecutableCode].

##  Any of

  * CodeExecutionResult
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part codeExecutionResult anyOf CodeExecutionResult

#### CodeExecutionResult

Type: object  


Result of executing the [ExecutableCode].

Only generated when using the [CodeExecution] tool, and always follows a  
`part` containing the [ExecutableCode].

No Additional Properties

##  outcome

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part codeExecutionResult anyOf CodeExecutionResult outcome

Default: null  


Required. Outcome of the code execution.

##  Any of

  * Outcome
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part codeExecutionResult anyOf CodeExecutionResult outcome anyOf Outcome

#### Outcome

Type: enum (of string)  


Required. Outcome of the code execution.

#### Must be one of:

  * "OUTCOME_UNSPECIFIED"
  * "OUTCOME_OK"
  * "OUTCOME_FAILED"
  * "OUTCOME_DEADLINE_EXCEEDED"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part codeExecutionResult anyOf CodeExecutionResult outcome anyOf item 1

Type: null  


##  output

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part codeExecutionResult anyOf CodeExecutionResult output

#### Output

Default: null  


Optional. Contains stdout when code execution is successful, stderr or other description otherwise.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part codeExecutionResult anyOf CodeExecutionResult output anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part codeExecutionResult anyOf CodeExecutionResult output anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part codeExecutionResult anyOf item 1

Type: null  


##  executableCode

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part executableCode

Default: null  


Optional. Code generated by the model that is meant to be executed.

##  Any of

  * ExecutableCode
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part executableCode anyOf ExecutableCode

#### ExecutableCode

Type: object  


Code generated by the model that is meant to be executed, and the result returned to the model.

Generated when using the [CodeExecution] tool, in which the code will be  
automatically executed, and a corresponding [CodeExecutionResult] will also be  
generated.

No Additional Properties

##  code

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part executableCode anyOf ExecutableCode code

#### Code

Default: null  


Required. The code to be executed.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part executableCode anyOf ExecutableCode code anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part executableCode anyOf ExecutableCode code anyOf item 1

Type: null  


##  language

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part executableCode anyOf ExecutableCode language

Default: null  


Required. Programming language of the `code`.

##  Any of

  * Language
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part executableCode anyOf ExecutableCode language anyOf Language

#### Language

Type: enum (of string)  


Required. Programming language of the `code`.

#### Must be one of:

  * "LANGUAGE_UNSPECIFIED"
  * "PYTHON"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part executableCode anyOf ExecutableCode language anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part executableCode anyOf item 1

Type: null  


##  functionCall

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall

Default: null  


Optional. A predicted [FunctionCall] returned from the model that contains a string representing the [FunctionDeclaration.name] with the parameters and their values.

##  Any of

  * FunctionCall
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall

#### FunctionCall

Type: object  


A function call.

No Additional Properties

##  id

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall id

#### Id

Default: null  


The unique id of the function call. If populated, the client to execute the  
`function_call` and return the response with the matching `id`.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall id anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall id anyOf item 1

Type: null  


##  args

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall args

#### Args

Default: null  


Optional. The function parameters and values in JSON object format. See [FunctionDeclaration.parameters] for parameter details.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall args anyOf item 0

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall args anyOf item 0 additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall args anyOf item 1

Type: null  


##  name

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall name

#### Name

Default: null  


Required. The name of the function to call. Matches [FunctionDeclaration.name].

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall name anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf FunctionCall name anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionCall anyOf item 1

Type: null  


##  functionResponse

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse

Default: null  


Optional. The result output of a [FunctionCall] that contains a string representing the [FunctionDeclaration.name] and a structured JSON object containing any output from the function call. It is used as context to the model.

##  Any of

  * FunctionResponse
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse

#### FunctionResponse

Type: object  


A function response.

No Additional Properties

##  willContinue

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse willContinue

#### Willcontinue

Default: null  


Signals that function call continues, and more responses will be returned, turning the function call into a generator. Is only applicable to NON _BLOCKING function calls (see FunctionDeclaration.behavior for details), ignored otherwise. If false, the default, future responses will not be considered. Is only applicable to NON_ BLOCKING function calls, is ignored otherwise. If set to false, future responses will not be considered. It is allowed to return empty `response` with `will_continue=False` to signal that the function call is finished.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse willContinue anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse willContinue anyOf item 1

Type: null  


##  scheduling

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse scheduling

Default: null  


Specifies how the response should be scheduled in the conversation. Only applicable to NON _BLOCKING function calls, is ignored otherwise. Defaults to WHEN_ IDLE.

##  Any of

  * FunctionResponseScheduling
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse scheduling anyOf FunctionResponseScheduling

#### FunctionResponseScheduling

Type: enum (of string)  


Specifies how the response should be scheduled in the conversation.

#### Must be one of:

  * "SCHEDULING_UNSPECIFIED"
  * "SILENT"
  * "WHEN_IDLE"
  * "INTERRUPT"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse scheduling anyOf item 1

Type: null  


##  id

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse id

#### Id

Default: null  


Optional. The id of the function call this response is for. Populated by the client to match the corresponding function call `id`.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse id anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse id anyOf item 1

Type: null  


##  name

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse name

#### Name

Default: null  


Required. The name of the function to call. Matches [FunctionDeclaration.name] and [FunctionCall.name].

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse name anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse name anyOf item 1

Type: null  


##  response

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse response

#### Response

Default: null  


Required. The function response in JSON object format. Use "output" key to specify function output and "error" key to specify error details (if any). If "output" and "error" keys are not specified, then whole "response" is treated as function output.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse response anyOf item 0

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse response anyOf item 0 additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf FunctionResponse response anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part functionResponse anyOf item 1

Type: null  


##  text

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part text

#### Text

Default: null  


Optional. Text part (can be code).

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part text anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 0 Part text anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content parts anyOf item 1

Type: null  


##  role

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content role

#### Role

Default: null  


Optional. The producer of the content. Must be either 'user' or  
'model'. Useful to set for multi-turn conversations, otherwise can be  
empty. If role is not specified, SDK will determine the role.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content role anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Content role anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items

  


##  Any of

  * File
  * Part
  * Option 3



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File

#### File

Type: object  


A file uploaded to the API.

No Additional Properties

##  name

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File name

#### Name

Default: null  


The `File` resource name. The ID (name excluding the "files/" prefix) can contain up to 40 characters that are lowercase alphanumeric or dashes (-). The ID cannot start or end with a dash. If the name is empty on create, a unique name will be generated. Example: `files/123-456`

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File name anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File name anyOf item 1

Type: null  


##  displayName

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File displayName

#### Displayname

Default: null  


Optional. The human-readable display name for the `File`. The display name must be no more than 512 characters in length, including spaces. Example: 'Welcome Image'

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File displayName anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File displayName anyOf item 1

Type: null  


##  mimeType

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File mimeType

#### Mimetype

Default: null  


Output only. MIME type of the file.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File mimeType anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File mimeType anyOf item 1

Type: null  


##  sizeBytes

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File sizeBytes

#### Sizebytes

Default: null  


Output only. Size of the file in bytes.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File sizeBytes anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File sizeBytes anyOf item 1

Type: null  


##  createTime

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File createTime

#### Createtime

Default: null  


Output only. The timestamp of when the `File` was created.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File createTime anyOf item 0

Type: stringFormat: date-time  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File createTime anyOf item 1

Type: null  


##  expirationTime

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File expirationTime

#### Expirationtime

Default: null  


Output only. The timestamp of when the `File` will be deleted. Only set if the `File` is scheduled to expire.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File expirationTime anyOf item 0

Type: stringFormat: date-time  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File expirationTime anyOf item 1

Type: null  


##  updateTime

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File updateTime

#### Updatetime

Default: null  


Output only. The timestamp of when the `File` was last updated.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File updateTime anyOf item 0

Type: stringFormat: date-time  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File updateTime anyOf item 1

Type: null  


##  sha256Hash

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File sha256Hash

#### Sha256Hash

Default: null  


Output only. SHA-256 hash of the uploaded bytes. The hash value is encoded in base64 format.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File sha256Hash anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File sha256Hash anyOf item 1

Type: null  


##  uri

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File uri

#### Uri

Default: null  


Output only. The URI of the `File`.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File uri anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File uri anyOf item 1

Type: null  


##  downloadUri

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File downloadUri

#### Downloaduri

Default: null  


Output only. The URI of the `File`, only set for downloadable (generated) files.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File downloadUri anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File downloadUri anyOf item 1

Type: null  


##  state

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File state

Default: null  


Output only. Processing state of the File.

##  Any of

  * FileState
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File state anyOf FileState

#### FileState

Type: enum (of string)  


State for the lifecycle of a File.

#### Must be one of:

  * "STATE_UNSPECIFIED"
  * "PROCESSING"
  * "ACTIVE"
  * "FAILED"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File state anyOf item 1

Type: null  


##  source

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File source

Default: null  


Output only. The source of the `File`.

##  Any of

  * FileSource
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File source anyOf FileSource

#### FileSource

Type: enum (of string)  


Source of the File.

#### Must be one of:

  * "SOURCE_UNSPECIFIED"
  * "UPLOADED"
  * "GENERATED"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File source anyOf item 1

Type: null  


##  videoMetadata

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File videoMetadata

#### Videometadata

Default: null  


Output only. Metadata for a video.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File videoMetadata anyOf item 0

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File videoMetadata anyOf item 0 additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File videoMetadata anyOf item 1

Type: null  


##  error

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error

Default: null  


Output only. Error status if File processing failed.

##  Any of

  * FileStatus
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus

#### FileStatus

Type: object  


Status of a File that uses a common error model.

No Additional Properties

##  details

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus details

#### Details

Default: null  


A list of messages that carry the error details. There is a common set of message types for APIs to use.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus details anyOf item 0

Type: array of object  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus details anyOf item 0 item 0 items

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus details anyOf item 0 item 0 items additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus details anyOf item 1

Type: null  


##  message

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus message

#### Message

Default: null  


A list of messages that carry the error details. There is a common set of message types for APIs to use.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus message anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus message anyOf item 1

Type: null  


##  code

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus code

#### Code

Default: null  


The status code. 0 for OK, 1 for CANCELLED

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus code anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf FileStatus code anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf File error anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf Part

#### Part

Type: object  


A datatype containing media content.

Exactly one field within a Part should be set, representing the specific type  
of content being conveyed. Using multiple fields within the same `Part`  
instance is considered invalid.

Same definition as Part

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 1 item 1 items anyOf item 2

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf File

#### File

Type: object  


A file uploaded to the API.

Same definition as File

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf Part

#### Part

Type: object  


A datatype containing media content.

Exactly one field within a Part should be set, representing the specific type  
of content being conveyed. Using multiple fields within the same `Part`  
instance is considered invalid.

Same definition as Part

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 4

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig systemInstruction anyOf item 5

Type: null  


##  temperature

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig temperature

#### Temperature

Default: null  


Value that controls the degree of randomness in token selection.  
Lower temperatures are good for prompts that require a less open-ended or  
creative response, while higher temperatures can lead to more diverse or  
creative results.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig temperature anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig temperature anyOf item 1

Type: null  


##  topP

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig topP

#### Topp

Default: null  


Tokens are selected from the most to least probable until the sum  
of their probabilities equals this value. Use a lower value for less  
random responses and a higher value for more random responses.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig topP anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig topP anyOf item 1

Type: null  


##  topK

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig topK

#### Topk

Default: null  


For each token selection step, the `top_k` tokens with the  
highest probabilities are sampled. Then tokens are further filtered based  
on `top_p` with the final token selected using temperature sampling. Use  
a lower number for less random responses and a higher number for more  
random responses.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig topK anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig topK anyOf item 1

Type: null  


##  candidateCount

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig candidateCount

#### Candidatecount

Default: null  


Number of response variations to return.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig candidateCount anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig candidateCount anyOf item 1

Type: null  


##  maxOutputTokens

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig maxOutputTokens

#### Maxoutputtokens

Default: null  


Maximum number of tokens that can be generated in the response.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig maxOutputTokens anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig maxOutputTokens anyOf item 1

Type: null  


##  stopSequences

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig stopSequences

#### Stopsequences

Default: null  


List of strings that tells the model to stop generating text if one  
of the strings is encountered in the response.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig stopSequences anyOf item 0

Type: array of string  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig stopSequences anyOf item 0 item 0 items

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig stopSequences anyOf item 1

Type: null  


##  responseLogprobs

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseLogprobs

#### Responselogprobs

Default: null  


Whether to return the log probabilities of the tokens that were  
chosen by the model at each step.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseLogprobs anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseLogprobs anyOf item 1

Type: null  


##  logprobs

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig logprobs

#### Logprobs

Default: null  


Number of top candidate tokens to return the log probabilities for  
at each generation step.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig logprobs anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig logprobs anyOf item 1

Type: null  


##  presencePenalty

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig presencePenalty

#### Presencepenalty

Default: null  


Positive values penalize tokens that already appear in the  
generated text, increasing the probability of generating more diverse  
content.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig presencePenalty anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig presencePenalty anyOf item 1

Type: null  


##  frequencyPenalty

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig frequencyPenalty

#### Frequencypenalty

Default: null  


Positive values penalize tokens that repeatedly appear in the  
generated text, increasing the probability of generating more diverse  
content.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig frequencyPenalty anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig frequencyPenalty anyOf item 1

Type: null  


##  seed

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig seed

#### Seed

Default: null  


When `seed` is fixed to a specific number, the model makes a best  
effort to provide the same response for repeated requests. By default, a  
random number is used.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig seed anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig seed anyOf item 1

Type: null  


##  responseMimeType

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseMimeType

#### Responsemimetype

Default: null  


Output response mimetype of the generated candidate text.  
Supported mimetype:  
\- `text/plain`: (default) Text output.  
\- `application/json`: JSON response in the candidates.  
The model needs to be prompted to output the appropriate response type,  
otherwise the behavior is undefined.  
This is a preview feature.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseMimeType anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseMimeType anyOf item 1

Type: null  


##  responseSchema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema

#### Responseschema

Default: null  


The `Schema` object allows the definition of input and output data types.  
These types can be objects, but also primitives and arrays.  
Represents a select subset of an [OpenAPI 3.0 schema  
object](https://spec.openapis.org/oas/v3.0.3#schema).  
If set, a compatible response _mime_ type must also be set.  
Compatible mimetypes: `application/json`: Schema for JSON response.

##  Any of

  * Option 1
  * Schema
  * Option 3



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf item 0

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf item 0 additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema

#### Schema

Type: object  


Schema is used to define the format of input/output data.

Represents a select subset of an [OpenAPI 3.0 schema  
object](https://spec.openapis.org/oas/v3.0.3#schema-object). More fields may  
be added in the future as needed.

No Additional Properties

##  additionalProperties

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema additionalProperties

#### Additionalproperties

Default: null  


Optional. Can either be a boolean or an object; controls the presence of additional properties.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema additionalProperties anyOf item 0

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema additionalProperties anyOf item 1

Type: null  


##  defs

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema defs

#### Defs

Default: null  


Optional. A map of definitions for use by `ref` Only allowed at the root of the schema.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema defs anyOf item 0

Type: object  


##  _Additional Properties_

Each additional property must conform to the following schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema defs anyOf item 0 Schema

#### Schema

Type: object  


Schema is used to define the format of input/output data.

Represents a select subset of an [OpenAPI 3.0 schema  
object](https://spec.openapis.org/oas/v3.0.3#schema-object). More fields may  
be added in the future as needed.

Same definition as Schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema defs anyOf item 1

Type: null  


##  ref

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema ref

#### Ref

Default: null  


Optional. Allows indirect references between schema nodes. The value should be a valid reference to a child of the root `defs`. For example, the following schema defines a reference to a schema node named "Pet": type: object properties: pet: ref: #/defs/Pet defs: Pet: type: object properties: name: type: string The value of the "pet" property is a reference to the schema node named "Pet". See details in https://json-schema.org/understanding-json-schema/structuring

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema ref anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema ref anyOf item 1

Type: null  


##  anyOf

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema anyOf

#### Anyof

Default: null  


Optional. The value should be validated against any (one or more) of the subschemas in the list.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema anyOf anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema anyOf anyOf item 0 Schema

#### Schema

Type: object  


Schema is used to define the format of input/output data.

Represents a select subset of an [OpenAPI 3.0 schema  
object](https://spec.openapis.org/oas/v3.0.3#schema-object). More fields may  
be added in the future as needed.

Same definition as Schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema anyOf anyOf item 1

Type: null  


##  default

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema default

#### Default

Default: null  


Optional. Default value of the data.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema default anyOf item 0

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema default anyOf item 1

Type: null  


##  description

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema description

#### Description

Default: null  


Optional. The description of the data.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema description anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema description anyOf item 1

Type: null  


##  enum

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema enum

#### Enum

Default: null  


Optional. Possible values of the element of primitive type with enum format. Examples: 1. We can define direction as : {type:STRING, format:enum, enum:["EAST", NORTH", "SOUTH", "WEST"]} 2. We can define apartment number as : {type:INTEGER, format:enum, enum:["101", "201", "301"]}

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema enum anyOf item 0

Type: array of string  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema enum anyOf item 0 item 0 items

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema enum anyOf item 1

Type: null  


##  example

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema example

#### Example

Default: null  


Optional. Example of the object. Will only populated when the object is the root.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema example anyOf item 0

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema example anyOf item 1

Type: null  


##  format

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema format

#### Format

Default: null  


Optional. The format of the data. Supported formats: for NUMBER type: "float", "double" for INTEGER type: "int32", "int64" for STRING type: "email", "byte", etc

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema format anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema format anyOf item 1

Type: null  


##  items

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema items

Default: null  


Optional. SCHEMA FIELDS FOR TYPE ARRAY Schema of the elements of Type.ARRAY.

##  Any of

  * Schema
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema items anyOf Schema

#### Schema

Type: object  


Schema is used to define the format of input/output data.

Represents a select subset of an [OpenAPI 3.0 schema  
object](https://spec.openapis.org/oas/v3.0.3#schema-object). More fields may  
be added in the future as needed.

Same definition as Schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema items anyOf item 1

Type: null  


##  maxItems

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maxItems

#### Maxitems

Default: null  


Optional. Maximum number of the elements for Type.ARRAY.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maxItems anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maxItems anyOf item 1

Type: null  


##  maxLength

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maxLength

#### Maxlength

Default: null  


Optional. Maximum length of the Type.STRING

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maxLength anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maxLength anyOf item 1

Type: null  


##  maxProperties

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maxProperties

#### Maxproperties

Default: null  


Optional. Maximum number of the properties for Type.OBJECT.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maxProperties anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maxProperties anyOf item 1

Type: null  


##  maximum

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maximum

#### Maximum

Default: null  


Optional. Maximum value of the Type.INTEGER and Type.NUMBER

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maximum anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema maximum anyOf item 1

Type: null  


##  minItems

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minItems

#### Minitems

Default: null  


Optional. Minimum number of the elements for Type.ARRAY.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minItems anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minItems anyOf item 1

Type: null  


##  minLength

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minLength

#### Minlength

Default: null  


Optional. SCHEMA FIELDS FOR TYPE STRING Minimum length of the Type.STRING

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minLength anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minLength anyOf item 1

Type: null  


##  minProperties

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minProperties

#### Minproperties

Default: null  


Optional. Minimum number of the properties for Type.OBJECT.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minProperties anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minProperties anyOf item 1

Type: null  


##  minimum

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minimum

#### Minimum

Default: null  


Optional. SCHEMA FIELDS FOR TYPE INTEGER and NUMBER Minimum value of the Type.INTEGER and Type.NUMBER

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minimum anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema minimum anyOf item 1

Type: null  


##  nullable

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema nullable

#### Nullable

Default: null  


Optional. Indicates if the value may be null.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema nullable anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema nullable anyOf item 1

Type: null  


##  pattern

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema pattern

#### Pattern

Default: null  


Optional. Pattern of the Type.STRING to restrict a string to a regular expression.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema pattern anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema pattern anyOf item 1

Type: null  


##  properties

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema properties

#### Properties

Default: null  


Optional. SCHEMA FIELDS FOR TYPE OBJECT Properties of Type.OBJECT.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema properties anyOf item 0

Type: object  


##  _Additional Properties_

Each additional property must conform to the following schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema properties anyOf item 0 Schema

#### Schema

Type: object  


Schema is used to define the format of input/output data.

Represents a select subset of an [OpenAPI 3.0 schema  
object](https://spec.openapis.org/oas/v3.0.3#schema-object). More fields may  
be added in the future as needed.

Same definition as Schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema properties anyOf item 1

Type: null  


##  propertyOrdering

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema propertyOrdering

#### Propertyordering

Default: null  


Optional. The order of the properties. Not a standard field in open api spec. Only used to support the order of the properties.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema propertyOrdering anyOf item 0

Type: array of string  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema propertyOrdering anyOf item 0 item 0 items

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema propertyOrdering anyOf item 1

Type: null  


##  required

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema required

#### Required

Default: null  


Optional. Required properties of Type.OBJECT.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema required anyOf item 0

Type: array of string  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema required anyOf item 0 item 0 items

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema required anyOf item 1

Type: null  


##  title

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema title

#### Title

Default: null  


Optional. The title of the Schema.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema title anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema title anyOf item 1

Type: null  


##  type

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema type

Default: null  


Optional. The type of the data.

##  Any of

  * Type
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema type anyOf Type

#### Type

Type: enum (of string)  


Optional. The type of the data.

#### Must be one of:

  * "TYPE_UNSPECIFIED"
  * "STRING"
  * "NUMBER"
  * "INTEGER"
  * "BOOLEAN"
  * "ARRAY"
  * "OBJECT"
  * "NULL"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf Schema type anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseSchema anyOf item 2

Type: null  


##  responseJsonSchema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseJsonSchema

#### Responsejsonschema

Default: null  


Optional. Output schema of the generated response.  
This is an alternative to `response_schema` that accepts [JSON  
Schema](https://json-schema.org/). If set, `response_schema` must be  
omitted, but `response_mime_type` is required. While the full JSON Schema  
may be sent, not all features are supported. Specifically, only the  
following properties are supported: - `$id` \- `$defs` \- `$ref` \- `$anchor`  
\- `type` \- `format` \- `title` \- `description` \- `enum` (for strings and  
numbers) - `items` \- `prefixItems` \- `minItems` \- `maxItems` \- `minimum` -  
`maximum` \- `anyOf` \- `oneOf` (interpreted the same as `anyOf`) -  
`properties` \- `additionalProperties` \- `required` The non-standard  
`propertyOrdering` property may also be set. Cyclic references are  
unrolled to a limited degree and, as such, may only be used within  
non-required properties. (Nullable properties are not sufficient.) If  
`$ref` is set on a sub-schema, no other properties, except for than those  
starting as a `$`, may be set.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseJsonSchema anyOf item 0

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseJsonSchema anyOf item 1

Type: null  


##  routingConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig

Default: null  


Configuration for model router requests.

##  Any of

  * GenerationConfigRoutingConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig

#### GenerationConfigRoutingConfig

Type: object  


The configuration for routing the request to a specific model.

No Additional Properties

##  autoMode

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig autoMode

Default: null  


Automated routing.

##  Any of

  * GenerationConfigRoutingConfigAutoRoutingMode
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig autoMode anyOf GenerationConfigRoutingConfigAutoRoutingMode

#### GenerationConfigRoutingConfigAutoRoutingMode

Type: object  


When automated routing is specified, the routing will be determined by the pretrained routing model and customer provided model routing preference.

No Additional Properties

##  modelRoutingPreference

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig autoMode anyOf GenerationConfigRoutingConfigAutoRoutingMode modelRoutingPreference

#### Modelroutingpreference

Default: null  


The model routing preference.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig autoMode anyOf GenerationConfigRoutingConfigAutoRoutingMode modelRoutingPreference anyOf item 0

Type: enum (of string)  


#### Must be one of:

  * "UNKNOWN"
  * "PRIORITIZE_QUALITY"
  * "BALANCED"
  * "PRIORITIZE_COST"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig autoMode anyOf GenerationConfigRoutingConfigAutoRoutingMode modelRoutingPreference anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig autoMode anyOf item 1

Type: null  


##  manualMode

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig manualMode

Default: null  


Manual routing.

##  Any of

  * GenerationConfigRoutingConfigManualRoutingMode
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig manualMode anyOf GenerationConfigRoutingConfigManualRoutingMode

#### GenerationConfigRoutingConfigManualRoutingMode

Type: object  


When manual routing is set, the specified model will be used directly.

No Additional Properties

##  modelName

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig manualMode anyOf GenerationConfigRoutingConfigManualRoutingMode modelName

#### Modelname

Default: null  


The model name to use. Only the public LLM models are accepted. See [Supported models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#supported-models).

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig manualMode anyOf GenerationConfigRoutingConfigManualRoutingMode modelName anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig manualMode anyOf GenerationConfigRoutingConfigManualRoutingMode modelName anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf GenerationConfigRoutingConfig manualMode anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig routingConfig anyOf item 1

Type: null  


##  modelSelectionConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig modelSelectionConfig

Default: null  


Configuration for model selection.

##  Any of

  * ModelSelectionConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig modelSelectionConfig anyOf ModelSelectionConfig

#### ModelSelectionConfig

Type: object  


Config for model selection.

No Additional Properties

##  featureSelectionPreference

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig modelSelectionConfig anyOf ModelSelectionConfig featureSelectionPreference

Default: null  


Options for feature selection preference.

##  Any of

  * FeatureSelectionPreference
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig modelSelectionConfig anyOf ModelSelectionConfig featureSelectionPreference anyOf FeatureSelectionPreference

#### FeatureSelectionPreference

Type: enum (of string)  


Options for feature selection preference.

#### Must be one of:

  * "FEATURE_SELECTION_PREFERENCE_UNSPECIFIED"
  * "PRIORITIZE_QUALITY"
  * "BALANCED"
  * "PRIORITIZE_COST"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig modelSelectionConfig anyOf ModelSelectionConfig featureSelectionPreference anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig modelSelectionConfig anyOf item 1

Type: null  


##  safetySettings

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings

#### Safetysettings

Default: null  


Safety settings in the request to block unsafe content in the  
response.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting

#### SafetySetting

Type: object  


Safety settings.

No Additional Properties

##  method

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting method

Default: null  


Determines if the harm block method uses probability or probability  
and severity scores.

##  Any of

  * HarmBlockMethod
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting method anyOf HarmBlockMethod

#### HarmBlockMethod

Type: enum (of string)  


Optional.

Specify if the threshold is used for probability or severity score. If not  
specified, the threshold is used for probability score.

#### Must be one of:

  * "HARM_BLOCK_METHOD_UNSPECIFIED"
  * "SEVERITY"
  * "PROBABILITY"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting method anyOf item 1

Type: null  


##  category

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting category

Default: null  


Required. Harm category.

##  Any of

  * HarmCategory
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting category anyOf HarmCategory

#### HarmCategory

Type: enum (of string)  


Required. Harm category.

#### Must be one of:

  * "HARM_CATEGORY_UNSPECIFIED"
  * "HARM_CATEGORY_HATE_SPEECH"
  * "HARM_CATEGORY_DANGEROUS_CONTENT"
  * "HARM_CATEGORY_HARASSMENT"
  * "HARM_CATEGORY_SEXUALLY_EXPLICIT"
  * "HARM_CATEGORY_CIVIC_INTEGRITY"
  * "HARM_CATEGORY_IMAGE_HATE"
  * "HARM_CATEGORY_IMAGE_DANGEROUS_CONTENT"
  * "HARM_CATEGORY_IMAGE_HARASSMENT"
  * "HARM_CATEGORY_IMAGE_SEXUALLY_EXPLICIT"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting category anyOf item 1

Type: null  


##  threshold

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting threshold

Default: null  


Required. The harm block threshold.

##  Any of

  * HarmBlockThreshold
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting threshold anyOf HarmBlockThreshold

#### HarmBlockThreshold

Type: enum (of string)  


Required. The harm block threshold.

#### Must be one of:

  * "HARM_BLOCK_THRESHOLD_UNSPECIFIED"
  * "BLOCK_LOW_AND_ABOVE"
  * "BLOCK_MEDIUM_AND_ABOVE"
  * "BLOCK_ONLY_HIGH"
  * "BLOCK_NONE"
  * "OFF"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 0 SafetySetting threshold anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig safetySettings anyOf item 1

Type: null  


##  tools

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools

#### Tools

Default: null  


Code that enables the system to interact with external systems to  
perform an action outside of the knowledge and scope of the model.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items

  


##  Any of

  * Tool
  * Tool



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool

#### Tool

Type: object  


Tool details of a tool that the model may use to generate a response.

No Additional Properties

##  functionDeclarations

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations

#### Functiondeclarations

Default: null  


List of function declarations that the tool supports.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration

#### FunctionDeclaration

Type: object  


Defines a function that the model can generate JSON inputs for.

The inputs are based on `OpenAPI 3.0 specifications <https://spec.openapis.org/oas/v3.0.3>`_.

No Additional Properties

##  behavior

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration behavior

Default: null  


Defines the function behavior.

##  Any of

  * Behavior
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration behavior anyOf Behavior

#### Behavior

Type: enum (of string)  


Defines the function behavior. Defaults to `BLOCKING`.

#### Must be one of:

  * "UNSPECIFIED"
  * "BLOCKING"
  * "NON_BLOCKING"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration behavior anyOf item 1

Type: null  


##  description

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration description

#### Description

Default: null  


Optional. Description and purpose of the function. Model uses it to decide how and whether to call the function.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration description anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration description anyOf item 1

Type: null  


##  name

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration name

#### Name

Default: null  


Required. The name of the function to call. Must start with a letter or an underscore. Must be a-z, A-Z, 0-9, or contain underscores, dots and dashes, with a maximum length of 64.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration name anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration name anyOf item 1

Type: null  


##  parameters

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration parameters

Default: null  


Optional. Describes the parameters to this function in JSON Schema Object format. Reflects the Open API 3.03 Parameter Object. string Key: the name of the parameter. Parameter names are case sensitive. Schema Value: the Schema defining the type used for the parameter. For function with no parameters, this can be left unset. Parameter names must start with a letter or an underscore and must only contain chars a-z, A-Z, 0-9, or underscores with a maximum length of 64. Example with 1 required and 1 optional parameter: type: OBJECT properties: param1: type: STRING param2: type: INTEGER required: - param1

##  Any of

  * Schema
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration parameters anyOf Schema

#### Schema

Type: object  


Schema is used to define the format of input/output data.

Represents a select subset of an [OpenAPI 3.0 schema  
object](https://spec.openapis.org/oas/v3.0.3#schema-object). More fields may  
be added in the future as needed.

Same definition as Schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration parameters anyOf item 1

Type: null  


##  parametersJsonSchema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration parametersJsonSchema

#### Parametersjsonschema

Default: null  


Optional. Describes the parameters to the function in JSON Schema format. The schema must describe an object where the properties are the parameters to the function. For example: `{ "type": "object", "properties": { "name": { "type": "string" }, "age": { "type": "integer" } }, "additionalProperties": false, "required": ["name", "age"], "propertyOrdering": ["name", "age"] }` This field is mutually exclusive with `parameters`.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration parametersJsonSchema anyOf item 0

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration parametersJsonSchema anyOf item 1

Type: null  


##  response

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration response

Default: null  


Optional. Describes the output from this function in JSON Schema format. Reflects the Open API 3.03 Response Object. The Schema defines the type used for the response value of the function.

##  Any of

  * Schema
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration response anyOf Schema

#### Schema

Type: object  


Schema is used to define the format of input/output data.

Represents a select subset of an [OpenAPI 3.0 schema  
object](https://spec.openapis.org/oas/v3.0.3#schema-object). More fields may  
be added in the future as needed.

Same definition as Schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration response anyOf item 1

Type: null  


##  responseJsonSchema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration responseJsonSchema

#### Responsejsonschema

Default: null  


Optional. Describes the output from this function in JSON Schema format. The value specified by the schema is the response value of the function. This field is mutually exclusive with `response`.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration responseJsonSchema anyOf item 0

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 0 FunctionDeclaration responseJsonSchema anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool functionDeclarations anyOf item 1

Type: null  


##  retrieval

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval

Default: null  


Optional. Retrieval tool type. System will always execute the provided retrieval tool(s) to get external knowledge to answer the prompt. Retrieval results are presented to the model for generation.

##  Any of

  * Retrieval
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval

#### Retrieval

Type: object  


Defines a retrieval tool that model can call to access external knowledge.

No Additional Properties

##  disableAttribution

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval disableAttribution

#### Disableattribution

Default: null  


Optional. Deprecated. This option is no longer supported.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval disableAttribution anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval disableAttribution anyOf item 1

Type: null  


##  externalApi

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi

Default: null  


Use data source powered by external API for grounding.

##  Any of

  * ExternalApi
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi

#### ExternalApi

Type: object  


Retrieve from data source powered by external API for grounding.

The external API is not owned by Google, but need to follow the pre-defined  
API spec.

No Additional Properties

##  apiAuth

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth

Default: null  


The authentication config to access the API. Deprecated. Please use auth_config instead.

##  Any of

  * ApiAuth
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth

#### ApiAuth

Type: object  


The generic reusable api auth config.

Deprecated. Please use AuthConfig (google/cloud/aiplatform/master/auth.proto)  
instead.

No Additional Properties

##  apiKeyConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth apiKeyConfig

Default: null  


The API secret.

##  Any of

  * ApiAuthApiKeyConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth apiKeyConfig anyOf ApiAuthApiKeyConfig

#### ApiAuthApiKeyConfig

Type: object  


The API secret.

No Additional Properties

##  apiKeySecretVersion

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth apiKeyConfig anyOf ApiAuthApiKeyConfig apiKeySecretVersion

#### Apikeysecretversion

Default: null  


Required. The SecretManager secret version resource name storing API key. e.g. projects/{project}/secrets/{secret}/versions/{version}

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth apiKeyConfig anyOf ApiAuthApiKeyConfig apiKeySecretVersion anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth apiKeyConfig anyOf ApiAuthApiKeyConfig apiKeySecretVersion anyOf item 1

Type: null  


##  apiKeyString

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth apiKeyConfig anyOf ApiAuthApiKeyConfig apiKeyString

#### Apikeystring

Default: null  


The API key string. Either this or `api_key_secret_version` must be set.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth apiKeyConfig anyOf ApiAuthApiKeyConfig apiKeyString anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth apiKeyConfig anyOf ApiAuthApiKeyConfig apiKeyString anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf ApiAuth apiKeyConfig anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiAuth anyOf item 1

Type: null  


##  apiSpec

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiSpec

Default: null  


The API spec that the external API implements.

##  Any of

  * ApiSpec
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiSpec anyOf ApiSpec

#### ApiSpec

Type: enum (of string)  


The API spec that the external API implements.

#### Must be one of:

  * "API_SPEC_UNSPECIFIED"
  * "SIMPLE_SEARCH"
  * "ELASTIC_SEARCH"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi apiSpec anyOf item 1

Type: null  


##  authConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig

Default: null  


The authentication config to access the API.

##  Any of

  * AuthConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig

#### AuthConfig

Type: object  


Auth configuration to run the extension.

No Additional Properties

##  apiKeyConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig apiKeyConfig

Default: null  


Config for API key auth.

##  Any of

  * ApiKeyConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig apiKeyConfig anyOf ApiKeyConfig

#### ApiKeyConfig

Type: object  


Config for authentication with API key.

No Additional Properties

##  apiKeyString

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig apiKeyConfig anyOf ApiKeyConfig apiKeyString

#### Apikeystring

Default: null  


The API key to be used in the request directly.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig apiKeyConfig anyOf ApiKeyConfig apiKeyString anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig apiKeyConfig anyOf ApiKeyConfig apiKeyString anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig apiKeyConfig anyOf item 1

Type: null  


##  authType

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig authType

Default: null  


Type of auth scheme.

##  Any of

  * AuthType
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig authType anyOf AuthType

#### AuthType

Type: enum (of string)  


Type of auth scheme.

#### Must be one of:

  * "AUTH_TYPE_UNSPECIFIED"
  * "NO_AUTH"
  * "API_KEY_AUTH"
  * "HTTP_BASIC_AUTH"
  * "GOOGLE_SERVICE_ACCOUNT_AUTH"
  * "OAUTH"
  * "OIDC_AUTH"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig authType anyOf item 1

Type: null  


##  googleServiceAccountConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig googleServiceAccountConfig

Default: null  


Config for Google Service Account auth.

##  Any of

  * AuthConfigGoogleServiceAccountConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig googleServiceAccountConfig anyOf AuthConfigGoogleServiceAccountConfig

#### AuthConfigGoogleServiceAccountConfig

Type: object  


Config for Google Service Account Authentication.

No Additional Properties

##  serviceAccount

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig googleServiceAccountConfig anyOf AuthConfigGoogleServiceAccountConfig serviceAccount

#### Serviceaccount

Default: null  


Optional. The service account that the extension execution service runs as. - If the service account is specified, the `iam.serviceAccounts.getAccessToken` permission should be granted to Vertex AI Extension Service Agent (https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) on the specified service account. - If not specified, the Vertex AI Extension Service Agent will be used to execute the Extension.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig googleServiceAccountConfig anyOf AuthConfigGoogleServiceAccountConfig serviceAccount anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig googleServiceAccountConfig anyOf AuthConfigGoogleServiceAccountConfig serviceAccount anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig googleServiceAccountConfig anyOf item 1

Type: null  


##  httpBasicAuthConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig httpBasicAuthConfig

Default: null  


Config for HTTP Basic auth.

##  Any of

  * AuthConfigHttpBasicAuthConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig httpBasicAuthConfig anyOf AuthConfigHttpBasicAuthConfig

#### AuthConfigHttpBasicAuthConfig

Type: object  


Config for HTTP Basic Authentication.

No Additional Properties

##  credentialSecret

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig httpBasicAuthConfig anyOf AuthConfigHttpBasicAuthConfig credentialSecret

#### Credentialsecret

Default: null  


Required. The name of the SecretManager secret version resource storing the base64 encoded credentials. Format: `projects/{project}/secrets/{secrete}/versions/{version}` \- If specified, the `secretmanager.versions.access` permission should be granted to Vertex AI Extension Service Agent (https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) on the specified resource.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig httpBasicAuthConfig anyOf AuthConfigHttpBasicAuthConfig credentialSecret anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig httpBasicAuthConfig anyOf AuthConfigHttpBasicAuthConfig credentialSecret anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig httpBasicAuthConfig anyOf item 1

Type: null  


##  oauthConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oauthConfig

Default: null  


Config for user oauth.

##  Any of

  * AuthConfigOauthConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oauthConfig anyOf AuthConfigOauthConfig

#### AuthConfigOauthConfig

Type: object  


Config for user oauth.

No Additional Properties

##  accessToken

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oauthConfig anyOf AuthConfigOauthConfig accessToken

#### Accesstoken

Default: null  


Access token for extension endpoint. Only used to propagate token from [[ExecuteExtensionRequest.runtime _auth_ config]] at request time.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oauthConfig anyOf AuthConfigOauthConfig accessToken anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oauthConfig anyOf AuthConfigOauthConfig accessToken anyOf item 1

Type: null  


##  serviceAccount

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oauthConfig anyOf AuthConfigOauthConfig serviceAccount

#### Serviceaccount

Default: null  


The service account used to generate access tokens for executing the Extension. - If the service account is specified, the `iam.serviceAccounts.getAccessToken` permission should be granted to Vertex AI Extension Service Agent (https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents) on the provided service account.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oauthConfig anyOf AuthConfigOauthConfig serviceAccount anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oauthConfig anyOf AuthConfigOauthConfig serviceAccount anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oauthConfig anyOf item 1

Type: null  


##  oidcConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oidcConfig

Default: null  


Config for user OIDC auth.

##  Any of

  * AuthConfigOidcConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oidcConfig anyOf AuthConfigOidcConfig

#### AuthConfigOidcConfig

Type: object  


Config for user OIDC auth.

No Additional Properties

##  idToken

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oidcConfig anyOf AuthConfigOidcConfig idToken

#### Idtoken

Default: null  


OpenID Connect formatted ID token for extension endpoint. Only used to propagate token from [[ExecuteExtensionRequest.runtime _auth_ config]] at request time.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oidcConfig anyOf AuthConfigOidcConfig idToken anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oidcConfig anyOf AuthConfigOidcConfig idToken anyOf item 1

Type: null  


##  serviceAccount

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oidcConfig anyOf AuthConfigOidcConfig serviceAccount

#### Serviceaccount

Default: null  


The service account used to generate an OpenID Connect (OIDC)-compatible JWT token signed by the Google OIDC Provider (accounts.google.com) for extension endpoint (https://cloud.google.com/iam/docs/create-short-lived-credentials-direct#sa-credentials-oidc). - The audience for the token will be set to the URL in the server url defined in the OpenApi spec. - If the service account is provided, the service account should grant `iam.serviceAccounts.getOpenIdToken` permission to Vertex AI Extension Service Agent (https://cloud.google.com/vertex-ai/docs/general/access-control#service-agents).

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oidcConfig anyOf AuthConfigOidcConfig serviceAccount anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oidcConfig anyOf AuthConfigOidcConfig serviceAccount anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf AuthConfig oidcConfig anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi authConfig anyOf item 1

Type: null  


##  elasticSearchParams

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams

Default: null  


Parameters for the elastic search API.

##  Any of

  * ExternalApiElasticSearchParams
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams

#### ExternalApiElasticSearchParams

Type: object  


The search parameters to use for the ELASTIC_SEARCH spec.

No Additional Properties

##  index

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams index

#### Index

Default: null  


The ElasticSearch index to use.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams index anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams index anyOf item 1

Type: null  


##  numHits

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams numHits

#### Numhits

Default: null  


Optional. Number of hits (chunks) to request. When specified, it is passed to Elasticsearch as the `num_hits` param.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams numHits anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams numHits anyOf item 1

Type: null  


##  searchTemplate

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams searchTemplate

#### Searchtemplate

Default: null  


The ElasticSearch search template to use.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams searchTemplate anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf ExternalApiElasticSearchParams searchTemplate anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi elasticSearchParams anyOf item 1

Type: null  


##  endpoint

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi endpoint

#### Endpoint

Default: null  


The endpoint of the external API. The system will call the API at this endpoint to retrieve the data for grounding. Example: https://acme.com:443/search

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi endpoint anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi endpoint anyOf item 1

Type: null  


##  simpleSearchParams

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi simpleSearchParams

Default: null  


Parameters for the simple search API.

##  Any of

  * ExternalApiSimpleSearchParams
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi simpleSearchParams anyOf ExternalApiSimpleSearchParams

#### ExternalApiSimpleSearchParams

Type: object  


The search parameters to use for SIMPLE_SEARCH spec.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf ExternalApi simpleSearchParams anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval externalApi anyOf item 1

Type: null  


##  vertexAiSearch

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch

Default: null  


Set to use data source powered by Vertex AI Search.

##  Any of

  * VertexAISearch
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch

#### VertexAISearch

Type: object  


Retrieve from Vertex AI Search datastore or engine for grounding.

datastore and engine are mutually exclusive. See  
https://cloud.google.com/products/agent-builder

No Additional Properties

##  dataStoreSpecs

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs

#### Datastorespecs

Default: null  


Specifications that define the specific DataStores to be searched, along with configurations for those data stores. This is only considered for Engines with multiple data stores. It should only be set if engine is used.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs anyOf item 0 VertexAISearchDataStoreSpec

#### VertexAISearchDataStoreSpec

Type: object  


Define data stores within engine to filter on in a search call and configurations for those data stores.

For more information, see  
https://cloud.google.com/generative-ai-app-builder/docs/reference/rpc/google.cloud.discoveryengine.v1#datastorespec

No Additional Properties

##  dataStore

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs anyOf item 0 VertexAISearchDataStoreSpec dataStore

#### Datastore

Default: null  


Full resource name of DataStore, such as Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs anyOf item 0 VertexAISearchDataStoreSpec dataStore anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs anyOf item 0 VertexAISearchDataStoreSpec dataStore anyOf item 1

Type: null  


##  filter

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs anyOf item 0 VertexAISearchDataStoreSpec filter

#### Filter

Default: null  


Optional. Filter specification to filter documents in the data store specified by data_store field. For more information on filtering, see [Filtering](https://cloud.google.com/generative-ai-app-builder/docs/filter-search-metadata)

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs anyOf item 0 VertexAISearchDataStoreSpec filter anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs anyOf item 0 VertexAISearchDataStoreSpec filter anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch dataStoreSpecs anyOf item 1

Type: null  


##  datastore

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch datastore

#### Datastore

Default: null  


Optional. Fully-qualified Vertex AI Search data store resource ID. Format: `projects/{project}/locations/{location}/collections/{collection}/dataStores/{dataStore}`

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch datastore anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch datastore anyOf item 1

Type: null  


##  engine

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch engine

#### Engine

Default: null  


Optional. Fully-qualified Vertex AI Search engine resource ID. Format: `projects/{project}/locations/{location}/collections/{collection}/engines/{engine}`

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch engine anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch engine anyOf item 1

Type: null  


##  filter

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch filter

#### Filter

Default: null  


Optional. Filter strings to be passed to the search API.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch filter anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch filter anyOf item 1

Type: null  


##  maxResults

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch maxResults

#### Maxresults

Default: null  


Optional. Number of search results to return per query. The default value is 10. The maximumm allowed value is 10.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch maxResults anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf VertexAISearch maxResults anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexAiSearch anyOf item 1

Type: null  


##  vertexRagStore

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore

Default: null  


Set to use data source powered by Vertex RAG store. User data is uploaded via the VertexRagDataService.

##  Any of

  * VertexRagStore
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore

#### VertexRagStore

Type: object  


Retrieve from Vertex RAG Store for grounding.

No Additional Properties

##  ragCorpora

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragCorpora

#### Ragcorpora

Default: null  


Optional. Deprecated. Please use rag_resources instead.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragCorpora anyOf item 0

Type: array of string  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragCorpora anyOf item 0 item 0 items

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragCorpora anyOf item 1

Type: null  


##  ragResources

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources

#### Ragresources

Default: null  


Optional. The representation of the rag source. It can be used to specify corpus only or ragfiles. Currently only support one corpus or multiple files from one corpus. In the future we may open up multiple corpora support.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 0 VertexRagStoreRagResource

#### VertexRagStoreRagResource

Type: object  


The definition of the Rag resource.

No Additional Properties

##  ragCorpus

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 0 VertexRagStoreRagResource ragCorpus

#### Ragcorpus

Default: null  


Optional. RagCorpora resource name. Format: `projects/{project}/locations/{location}/ragCorpora/{rag_corpus}`

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 0 VertexRagStoreRagResource ragCorpus anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 0 VertexRagStoreRagResource ragCorpus anyOf item 1

Type: null  


##  ragFileIds

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 0 VertexRagStoreRagResource ragFileIds

#### Ragfileids

Default: null  


Optional. rag _file_ id. The files should be in the same rag _corpus set in rag_ corpus field.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 0 VertexRagStoreRagResource ragFileIds anyOf item 0

Type: array of string  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 0 VertexRagStoreRagResource ragFileIds anyOf item 0 item 0 items

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 0 VertexRagStoreRagResource ragFileIds anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragResources anyOf item 1

Type: null  


##  ragRetrievalConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig

Default: null  


Optional. The retrieval config for the Rag query.

##  Any of

  * RagRetrievalConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig

#### RagRetrievalConfig

Type: object  


Specifies the context retrieval config.

No Additional Properties

##  filter

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter

Default: null  


Optional. Config for filters.

##  Any of

  * RagRetrievalConfigFilter
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter

#### RagRetrievalConfigFilter

Type: object  


Config for filters.

No Additional Properties

##  metadataFilter

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter metadataFilter

#### Metadatafilter

Default: null  


Optional. String for metadata filtering.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter metadataFilter anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter metadataFilter anyOf item 1

Type: null  


##  vectorDistanceThreshold

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter vectorDistanceThreshold

#### Vectordistancethreshold

Default: null  


Optional. Only returns contexts with vector distance smaller than the threshold.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter vectorDistanceThreshold anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter vectorDistanceThreshold anyOf item 1

Type: null  


##  vectorSimilarityThreshold

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter vectorSimilarityThreshold

#### Vectorsimilaritythreshold

Default: null  


Optional. Only returns contexts with vector similarity larger than the threshold.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter vectorSimilarityThreshold anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf RagRetrievalConfigFilter vectorSimilarityThreshold anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig filter anyOf item 1

Type: null  


##  hybridSearch

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig hybridSearch

Default: null  


Optional. Config for Hybrid Search.

##  Any of

  * RagRetrievalConfigHybridSearch
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig hybridSearch anyOf RagRetrievalConfigHybridSearch

#### RagRetrievalConfigHybridSearch

Type: object  


Config for Hybrid Search.

No Additional Properties

##  alpha

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig hybridSearch anyOf RagRetrievalConfigHybridSearch alpha

#### Alpha

Default: null  


Optional. Alpha value controls the weight between dense and sparse vector search results. The range is [0, 1], while 0 means sparse vector search only and 1 means dense vector search only. The default value is 0.5 which balances sparse and dense vector search equally.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig hybridSearch anyOf RagRetrievalConfigHybridSearch alpha anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig hybridSearch anyOf RagRetrievalConfigHybridSearch alpha anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig hybridSearch anyOf item 1

Type: null  


##  ranking

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking

Default: null  


Optional. Config for ranking and reranking.

##  Any of

  * RagRetrievalConfigRanking
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking

#### RagRetrievalConfigRanking

Type: object  


Config for ranking and reranking.

No Additional Properties

##  llmRanker

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking llmRanker

Default: null  


Optional. Config for LlmRanker.

##  Any of

  * RagRetrievalConfigRankingLlmRanker
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking llmRanker anyOf RagRetrievalConfigRankingLlmRanker

#### RagRetrievalConfigRankingLlmRanker

Type: object  


Config for LlmRanker.

No Additional Properties

##  modelName

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking llmRanker anyOf RagRetrievalConfigRankingLlmRanker modelName

#### Modelname

Default: null  


Optional. The model name used for ranking. See [Supported models](https://cloud.google.com/vertex-ai/generative-ai/docs/model-reference/inference#supported-models).

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking llmRanker anyOf RagRetrievalConfigRankingLlmRanker modelName anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking llmRanker anyOf RagRetrievalConfigRankingLlmRanker modelName anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking llmRanker anyOf item 1

Type: null  


##  rankService

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking rankService

Default: null  


Optional. Config for Rank Service.

##  Any of

  * RagRetrievalConfigRankingRankService
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking rankService anyOf RagRetrievalConfigRankingRankService

#### RagRetrievalConfigRankingRankService

Type: object  


Config for Rank Service.

No Additional Properties

##  modelName

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking rankService anyOf RagRetrievalConfigRankingRankService modelName

#### Modelname

Default: null  


Optional. The model name of the rank service. Format: `semantic-ranker-512@latest`

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking rankService anyOf RagRetrievalConfigRankingRankService modelName anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking rankService anyOf RagRetrievalConfigRankingRankService modelName anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf RagRetrievalConfigRanking rankService anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig ranking anyOf item 1

Type: null  


##  topK

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig topK

#### Topk

Default: null  


Optional. The number of contexts to retrieve.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig topK anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf RagRetrievalConfig topK anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore ragRetrievalConfig anyOf item 1

Type: null  


##  similarityTopK

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore similarityTopK

#### Similaritytopk

Default: null  


Optional. Number of top k results to return from the selected corpora.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore similarityTopK anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore similarityTopK anyOf item 1

Type: null  


##  storeContext

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore storeContext

#### Storecontext

Default: null  


Optional. Currently only supported for Gemini Multimodal Live API. In Gemini Multimodal Live API, if `store_context` bool is specified, Gemini will leverage it to automatically memorize the interactions between the client and Gemini, and retrieve context when needed to augment the response generation for users' ongoing and future interactions.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore storeContext anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore storeContext anyOf item 1

Type: null  


##  vectorDistanceThreshold

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore vectorDistanceThreshold

#### Vectordistancethreshold

Default: null  


Optional. Only return results with vector distance smaller than the threshold.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore vectorDistanceThreshold anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf VertexRagStore vectorDistanceThreshold anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf Retrieval vertexRagStore anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool retrieval anyOf item 1

Type: null  


##  googleSearch

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch

Default: null  


Optional. Google Search tool type. Specialized retrieval tool  
that is powered by Google Search.

##  Any of

  * GoogleSearch
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch

#### GoogleSearch

Type: object  


Tool to support Google Search in Model. Powered by Google.

No Additional Properties

##  timeRangeFilter

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch timeRangeFilter

Default: null  


Optional. Filter search results to a specific time range.  
If customers set a start time, they must set an end time (and vice versa).

##  Any of

  * Interval
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch timeRangeFilter anyOf Interval

#### Interval

Type: object  


Represents a time interval, encoded as a start time (inclusive) and an end time (exclusive).

The start time must be less than or equal to the end time.  
When the start equals the end time, the interval is an empty interval.  
(matches no time)  
When both start and end are unspecified, the interval matches any time.

No Additional Properties

##  startTime

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch timeRangeFilter anyOf Interval startTime

#### Starttime

Default: null  


The start time of the interval.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch timeRangeFilter anyOf Interval startTime anyOf item 0

Type: stringFormat: date-time  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch timeRangeFilter anyOf Interval startTime anyOf item 1

Type: null  


##  endTime

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch timeRangeFilter anyOf Interval endTime

#### Endtime

Default: null  


The end time of the interval.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch timeRangeFilter anyOf Interval endTime anyOf item 0

Type: stringFormat: date-time  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch timeRangeFilter anyOf Interval endTime anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf GoogleSearch timeRangeFilter anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearch anyOf item 1

Type: null  


##  googleSearchRetrieval

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval

Default: null  


Optional. GoogleSearchRetrieval tool type. Specialized retrieval tool that is powered by Google search.

##  Any of

  * GoogleSearchRetrieval
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval

#### GoogleSearchRetrieval

Type: object  


Tool to retrieve public web data for grounding, powered by Google.

No Additional Properties

##  dynamicRetrievalConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval dynamicRetrievalConfig

Default: null  


Specifies the dynamic retrieval configuration for the given source.

##  Any of

  * DynamicRetrievalConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval dynamicRetrievalConfig anyOf DynamicRetrievalConfig

#### DynamicRetrievalConfig

Type: object  


Describes the options to customize dynamic retrieval.

No Additional Properties

##  mode

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval dynamicRetrievalConfig anyOf DynamicRetrievalConfig mode

Default: null  


The mode of the predictor to be used in dynamic retrieval.

##  Any of

  * DynamicRetrievalConfigMode
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval dynamicRetrievalConfig anyOf DynamicRetrievalConfig mode anyOf DynamicRetrievalConfigMode

#### DynamicRetrievalConfigMode

Type: enum (of string)  


Config for the dynamic retrieval config mode.

#### Must be one of:

  * "MODE_UNSPECIFIED"
  * "MODE_DYNAMIC"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval dynamicRetrievalConfig anyOf DynamicRetrievalConfig mode anyOf item 1

Type: null  


##  dynamicThreshold

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval dynamicRetrievalConfig anyOf DynamicRetrievalConfig dynamicThreshold

#### Dynamicthreshold

Default: null  


Optional. The threshold to be used in dynamic retrieval. If not set, a system default value is used.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval dynamicRetrievalConfig anyOf DynamicRetrievalConfig dynamicThreshold anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval dynamicRetrievalConfig anyOf DynamicRetrievalConfig dynamicThreshold anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf GoogleSearchRetrieval dynamicRetrievalConfig anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleSearchRetrieval anyOf item 1

Type: null  


##  enterpriseWebSearch

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool enterpriseWebSearch

Default: null  


Optional. Enterprise web search tool type. Specialized retrieval  
tool that is powered by Vertex AI Search and Sec4 compliance.

##  Any of

  * EnterpriseWebSearch
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool enterpriseWebSearch anyOf EnterpriseWebSearch

#### EnterpriseWebSearch

Type: object  


Tool to search public web data, powered by Vertex AI Search and Sec4 compliance.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool enterpriseWebSearch anyOf item 1

Type: null  


##  googleMaps

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleMaps

Default: null  


Optional. Google Maps tool type. Specialized retrieval tool  
that is powered by Google Maps.

##  Any of

  * GoogleMaps
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleMaps anyOf GoogleMaps

#### GoogleMaps

Type: object  


Tool to support Google Maps in Model.

No Additional Properties

##  authConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleMaps anyOf GoogleMaps authConfig

Default: null  


Optional. Auth config for the Google Maps tool.

##  Any of

  * AuthConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleMaps anyOf GoogleMaps authConfig anyOf AuthConfig

#### AuthConfig

Type: object  


Auth configuration to run the extension.

Same definition as AuthConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleMaps anyOf GoogleMaps authConfig anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool googleMaps anyOf item 1

Type: null  


##  urlContext

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool urlContext

Default: null  


Optional. Tool to support URL context retrieval.

##  Any of

  * UrlContext
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool urlContext anyOf UrlContext

#### UrlContext

Type: object  


Tool to support URL context retrieval.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool urlContext anyOf item 1

Type: null  


##  codeExecution

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool codeExecution

Default: null  


Optional. CodeExecution tool type. Enables the model to execute code as part of generation.

##  Any of

  * ToolCodeExecution
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool codeExecution anyOf ToolCodeExecution

#### ToolCodeExecution

Type: object  


Tool that executes code generated by the model, and automatically returns the result to the model.

See also [ExecutableCode]and [CodeExecutionResult] which are input and output  
to this tool.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool codeExecution anyOf item 1

Type: null  


##  computerUse

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool computerUse

Default: null  


Optional. Tool to support the model interacting directly with the computer. If enabled, it automatically populates computer-use specific Function Declarations.

##  Any of

  * ToolComputerUse
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool computerUse anyOf ToolComputerUse

#### ToolComputerUse

Type: object  


Tool to support computer use.

No Additional Properties

##  environment

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool computerUse anyOf ToolComputerUse environment

Default: null  


Required. The environment being operated.

##  Any of

  * Environment
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool computerUse anyOf ToolComputerUse environment anyOf Environment

#### Environment

Type: enum (of string)  


Required. The environment being operated.

#### Must be one of:

  * "ENVIRONMENT_UNSPECIFIED"
  * "ENVIRONMENT_BROWSER"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool computerUse anyOf ToolComputerUse environment anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool computerUse anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool

#### Tool

Type: object  


Definition for a tool the client can call.

##  name Required

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool name

#### Name

Type: string  


##  title

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool title

#### Title

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool title anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool title anyOf item 1

Type: null  


##  description

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool description

#### Description

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool description anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool description anyOf item 1

Type: null  


##  inputSchema Required

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool inputSchema

#### Inputschema

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool inputSchema additionalProperties

Type: object  


##  outputSchema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool outputSchema

#### Outputschema

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool outputSchema anyOf item 0

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool outputSchema anyOf item 0 additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool outputSchema anyOf item 1

Type: null  


##  annotations

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations

Default: null  


##  Any of

  * ToolAnnotations
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations

#### ToolAnnotations

Type: object  


Additional properties describing a Tool to clients.

NOTE: all properties in ToolAnnotations are **hints**.  
They are not guaranteed to provide a faithful description of  
tool behavior (including descriptive properties like `title`).

Clients should never make tool use decisions based on ToolAnnotations  
received from untrusted servers.

##  title

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations title

#### Title

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations title anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations title anyOf item 1

Type: null  


##  readOnlyHint

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations readOnlyHint

#### Readonlyhint

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations readOnlyHint anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations readOnlyHint anyOf item 1

Type: null  


##  destructiveHint

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations destructiveHint

#### Destructivehint

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations destructiveHint anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations destructiveHint anyOf item 1

Type: null  


##  idempotentHint

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations idempotentHint

#### Idempotenthint

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations idempotentHint anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations idempotentHint anyOf item 1

Type: null  


##  openWorldHint

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations openWorldHint

#### Openworldhint

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations openWorldHint anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations openWorldHint anyOf item 1

Type: null  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf ToolAnnotations additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool annotations anyOf item 1

Type: null  


##  _meta

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool _meta

#### Meta

Default: null  


##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool _meta anyOf item 0

Type: object  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool _meta anyOf item 0 additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool _meta anyOf item 1

Type: null  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 0 item 0 items anyOf Tool additionalProperties

Type: object  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig tools anyOf item 1

Type: null  


##  toolConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig

Default: null  


Associates model output to a specific function call.

##  Any of

  * ToolConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig

#### ToolConfig

Type: object  


Tool config.

This config is shared for all tools provided in the request.

No Additional Properties

##  functionCallingConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig

Default: null  


Optional. Function calling config.

##  Any of

  * FunctionCallingConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig anyOf FunctionCallingConfig

#### FunctionCallingConfig

Type: object  


Function calling config.

No Additional Properties

##  mode

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig anyOf FunctionCallingConfig mode

Default: null  


Optional. Function calling mode.

##  Any of

  * FunctionCallingConfigMode
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig anyOf FunctionCallingConfig mode anyOf FunctionCallingConfigMode

#### FunctionCallingConfigMode

Type: enum (of string)  


Config for the function calling config mode.

#### Must be one of:

  * "MODE_UNSPECIFIED"
  * "AUTO"
  * "ANY"
  * "NONE"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig anyOf FunctionCallingConfig mode anyOf item 1

Type: null  


##  allowedFunctionNames

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig anyOf FunctionCallingConfig allowedFunctionNames

#### Allowedfunctionnames

Default: null  


Optional. Function names to call. Only set when the Mode is ANY. Function names should match [FunctionDeclaration.name]. With mode set to ANY, model will predict a function call from the set of function names provided.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig anyOf FunctionCallingConfig allowedFunctionNames anyOf item 0

Type: array of string  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig anyOf FunctionCallingConfig allowedFunctionNames anyOf item 0 item 0 items

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig anyOf FunctionCallingConfig allowedFunctionNames anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig functionCallingConfig anyOf item 1

Type: null  


##  retrievalConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig

Default: null  


Optional. Retrieval config.

##  Any of

  * RetrievalConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig

#### RetrievalConfig

Type: object  


Retrieval config.

No Additional Properties

##  latLng

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig latLng

Default: null  


Optional. The location of the user.

##  Any of

  * LatLng
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig latLng anyOf LatLng

#### LatLng

Type: object  


An object that represents a latitude/longitude pair.

This is expressed as a pair of doubles to represent degrees latitude and  
degrees longitude. Unless specified otherwise, this object must conform to the  
<a href="https://en.wikipedia.org/wiki/World_Geodetic_System#1984_version">  
WGS84 standard</a>. Values must be within normalized ranges.

No Additional Properties

##  latitude

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig latLng anyOf LatLng latitude

#### Latitude

Default: null  


The latitude in degrees. It must be in the range [-90.0, +90.0].

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig latLng anyOf LatLng latitude anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig latLng anyOf LatLng latitude anyOf item 1

Type: null  


##  longitude

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig latLng anyOf LatLng longitude

#### Longitude

Default: null  


The longitude in degrees. It must be in the range [-180.0, +180.0]

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig latLng anyOf LatLng longitude anyOf item 0

Type: number  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig latLng anyOf LatLng longitude anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig latLng anyOf item 1

Type: null  


##  languageCode

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig languageCode

#### Languagecode

Default: null  


The language code of the user.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig languageCode anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf RetrievalConfig languageCode anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf ToolConfig retrievalConfig anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig toolConfig anyOf item 1

Type: null  


##  labels

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig labels

#### Labels

Default: null  


Labels with user-defined metadata to break down billed charges.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig labels anyOf item 0

Type: object  


##  _Additional Properties_

Each additional property must conform to the following schema

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig labels anyOf item 0 additionalProperties

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig labels anyOf item 1

Type: null  


##  cachedContent

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig cachedContent

#### Cachedcontent

Default: null  


Resource name of a context cache that can be used in subsequent  
requests.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig cachedContent anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig cachedContent anyOf item 1

Type: null  


##  responseModalities

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseModalities

#### Responsemodalities

Default: null  


The requested modalities of the response. Represents the set of  
modalities that the model can return.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseModalities anyOf item 0

Type: array of string  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseModalities anyOf item 0 item 0 items

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig responseModalities anyOf item 1

Type: null  


##  mediaResolution

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig mediaResolution

Default: null  


If specified, the media resolution specified will be used.

##  Any of

  * MediaResolution
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig mediaResolution anyOf MediaResolution

#### MediaResolution

Type: enum (of string)  


The media resolution to use.

#### Must be one of:

  * "MEDIA_RESOLUTION_UNSPECIFIED"
  * "MEDIA_RESOLUTION_LOW"
  * "MEDIA_RESOLUTION_MEDIUM"
  * "MEDIA_RESOLUTION_HIGH"



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig mediaResolution anyOf item 1

Type: null  


##  speechConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig

#### Speechconfig

Default: null  


The speech generation configuration.

##  Any of

  * SpeechConfig
  * Option 2
  * Option 3



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig

#### SpeechConfig

Type: object  


The speech generation configuration.

No Additional Properties

##  voiceConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig voiceConfig

Default: null  


The configuration for the speaker to use.

##  Any of

  * VoiceConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig voiceConfig anyOf VoiceConfig

#### VoiceConfig

Type: object  


The configuration for the voice to use.

No Additional Properties

##  prebuiltVoiceConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig voiceConfig anyOf VoiceConfig prebuiltVoiceConfig

Default: null  


The configuration for the speaker to use.

##  Any of

  * PrebuiltVoiceConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig voiceConfig anyOf VoiceConfig prebuiltVoiceConfig anyOf PrebuiltVoiceConfig

#### PrebuiltVoiceConfig

Type: object  


The configuration for the prebuilt speaker to use.

No Additional Properties

##  voiceName

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig voiceConfig anyOf VoiceConfig prebuiltVoiceConfig anyOf PrebuiltVoiceConfig voiceName

#### Voicename

Default: null  


The name of the prebuilt voice to use.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig voiceConfig anyOf VoiceConfig prebuiltVoiceConfig anyOf PrebuiltVoiceConfig voiceName anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig voiceConfig anyOf VoiceConfig prebuiltVoiceConfig anyOf PrebuiltVoiceConfig voiceName anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig voiceConfig anyOf VoiceConfig prebuiltVoiceConfig anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig voiceConfig anyOf item 1

Type: null  


##  multiSpeakerVoiceConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig

Default: null  


The configuration for the multi-speaker setup.  
It is mutually exclusive with the voice_config field.

##  Any of

  * MultiSpeakerVoiceConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig

#### MultiSpeakerVoiceConfig

Type: object  


The configuration for the multi-speaker setup.

No Additional Properties

##  speakerVoiceConfigs

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs

#### Speakervoiceconfigs

Default: null  


The configuration for the speaker to use.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs anyOf item 0 SpeakerVoiceConfig

#### SpeakerVoiceConfig

Type: object  


The configuration for the speaker to use.

No Additional Properties

##  speaker

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs anyOf item 0 SpeakerVoiceConfig speaker

#### Speaker

Default: null  


The name of the speaker to use. Should be the same as in the  
prompt.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs anyOf item 0 SpeakerVoiceConfig speaker anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs anyOf item 0 SpeakerVoiceConfig speaker anyOf item 1

Type: null  


##  voiceConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs anyOf item 0 SpeakerVoiceConfig voiceConfig

Default: null  


The configuration for the voice to use.

##  Any of

  * VoiceConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs anyOf item 0 SpeakerVoiceConfig voiceConfig anyOf VoiceConfig

#### VoiceConfig

Type: object  


The configuration for the voice to use.

Same definition as VoiceConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs anyOf item 0 SpeakerVoiceConfig voiceConfig anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf MultiSpeakerVoiceConfig speakerVoiceConfigs anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig multiSpeakerVoiceConfig anyOf item 1

Type: null  


##  languageCode

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig languageCode

#### Languagecode

Default: null  


Language code (ISO 639. e.g. en-US) for the speech synthesization.  
Only available for Live API.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig languageCode anyOf item 0

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf SpeechConfig languageCode anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf item 1

Type: string  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig speechConfig anyOf item 2

Type: null  


##  audioTimestamp

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig audioTimestamp

#### Audiotimestamp

Default: null  


If enabled, audio timestamp will be included in the request to the  
model.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig audioTimestamp anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig audioTimestamp anyOf item 1

Type: null  


##  automaticFunctionCalling

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling

Default: null  


The configuration for automatic function calling.

##  Any of

  * AutomaticFunctionCallingConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig

#### AutomaticFunctionCallingConfig

Type: object  


The configuration for automatic function calling.

No Additional Properties

##  disable

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig disable

#### Disable

Default: null  


Whether to disable automatic function calling.  
If not set or set to False, will enable automatic function calling.  
If set to True, will disable automatic function calling.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig disable anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig disable anyOf item 1

Type: null  


##  maximumRemoteCalls

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig maximumRemoteCalls

#### Maximumremotecalls

Default: 10  


If automatic function calling is enabled,  
maximum number of remote calls for automatic function calling.  
This number should be a positive integer.  
If not set, SDK will set maximum number of remote calls to 10.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig maximumRemoteCalls anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig maximumRemoteCalls anyOf item 1

Type: null  


##  ignoreCallHistory

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig ignoreCallHistory

#### Ignorecallhistory

Default: null  


If automatic function calling is enabled,  
whether to ignore call history to the response.  
If not set, SDK will set ignore _call_ history to false,  
and will append the call history to  
GenerateContentResponse.automatic _function_ calling_history.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig ignoreCallHistory anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf AutomaticFunctionCallingConfig ignoreCallHistory anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig automaticFunctionCalling anyOf item 1

Type: null  


##  thinkingConfig

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig thinkingConfig

Default: null  


The thinking features configuration.

##  Any of

  * ThinkingConfig
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig thinkingConfig anyOf ThinkingConfig

#### ThinkingConfig

Type: object  


The thinking features configuration.

No Additional Properties

##  includeThoughts

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig thinkingConfig anyOf ThinkingConfig includeThoughts

#### Includethoughts

Default: null  


Indicates whether to include thoughts in the response. If true, thoughts are returned only if the model supports thought and thoughts are available.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig thinkingConfig anyOf ThinkingConfig includeThoughts anyOf item 0

Type: boolean  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig thinkingConfig anyOf ThinkingConfig includeThoughts anyOf item 1

Type: null  


##  thinkingBudget

root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig thinkingConfig anyOf ThinkingConfig thinkingBudget

#### Thinkingbudget

Default: null  


Indicates the thinking budget in tokens. 0 is DISABLED. -1 is AUTOMATIC. The default values and allowed ranges are model dependent.

##  Any of

  * Option 1
  * Option 2



root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig thinkingConfig anyOf ThinkingConfig thinkingBudget anyOf item 0

Type: integer  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig thinkingConfig anyOf ThinkingConfig thinkingBudget anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf GenerateContentConfig thinkingConfig anyOf item 1

Type: null  


root  anyOf LlmAgentConfig generate_content_config anyOf item 1

Type: null  


root  anyOf LoopAgentConfig

#### LoopAgentConfig

Type: object  


The config for the YAML schema of a LoopAgent.

No Additional Properties

##  agent_class

root  anyOf LoopAgentConfig agent_class

#### Agent Class

Type: const Default: "LoopAgent"  


The value is used to uniquely identify the LoopAgent class.

Specific value: `"LoopAgent"`

##  name Required

root  anyOf LoopAgentConfig name

#### Name

Type: string  


Required. The name of the agent.

##  description

root  anyOf LoopAgentConfig description

#### Description

Type: string Default: ""  


Optional. The description of the agent.

##  sub_agents

root  anyOf LoopAgentConfig sub_agents

#### Sub Agents

Default: null  


Optional. The sub-agents of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf LoopAgentConfig sub_agents anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LoopAgentConfig sub_agents anyOf item 0 AgentRefConfig

#### AgentRefConfig

Type: object  


The config for the reference to another agent.

Same definition as AgentRefConfig

root  anyOf LoopAgentConfig sub_agents anyOf item 1

Type: null  


##  before_agent_callbacks

root  anyOf LoopAgentConfig before_agent_callbacks

#### Before Agent Callbacks

Default: null  


Optional. The before _agent_ callbacks of the agent.

Example:  

    
    
    before_agent_callbacks:
      - name: my_library.security_callbacks.before_agent_callback  
    
      

##  Any of

  * Option 1
  * Option 2



root  anyOf LoopAgentConfig before_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LoopAgentConfig before_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf LoopAgentConfig before_agent_callbacks anyOf item 1

Type: null  


##  after_agent_callbacks

root  anyOf LoopAgentConfig after_agent_callbacks

#### After Agent Callbacks

Default: null  


Optional. The after _agent_ callbacks of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf LoopAgentConfig after_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf LoopAgentConfig after_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf LoopAgentConfig after_agent_callbacks anyOf item 1

Type: null  


##  max_iterations

root  anyOf LoopAgentConfig max_iterations

#### Max Iterations

Default: null  


Optional. LoopAgent.max_iterations.

##  Any of

  * Option 1
  * Option 2



root  anyOf LoopAgentConfig max_iterations anyOf item 0

Type: integer  


root  anyOf LoopAgentConfig max_iterations anyOf item 1

Type: null  


root  anyOf ParallelAgentConfig

#### ParallelAgentConfig

Type: object  


The config for the YAML schema of a ParallelAgent.

No Additional Properties

##  agent_class

root  anyOf ParallelAgentConfig agent_class

#### Agent Class

Type: const Default: "ParallelAgent"  


The value is used to uniquely identify the ParallelAgent class.

Specific value: `"ParallelAgent"`

##  name Required

root  anyOf ParallelAgentConfig name

#### Name

Type: string  


Required. The name of the agent.

##  description

root  anyOf ParallelAgentConfig description

#### Description

Type: string Default: ""  


Optional. The description of the agent.

##  sub_agents

root  anyOf ParallelAgentConfig sub_agents

#### Sub Agents

Default: null  


Optional. The sub-agents of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf ParallelAgentConfig sub_agents anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf ParallelAgentConfig sub_agents anyOf item 0 AgentRefConfig

#### AgentRefConfig

Type: object  


The config for the reference to another agent.

Same definition as AgentRefConfig

root  anyOf ParallelAgentConfig sub_agents anyOf item 1

Type: null  


##  before_agent_callbacks

root  anyOf ParallelAgentConfig before_agent_callbacks

#### Before Agent Callbacks

Default: null  


Optional. The before _agent_ callbacks of the agent.

Example:  

    
    
    before_agent_callbacks:
      - name: my_library.security_callbacks.before_agent_callback  
    
      

##  Any of

  * Option 1
  * Option 2



root  anyOf ParallelAgentConfig before_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf ParallelAgentConfig before_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf ParallelAgentConfig before_agent_callbacks anyOf item 1

Type: null  


##  after_agent_callbacks

root  anyOf ParallelAgentConfig after_agent_callbacks

#### After Agent Callbacks

Default: null  


Optional. The after _agent_ callbacks of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf ParallelAgentConfig after_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf ParallelAgentConfig after_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf ParallelAgentConfig after_agent_callbacks anyOf item 1

Type: null  


root  anyOf SequentialAgentConfig

#### SequentialAgentConfig

Type: object  


The config for the YAML schema of a SequentialAgent.

No Additional Properties

##  agent_class

root  anyOf SequentialAgentConfig agent_class

#### Agent Class

Type: const Default: "SequentialAgent"  


The value is used to uniquely identify the SequentialAgent class.

Specific value: `"SequentialAgent"`

##  name Required

root  anyOf SequentialAgentConfig name

#### Name

Type: string  


Required. The name of the agent.

##  description

root  anyOf SequentialAgentConfig description

#### Description

Type: string Default: ""  


Optional. The description of the agent.

##  sub_agents

root  anyOf SequentialAgentConfig sub_agents

#### Sub Agents

Default: null  


Optional. The sub-agents of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf SequentialAgentConfig sub_agents anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf SequentialAgentConfig sub_agents anyOf item 0 AgentRefConfig

#### AgentRefConfig

Type: object  


The config for the reference to another agent.

Same definition as AgentRefConfig

root  anyOf SequentialAgentConfig sub_agents anyOf item 1

Type: null  


##  before_agent_callbacks

root  anyOf SequentialAgentConfig before_agent_callbacks

#### Before Agent Callbacks

Default: null  


Optional. The before _agent_ callbacks of the agent.

Example:  

    
    
    before_agent_callbacks:
      - name: my_library.security_callbacks.before_agent_callback  
    
      

##  Any of

  * Option 1
  * Option 2



root  anyOf SequentialAgentConfig before_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf SequentialAgentConfig before_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf SequentialAgentConfig before_agent_callbacks anyOf item 1

Type: null  


##  after_agent_callbacks

root  anyOf SequentialAgentConfig after_agent_callbacks

#### After Agent Callbacks

Default: null  


Optional. The after _agent_ callbacks of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf SequentialAgentConfig after_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf SequentialAgentConfig after_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf SequentialAgentConfig after_agent_callbacks anyOf item 1

Type: null  


root  anyOf BaseAgentConfig

#### BaseAgentConfig

Type: object  


The config for the YAML schema of a BaseAgent.

Do not use this class directly. It's the base class for all agent configs.

##  agent_class

root  anyOf BaseAgentConfig agent_class

#### Agent Class

Default: "BaseAgent"  


Required. The class of the agent. The value is used to differentiate among different agent classes.

##  Any of

  * Option 1
  * Option 2



root  anyOf BaseAgentConfig agent_class anyOf item 0

Type: const  
Specific value: `"BaseAgent"`

root  anyOf BaseAgentConfig agent_class anyOf item 1

Type: string  


##  name Required

root  anyOf BaseAgentConfig name

#### Name

Type: string  


Required. The name of the agent.

##  description

root  anyOf BaseAgentConfig description

#### Description

Type: string Default: ""  


Optional. The description of the agent.

##  sub_agents

root  anyOf BaseAgentConfig sub_agents

#### Sub Agents

Default: null  


Optional. The sub-agents of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf BaseAgentConfig sub_agents anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf BaseAgentConfig sub_agents anyOf item 0 AgentRefConfig

#### AgentRefConfig

Type: object  


The config for the reference to another agent.

Same definition as AgentRefConfig

root  anyOf BaseAgentConfig sub_agents anyOf item 1

Type: null  


##  before_agent_callbacks

root  anyOf BaseAgentConfig before_agent_callbacks

#### Before Agent Callbacks

Default: null  


Optional. The before _agent_ callbacks of the agent.

Example:  

    
    
    before_agent_callbacks:
      - name: my_library.security_callbacks.before_agent_callback  
    
      

##  Any of

  * Option 1
  * Option 2



root  anyOf BaseAgentConfig before_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf BaseAgentConfig before_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf BaseAgentConfig before_agent_callbacks anyOf item 1

Type: null  


##  after_agent_callbacks

root  anyOf BaseAgentConfig after_agent_callbacks

#### After Agent Callbacks

Default: null  


Optional. The after _agent_ callbacks of the agent.

##  Any of

  * Option 1
  * Option 2



root  anyOf BaseAgentConfig after_agent_callbacks anyOf item 0

Type: array  
No Additional Items

#### Each item of this array must be:

root  anyOf BaseAgentConfig after_agent_callbacks anyOf item 0 CodeConfig

#### CodeConfig

Type: object  


Code reference config for a variable, a function, or a class.

This config is used for configuring callbacks and tools.

Same definition as CodeConfig

root  anyOf BaseAgentConfig after_agent_callbacks anyOf item 1

Type: null  


##  _Additional Properties_

Additional Properties of any type are allowed.

root  anyOf BaseAgentConfig additionalProperties

Type: object  


Generated using [json-schema-for-humans](https://github.com/coveooss/json-schema-for-humans) on 2025-08-20 at 20:50:19 +0000
