[ADK for TypeScript: API Reference](../index.html)

SystemLightDark

Search…




Preparing search index...

  * [ContainerCodeExecutorOptions]()



# Interface ContainerCodeExecutorOptions

Options for [ContainerCodeExecutor](../classes/ContainerCodeExecutor.html).

interface ContainerCodeExecutorOptions {  
baseUrl?: string;  
docker?: Dockerode;  
dockerPath?: string;  
image?: string;  
networkEnabled?: boolean;  
timeoutSeconds?: number;  
}

  * Defined in [core/src/code_executors/container_code_executor.ts:39](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L39)



## Properties

### `Optional`baseUrl

baseUrl?: string

Optional base url of a user-hosted Docker daemon (e.g. `tcp://host:2375`).

  * Defined in [core/src/code_executors/container_code_executor.ts:41](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L41)



### `Optional`docker

docker?: Dockerode

Injected Docker client, primarily for testing so unit tests never touch a real Docker daemon. Defaults to a new client built from `baseUrl`.

  * Defined in [core/src/code_executors/container_code_executor.ts:72](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L72)



### `Optional`dockerPath

dockerPath?: string

Path to a directory containing a Dockerfile. If set, the image is built from it instead of using a prebuilt tag. Either `image` or `dockerPath` must be set.

  * Defined in [core/src/code_executors/container_code_executor.ts:53](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L53)



### `Optional`image

image?: string

Tag of the predefined or custom image to run on the container. Either `image` or `dockerPath` must be set. Defaults to `adk-code-executor:latest` when only `dockerPath` is given.

  * Defined in [core/src/code_executors/container_code_executor.ts:47](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L47)



### `Optional`networkEnabled

networkEnabled?: boolean

Start the container with networking enabled. Defaults to false so untrusted, model-generated code cannot reach the network (the cloud metadata endpoint, internal services, or exfiltration destinations).

  * Defined in [core/src/code_executors/container_code_executor.ts:59](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L59)



### `Optional`timeoutSeconds

timeoutSeconds?: number

Wall-clock timeout in seconds for a single execution. Must be greater than 0; defaults to 300. Every execution shares one long-lived container, so an unbounded run (e.g. a loop emitted by the model) would burn that container's CPU for every later caller. Raise it rather than remove it for a computation that legitimately runs longer.

  * Defined in [core/src/code_executors/container_code_executor.ts:67](https://github.com/google/adk-js/blob/1c220dbbf5088598bdafe78777e9787baf6388e4/core/src/code_executors/container_code_executor.ts#L67)



Properties

baseUrldockerdockerPathimagenetworkEnabledtimeoutSeconds

[ADK for TypeScript: API Reference - v2.2.1](../index.html)

  * Loading...


