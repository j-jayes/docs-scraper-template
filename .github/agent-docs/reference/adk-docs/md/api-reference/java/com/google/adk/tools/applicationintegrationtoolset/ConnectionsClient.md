JavaScript is disabled on your browser.

   

Skip navigation links

  * [Overview](../../../../../index.html)
  * Class
  * [Use](class-use/ConnectionsClient.html)
  * [Tree](package-tree.html)
  * [Index](../../../../../index-all.html)
  * [Search](../../../../../search.html)



  1. [com.google.adk.tools.applicationintegrationtoolset](package-summary.html)
  2. [ConnectionsClient](ConnectionsClient.html)



Contents 

Hide sidebar ❮❯ Show sidebar

  1. Description
  2. Nested Class Summary
  3. Constructor Summary
  4. Method Summary
  5. Constructor Details
     1. ConnectionsClient(String, String, String, IntegrationConnectorTool.HttpExecutor, ObjectMapper)
  6. Method Details
     1. getConnectionDetails()
     2. getEntitySchemaAndOperations(String)
     3. getActionSchema(String)
     4. convertJsonSchemaToOpenApiSchema(Map)
     5. connectorPayload(Map)
     6. getConnectorBaseSpec()
     7. getActionOperation(String, String, String, String, String)
     8. listOperation(String, String, String, String)
     9. getOperation(String, String, String, String)
     10. createOperation(String, String, String)
     11. updateOperation(String, String, String)
     12. deleteOperation(String, String, String)
     13. createOperationRequest(String)
     14. updateOperationRequest(String)
     15. getOperationRequest()
     16. deleteOperationRequest()
     17. listOperationRequest()
     18. actionRequest(String)
     19. actionResponse(String)
     20. executeCustomQueryRequest()



# Class ConnectionsClient

