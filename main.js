const API = "https://filehub-c63o.onrender.com/files";

fetch(API)
  .then(res => res.json())
  .then(data => {
    const container = document.getElementById("fileList");

    data.reverse().forEach(file => {
        const div = document.createElement("div");
        div.className = "card";

        div.innerHTML = `
            <h3>${file.name}</h3>
            <small>${new Date(file.date).toLocaleString()}</small>
            <br>
            <a href="${file.url}" target="_blank">
                <button>Download</button>
            </a>
        `;

        container.appendChild(div);
    });
  });