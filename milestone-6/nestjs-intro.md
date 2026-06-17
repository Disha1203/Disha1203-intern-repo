# What is NestJS? (Framework Overview)

## Goal

Understand the NestJS framework, how it differs from Express.js, and why it is used in backend development.

## Architecture

### Modules
* A Module is a logical boundary – a container that groups related components (controllers, providers, and even other modules).
* Every NestJS app has at least one root module (usually `AppModule`), and you create feature modules (`UsersModule`, `AuthModule`, and so on) to organize code by domain.

### Controllers
* A Controller maps incoming HTTP requests to handler methods.
* It’s responsible for extracting request data (query parameters, body, headers) and returning a response. 
* Controllers should remain thin – delegating business logic to providers.

### Services
* Services are classes annotated with `@Injectable()` that contain your business logic or data access. 
* Anything you want to inject elsewhere must be a service. 
* You can provide plain values, factory functions, or classes.


## Reflection

### What are the key differences between NestJS and Express.js?

* **Framework Type**: NestJS is a full-featured Node.js framework, while Express.js is a minimal web framework.
* **Underlying Technology**: NestJS runs on top of Express.js by default (or Fastify), adding an additional architectural layer.
* **TypeScript Support**: NestJS is built with and optimized for TypeScript; Express.js supports TypeScript but requires additional setup.
* **Architecture**: NestJS follows a structured, opinionated architecture , whereas Express.js is unopinionated and lets developers choose their own structure.
* **Project Organization**: NestJS organizes code into modules, controllers, and services/providers; Express.js does not enforce any specific organization.
* **Scalability**: NestJS is designed for large, maintainable applications, while Express.js can become difficult to manage as projects grow if conventions are not established.
* **Dependency Injection**: NestJS provides built-in dependency injection; Express.js requires manual dependency management.
* **Development Approach**: Express.js acts as a toolkit that provides routing and middleware, whereas NestJS acts as a complete application framework built on top of that toolkit.*


### Why does NestJS use decorators extensively?
* Decorators allow devs to define app behavior declaratively using metadata.
* They reduce boilerplate code by eliminating the need for manual route and dependency registration.
* They make code more readable and self-descriptive.
* They help NestJS identify and configure controllers, services, modules, and routes automatically.
* They simplify request handling by extracting parameters, headers, and request bodies.
* They enable framework features such as guards, interceptors, pipes, and middleware.
* They provide a consistent structure across the application.

### How does NestJS handle dependency injection?
* NestJS includes a built-in Dependency Injection container.
* Services are registered as providers using the `@Injectable()` decorator.
* Dependencies are injected automatically through constructors.
* NestJS creates and manages service instances, eliminating the need for manual instantiation.
* DI promotes loose coupling, making applications easier to maintain and test.

### What benefits does modular architecture provide in a large-scale app?
* Organizes related functionality into separate modules, improving code structure.
* Promotes separation of concerns, making features easier to develop and maintain.
* Enhances scalability by allowing new modules to be added independently.
* Improves team collaboration, as different teams can work on different modules.
* Increases reusability and testability by keeping components isolated and modular.



