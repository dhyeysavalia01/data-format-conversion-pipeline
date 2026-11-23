# Data Formats

###  1. CSV (Comma Separated Values)
- Easy to read.
- Easy to open in Excel.
- Supported almost everywhere.
- Simple to transfer between systems.
- Does not inherently preserve strict data types.
- Not efficient for large analytical datasets.

**Where it is used**

- Data exports
- Small datasets
- Legacy systems
- Data exchange
- Initial raw ingestion

**Example:**

```CSV
    city,temperature,humidity,timestamp
    Bangalore,26.5,62,2026-11-23 09:00
    Mumbai,31.2,75,2026-11-23 09:00
    Pune,27.1,55,2026-11-23 09:00
```

### 2. JSON (JavaScript Object Notation)
- Supports nested structures.
- Supports arrays and objects.
- Naturally maps to Python dictionaries and lists.
- Frequently used in REST APIs.
- More flexible than CSV.

**Where is it used**


- REST API responses
- Application configuration
- Raw ingestion data
- NoSQL-style data exchange
- Logging and event data

**Example:**
```JSON
[
  {
    "city": "Bangalore",
    "temperature": 26.5,
    "humidity": 62,
    "timestamp": "2026-11-23 09:00"
  },
  {
    "city": "Mumbai",
    "temperature": 31.2,
    "humidity": 75,
    "timestamp": "2026-11-23 09:00"
  }
]
```

### 3. XML (eXtensible Markup Language)
- Uses tags.
- Supports nested structures.
- Verbose compared to JSON.
- Common in enterprise integrations and older systems.
- Found in configuration, finance, healthcare, government, and legacy applications.

**Example:**

```XML
<weather>
  <city name="Bangalore">
    <temperature>26.5</temperature>
    <humidity>62</humidity>
    <timestamp>2026-11-23 09:00</timestamp>
  </city>
  <city name="Mumbai">
    <temperature>31.2</temperature>
    <humidity>75</humidity>
    <timestamp>2026-11-23 09:00</timestamp>
  </city>
</weather>
```

### 4. Parquet
- Columnar storage format.
- Highly efficient for analytical queries.
- Supports compression and encoding.
- Column projection pushdown.
- Predicate pushdown.

**Where it is used**

- Big data processing.
- Data lakes.
- Analytics warehouses.
- Spark-based ETL.
- High-performance querying.

**Example:**

```Parquet
# No simple text representation possible
# It's a binary format.
# But conceptually it stores data in columns:

# Column: city        | temperature | humidity | timestamp
# Row 1:  Bangalore   | 26.5        | 62         | 2026-11-23 09:00
# Row 2:  Mumbai      | 31.2        | 75         | 2026-11-23 09:00
# Row 3:  Pune        | 27.1        | 55         | 2026-11-23 09:00
```


Suppose you have a dataset with 50 columns and 10 million rows.

You want to calculate only the average temperature.

With a columnar format, an analytical engine can read the relevant temperature column without needing to read all 50 columns. This can reduce I/O significantly.