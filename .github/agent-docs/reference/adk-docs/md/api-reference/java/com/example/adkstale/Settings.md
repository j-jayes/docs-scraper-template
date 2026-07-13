JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../index.html)
  * Class
  * [Use](class-use/Settings.html)
  * [Tree](package-tree.html)
  * [Deprecated](../../../deprecated-list.html)
  * [Index](../../../index-all.html)
  * [Search](../../../search.html)
  * 


Select Theme

LightDarkSystem Setting

  1. [com.example.adkstale](package-summary.html)
  2. [Settings](Settings.html)



Contents  

  1. Description
  2. Method Summary
  3. Method Details
     1. githubToken()
     2. hasGithubToken()
     3. owner()
     4. repo()
     5. model()
     6. staleLabel()
     7. requestClarificationLabel()
     8. eventName()
     9. issueNumber()
     10. issueCountToProcess()
     11. maintainersOverride()
     12. isInteractive()
     13. isDryRun()
     14. staleHoursThreshold()
     15. closeHoursAfterStaleThreshold()
     16. graphqlCommentLimit()
     17. graphqlEditLimit()
     18. graphqlTimelineLimit()
     19. sleepBetweenIssuesMs()
     20. parseNumberString(String, int)

Hide sidebar  Show sidebar

# Class Settings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adkstale.Settings

* * *

public final class Settings extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Configuration read from environment variables. Mirrors `settings.py` in the Python ADK stale issue auditor. 

Values are exposed as **accessor methods** (read lazily on each call) rather than ` static final` fields. This keeps the class loadable in unit tests and agent loaders without a `GITHUB_TOKEN` present -- only `githubToken()` throws when the token is actually required (i.e. right before a network call). 

Required variables: 

  * `GITHUB_TOKEN` -- GitHub Personal Access Token (or the workflow's built-in token) with `issues:write`. Required for both interactive and workflow modes. 
  * `GOOGLE_API_KEY` -- Gemini API key. Required for both modes (or set up Vertex AI credentials and `GOOGLE_GENAI_USE_VERTEXAI=TRUE`). 


Optional variables (defaults match the Python sample unless noted): 

  * `OWNER` / `REPO` -- default to `google` / `adk-java`. 
  * `MODEL` -- Gemini model used for reasoning. Defaults to ` gemini-flash-latest`; this is a high-volume, low-complexity classification task for which a Flash model is the right cost/latency trade-off (the Python sample uses ` gemini-2.5-flash`). Overridable without a code change. 
  * `INTERACTIVE` -- `1`/`true` for interactive mode (asks for confirmation before mutating issues), `0`/`false` for unattended workflow mode. Defaults to interactive when unset. 
  * `DRY_RUN` -- `1`/`true` to log intended comments/labels/closures without calling the GitHub mutation endpoints. Defaults to off. 
  * `EVENT_NAME` -- the GitHub event that triggered the workflow (`schedule`, `workflow_dispatch`, `issues`, ...). Drives single-issue vs. batch behavior. 
  * `ISSUE_NUMBER` -- populated by GitHub Actions for issue events; audits that one issue. 
  * `ISSUE_COUNT_TO_PROCESS` -- max number of stale-candidate issues to audit per batch run. Defaults to `20`. 
  * `STALE_LABEL` -- the label that marks an issue as stale. Defaults to ` stale`. This label must exist in the repository. 
  * `REQUEST_CLARIFICATION_LABEL` -- label applied alongside `stale` when a maintainer asked for clarification. Defaults to `request clarification`. 
  * `MAINTAINERS` -- optional comma-separated list of GitHub handles to treat as maintainers. When set, it overrides the (push-access) collaborator lookup -- useful when the token cannot list collaborators. 
  * `STALE_HOURS_THRESHOLD` -- hours of inactivity after a maintainer question before an issue is marked stale. Defaults to `168` (7 days). 
  * `CLOSE_HOURS_AFTER_STALE_THRESHOLD` -- hours an issue may remain stale before it is closed. Defaults to `168` (7 days). 
  * `GRAPHQL_COMMENT_LIMIT` / `GRAPHQL_EDIT_LIMIT` / `GRAPHQL_TIMELINE_LIMIT` -- how many recent comments / body edits / timeline events to fetch per issue. Default to `30` / `10` / `20`. 
  * `SLEEP_BETWEEN_ISSUES_MS` -- pause between issues in a batch run to respect rate limits. Defaults to `1500`. 


  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static double`

`closeHoursAfterStaleThreshold()`

Hours an issue may stay marked stale before it is closed.

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`eventName()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`githubToken()`

Returns the GitHub token, throwing a clear error if it is not configured.

`static int`

`graphqlCommentLimit()`

 

`static int`

`graphqlEditLimit()`

 

`static int`

`graphqlTimelineLimit()`

 

`static boolean`

`hasGithubToken()`

Returns true if a `GITHUB_TOKEN` is configured, without throwing.

`static boolean`

`isDryRun()`

 

`static boolean`

`isInteractive()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`issueCountToProcess()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`issueNumber()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`maintainersOverride()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`model()`

Returns the Gemini model used for reasoning.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`owner()`

 

`static int`

`parseNumberString(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value, int defaultValue)`

Parses a number from a string, falling back to `defaultValue` on null/blank/invalid input.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`repo()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`requestClarificationLabel()`

 

`static long`

`sleepBetweenIssuesMs()`

 

`static double`

`staleHoursThreshold()`

Hours of inactivity after a maintainer question before an issue is marked stale.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`staleLabel()`

 

### Methods inherited from class [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#method-summary "class in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "clone\(\)"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "equals\(Object\)"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "finalize\(\)"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "getClass\(\)"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "hashCode\(\)"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "notify\(\)"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "notifyAll\(\)"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "toString\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "wait\(\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "wait\(long\)"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "wait\(long, int\)")`




  * ## Method Details

    * ### githubToken

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") githubToken()

Returns the GitHub token, throwing a clear error if it is not configured.

    * ### hasGithubToken

public static boolean hasGithubToken()

Returns true if a `GITHUB_TOKEN` is configured, without throwing.

    * ### owner

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") owner()

    * ### repo

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") repo()

    * ### model

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") model()

Returns the Gemini model used for reasoning. Defaults to `gemini-flash-latest` (a Flash model suits this high-volume, low-complexity decision task) and is overridable via the ` MODEL` environment variable.

    * ### staleLabel

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") staleLabel()

    * ### requestClarificationLabel

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") requestClarificationLabel()

    * ### eventName

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventName()

    * ### issueNumber

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") issueNumber()

    * ### issueCountToProcess

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") issueCountToProcess()

    * ### maintainersOverride

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") maintainersOverride()

    * ### isInteractive

public static boolean isInteractive()

    * ### isDryRun

public static boolean isDryRun()

    * ### staleHoursThreshold

public static double staleHoursThreshold()

Hours of inactivity after a maintainer question before an issue is marked stale.

    * ### closeHoursAfterStaleThreshold

public static double closeHoursAfterStaleThreshold()

Hours an issue may stay marked stale before it is closed.

    * ### graphqlCommentLimit

public static int graphqlCommentLimit()

    * ### graphqlEditLimit

public static int graphqlEditLimit()

    * ### graphqlTimelineLimit

public static int graphqlTimelineLimit()

    * ### sleepBetweenIssuesMs

public static long sleepBetweenIssuesMs()

    * ### parseNumberString

public static int parseNumberString(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value, int defaultValue)

Parses a number from a string, falling back to `defaultValue` on null/blank/invalid input. Mirrors `parse_number_string` in the Python utils.




* * *

Copyright (C) 1980\. All rights reserved.
