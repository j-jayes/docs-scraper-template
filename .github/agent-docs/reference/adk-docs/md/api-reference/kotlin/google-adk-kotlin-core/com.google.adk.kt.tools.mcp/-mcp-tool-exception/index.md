toggle menu

[ google-adk-kotlin ](../../../index.html)

0.5.0 

jvm

switch theme

search in API

[google-adk-kotlin-core](../../index.html)/[com.google.adk.kt.tools.mcp](../index.html)/McpToolException

# McpToolException

jvm

sealed class [McpToolException](index.html) : [RuntimeException](https://docs.oracle.com/javase/8/docs/api/java/lang/RuntimeException.html)

Base exception for MCP tools.

#### Inheritors

[McpToolDeclarationException](-mcp-tool-declaration-exception/index.html)

[McpToolLoadingException](-mcp-tool-loading-exception/index.html)

[McpToolExecutionException](-mcp-tool-execution-exception/index.html)

Members

## Types

[McpToolDeclarationException](-mcp-tool-declaration-exception/index.html)

Link copied to clipboard

jvm

class [McpToolDeclarationException](-mcp-tool-declaration-exception/index.html)(message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), cause: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [McpToolException](index.html)

Exception thrown when there's an error during MCP tool declaration generated.

[McpToolExecutionException](-mcp-tool-execution-exception/index.html)

Link copied to clipboard

jvm

class [McpToolExecutionException](-mcp-tool-execution-exception/index.html)(message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), cause: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [McpToolException](index.html)

Exception thrown when there's an error executing a built-in MCP tool.

[McpToolLoadingException](-mcp-tool-loading-exception/index.html)

Link copied to clipboard

jvm

class [McpToolLoadingException](-mcp-tool-loading-exception/index.html)(message: [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html), cause: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)? = null) : [McpToolException](index.html)

Exception thrown when there's an error during MCP tools loading/initialization.

## Properties

[cause](-mcp-tool-execution-exception/index.html#-654012527%2FProperties%2F-1959370187)

Link copied to clipboard

jvm

open val [cause](-mcp-tool-execution-exception/index.html#-654012527%2FProperties%2F-1959370187): [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)?

[message](-mcp-tool-execution-exception/index.html#1824300659%2FProperties%2F-1959370187)

Link copied to clipboard

jvm

open val [message](-mcp-tool-execution-exception/index.html#1824300659%2FProperties%2F-1959370187): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)?

## Functions

[addSuppressed](-mcp-tool-execution-exception/index.html#282858770%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

fun [addSuppressed](-mcp-tool-execution-exception/index.html#282858770%2FFunctions%2F-1959370187)(p0: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html))

[fillInStackTrace](-mcp-tool-execution-exception/index.html#-1102069925%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [fillInStackTrace](-mcp-tool-execution-exception/index.html#-1102069925%2FFunctions%2F-1959370187)(): [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)

[getLocalizedMessage](-mcp-tool-execution-exception/index.html#1043865560%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [getLocalizedMessage](-mcp-tool-execution-exception/index.html#1043865560%2FFunctions%2F-1959370187)(): [String](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-string/index.html)

[getStackTrace](-mcp-tool-execution-exception/index.html#2050903719%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [getStackTrace](-mcp-tool-execution-exception/index.html#2050903719%2FFunctions%2F-1959370187)(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html)<[StackTraceElement](https://docs.oracle.com/javase/8/docs/api/java/lang/StackTraceElement.html)>

[getSuppressed](-mcp-tool-execution-exception/index.html#672492560%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

fun [getSuppressed](-mcp-tool-execution-exception/index.html#672492560%2FFunctions%2F-1959370187)(): [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html)<[Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)>

[initCause](-mcp-tool-execution-exception/index.html#-418225042%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [initCause](-mcp-tool-execution-exception/index.html#-418225042%2FFunctions%2F-1959370187)(p0: [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)): [Throwable](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-throwable/index.html)

[printStackTrace](-mcp-tool-execution-exception/index.html#-1769529168%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [printStackTrace](-mcp-tool-execution-exception/index.html#-1769529168%2FFunctions%2F-1959370187)()

open fun [printStackTrace](-mcp-tool-execution-exception/index.html#1841853697%2FFunctions%2F-1959370187)(p0: [PrintStream](https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html))

open fun [printStackTrace](-mcp-tool-execution-exception/index.html#1175535278%2FFunctions%2F-1959370187)(p0: [PrintWriter](https://docs.oracle.com/javase/8/docs/api/java/io/PrintWriter.html))

[setStackTrace](-mcp-tool-execution-exception/index.html#2135801318%2FFunctions%2F-1959370187)

Link copied to clipboard

jvm

open fun [setStackTrace](-mcp-tool-execution-exception/index.html#2135801318%2FFunctions%2F-1959370187)(p0: [Array](https://kotlinlang.org/api/latest/jvm/stdlib/kotlin-stdlib/kotlin/-array/index.html)<[StackTraceElement](https://docs.oracle.com/javase/8/docs/api/java/lang/StackTraceElement.html)>)

© 2026 CopyrightGenerated by [dokka](https://github.com/Kotlin/dokka)
