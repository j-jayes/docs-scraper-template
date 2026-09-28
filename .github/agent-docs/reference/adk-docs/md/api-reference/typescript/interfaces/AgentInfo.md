[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [AgentInfo]()



# Interface AgentInfo

interface AgentInfo {  
card?: { content?: AgentCard; type?: string };  
description?: string;  
displayName?: string;  
interfaces?: [Interface](Interface.html)[];  
protocols?: {  
interfaces?: [Interface](Interface.html)[];  
protocolVersion?: string;  
type?: [ProtocolType](../enums/ProtocolType.html);  
}[];  
skills?: [AgentSkillMetadata](AgentSkillMetadata.html)[];  
version?: string;  
[key: string]: unknown;  
}

#### Indexable

  * [key: string]: unknown




  * Defined in [core/src/integrations/agent_registry/types.ts:91](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/types.ts#L91)



## Properties

### `Optional`card

card?: { content?: AgentCard; type?: string }

  * Defined in [core/src/integrations/agent_registry/types.ts:95](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/types.ts#L95)



### `Optional`description

description?: string

  * Defined in [core/src/integrations/agent_registry/types.ts:93](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/types.ts#L93)



### `Optional`displayName

displayName?: string

  * Defined in [core/src/integrations/agent_registry/types.ts:92](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/types.ts#L92)



### `Optional`interfaces

interfaces?: [Interface](Interface.html)[]

  * Defined in [core/src/integrations/agent_registry/types.ts:99](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/types.ts#L99)



### `Optional`protocols

protocols?: {  
interfaces?: [Interface](Interface.html)[];  
protocolVersion?: string;  
type?: [ProtocolType](../enums/ProtocolType.html);  
}[]

  * Defined in [core/src/integrations/agent_registry/types.ts:100](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/types.ts#L100)



### `Optional`skills

skills?: [AgentSkillMetadata](AgentSkillMetadata.html)[]

  * Defined in [core/src/integrations/agent_registry/types.ts:105](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/types.ts#L105)



### `Optional`version

version?: string

  * Defined in [core/src/integrations/agent_registry/types.ts:94](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/integrations/agent_registry/types.ts#L94)



Properties

carddescriptiondisplayNameinterfacesprotocolsskillsversion

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


