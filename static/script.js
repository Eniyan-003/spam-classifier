async function checkSpam() {
    const text = document.getElementById("message").value;

    const response = await fetch("/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ text })
    });

    const data = await response.json();
    document.getElementById("result").innerText = "Result: " + data.prediction;
}