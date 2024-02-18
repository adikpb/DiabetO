document.addEventListener("DOMContentLoaded", function () {
    console.log("haiii")
    const postDataButton = document.getElementById('submit-button-main');
    postDataButton.addEventListener('click', postData);
});

function showOutput(result) {
    // Display the prediction result on the page
    var outputTextElement = document.getElementById("outputText");

    if (result.outcome === true) {
        alert("You have diabetes.");
    } else {
        alert("You do not have diabetes.");
    }

    // Show the output section
    document.getElementById("outputSection").classList.remove("d-none");
}

function postData() {
    const apiUrl = 'https://diabeto.onrender.com/predict';

    const ageValue = parseInt(document.getElementById('age').value, 10) || 0;
    const genderValue = parseInt(document.getElementById('gender').value, 10) || 0;
    const hypertensionValue = parseFloat(document.getElementById('hypertension').value) || 0;
    const heart_diseasesValue = parseFloat(document.getElementById('heart_diseases').value) || 0;
    const smoking_historyValue = parseFloat(document.getElementById('smoking_history').value) || 0;
    const bmiValue = parseFloat(document.getElementById('bmi').value) || 0;
    const hba1c_levelValue = parseFloat(document.getElementById('hba1c_level').value) || 0;
    const blood_glucose_levelValue = parseFloat(document.getElementById('blood_glucose_level').value) || 0;

    const requestBody = {
        age: ageValue,
        gender: genderValue,
        hypertension: hypertensionValue,
        heart_diseases: heart_diseasesValue,
        smoking_history: smoking_historyValue,
        bmi: bmiValue,
        HbA1c_level: hba1c_levelValue,
        blood_glucose_level: blood_glucose_levelValue
    }

    fetch(apiUrl,
        {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json', // Set the content type to JSON
                // Add any additional headers if needed
            },
            body: JSON.stringify(requestBody), // Convert the request body to JSON
        })
        .then(response => response.json())
        .then(data => {
            // Handle the response data
            console.log('Response:', data);
            showOutput(data);

        })
        .catch(error => {
            console.error('Error sending POST request:', error);
        });
}
