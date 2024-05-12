//Imports
const { MongoClient } = require("mongodb");
const uri = "mongodb://127.0.0.1:27017/";
const client = new MongoClient(uri);

// Data insertion
async function insertion() {
  try {
    console.log("Trying insert....");
    const database = client.db('testdb');
    const customers = database.collection('customers');
    const myobj = [
        { name: 'John', address: 'Highway 71'},
        { name: 'Peter', address: 'Lowstreet 4'},
        { name: 'Amy', address: 'Apple st 652'},
        { name: 'Hannah', address: 'Mountain 21'},
        { name: 'Michael', address: 'Valley 345'},
        { name: 'Sandy', address: 'Ocean blvd 2'},
        { name: 'Betty', address: 'Green Grass 1'},
        { name: 'Richard', address: 'Sky st 331'},
        { name: 'Susan', address: 'One way 98'},
        { name: 'Vicky', address: 'Yellow Garden 2'},
        { name: 'Ben', address: 'Park Lane 38'},
        { name: 'William', address: 'Central st 954'},
        { name: 'Chuck', address: 'Main Road 989'},
        { name: 'Viola', address: 'Sideway 1633'}
      ];
    const result = await customers.insertMany(myobj);
    console.log(result);
  } finally {
    // Ensures that the client will close when you finish/error
    // await client.close();
    console.log("Done.");
  }
}
insertion().catch(console.dir);

// Data search
async function search() {
  try {
    console.log("Data search:");
    const database = client.db('testdb');
    const customers = database.collection('customers');
    const result = await customers.find({}).toArray() 
    console.log(result);
} finally {
        // Ensures that the client will close when you finish/error
        // await client.close();
        console.log("Done.");
      }
    }
    search().catch(console.dir);
    

// Query call
async function query() {
    try {
      console.log("Query:");
      const database = client.db('testdb');
      const customers = database.collection('customers');
      const query = { address: "Park Lane 38" };
      const result = await customers.find(query).toArray()
      console.log(result);
} finally {
        // Ensures that the client will close when you finish/error
        // await client.close();
        console.log("Done.");
      }
    }
    query().catch(console.dir);

// Sort search
async function sort() {
    try {
      console.log("Sort:");
      const database = client.db('testdb');
      const customers = database.collection('customers');
      const mysort = { name: 1 };
      const result = await customers.find().sort(mysort).toArray()
      console.log(result);
    } finally {
            // Ensures that the client will close when you finish/error
            // await client.close();
            console.log("Done.");
          }
        }
        sort().catch(console.dir);

// Data deletion
async function delete_info() {
    try {
        console.log("Information delete:");
        const database = client.db('testdb');
        const customers = database.collection('customers');
        const myquery = { address: 'Mountain 21' };
        const result = await customers.deleteOne(myquery);
        console.log(result);
    } finally {
            // Ensures that the client will close when you finish/error
            // await client.close();
            console.log("Done.");
          }
        }
        delete_info().catch(console.dir);

// Table limiting
async function info_limit() {
    try {
        console.log("Table limit:");
        const database = client.db('testdb');
        const customers = database.collection('customers');
        const result = await customers.find().limit(5).toArray();
    } finally {
            // Ensures that the client will close when you finish/error
            // await client.close();
            console.log("Done.");
          }
        }
        info_limit().catch(console.dir);