# Handling Environment Variables & Configuration in NestJS

## Goal

Learn how to securely manage environment variables and application configuration in NestJS.



## Reflections

### How does @nestjs/config help manage environment variables?

* `@nestjs/config` provides a centralized way to access configuration values throughout a NestJS application.
* It loads environment variables from `.env` files into process`.env`.
* The `ConfigService` allows modules and services to access configuration values safely.
* Configuration can be organized into reusable configuration files and modules.
* It supports different environment files for development, testing, and production.
* It simplifies application configuration and reduces hardcoded values in the codebase.


### Why should secrets (e.g., API keys, database passwords) never be stored in source code?

* Source code is often stored in version control systems where many people may have access.
* Accidentally committing secrets to a repository can expose sensitive information.
* Attackers who gain access to the repository can use exposed credentials to access systems and data.
* Rotating compromised secrets can be time-consuming and disruptive.
* Environment variables keep sensitive information separate from application code.
* Storing secrets externally improves security and follows industry best practices.

### How can you validate environment variables before the app starts?

* NestJS can validate environment variables during application startup using validation schemas.
* Libraries such as Joi are commonly used for validation.
* Required variables can be marked as mandatory.
* Variables can be checked for correct formats, types, and allowed values.
* If validation fails, the application can stop immediately instead of running with invalid configuration.
* Early validation helps prevent runtime errors and deployment issues.

### How can you separate configuration for different environments (e.g., local vs. production)?

* Different `.env` files can be used for each environment.
* Examples include `.env.development`, `.env.test`, and `.env`.production.
* NestJS can load a specific file based on the current environment.
* Environment-specific settings can include database URLs, API endpoints, and logging levels.
* This allows the same codebase to run in multiple environments with different configurations.
* Separating configurations reduces the risk of using incorrect settings in production.


## Tasks

### Validate env variables

app.module.ts
``` Typescript

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      validationSchema: Joi.object({
        // Database — all required
        DB_HOST: Joi.string().required(),
        DB_PORT: Joi.number().default(5432),
        DB_USERNAME: Joi.string().required(),
        DB_PASSWORD: Joi.string().allow('').default(''),  // optional — empty string is valid
        DB_NAME: Joi.string().required(),
    
        // Redis — required
        REDIS_HOST: Joi.string().required(),
        REDIS_PORT: Joi.number().default(6379),
    
        // Auth0 — required
        AUTH0_DOMAIN: Joi.string().required(),
        AUTH0_AUDIENCE: Joi.string().required(),
      }),
    }),
    TypeOrmModule.forRootAsync({
      imports: [ConfigModule],
      inject: [ConfigService],
      useFactory: (config: ConfigService) => ({
        type: 'postgres',
        host: config.get<string>('DB_HOST'),
        port: config.get<number>('DB_PORT'),
        username: config.get<string>('DB_USERNAME'),
        password: config.get<string>('DB_PASSWORD'),
        database: config.get<string>('DB_NAME'),
        entities: [Todo],
        synchronize: false,
      }),
    }),
    BullModule.forRootAsync({
      imports: [ConfigModule],
      inject: [ConfigService],
      useFactory: (config: ConfigService) => ({
        connection: {
          host: config.get<string>('REDIS_HOST'),
          port: config.get<number>('REDIS_PORT'),
        },
      }),
    }),
    AuthModule,
    TodosModule,
  ],
  controllers: [AppController],
  providers: [AppService],
})
export class AppModule implements NestModule {
  configure(consumer: MiddlewareConsumer) {
    consumer.apply(LoggerMiddleware).forRoutes('*');
  }
}
```

### Config validation error

![Config validation error](/Screenshots/Config-validation-error.png)