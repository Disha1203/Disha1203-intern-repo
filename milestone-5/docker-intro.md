# Docker Introduction

## Goal
Understand what Docker is, how it differs from traditional development setups, and why Focus Bear uses it.


## Reflection 

### 1. How does Docker differ from a virtual machine?

Docker containers share the host operating system kernel and package only the application and its dependencies, making them lightweight and fast. Virtual machines include a complete guest operating system, which consumes more resources and takes longer to start.

### 2. Why is containerization useful for a backend like Focus Bear's?

Containerization ensures that every developer and deployment environment runs the backend in exactly the same way. This reduces configuration issues, simplifies onboarding, and improves reliability when deploying updates.

### 3. How do containers help with dependency management?

Containers isolate application dependencies from the host machine. Developers can use specific versions of libraries, runtimes, and tools without worrying about conflicts with software installed elsewhere on the system.

### 4. What are the potential downsides of using Docker?

Some disadvantages include:

* Additional learning curve for new developers.
* Increased complexity compared to running applications directly.
* Debugging can sometimes be more difficult.
* Containers consume storage through images and volumes.
* Performance overhead exists, although it is generally much smaller than virtual machines.
* Networking and container orchestration can become complex in large systems.
