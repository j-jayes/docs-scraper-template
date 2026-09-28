[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [GCPSkillRegistry]()



# Class GCPSkillRegistry

GCP implementation of SkillRegistry using GCP Skill Registry API.

#### Implements

  * [SkillRegistry](../interfaces/SkillRegistry.html)



  * Defined in [core/src/skills/gcp_skill_registry.ts:23](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/skills/gcp_skill_registry.ts#L23)



## Constructors

### constructor

  * new GCPSkillRegistry(options?: [GCPSkillRegistryOptions](../interfaces/GCPSkillRegistryOptions.html)): [GCPSkillRegistry]()

#### Parameters

    * options: [GCPSkillRegistryOptions](../interfaces/GCPSkillRegistryOptions.html) = {}

#### Returns [GCPSkillRegistry]()

    * Defined in [core/src/skills/gcp_skill_registry.ts:28](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/skills/gcp_skill_registry.ts#L28)




## Methods

### getSkill

  * getSkill(name: string): Promise<[Skill](../interfaces/Skill.html)>

Fetches a skill from the registry.

#### Parameters

    * name: string

The name of the skill.

#### Returns Promise<[Skill](../interfaces/Skill.html)>

A Promise resolving to a Skill object.

Implementation of [SkillRegistry](../interfaces/SkillRegistry.html).[getSkill](../interfaces/SkillRegistry.html#getskill)

    * Defined in [core/src/skills/gcp_skill_registry.ts:39](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/skills/gcp_skill_registry.ts#L39)




### searchSkills

  * searchSkills(query: string): Promise<[Frontmatter](../interfaces/Frontmatter.html)[]>

Searches for skills in the registry.

#### Parameters

    * query: string

The search query.

#### Returns Promise<[Frontmatter](../interfaces/Frontmatter.html)[]>

A Promise resolving to a list of Frontmatter objects for discovery.

Implementation of [SkillRegistry](../interfaces/SkillRegistry.html).[searchSkills](../interfaces/SkillRegistry.html#searchskills)

    * Defined in [core/src/skills/gcp_skill_registry.ts:68](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/skills/gcp_skill_registry.ts#L68)




Constructors

constructor

Methods

getSkillsearchSkills

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


