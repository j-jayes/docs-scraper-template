[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [SkillRegistry]()



# Interface SkillRegistry

Interface for a skill registry.

interface SkillRegistry {  
getSkill(name: string): Promise<[Skill](Skill.html)>;  
searchSkills(query: string): Promise<[Frontmatter](Frontmatter.html)[]>;  
searchToolDescription?(): string | undefined;  
}

#### Implemented by

  * [GCPSkillRegistry](../classes/GCPSkillRegistry.html)



  * Defined in [core/src/skills/skill_registry.ts:12](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/skills/skill_registry.ts#L12)



## Methods

### getSkill

  * getSkill(name: string): Promise<[Skill](Skill.html)>

Fetches a skill from the registry.

#### Parameters

    * name: string

The name of the skill.

#### Returns Promise<[Skill](Skill.html)>

A Promise resolving to a Skill object.

    * Defined in [core/src/skills/skill_registry.ts:19](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/skills/skill_registry.ts#L19)




### searchSkills

  * searchSkills(query: string): Promise<[Frontmatter](Frontmatter.html)[]>

Searches for skills in the registry.

#### Parameters

    * query: string

The search query.

#### Returns Promise<[Frontmatter](Frontmatter.html)[]>

A Promise resolving to a list of Frontmatter objects for discovery.

    * Defined in [core/src/skills/skill_registry.ts:27](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/skills/skill_registry.ts#L27)




### `Optional`searchToolDescription

  * searchToolDescription?(): string | undefined

Returns the description for the search_skills tool.

#### Returns string | undefined

    * Defined in [core/src/skills/skill_registry.ts:32](https://github.com/google/adk-js/blob/be3edbe2d6d74bfc3753db87b7a31e992d5ad9ca/core/src/skills/skill_registry.ts#L32)




Methods

getSkillsearchSkillssearchToolDescription

[ADK for TypeScript: API Reference - v1.5.0](../index.html)

  * Loading...


