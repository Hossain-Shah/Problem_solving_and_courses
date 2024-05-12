const { verifySignUp } = require("../middleware");
const controller = require("../controllers/auth.controller");

module.exports = function(app) {
  app.use(function(req, res, next) {
    res.header(
      "Access-Control-Allow-Headers",
      "Origin, Content-Type, Accept"
    );
    next();
  });

  app.post(
    "/api/auth/signup",
    [
      verifySignUp.checkDuplicateUsernameOrEmail,
      verifySignUp.checkRolesExisted
    ],
    controller.signup
  );

  app.post("/api/auth/signin", controller.signin);

  app.post("/api/auth/signout", controller.signout);

  let post = [];

  app.post('/api/post', (req, res) => {
    const new_post = req.body;
    post.push(new_post);
    res.status(201).json(new_post);
  });

  app.get('/api/get', (req, res) => {
    res.json(post);
  });

  app.get('/api/auth/signin?id=', (req, res) => {
    res.json(post);
  });

  app.put('/api/edit/:id', (req, res) => {
    const new_post = req.body;
    post.push(new_post);
    res.status(201).json(new_post);
  });

  app.delete('/api/delete/:id', (req, res) => {
    const new_post = req.body;
    post.pop(new_post);
    res.status(201).json(new_post);
  });
};
