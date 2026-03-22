async function checkSpam() {
    const text = document.getElementById("message").value;
    const loader = document.getElementById("loader");
    const result = document.getElementById("result");

    if (data.prediction === "spam") {
    result.style.color = "red";
} else {
    result.style.color = "green";
}

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