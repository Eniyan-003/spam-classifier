async function checkSpam() {
    const text = document.getElementById("message").value;
    const loader = document.getElementById("loader");
    const result = document.getElementById("result");

    loader.style.display = "block";
    result.innerText = "";

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    });

    const data = await response.json();

    loader.style.display = "none";
    result.innerText = "Result: " + data.prediction;
}