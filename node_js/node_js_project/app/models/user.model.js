module.exports = (sequelize, Sequelize) => {
  const User = sequelize.define("users", {
    username: {
      type: Sequelize.STRING
    },
    email: {
      type: Sequelize.STRING
    },
    password: {
      type: Sequelize.STRING
    },
    // profile: {
    //   type: Sequelize.TEXT
    // },
    // post: {
    //   type: Sequelize.TEXT
    // }
  });

  return User;
};
