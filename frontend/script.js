async function submitScore() {
    // Get the values for score and hours from the input fields
    const scoreInput = document.getElementById("scoreInput").value;  // Corrected ID
    const hoursInput = document.getElementById("hoursInput").value;  // Corrected ID

    // Convert the inputs to numbers and validate
    const hours = parseFloat(hoursInput);
    const score = parseFloat(scoreInput);

    if (isNaN(hours) || isNaN(score)) {
        document.getElementById("result").textContent = "Please enter valid numbers for both score and hours!";
        return;
    }

    // Create the features array to send to Flask (this represents a NumPy array)
    const features = [hours, score];  // Format as a regular array
    console.log("Features to send:", features);

    try {
        // Send the POST request to the Flask backend's /predict route
        const response = await fetch("http://127.0.0.1:5000/predict", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"  // Specify content type as JSON
            },
            body: JSON.stringify({ features: features })  // Send features as JSON
        });

        // Parse the server response
        const data = await response.json();
        console.log("Response from server:", data);  // Debug log

        // If the server returned a predicted class, display it
        if (data.predicted_class !== undefined) {
            const predictedClass = data.predicted_class === 1 ? "Pass" : "Fail";
            const predictedProb = data.predicted_probability;

            // Display the result with prediction class and formatted probabilities
            document.getElementById("result").innerHTML =
                `Prediction: <strong>${predictedClass}</strong><br> 
                Probability of Pass: <strong>${(predictedProb[1] * 100).toFixed(2)}%</strong><br>
                Probability of Fail: <strong>${(predictedProb[0] * 100).toFixed(2)}%</strong>`;
        } else {
            document.getElementById("result").textContent = `Error: ${data.error || "Unknown error"}`;
        }

    } catch (err) {
        // Handle fetch errors
        console.error("Fetch error:", err);
        document.getElementById("result").textContent = "Error connecting to server.";
    }
}

  
  
  