[java.lang.Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

com.google.adk.tools.applicationintegrationtoolset.ConnectionsClient

* * *

public class ConnectionsClient extends [Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

Utility class for interacting with the Google Cloud Connectors API. 

This class provides methods to fetch connection details, schemas for entities and actions, and to generate OpenAPI specifications for creating tools based on these connections.

  * ## Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

`static class `

`[ConnectionsClient.ActionSchema](ConnectionsClient.ActionSchema.html "class in com.google.adk.tools.applicationintegrationtoolset")`

Represents the schema for an action.

`static class `

`[ConnectionsClient.ConnectionDetails](ConnectionsClient.ConnectionDetails.html "class in com.google.adk.tools.applicationintegrationtoolset")`

Represents details of a connection.

`static class `

`[ConnectionsClient.EntitySchemaAndOperations](ConnectionsClient.EntitySchemaAndOperations.html "class in com.google.adk.tools.applicationintegrationtoolset")`

Represents the schema and available operations for an entity.

  * ## Constructor Summary

Constructors

Constructor

Description

`ConnectionsClient([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") project, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") location, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connection, com.google.adk.tools.applicationintegrationtoolset.IntegrationConnectorTool.HttpExecutor httpExecutor, com.fasterxml.jackson.databind.ObjectMapper objectMapper)`

Initializes the ConnectionsClient.

  * ## Method Summary

All MethodsStatic MethodsInstance MethodsConcrete Methods

Modifier and Type

Method

Description

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`actionRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") action)`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`actionResponse([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") action)`

 

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`connectorPayload([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> jsonSchema)`

 

`[Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`convertJsonSchemaToOpenApiSchema([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> jsonSchema)`

Converts a JSON Schema dictionary to an OpenAPI schema dictionary.

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`createOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`createOperationRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity)`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`deleteOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`deleteOperationRequest()`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`executeCustomQueryRequest()`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`getActionOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") action, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") operation, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") actionDisplayName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)`

 

`[ConnectionsClient.ActionSchema](ConnectionsClient.ActionSchema.html "class in com.google.adk.tools.applicationintegrationtoolset")`

`getActionSchema([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") action)`

Retrieves the input and output JSON schema for a given action.

`[ConnectionsClient.ConnectionDetails](ConnectionsClient.ConnectionDetails.html "class in com.google.adk.tools.applicationintegrationtoolset")`

`getConnectionDetails()`

Retrieves service details for a given connection.

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`getConnectorBaseSpec()`

 

`[ConnectionsClient.EntitySchemaAndOperations](ConnectionsClient.EntitySchemaAndOperations.html "class in com.google.adk.tools.applicationintegrationtoolset")`

`getEntitySchemaAndOperations([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity)`

Retrieves the JSON schema and available operations for a given entity.

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`getOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") schemaAsString, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`getOperationRequest()`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`listOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") schemaAsString, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`listOperationRequest()`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`updateOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)`

 

`static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")>`

`updateOperationRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity)`

 

### Methods inherited from class java.lang.[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")

`[clone](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#clone\(\) "class or interface in java.lang"), [equals](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#equals\(java.lang.Object\) "class or interface in java.lang"), [finalize](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#finalize\(\) "class or interface in java.lang"), [getClass](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#getClass\(\) "class or interface in java.lang"), [hashCode](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#hashCode\(\) "class or interface in java.lang"), [notify](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notify\(\) "class or interface in java.lang"), [notifyAll](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#notifyAll\(\) "class or interface in java.lang"), [toString](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#toString\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long\) "class or interface in java.lang"), [wait](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html#wait\(long,int\) "class or interface in java.lang")`




  * ## Constructor Details

    * ### ConnectionsClient

public ConnectionsClient([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") project, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") location, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") connection, com.google.adk.tools.applicationintegrationtoolset.IntegrationConnectorTool.HttpExecutor httpExecutor, com.fasterxml.jackson.databind.ObjectMapper objectMapper)

Initializes the ConnectionsClient.

Parameters:
    `project` \- The Google Cloud project ID.
    `location` \- The Google Cloud location (e.g., us-central1).
    `connection` \- The connection name.

  * ## Method Details

    * ### getConnectionDetails

public [ConnectionsClient.ConnectionDetails](ConnectionsClient.ConnectionDetails.html "class in com.google.adk.tools.applicationintegrationtoolset") getConnectionDetails() throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")

Retrieves service details for a given connection.

Returns:
    A [`ConnectionsClient.ConnectionDetails`](ConnectionsClient.ConnectionDetails.html "class in com.google.adk.tools.applicationintegrationtoolset") object with the connection's info.
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` \- If there is an issue with network communication or credentials.
    `[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")` \- If the thread is interrupted during the API call.

    * ### getEntitySchemaAndOperations

public [ConnectionsClient.EntitySchemaAndOperations](ConnectionsClient.EntitySchemaAndOperations.html "class in com.google.adk.tools.applicationintegrationtoolset") getEntitySchemaAndOperations([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")

Retrieves the JSON schema and available operations for a given entity.

Parameters:
    `entity` \- The entity name.
Returns:
    A [`ConnectionsClient.EntitySchemaAndOperations`](ConnectionsClient.EntitySchemaAndOperations.html "class in com.google.adk.tools.applicationintegrationtoolset") object.
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` \- If there is an issue with network communication or credentials.
    `[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")` \- If the thread is interrupted during polling.

    * ### getActionSchema

public [ConnectionsClient.ActionSchema](ConnectionsClient.ActionSchema.html "class in com.google.adk.tools.applicationintegrationtoolset") getActionSchema([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") action) throws [IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io"), [InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")

Retrieves the input and output JSON schema for a given action.

Parameters:
    `action` \- The action name.
Returns:
    An [`ConnectionsClient.ActionSchema`](ConnectionsClient.ActionSchema.html "class in com.google.adk.tools.applicationintegrationtoolset") object.
Throws:
    `[IOException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/io/IOException.html "class or interface in java.io")` \- If there is an issue with network communication or credentials.
    `[InterruptedException](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/InterruptedException.html "class or interface in java.lang")` \- If the thread is interrupted during polling.

    * ### convertJsonSchemaToOpenApiSchema

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> convertJsonSchemaToOpenApiSchema([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> jsonSchema)

Converts a JSON Schema dictionary to an OpenAPI schema dictionary.

Parameters:
    `jsonSchema` \- The input JSON schema map.
Returns:
    The converted OpenAPI schema map.

    * ### connectorPayload

public [Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> connectorPayload([Map](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/util/Map.html "class or interface in java.util")<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> jsonSchema)

    * ### getConnectorBaseSpec

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> getConnectorBaseSpec()

    * ### getActionOperation

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> getActionOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") action, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") operation, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") actionDisplayName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)

    * ### listOperation

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> listOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") schemaAsString, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)

    * ### getOperation

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> getOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") schemaAsString, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)

    * ### createOperation

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> createOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)

    * ### updateOperation

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> updateOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)

    * ### deleteOperation

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> deleteOperation([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolName, [String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") toolInstructions)

    * ### createOperationRequest

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> createOperationRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity)

    * ### updateOperationRequest

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> updateOperationRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") entity)

    * ### getOperationRequest

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> getOperationRequest()

    * ### deleteOperationRequest

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> deleteOperationRequest()

    * ### listOperationRequest

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> listOperationRequest()

    * ### actionRequest

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> actionRequest([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") action)

    * ### actionResponse

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> actionResponse([String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang") action)

    * ### executeCustomQueryRequest

public static com.google.common.collect.ImmutableMap<[String](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/String.html "class or interface in java.lang"),[Object](https://docs.oracle.com/en/java/javase/17/docs/api/java.base/java/lang/Object.html "class or interface in java.lang")> executeCustomQueryRequest()




* * *

Copyright (C) 2025\. All rights reserved.
