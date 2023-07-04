const express = require("express");
const app = express();
const path = require("path");

app.listen(8080, () => {
  console.log("hi");
});

// Ajax를 위한 코드
app.use(express.json());
const cors = require("cors");
app.use(cors());

app.use(express.static(path.join(__dirname, "../shop/build")));

// main 페이지
app.get("/", (req, res) => {
  res.sendFile(path.join(__dirname, "../shop/build/index.html"));
});

// 만약 db에 있던 상품명을 보여주려면?
app.get("/product", (req, res) => {
  res.json({ name: "black shoes" });
});

app.get("*", (req, res) => {
  res.sendFile(path.join(__dirname, "../shop/build/index.html"));
});
