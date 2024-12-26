const express = require("express");
const fileUpload = require("express-fileupload");
const path = require("path");
const fs = require("fs");

const app = express();

// Enable file uploads, up to 100 MB
app.use(
  fileUpload({
    limits: { fileSize: 100 * 1024 * 1024 },
  })
);

// Serve the "uploads" folder statically (for direct download)
app.use(express.static(path.join(__dirname, "uploads")));

// GET / - show upload form and list uploaded files
app.get("/", (req, res) => {
  fs.readdir(path.join(__dirname, "uploads"), (err, files) => {
    if (err) {
      console.error("Could not list the uploads folder.", err);
      return res.status(500).send("Error reading uploads folder.");
    }

    let fileListHtml = files
      .map((file) => {
        // Each file can be downloaded by /<file>
        return `<li><a href="${file}" download>${file}</a></li>`;
      })
      .join("");

    let htmlContent = `
      <!DOCTYPE html>
      <html>
        <head>
          <meta charset="utf-8" />
          <title>Simple File Sharing</title>
        </head>
        <body>
          <h1>File Sharing Service</h1>

          <!-- Upload form -->
          <form action="/upload" method="POST" encType="multipart/form-data">
            <label>Select a file to upload:</label><br><br>
            <input type="file" name="myFile" />
            <button type="submit">Upload</button>
          </form>

          <hr>

          <!-- List of previously uploaded files -->
          <h2>Uploaded Files</h2>
          <ul>${fileListHtml}</ul>
        </body>
      </html>
    `;
    res.send(htmlContent);
  });
});

// POST /upload - handle file upload
app.post("/upload", (req, res) => {
  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send("No files were uploaded.");
  }

  let file = req.files.myFile;
  let uploadPath = path.join(__dirname, "uploads", file.name);

  // Move the file into the "uploads" folder
  file.mv(uploadPath, (err) => {
    if (err) {
      console.error("Error moving file:", err);
      return res.status(500).send(err);
    }
    // Redirect back to the main page so user can see the updated file list
    res.redirect("/");
  });
});

const PORT = 8080;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});
