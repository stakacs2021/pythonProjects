const express = require("express");
const fileUpload = require("express-fileupload");
const path = require("path");
const fs = require("fs");

const app = express();

// Enable file uploads now with 100mb
app.use(
  fileUpload({
    limits: { fileSize: 100 * 1024 * 1024 }, // 100 MB
  }),
);

// Serve the "uploads" folder statically (so files can be downloaded directly)
app.use(express.static(path.join(__dirname, "uploads")));

// GET / - show upload form and list uploaded files
app.get("/", (req, res) => {
  // Read all files in the "uploads" folder
  fs.readdir(path.join(__dirname, "uploads"), (err, files) => {
    if (err) {
      console.error("Could not list the uploads folder.", err);
      return res.status(500).send("Error reading uploads folder.");
    }

    // Build an HTML response that includes
    // 1) The upload form
    // 2) A list of existing files as download links
    let fileListHtml = files
      .map((file) => {
        // Each file can be downloaded by going to: http://<host>:<port>/<file>
        return `<li><a href="${file}" download>${file}</a></li>`;
      })
      .join("");

    // The HTML page content
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
  // Check if a file was included
  if (!req.files || Object.keys(req.files).length === 0) {
    return res.status(400).send("No files were uploaded.");
  }

  // 'myFile' is the name attribute in the HTML form
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

// Start the server
const PORT = 8080;
app.listen(PORT, () => {
  console.log(`Server is running on port ${PORT}.`);
});
