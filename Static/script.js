document.addEventListener("DOMContentLoaded", function () {
    // 1. Language dropdown cookie sync
    const select = document.getElementById("lang");
    if (select) {
        const match = document.cookie.match(/googtrans=\/en\/([a-z-]+)/i);
        if (match) select.value = match[1];

        select.addEventListener("change", function () {
            document.cookie = "googtrans=/en/" + this.value + "; path=/";
            location.reload();
        });
    }


    const modal = document.getElementById("videoModal");
const video = document.getElementById("movieVideo");

document.getElementById("firstPoster").addEventListener("click", () => {
  modal.classList.add("show");
  video.play();
});

function closeModal() {
  modal.classList.remove("show");
  video.pause();
  video.currentTime = 0;
}

document.getElementById("closeBtn").addEventListener("click", closeModal);

modal.addEventListener("click", (e) => {
  if (e.target === modal) closeModal();
});   



    // 2. Email signup handler
    document.querySelectorAll(".four").forEach(function (btn) {
        btn.addEventListener("click", async function (e) {
            e.preventDefault();
            
            const container = btn.parentElement;
            const input = container.querySelector(".three");
            
            if (!input || !input.value.trim()) {
                alert("Please enter an email!");
                return;
            }

            try {
                const res = await fetch("/signup", {
                    method: "POST",
                    headers: { "Content-Type": "application/json" },
                    body: JSON.stringify({ email: input.value })
                });
                
                const data = await res.json();
                alert(data.message);
            } catch (err) {
                console.error("Error connecting to server:", err);
                alert("Failed to connect to backend server.");
            }
        });
    });
});