const API_BASE = "http://127.0.0.1:8000"; // change to EC2 IP later

let uploadedFile = null;

// ✅ Capture file
document.getElementById("fileInput").addEventListener("change", function(e) {
    uploadedFile = e.target.files[0];
});

// ✅ Add message to chat
function addMessage(text, type) {
    let chatBox = document.getElementById("chatBox");

    let msg = document.createElement("div");
    msg.className = "message " + type;
    msg.innerText = text;

    chatBox.appendChild(msg);
    chatBox.scrollTop = chatBox.scrollHeight;
}

// ✅ Send query to backend
async function sendQuery() {
    let query = document.getElementById("query").value;

    if (!uploadedFile) {
        alert("Please upload a CSV file");
        return;
    }

    addMessage(query, "user");

    // 🔥 Loading message
    addMessage("Thinking...", "bot");

    let formData = new FormData();
    formData.append("file", uploadedFile);
    formData.append("query", query);

    try {
        let response = await fetch(`${API_BASE}/analyze`, {
            method: "POST",
            body: formData
        });

        const contentType = response.headers.get("content-type");

        // ✅ Handle IMAGE (chart)
        if (contentType && contentType.includes("image")) {
            let blob = await response.blob();
            let url = URL.createObjectURL(blob);

            let img = document.createElement("img");
            img.src = url;
            img.style.maxWidth = "100%";
            img.style.marginTop = "10px";

            document.getElementById("chatBox").appendChild(img);
        }

        // ✅ Handle JSON (text response)
        else {
            let data = await response.json();

            let text =
                data.final_answer ||
                (typeof data.analysis === "string" ? data.analysis : JSON.stringify(data.analysis)) ||
                data.error ||
                "No response";

            addMessage(text, "bot");
        }

    } catch (err) {
        addMessage("Server connection error", "bot");
    }
}