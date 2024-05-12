// Imports
const { MongoClient } = require("mongodb");
const uri = "mongodb://127.0.0.1:27017/db_query";
const client = new MongoClient(uri);

// Database generation
async function generation() {
    try {
        console.log("Database created!");
    } finally {
        // Ensures that the client will close when you finish/error
        // await client.close();
        console.log("Done.");
      }
    }
    generation().catch(console.dir);

// Collection generation
async function collection() {
    try {
      console.log("Collection created!");
      const database = client.db('db_query');
      const customers = await database.createCollection('customers');
      console.log(customers);
    } finally {
      // Ensures that the client will close when you finish/error
      // await client.close();
      console.log("Done.");
    }
  }
  collection().catch(console.dir);

async function insert() {
  try {
    console.log("Trying insert....");
    const database = client.db('db_query');
    const customers = database.collection('customers');
    const myobj = { name: "Company Inc", address: "Highway 37" };
    const result = await customers.insertOne(myobj);
    console.log(result);
  } finally {
    // Ensures that the client will close when you finish/error
    // await client.close();
    console.log("Done.");
  }
}
insert().catch(console.dir);

// Table update
async function update_table() {
  try {
      console.log("Table update:");
      const database = client.db('db_query');
      const myquery = { address: "Highway 37" };
      const newvalues = { $set: {name: "Mickey", address: "Canyon 123" } };
      const customers = database.collection('customers');
      const result = await customers.updateOne(myquery);
      console.log(result);
  } finally {
          // Ensures that the client will close when you finish/error
          // await client.close();
          console.log("Done.");
        }
      }
      update_table().catch(console.dir);

// Table drop
async function drop_table() {
    try {
        console.log("Table drop:");
        const database = client.db('db_query');
        const customers = database.collection('customers');
        const result = await customers.drop();
        console.log(result);
    } finally {
            // Ensures that the client will close when you finish/error
            // await client.close();
            console.log("Done.");
          }
        }
        drop_table().catch(console.dir);
