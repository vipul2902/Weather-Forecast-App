// Function to fetch weather data
function getData() {
    var city = document.getElementById("city").value;

    // Check if a city is selected
    if (city !== "") {
        var api_key = "5ebe36183f12b0f0ef9764dc144a1ca9";
        var url = `https://api.openweathermap.org/data/2.5/weather?q=${city}&appid=${api_key}`;

        // Fetch data from API
        fetch(url)
            .then(response => response.json())
            .then(data => {
                if (data.weather) {
                    var weatherData = `
                        <div class="weather-item">
                            <span class="feature">Temperature:</span>
                            <i class="fas fa-thermometer-half"></i>
                            <span class="value">${Math.round(data.main.temp - 273.15)}°C</span>
                        </div>
                        <div class="weather-item">
                            <span class="feature">Humidity:</span>
                            <i class="fas fa-tint"></i>
                            <span class="value">${data.main.humidity}%</span>
                        </div>
                        <div class="weather-item">
                            <span class="feature">Cloudiness:</span>
                            <i class="fas fa-cloud"></i>
                            <span class="value">${data.weather[0].description}</span>
                        </div>
                        <div class="weather-item">
                            <span class="feature">Wind Speed:</span>
                            <i class="fas fa-wind"></i>
                            <span class="value">${Math.round(data.wind.speed * 3.6)} km/h</span>
                        </div>
                        <div class="weather-item">
                            <span class="feature">Precipitation:</span>
                            <i class="fas fa-umbrella"></i>
                            <span class="value">${data.rain ? (data.rain["1h"] ? data.rain["1h"] + " mm" : "0 mm") : "0 mm"}</span>
                        </div>
                    `;
                    document.getElementById("weatherData").innerHTML = weatherData;
                } else {
                    document.getElementById("weatherData").innerHTML = "<p>No weather data found</p>";
                }
            })
            .catch(error => {
                console.log("Error fetching weather data:", error);
                document.getElementById("weatherData").innerHTML = "<p>Error fetching weather data</p>";
            });
    } else {
        alert("Please select a city.");
    }
}

// Populate select dropdown with cities
document.addEventListener("DOMContentLoaded", function() {
    var cities = [
        "Andhra Pradesh", "Arunachal Pradesh", "Assam", "Bihar", "Chhattisgarh", "Goa", "Gujarat", "Haryana",
        "Himachal Pradesh", "Jammu and Kashmir", "Jharkhand", "Karnataka", "Kerala", "Madhya Pradesh",
        "Maharashtra", "Manipur", "Meghalaya", "Mizoram", "Nagaland", "Odisha", "Punjab", "Rajasthan", "Sikkim",
        "Tamil Nadu", "Telangana", "Tripura", "Uttar Pradesh", "Uttarakhand", "West Bengal",
        "Andaman and Nicobar Islands", "Chandigarh", "Dadra and Nagar Haveli", "Daman and Diu", "Lakshadweep",
        "National Capital Territory of Delhi", "Puducherry", "Bangalore", "Mysore", "Coorg", "Ooty", "Indore"
    ];

    var select = document.getElementById("city");

    cities.forEach(function(city) {
        var option = document.createElement("option");
        option.text = city;
        option.value = city;
        select.appendChild(option);
    });
});
