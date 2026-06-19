# Dependency Injection in NestJS

## Goal
Understand how dependency injection (DI) works in NestJS and why it is fundamental to the framework.

## Reflection

### 1. How does dependency injection improve maintainability?
* Decoupling — A class depends on an abstraction (or another class's public interface) rather than constructing its own dependencies, so the implementation behind that dependency can change without touching the class that uses it.
* Easier testing — In unit tests, you can inject a mock or stub instead of the real provider, without modifying the class under test.
* Single point of change — If a service's constructor needs new dependencies, you update that one place rather than every spot that previously called new.
* Consistent lifecycle management — Nest manages instance creation centrally, so you're not scattering object-creation logic throughout the codebase.



### 2. What is the purpose of the @Injectable() decorator?
`@Injectable()` marks a class as something Nest's DI container is allowed to manage — it tells Nest this class can be instantiated, have its own dependencies injected into it, and in turn be injected into other classes (controllers, other services, guards, etc.). 
* Without it, Nest has no metadata about the class's constructor parameters and can't construct it automatically. 
* It's also what allows a class to optionally declare a scope (like Scope.REQUEST), since scope is configured through this same decorator.


### 3. What are the different types of provider scopes, and when would you use each?
* DEFAULT (singleton) — One instance created when the application starts, shared by every part of the app for the app's entire lifetime. 
    * This is the default for almost everything, since most services (logging, config, generic business logic) don't need per-request state and sharing one instance is more efficient.
* REQUEST — A new instance created for every incoming request, and reused only within that single request.
    * Useful when a provider needs to hold request-specific state 
    * For example, tracking a request ID throughout a request's lifecycle, or a service that depends on another REQUEST-scoped provider (scope is "infectious" upward through the dependency chain).
* TRANSIENT — A new instance created every single time the provider is injected, even multiple times within the same request. 
    * Useful for lightweight, stateless helper classes where you specifically want no sharing at all, even within one request — though it's the least commonly used of the three since it gives up the efficiency of caching without the request-tracking benefit REQUEST offers.


### 4. How does NestJS automatically resolve dependencies?

* When Nest builds the application, it scans each provider's constructor for parameter types (this is why TypeScript's type metadata matters — Nest relies on it under the hood, via reflect-metadata).
*  For each parameter, Nest looks at the module graph to find a provider matching that type, instantiates it if it hasn't already (respecting whatever scope is configured), and passes it in. 
* This happens recursively — if TasksService itself depended on something else, Nest would resolve that first — building up a full dependency tree before anything actually runs. 
* As long as a provider is registered somewhere in the visible module graph (in the same module, or exported by an imported module), you never have to manually wire it up; declaring it as a constructor parameter is enough for Nest to find and supply it.




