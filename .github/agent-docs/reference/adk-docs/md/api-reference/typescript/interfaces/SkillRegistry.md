[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SkillRegistry]()



# Interface SkillRegistry

Interface for a skill registry.

interface SkillRegistry {  
close?(): Promise<void>;  
getSkill(name: string): Promise<[Skill](Skill.html)>;  
searchSkills(query: string): Promise<[Frontmatter](Frontmatter.html)[]>;  
searchToolDescription?(): string | undefined;  
}

#### Implemented by

  * [GCPSkillRegistry](../classes/GCPSkillRegistry.html)



  * Defined in [core/src/skills/skill_registry.ts:12](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/skills/skill_registry.ts#L12)



## Methods

### `Optional`close

  * close?(): Promise<void>

Releases resources held by the registry, such as network clients or temporary credentials.

Optional: registries that hold no resources may omit it. `SkillToolset` invokes it, when present, from its own `close()`.

#### Returns Promise<void>

    * Defined in [core/src/skills/skill_registry.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/skills/skill_registry.ts#L41)




### getSkill

  * getSkill(name: string): Promise<[Skill](Skill.html)>

Fetches a skill from the registry.

#### Parameters

    * name: string

The name of the skill.

#### Returns Promise<[Skill](Skill.html)>

A Promise resolving to a Skill object.

    * Defined in [core/src/skills/skill_registry.ts:19](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/skills/skill_registry.ts#L19)




### searchSkills

  * searchSkills(query: string): Promise<[Frontmatter](Frontmatter.html)[]>

Searches for skills in the registry.

#### Parameters

    * query: string

The search query.

#### Returns Promise<[Frontmatter](Frontmatter.html)[]>

A Promise resolving to a list of Frontmatter objects for discovery.

    * Defined in [core/src/skills/skill_registry.ts:27](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/skills/skill_registry.ts#L27)




### `Optional`searchToolDescription

  * searchToolDescription?(): string | undefined

Returns the description for the search_skills tool.

#### Returns string | undefined

    * Defined in [core/src/skills/skill_registry.ts:32](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/skills/skill_registry.ts#L32)




Methods

closegetSkillsearchSkillssearchToolDescription

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


