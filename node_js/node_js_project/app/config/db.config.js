module.exports = {
  HOST: "localhost",
  USER: "DB_DEVELOPER",
  PASSWORD: "DONT_forget11",
  DB: "mydb",
  dialect: "mysql",
  pool: {
    max: 5,
    min: 0,
    acquire: 30000,
    idle: 10000
  }
};
