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

  1. [com.example.adktriaging](package-summary.html)
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
     6. eventName()
     7. issueNumber()
     8. issueTitle()
     9. issueBody()
     10. issueCountToProcess()
     11. gtechAssignees()
     12. isInteractive()
     13. isDryRun()
     14. parseNumberString(String, int)

Hide sidebar  Show sidebar

# Class Settings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adktriaging.Settings

* * *

public final class Settings extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Configuration read from environment variables. Mirrors `settings.py` in the Python ADK issue triaging agent. 

Values are exposed as **accessor methods** (read lazily on each call) rather than ` static final` fields. This keeps the class loadable in unit tests and agent loaders without a `GITHUB_TOKEN` present -- only `githubToken()` throws when the token is actually required (i.e. right before a network call). 

Required variables: 

  * `GITHUB_TOKEN` -- GitHub Personal Access Token with `issues:write` permission. Required for both interactive and workflow modes. 
  * `GOOGLE_API_KEY` -- Gemini API key. Required for both modes (or set up Vertex AI credentials and `GOOGLE_GENAI_USE_VERTEXAI=TRUE`). 


Optional variables: 

  * `OWNER` -- defaults to `google`. 
  * `REPO` -- defaults to `adk-java`. 
  * `MODEL` -- Gemini model used for triaging. Defaults to `gemini-2.5-pro`; a Pro model favors classification quality over latency, which suits this low-volume, accuracy-sensitive task. Overridable without a code change. 
  * `INTERACTIVE` -- `1`/`true` for interactive mode (asks for confirmation before applying labels), `0`/`false` for unattended workflow mode. Defaults to interactive when unset. 
  * `DRY_RUN` -- `1`/`true` to log intended label/assignment changes without calling the GitHub mutation endpoints. Lets you verify the full pipeline (incl. Gemini) without modifying any real issue. Defaults to off. 
  * `EVENT_NAME` -- the GitHub event that triggered the workflow (`issues`, `schedule`, etc.). Drives single-issue vs. batch behavior in [`AdkTriagingAgentRun`](AdkTriagingAgentRun.html "class in com.example.adktriaging"). 
  * `ISSUE_NUMBER`, `ISSUE_TITLE`, `ISSUE_BODY` -- populated by the GitHub Actions workflow when the trigger is an issue event. 
  * `ISSUE_COUNT_TO_PROCESS` -- how many untriaged issues to process per scheduled run. Defaults to `3`. 
  * `GTECH_ASSIGNEES` -- comma-separated list of GitHub handles to round-robin assign issues to. When unset, owner assignment is disabled (the agent reports that no triagers are configured). adk-java has no public `CODEOWNERS`, so real handles are supplied here rather than hard-coded in source. 


  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`eventName()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`githubToken()`

Returns the GitHub token, throwing a clear error if it is not configured.

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`gtechAssignees()`

 

`static boolean`

`hasGithubToken()`

Returns true if a `GITHUB_TOKEN` is configured, without throwing.

`static boolean`

`isDryRun()`

 

`static boolean`

`isInteractive()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`issueBody()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`issueCountToProcess()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`issueNumber()`

 

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`issueTitle()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`model()`

Returns the Gemini model used for triaging.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`owner()`

 

`static int`

`parseNumberString(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value, int defaultValue)`

Parses a number from a string, falling back to `defaultValue` on null/blank/invalid input.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`repo()`

 

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

Returns the Gemini model used for triaging. Defaults to `gemini-pro-latest` (a Pro model favors classification quality over latency for this low-volume, accuracy-sensitive task) and is overridable via the `MODEL` environment variable, so it can be changed without editing source.

    * ### eventName

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") eventName()

    * ### issueNumber

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") issueNumber()

    * ### issueTitle

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") issueTitle()

    * ### issueBody

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") issueBody()

    * ### issueCountToProcess

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") issueCountToProcess()

    * ### gtechAssignees

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") gtechAssignees()

    * ### isInteractive

public static boolean isInteractive()

    * ### isDryRun

public static boolean isDryRun()

    * ### parseNumberString

public static int parseNumberString(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value, int defaultValue)

Parses a number from a string, falling back to `defaultValue` on null/blank/invalid input. Mirrors `parse_number_string` in the Python utils.




* * *

Copyright (C) 1980\. All rights reserved.
