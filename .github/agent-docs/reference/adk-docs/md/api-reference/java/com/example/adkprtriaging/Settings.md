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

  1. [com.example.adkprtriaging](package-summary.html)
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
     7. pullRequestNumber()
     8. isInteractive()
     9. isDryRun()
     10. contributingGuidelines()
     11. parseNumberString(String, int)

Hide sidebar  Show sidebar

# Class Settings

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

com.example.adkprtriaging.Settings

* * *

public final class Settings extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class in java.lang")

Configuration read from environment variables. Mirrors `settings.py` in the Python ADK PR triaging agent, and matches the lazy-accessor style of the sibling ADK Issue Triaging Agent sample. 

Values are exposed as **accessor methods** (read lazily on each call) rather than ` static final` fields. This keeps the class loadable in unit tests and `adk web` agent loaders without a `GITHUB_TOKEN` present -- only `githubToken()` throws when the token is actually required (i.e. right before a network call). 

Required variables: 

  * `GITHUB_TOKEN` -- GitHub Personal Access Token with `pull_requests:write` permission. Required for both interactive and workflow modes. 
  * `GOOGLE_API_KEY` -- Gemini API key. Required for both modes (or set up Vertex AI credentials and `GOOGLE_GENAI_USE_VERTEXAI=TRUE`). 


Optional variables: 

  * `OWNER` -- defaults to `google`. 
  * `REPO` -- defaults to `adk-java`. 
  * `MODEL` -- Gemini model used for triaging. Defaults to ` gemini-pro-latest`; a Pro model favors classification quality over latency, which suits this low-volume, accuracy-sensitive task. Overridable without a code change. 
  * `INTERACTIVE` -- `1`/`true` for interactive mode (asks for confirmation before labeling/commenting), `0`/`false` for unattended workflow mode. Defaults to interactive when unset. 
  * `DRY_RUN` -- `1`/`true` to log intended label/comment changes without calling the GitHub mutation endpoints. Lets you verify the full pipeline (incl. Gemini) without modifying any real pull request. Defaults to off. 
  * `PULL_REQUEST_NUMBER` -- the pull request to triage in workflow mode. Populated by the GitHub Actions workflow from the triggering PR. 
  * `EVENT_NAME` -- the GitHub event that triggered the workflow (` pull_request_target`, `workflow_dispatch`, ...). Logged for diagnostics. 
  * `CONTRIBUTING_MD_PATH` -- path to the repository's `CONTRIBUTING.md` (default `CONTRIBUTING.md`, resolved against the working directory, which is the repo root in the workflow). Its content is embedded in the agent instruction so the guideline check stays in sync with the repo. Missing file is tolerated (empty content). 


  * ## Method Summary

All MethodsStatic MethodsConcrete Methods

Modifier and Type

Method

Description

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`contributingGuidelines()`

Reads the repository's `CONTRIBUTING.md` (path overridable via ` CONTRIBUTING_MD_PATH`) so the agent can check pull requests against the real contribution guidelines, mirroring the Python agent's `read_file(CONTRIBUTING.md)`.

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`eventName()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`githubToken()`

Returns the GitHub token, throwing a clear error if it is not configured.

`static boolean`

`hasGithubToken()`

Returns true if a `GITHUB_TOKEN` is configured, without throwing.

`static boolean`

`isDryRun()`

 

`static boolean`

`isInteractive()`

 

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`model()`

Returns the Gemini model used for triaging.

`static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`owner()`

 

`static int`

`parseNumberString(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value, int defaultValue)`

Parses a number from a string, falling back to `defaultValue` on null/blank/invalid input.

`static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang")`

`pullRequestNumber()`

 

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

    * ### pullRequestNumber

public static @Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") pullRequestNumber()

    * ### isInteractive

public static boolean isInteractive()

    * ### isDryRun

public static boolean isDryRun()

    * ### contributingGuidelines

public static [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") contributingGuidelines()

Reads the repository's `CONTRIBUTING.md` (path overridable via ` CONTRIBUTING_MD_PATH`) so the agent can check pull requests against the real contribution guidelines, mirroring the Python agent's `read_file(CONTRIBUTING.md)`. Returns an empty string if the file cannot be read (e.g. in unit tests or when the working directory is not the repo root), so callers never need to handle an exception.

    * ### parseNumberString

public static int parseNumberString(@Nullable [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class in java.lang") value, int defaultValue)

Parses a number from a string, falling back to `defaultValue` on null/blank/invalid input. Mirrors `parse_number_string` in the Python utils.




* * *

Copyright (C) 1980\. All rights reserved.
