# 0x01. NoSQL
## What is NoSQL?
NoSQL, which stands for "not only SQL," is a database approach designed to handle massive amounts of data with high scalability and performance. Unlike traditional SQL databases, NoSQL databases adopt a flexible schema and do not rely on a fixed tabular structure. They prioritize scalability, availability, and ease of development, making them ideal for modern applications and use cases.

## SQL vs. NoSQL:
The primary difference between SQL and NoSQL lies in their data models and query languages. SQL databases, also known as relational databases, store data in predefined tables with strict schemas. They use Structured Query Language (SQL) to query and manipulate data. NoSQL databases, on the other hand, employ various data models such as key-value, document, columnar, and graph. They use different query languages, APIs, or protocols specific to their data model.

## ACID:
ACID is an acronym for Atomicity, Consistency, Isolation, and Durability. It represents a set of properties that guarantee the reliability of database transactions. Traditional SQL databases are known for their strong ACID compliance, ensuring that each transaction is executed reliably, maintaining data integrity and consistency. NoSQL databases, however, often relax some of these ACID properties in favor of scalability and performance. They offer different levels of consistency and trade-offs based on the specific use case.

## Document Storage:
Document storage is a NoSQL data model that organizes data in self-contained documents, typically represented in formats like JSON or BSON. Each document is a semi-structured unit that contains key-value pairs or nested structures. Document-oriented databases, such as MongoDB, are widely used for their flexibility in handling evolving and diverse data structures.

## Types of NoSQL Databases:
NoSQL databases can be categorized into several types based on their data models:

1. Key-Value Stores: These databases store data as simple key-value pairs, allowing fast retrieval by key.
2. Document Stores: Document-oriented databases, like MongoDB, store and retrieve data in flexible, schema-less documents.
3. Columnar Databases: Columnar stores optimize data retrieval by storing columns of data together, ideal for analytics and reporting.
4. Graph Databases: Graph databases represent data as nodes, edges, and properties, enabling efficient traversal and analysis of relationships.
## Benefits of NoSQL Databases:
NoSQL databases offer several advantages over traditional SQL databases, including:

1. Scalability: NoSQL databases are designed to scale horizontally, allowing them to handle massive amounts of data and high traffic loads.
2. Flexibility: NoSQL databases accommodate evolving data structures and schema changes without requiring complex migrations.
3. Performance: With optimized data models and flexible schemas, NoSQL databases provide high-performance reads and writes.
4. Availability: Many NoSQL databases offer built-in replication and fault-tolerance mechanisms, ensuring high availability of data.
5. Developer-friendly: NoSQL databases often provide easy-to-use APIs, intuitive data models, and flexible query languages, facilitating rapid application development.
## Querying Data in NoSQL Databases:
Each NoSQL database has its own query language or API for interacting with the data. Let's take MongoDB as an example:

MongoDB Query Language (MQL): MQL is a powerful and expressive query language used to retrieve data from MongoDB. It supports a wide range of operators for filtering, sorting, aggregating, and transforming data.
Example MQL query in MongoDB:

db.collection("users").find({ age: { $gte: 18 } }).sort({ name: 1 });
## Inserting, Updating, and Deleting Data:
NoSQL databases provide straightforward operations for inserting, updating, and deleting data. Using MongoDB as an example:

### Inserting data:
db.collection("users").insertOne({ name: "John", age: 25 });
### Updating data:
db.collection("users").updateOne({ name: "John" }, { $set: { age: 26 } });
### Deleting data:
db.collection("users").deleteOne({ name: "John" });
## Using MongoDB:
MongoDB is a popular and widely adopted NoSQL database known for its flexibility, scalability, and ease of use. To use MongoDB:

Install MongoDB on your system and start the MongoDB server.
Connect to the MongoDB server using a programming language driver or MongoDB's command-line interface.
Create databases, collections, and perform CRUD operations using the appropriate API or query language.
Example connection and CRUD operations in JavaScript:

const { MongoClient } = require("mongodb");

const uri = "mongodb://localhost:27017";
const client = new MongoClient(uri);

async function main() {
  try {
    await client.connect();
    const database = client.db("mydb");
    const collection = database.collection("users");

    // Insert a document
    await collection.insertOne({ name: "John", age: 25 });

    // Find documents
    const result = await collection.find({ age: { $gte: 18 } }).toArray();
    console.log(result);

    // Update a document
    await collection.updateOne({ name: "John" }, { $set: { age: 26 } });

    // Delete a document
    await collection.deleteOne({ name: "John" });
  } finally {
    await client.close();
  }
}

main().catch(console.error);

# Conclusion:
NoSQL databases provide a flexible and scalable approach to managing large volumes of data. They offer distinct data models, relaxed consistency guarantees, and numerous benefits for modern applications. MongoDB, a prominent NoSQL database, showcases the power and versatility of NoSQL technologies. By understanding NoSQL concepts, differences from SQL, document storage, querying, and CRUD operations, developers can harness the advantages of NoSQL databases and make informed architectural decisions for their projects.
