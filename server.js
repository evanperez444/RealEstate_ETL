
require('dotenv').config();
const express = require('express');
const fetch = require('node-fetch');
const cors = require('cors');  // Import cors


const app = express();
const PORT = process.env.PORT || 5001;

// Enable CORS
app.use(cors());

const url = 'https://us-real-estate-listings.p.rapidapi.com/property/marketTrends?property_url=https%3A%2F%2Fwww.realtor.com%2Frealestateandhomes-detail%2F2433-S-Ramona-Cir_Tampa_FL_33612_M56257-22633'

app.get('/api/data', async (req, res) => {
    const response = await fetch(url, {
        method: 'GET',
        headers: {
            'x-rapidapi-key': process.env.API_KEY,
            
            'x-rapidapi-host': process.env.RAPIDAPI_HOST
        }
    });
    const data = await response.json();
    res.json(data);
});

app.listen(PORT, () => {
    console.log(`Server is running on port ${PORT}`);
});
