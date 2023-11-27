import express from "express";
import bodyParser from "body-parser"; // Add body-parser for parsing POST request data
import JSONdb from "simple-json-db";

const app = express();
const port = 3000;

// Create a new JSONdb instance
const db = new JSONdb("db/db.json");

// Middleware to parse JSON requests
app.use(express.json());

// Middleware to serve static files from the 'public' directory
app.use(express.static("public"));

// Middleware to parse POST request data
app.use(bodyParser.urlencoded({ extended: true }));

// Set up Pug as the view engine
// app.set("views", path.join(__dirname, "views"));
app.set("view engine", "pug");

app.get("/", (req, res) => {
  res.render("index");
});

app.get("/posts", (req, res) => {
  const posts = db.get("posts");
  res.render("posts", { posts });
});

app.post("/clicked", (req, res) => {
  res.render("container", { content: "This is a container!" });
});

// Start the server
app.listen(port, () => {
  console.log(`Server is running on http://localhost:${port}`);
});
