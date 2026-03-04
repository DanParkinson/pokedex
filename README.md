# Overview
A fully tested, contract‑driven ETL pipeline that extracts data from the public PokéAPI, transforms it into structured relational tables, and loads it into a DuckDB database.

Built with Python, DuckDB, pytest, and a modular architecture designed for maintainability, testability, and production‑ready workflows

## Features
### Contract‑driven transform layer
Every resource is parsed using explicit schemas that define required fields, output fields, and transformation logic. This enforces consistency, makes the pipeline predictable, and keeps transformations testable and maintainable.
### Modular ETL architecture
The pipeline is split into clear extract, transform, and load stages. Each stage is independently testable and follows single‑responsibility principles.
### DuckDB analytical storage
Data is loaded into a local DuckDB database, giving fast analytical performance with zero external dependencies.
### Robust extraction layer
Includes API entry‑point handling, pagination, URL construction, and safe JSON fetching with error handling and logging.
### Batch‑based loading
Data is inserted in batches with idempotent table creation, ensuring the ETL can be re‑run safely without corrupting or duplicating data.
### Full test suite
Comprehensive unit and integration tests cover extraction, transformation contracts, loading, and the ETL orchestration loop. Tests use mocking to isolate external boundaries and ensure deterministic behaviour.
### Clean project structure
Source code is organized under backend/src/pokedex, with clear module boundaries and a consistent layout for extract/transform/load/database layers.
### Logging and error handling
Structured logging across all stages and custom error types for database and HTTP failures.

## Architecture

The project follows a clean, layered ETL architecture designed for testability, maintainability, and predictable data flow. Each stage has a single responsibility and is independently tested.

### Extract Layer
The extract layer handles all communication with the external API. Its responsibilities include:
- Building entry‑point URLs for each resource
- Fetching JSON responses
- Handling pagination (next URLs)
- Normalizing raw API responses into a consistent internal format
- Logging and error handling for network failures
This layer is intentionally thin and side‑effect‑free, making it easy to mock in tests.

### Transform Layer (Contract‑Driven)
The transform layer is the core of the system. It uses resource contracts to define:
- Required input fields
- Output schema
- Transformation logic
- Table mapping
Each contract is a self‑contained specification that ensures:
- Schema consistency
- Predictable transformations
- Clear separation between raw API data and structured relational data
- Easy extensibility (adding a new contract requires no changes to the ETL engine)
This design mirrors production‑grade data engineering patterns such as schema‑first pipelines and declarative transformations.

### Load Layer
The load layer writes transformed data into a DuckDB database. It provides:
- Idempotent table creation
- Batch inserts for performance
- A clean abstraction over the database connection
- Error handling via custom exceptions
DuckDB is used as a lightweight analytical engine, giving fast local queries without external dependencies.
Orchestration (run_etl)
The run_etl script coordinates the full pipeline:
- Fetch the first page for a resource
- Loop through all pages
- For each page:
- Extract raw rows
- Apply every contract associated with the resource
- Load each contract’s output into its corresponding table
- Stop when pagination ends
This orchestration is intentionally simple and deterministic, making it easy to test with mocked boundaries.


## Structure
```python
backend/
  src/
    pokedex/
      extract/      # API entry points, pagination, fetch_json
      transform/    # contract system, parse_resource, parse_resource_batch
      load/         # DuckDB connection, batch inserts
      database/     # connection management, schema setup
      scripts/      # run_etl entry point
  tests/
    extract/
    transform/
    load/
    scripts/
```

## Installation & Setup

The project uses uv for fast, reproducible Python environments and dependency management. Everything is defined in pyproject.toml.
Requirements
- Python 3.11+
- uv (https://github.com/astral-sh/uv)
- Git

1. Clone the repository
```python
git clone <your-repo-url>
cd backend
```

2. Create and activate the environment with uv
```python
uv venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

3. Install dependencies from pyproject.toml
```python
uv pip install -e .
```

This installs the project in editable mode and resolves all dependencies declared in the pyproject.toml.

4. Initialise the database
The database is not included in the repository. You must create it before running the ETL:
```python
uv run init_db
```

This command:
- Creates the backend/data/ directory if it doesn’t exist
- Creates pokedex.duckdb
- Sets up all required tables based on your contract definitions

5. Run the ETL to populate the database
```python
uv run run_etl
```

This fetches data from the PokéAPI, applies all contracts for the pokemon resource, and loads the results into DuckDB.

6. Run the test suite
```python
pytest -q
```
