async function submitScore() {
    // Get the values for score, hours, and sleep
    const scoreInput = document.getElementById("scoreInput").value;
    const hoursInput = document.getElementById("hoursInput").value;
    const sleepInput = document.getElementById("sleepInput").value;

    // Convert the inputs to numbers and validate
    const hours = parseFloat(hoursInput);
    const score = parseFloat(scoreInput);
    const sleep = parseFloat(sleepInput);

    // Get the result div
    const resultDiv = document.getElementById("result");

    // Validate inputs
    if (isNaN(hours) || isNaN(score) || isNaN(sleep)) {
        resultDiv.className = 'result show result-fail';
        resultDiv.innerHTML = "Please enter valid numbers for all fields";
        return;
    }

    if (score < 0 || score > 100) {
        resultDiv.className = 'result show result-fail';
        resultDiv.innerHTML = "Score must be between 0 and 100";
        return;
    }

    if (sleep < 0 || sleep > 12) {
        resultDiv.className = 'result show result-fail';
        resultDiv.innerHTML = "Sleep must be between 0 and 12 hours";
        return;
    }

    // Create the features array
    const features = [hours, score, sleep];
    console.log("Sending features:", features);

    try {
        // Show loading state
        resultDiv.className = 'result show';
        resultDiv.innerHTML = `
            <div class="loading">
                ANALYZING DATA...
            </div>
        `;

        // Send request to backend
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ features: features })
        });

        const data = await response.json();
        console.log("Received data:", data);

        if (data.predicted_class !== undefined) {
            const predictedClass = data.predicted_class === 1 ? "Pass" : "Fail";
            const predictedProb = data.predicted_probability;

            resultDiv.className = `result show result-${predictedClass.toLowerCase()}`;
            resultDiv.innerHTML = `
                <div class="prediction-result">
                    <div class="prediction-title">PREDICTION: ${predictedClass}</div>
                    <div class="prediction-probabilities">
                        <div>Pass Probability: ${(predictedProb[1] * 100).toFixed(1)}%</div>
                        <div>Fail Probability: ${(predictedProb[0] * 100).toFixed(1)}%</div>
                    </div>
                </div>
            `;
        } else {
            resultDiv.className = 'result show result-fail';
            resultDiv.innerHTML = `Error: ${data.error || "Unknown error"}`;
        }

    } catch (err) {
        console.error("Error:", err);
        resultDiv.className = 'result show result-fail';
        resultDiv.innerHTML = "Error connecting to server. Please try again.";
    }
}

  
  
  