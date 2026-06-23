# NestJS Testing Introduction

## What are the key differences between unit, integration, and E2E tests?

| Type        | What it tests                        | Speed  | Dependencies      |
|-------------|--------------------------------------|--------|-------------------|
| Unit        | Single class/function in isolation   | Fast   | All mocked        |
| Integration | Multiple modules working together    | Medium | Real DI, test DB  |
| E2E         | Full HTTP request/response cycle     | Slow   | Full app running  |

- **Unit** — test `TodosService.findOne()` with a mocked repository
- **Integration** — test `TodosModule` with real TypeORM but a test database
- **E2E** — send `GET /todos` via Supertest and assert the response

## Why is testing important for a NestJS backend?

- Catches regressions before they reach production
- CI blocks broken pushes automatically
- Lets developers refactor confidently
- Focus Bear's backend handles health data — bugs here have real user impact

## How does `@nestjs/testing` simplify testing?

Instead of instantiating classes manually (which fails because of DI),
`@nestjs/testing` lets you create a lightweight DI container for tests:

```typescript
const module: TestingModule = await Test.createTestingModule({
  providers: [
    TodosService,
    { provide: getRepositoryToken(Todo), useValue: mockRepository },
    { provide: getQueueToken('notifications'), useValue: mockQueue },
  ],
}).compile();

const service = module.get<TodosService>(TodosService);
```

You swap real dependencies (TypeORM repository, BullMQ queue) with mock objects,
so tests run with no database or Redis needed.

## What are the challenges of writing tests for a NestJS application?

- **DI complexity** — you must provide every dependency the class needs,
  including nested ones like `getRepositoryToken()` and `getQueueToken()`
- **Auto-generated stubs** — NestJS scaffolds empty `.spec.ts` files that
  fail immediately because they don't wire dependencies (fixed `todos.controller.spec.ts`)
- **Async everywhere** — most NestJS methods are async, so tests need
  `await` and `rejects.toThrow()` patterns throughout

## Test Implementation

### Screenshot 
![nest-test](Screenshots/nest-test.pngScreenshots/nest-test.png)

### `src/todos/todos.service.spec.ts`

```typescript
import { Test, TestingModule } from '@nestjs/testing';
import { TodosService } from './todos.service';
import { getRepositoryToken } from '@nestjs/typeorm';
import { Todo } from './todo.entity';
import { getQueueToken } from '@nestjs/bullmq';
import { NotFoundException } from '@nestjs/common';

const mockRepository = {
  find: jest.fn(),
  findOneBy: jest.fn(),
  create: jest.fn(),
  save: jest.fn(),
  delete: jest.fn(),
};

const mockQueue = {
  add: jest.fn(),
};

describe('TodosService', () => {
  let service: TodosService;

  beforeEach(async () => {
    const module: TestingModule = await Test.createTestingModule({
      providers: [
        TodosService,
        { provide: getRepositoryToken(Todo), useValue: mockRepository },
        { provide: getQueueToken('notifications'), useValue: mockQueue },
      ],
    }).compile();

    service = module.get<TodosService>(TodosService);
  });

  afterEach(() => jest.clearAllMocks());

  describe('findAll', () => {
    it('should return an array of todos', async () => {
      const todos = [{ id: 1, title: 'Test', completed: false }];
      mockRepository.find.mockResolvedValue(todos);
      const result = await service.findAll();
      expect(result).toEqual(todos);
      expect(mockRepository.find).toHaveBeenCalledTimes(1);
    });
  });

  describe('findOne', () => {
    it('should return a todo if found', async () => {
      const todo = { id: 1, title: 'Test', completed: false };
      mockRepository.findOneBy.mockResolvedValue(todo);
      const result = await service.findOne(1);
      expect(result).toEqual(todo);
      expect(mockRepository.findOneBy).toHaveBeenCalledWith({ id: 1 });
    });

    it('should throw NotFoundException if todo not found', async () => {
      mockRepository.findOneBy.mockResolvedValue(null);
      await expect(service.findOne(999)).rejects.toThrow(NotFoundException);
    });
  });

  describe('create', () => {
    it('should create a todo and add a queue job', async () => {
      const dto = { title: 'New Todo', completed: false };
      const savedTodo = { id: 1, ...dto };
      mockRepository.create.mockReturnValue(dto);
      mockRepository.save.mockResolvedValue(savedTodo);
      mockQueue.add.mockResolvedValue({});
      const result = await service.create(dto);
      expect(result).toEqual(savedTodo);
      expect(mockQueue.add).toHaveBeenCalledWith('todo-created', {
        title: savedTodo.title,
        id: savedTodo.id,
      });
    });
  });

  describe('remove', () => {
    it('should delete a todo', async () => {
      const todo = { id: 1, title: 'Test', completed: false };
      mockRepository.findOneBy.mockResolvedValue(todo);
      mockRepository.delete.mockResolvedValue({ affected: 1 });
      await service.remove(1);
      expect(mockRepository.delete).toHaveBeenCalledWith(1);
    });

    it('should throw NotFoundException if todo does not exist', async () => {
      mockRepository.findOneBy.mockResolvedValue(null);
      await expect(service.remove(999)).rejects.toThrow(NotFoundException);
    });
  });
});
```